import heapq
import math
from collections import Counter, deque
from dataclasses import dataclass
from typing import Literal, NamedTuple

from tqdm.auto import tqdm


class Signal(NamedTuple):
    src: str
    dst: str
    power: bool


class Transition(NamedTuple):
    time: int
    to_signal: Signal


@dataclass
class Module:
    name: str
    type: Literal["%", "&", "broadcaster"]
    dst: tuple[str]
    # For FlipFlop, the state is a bool. For inverters, the state is a list of bools for each input
    state: bool | dict[str, bool] | None

    @classmethod
    def from_str(cls, line: str) -> "Module":
        name, dsts = line.split(" -> ")
        if name[0] in "%&":
            type_ = name[0]
            name = name[1:]
        elif name == "broadcaster":
            type_ = "broadcaster"
        else:
            raise ValueError(f"Invalid module name: {name}")

        # "&" must be fixed later
        state = False if type_ == "%" else {} if type_ == "&" else None
        return cls(name, type_, dsts.split(", "), state)

    @classmethod
    def fix_inverters(cls, modules: dict[str, "Module"]) -> None:
        for module in modules.values():
            for dst in module.dst:
                if dst in modules and modules[dst].type == "&":
                    modules[dst].state[module.name] = False


def press_button(modules: dict[str, Module]) -> list[Signal]:
    seen_powers = Counter()
    q = [Signal("button", "broadcaster", False)]
    for signal in q:
        seen_powers[signal.power] += 1
        match modules.get(signal.dst, None):
            case Module(name, "broadcaster", dsts, _):
                q.extend(Signal(name, dst, signal.power) for dst in dsts)

            case Module(name, "%", dsts, state) as flipflop:
                if signal.power:
                    continue  # Skip high power signals
                out_power = flipflop.state = not state
                q.extend(Signal(name, dst, out_power) for dst in dsts)

            case Module(name, "&", dsts, state):
                state[signal.src] = signal.power
                power = not all(state.values())  # Lo if all inputs are high, else Hi
                q.extend(Signal(name, dst, power) for dst in dsts)
            case None:
                pass  # Output only module

            case _:
                raise ValueError(f"Invalid module: {modules[signal.dst]}")
    return q


def solve1(input: list[str]) -> str:
    modules = {(m := Module.from_str(line)).name: m for line in input}
    Module.fix_inverters(modules)

    seen_powers = Counter()
    for _ in range(1000):
        for signal in press_button(modules):
            seen_powers[signal.power] += 1

    product = 1
    for k in seen_powers.values():
        product *= k

    return str(product)


def bfs(G, start, end) -> list[str]:
    seen = set()
    queue = [start]
    for node in queue:
        if node == end:
            continue  # Don't continue from here
        new = set(G[node]) - seen
        queue.extend(new)
        seen |= new
    return queue


