import hello_rust as rust_impl
import pandas as pd
import hello_rust.python as python_impl
import time
from typing import NamedTuple, Any


def test_execution_time(capsys):
    # This test should not be able to fail, but instead prints an excecution time table summary
    timings_data = []

    repeats = 10
    for day in range(1, 2):
        for impl in [rust_impl, python_impl]:
            for task in [1, 2]:
                python_module = getattr(python_impl, f"d{day}")
                if impl == rust_impl:
                    func = getattr(rust_impl, f"d{day}_solve_task_{task}")
                else:
                    func = getattr(python_module, f"solve_task_{task}")

                for input_name in ["sample", "full"]:
                    input = getattr(python_module, f"{input_name}_input{task}")

                    for _ in range(repeats):
                        s = time.perf_counter_ns()
                        func(input)
                        func
                        timings_data.append(
                            {
                                "day": day,
                                "impl": impl.__name__,
                                "task": task,
                                "input": input_name,
                                "duration_ms": time.perf_counter_ns() - s,
                            }
                        )

    avg_ms = (
        pd.DataFrame(timings_data)
        .groupby(["day", "impl", "task"])
        .duration_ms.agg("mean")
        .rename(f"duration [ms, avg of {repeats} runs]")
    )
    formatted = avg_ms.map("{:.0}".format)
    rust_vs_python = formatted.unstack(level="impl")
    with capsys.disabled():
        print(f"\n{rust_vs_python}")
