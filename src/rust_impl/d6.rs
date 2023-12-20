pub fn solve1(input: Vec<String>) -> String {
    let times = input.get(0).unwrap().replace("Time:", "");
    let dists = input.get(1).unwrap().replace("Distance:", "");
    let times = times
        .split_ascii_whitespace()
        .map(|n| n.parse::<i64>().unwrap())
        .collect::<Vec<_>>();

    let dists = dists
        .split_ascii_whitespace()
        .map(|n| n.parse::<i64>().unwrap())
        .collect::<Vec<_>>();

    let mut solutions = 1;
    for (dist, time) in std::iter::zip(dists, times) {
        let mut this_race_sol = 0;
        for charge_time in 1..time {
            let traversed = charge_time * (time - charge_time);
            if traversed > dist {
                this_race_sol += 1
            }
        }
        solutions *= this_race_sol;
    }
    solutions.to_string()
}

pub fn solve2(input: Vec<String>) -> String {
    let times = input.get(0).unwrap().replace("Time:", "");
    let dists = input.get(1).unwrap().replace("Distance:", "");
    let time = times.replace(" ", "").parse::<i64>().unwrap();
    let dist = dists.replace(" ", "").parse::<i64>().unwrap();

    let mut solutions = 1;
    let mut this_race_sol = 0;
    for charge_time in 1..time {
        let traversed = charge_time * (time - charge_time);
        if traversed > dist {
            this_race_sol += 1
        }
    }
    solutions *= this_race_sol;
    solutions.to_string()
}

pub fn sample_input1() -> Vec<String> {
    vec![
        "Time:      7  15   30".to_string(),
        "Distance:  9  40  200".to_string(),
    ]
}

pub fn sample_input2() -> Vec<String> {
    sample_input1()
}
pub fn full_input1() -> Vec<String> {
    full_input2()
}

pub fn full_input2() -> Vec<String> {
    vec![
        "Time:        38     67     76     73".to_string(),
        "Distance:   234   1027   1157   1236".to_string(),
    ]
}