def solve2(input: list[str]) -> str:
    """
    We need to send a low signal to rx
    This is only possible if the memory of bb is set to all high
    rx <-low- bb <-high- ks
                 <-high- kp
                 <-high- xc
                 <-high- ct
    It turns out these 4 input modules form 4 cyclic groups
    So if we can quickly simulate/traverse state transitions of the 4
        input modules by skipping cyclic computations, we can quickly
        find the first time they are all high.
    """
    modules = {(m := Module.from_str(line)).name: m for line in input}
    Module.fix_inverters(modules)
    assert modules["bb"].type == "&" and modules["bb"].dst == ["rx"]

    G_dict_of_lists = {m.name: m.dst for m in modules.values()}

    # These are the start:end points of the 4 cyclic groups
    # These groups can be determined using this code
    # >>> import matplotlib.pyplot as plt
    # >>> import networkx as nx
    # >>> kwargs = {"with_labels": True, "font_weight": "bold", "node_size": 10}
    # >>> G = nx.from_dict_of_lists(G_dict_of_lists)
    # >>> plt.figure(figsize=(20, 20))
    # >>> nx.draw_spring(G, **kwargs)
    cyclic_start_end = {"fr": "ks", "mf": "kp", "jf": "xc", "bv": "ct"}
    cyclic_groups = {
        end: bfs(G_dict_of_lists, start, end) for start, end in cyclic_start_end.items()
    }
    # The cyclic groups all end in a single &inverter with 1 state
    # So if we record when this state turns on, we can just skip
    # time until we reach that ON state
    assert all(
        [
            m.type == "&" and len(m.state) == 1
            for m in map(modules.__getitem__, cyclic_groups)
        ]
    )

    # If we encounter the starting configuration again, we have a cycle
    def get_cycle_id(cycle_end: str):
        return tuple(
            str(module.state)
            for module in map(modules.__getitem__, cyclic_groups[cycle_end])
        )

    end_transitions = {end: [Transition(-1, False)] for end in cyclic_groups}

    cyclic_ends = {end: 0 for end in cyclic_groups}
    seen = {end: set() for end in cyclic_groups}
    for i in range(int(10_000)):
        press_button(modules)
        for cycle_end in cyclic_groups:
            group_id = get_cycle_id(cycle_end)
            if group_id in seen[cycle_end]:
                if cyclic_ends[cycle_end] == 0:
                    seen[cycle_end].clear()
                    cyclic_ends[cycle_end] = i
                else:
                    seen[cycle_end].clear()
                    assert i % cyclic_ends[cycle_end] == 0
            seen[cycle_end].add(group_id)

            end_state = all(modules[cycle_end].state.values())
            if end_state != end_transitions[cycle_end][-1].to_signal:
                end_transitions[cycle_end].append(Transition(i, end_state))

    # Luckily, the groups all flip their state exactly once, at exactly the end of the cycle
    # So we do not need to consider many state flips. Just consider entire cycles
    # print(end_transitions)

    assert all(cyclic_ends.values())

    # Much too slow. ETA: 12 hours
    # hq = sorted([(time, key) for key, time in cyclic_ends.items()])
    # with tqdm(total=211712400442661, mininterval=1) as pbar:
    #     while hq[0][0] != max(hq)[0]:
    #         time, key = heapq.heappop(hq)
    #         heapq.heappush(hq, (cyclic_ends[key] + time, key))
    #         pbar.set_description(f"Time: {time}", refresh=False)
    #         pbar.update()
    return str(math.lcm(*cyclic_ends.values()))


sample_input2 = sample_input1 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".splitlines()

full_input1 = full_input2 = """%mq -> zt
%jr -> gt, hv
%qh -> gt, kt
%hr -> hg, zt
%px -> nl
%fx -> mv
%tz -> jl, zt
%mv -> xd, ss
%cb -> sj, zt
%sn -> kx
%xp -> vl, zt
%nl -> hz
%dp -> bj, xd
%zq -> xd, fx
%hv -> gt
%zm -> ms, vr
&ct -> bb
&xd -> kp, bg, ss, sn, mf, qb, fx
&kp -> bb
&gt -> pm, xh, gp, nn, bv, ct
%ss -> bg
&zt -> jl, xc, jf, fh
&ms -> br, nl, px, vg, vr, ks, fr
%xj -> ms, vt
%ts -> ms
%lt -> gt, xh
%gp -> bx
%br -> px
%sj -> mq, zt
broadcaster -> fr, jf, mf, bv
%jl -> cb
%mf -> xd, qb
%vl -> zt, tz
&ks -> bb
&bb -> rx
%bv -> gt, nn
%bs -> xj, ms
%vt -> ms, ts
%nn -> nz
%nz -> pm, gt
%xh -> qh
%xl -> xd, sn
%fr -> ms, zm
%pd -> hr, zt
%pm -> lt
%vg -> bs
%bj -> xd
%fh -> xp
%qb -> zq
%kx -> dp, xd
%bx -> jr, gt
%vr -> br
%hg -> fh, zt
%kt -> gp, gt
%hz -> ms, vg
%jf -> zt, pd
%bg -> xl
&xc -> bb""".splitlines()

if __name__ == "__main__":
    input = sample_input1
    input = full_input1

    print(solve1(input))
    print(solve2(input))
