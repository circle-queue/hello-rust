use std::collections::HashMap;

pub fn solve1(input: Vec<String>) -> String {
    let max_colors = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    let mut valid = 0;
    'line_loop: for (id, line) in input.iter().enumerate() {
        let count_str = line.split(": ").last().expect("1");
        for draw in count_str.split("; ") {
            for item in draw.split(", ") {
                let counts_color: Vec<&str> = item.split(" ").collect();
                let counts: i32 = counts_color[0].trim().parse().expect("2");
                let color = counts_color[1];

                if counts > max_colors[color] {
                    continue 'line_loop; // This line of draws is invalid
                }
            }
        }
        // dbg!(id + 1);
        valid += id + 1;
    }
    valid.to_string()
}

pub fn solve2(input: Vec<String>) -> String {
    let mut valid = 0;
    for line in input {
        let count_str = line.split(": ").last().expect("1");

        let mut max_colors = HashMap::new();
        for draw in count_str.split("; ") {
            for item in draw.split(", ") {
                let counts_color: Vec<&str> = item.split(" ").collect();
                let counts = counts_color[0].trim().parse().expect("2");
                let color = counts_color[1];

                if counts > *max_colors.entry(color).or_default() {
                    max_colors.insert(color, counts);
                }
            }
        }
        let mut product = 1;
        for value in max_colors.values() {
            product *= value;
        }
        // dbg!(product);
        valid += product;
    }
    valid.to_string()
}

pub fn sample_input1() -> Vec<String> {
    vec![
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green".to_string(),
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue".to_string(),
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red".to_string(),
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red".to_string(),
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green".to_string(),
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
        "Game 1: 5 red, 1 green; 6 red, 3 blue; 9 red; 1 blue, 1 green, 4 red; 1 green, 2 blue; 2 blue, 1 red".to_string(),
        "Game 2: 12 red, 2 green, 9 blue; 8 red, 12 blue; 9 red, 1 blue, 2 green; 12 blue, 8 red, 2 green; 4 red, 5 blue; 1 green, 9 blue, 10 red".to_string(),
        "Game 3: 2 red, 8 blue, 5 green; 10 red, 10 green, 7 blue; 9 green, 13 red, 5 blue".to_string(),
        "Game 4: 3 red; 1 blue, 3 green, 3 red; 3 blue, 8 green, 5 red; 8 green, 2 blue".to_string(),
        "Game 5: 8 blue, 1 red, 1 green; 1 blue, 1 red, 7 green; 7 green, 5 blue".to_string(),
        "Game 6: 2 red, 8 blue; 5 blue, 4 green; 5 blue, 4 red, 3 green; 3 red, 9 blue; 5 green, 9 blue, 7 red; 6 red, 9 blue, 5 green".to_string(),
        "Game 7: 3 green, 4 blue; 7 green, 3 red, 3 blue; 7 red, 4 green, 6 blue; 4 blue, 1 green, 5 red; 6 blue, 2 red, 7 green; 1 green, 4 blue, 4 red".to_string(),
        "Game 8: 2 blue, 12 red; 1 green, 2 blue, 10 red; 12 red, 10 blue; 5 red, 1 green, 2 blue; 13 red, 16 blue, 1 green; 2 blue, 18 red".to_string(),
        "Game 9: 5 green, 2 red, 13 blue; 5 green, 1 red; 7 green, 8 blue, 1 red; 16 blue; 5 blue, 2 green, 3 red".to_string(),
        "Game 10: 5 blue, 2 red; 13 blue, 3 red, 5 green; 2 red, 3 blue; 6 red, 9 blue, 5 green; 9 blue, 3 green, 3 red".to_string(),
        "Game 11: 9 red, 4 green, 3 blue; 8 blue, 8 red; 1 green, 13 blue; 11 blue, 8 red, 4 green".to_string(),
        "Game 12: 1 green; 1 blue, 4 red, 6 green; 1 red, 8 green; 7 red, 1 blue, 3 green; 8 green, 1 blue, 8 red".to_string(),
        "Game 13: 5 blue, 14 red, 1 green; 10 red, 4 blue, 1 green; 6 red, 1 green, 3 blue; 7 blue, 4 red; 14 red, 2 blue, 1 green".to_string(),
        "Game 14: 9 green, 1 blue; 6 red, 9 green; 7 green, 3 blue".to_string(),
        "Game 15: 1 green, 4 blue, 2 red; 8 red, 3 blue; 1 red, 3 blue".to_string(),
        "Game 16: 6 blue, 10 green, 5 red; 11 blue, 1 red; 3 red, 2 green, 3 blue; 1 green, 4 red, 6 blue; 11 blue, 2 red, 11 green".to_string(),
        "Game 17: 4 green, 5 blue, 8 red; 6 green, 7 red; 3 green, 8 red, 5 blue; 4 green, 8 red; 5 green, 11 blue, 3 red; 5 green, 15 blue, 1 red".to_string(),
        "Game 18: 7 green, 17 blue, 14 red; 4 green, 11 red, 7 blue; 13 blue, 8 green; 3 red, 7 green, 11 blue".to_string(),
        "Game 19: 13 red, 13 blue, 1 green; 7 blue, 1 red, 5 green; 18 blue, 1 green, 11 red; 4 blue, 13 red, 6 green".to_string(),
        "Game 20: 1 blue, 6 green, 7 red; 5 green, 4 red, 1 blue; 1 blue, 1 red, 4 green".to_string(),
        "Game 21: 3 red, 5 green, 7 blue; 6 green, 10 blue, 5 red; 9 red, 1 blue; 5 green, 8 blue, 9 red; 2 red, 11 green, 4 blue; 5 red, 6 blue".to_string(),
        "Game 22: 8 blue, 1 red, 1 green; 10 blue; 13 blue, 1 green, 4 red; 1 green, 8 blue, 4 red; 3 blue, 1 red".to_string(),
        "Game 23: 2 blue; 3 blue, 5 green; 6 blue, 5 green, 2 red; 1 green".to_string(),
        "Game 24: 1 red, 13 green, 4 blue; 16 green, 4 blue; 4 red, 5 blue, 11 green; 15 green, 5 red, 10 blue; 16 green, 1 red; 5 red, 3 blue, 10 green".to_string(),
        "Game 25: 12 red, 7 green, 6 blue; 5 blue, 5 red, 12 green; 12 green, 3 red; 5 green, 5 red, 3 blue".to_string(),
        "Game 26: 2 green, 11 blue; 5 red, 3 blue; 5 red, 12 blue, 3 green".to_string(),
        "Game 27: 3 green, 5 red, 12 blue; 3 red, 11 blue, 1 green; 3 red, 4 blue, 3 green; 3 red, 9 green, 9 blue; 14 blue, 1 green, 12 red".to_string(),
        "Game 28: 8 green, 9 blue; 6 green, 8 red, 1 blue; 7 red, 6 green; 12 red, 2 blue, 2 green".to_string(),
        "Game 29: 16 red, 4 green, 1 blue; 10 red, 7 green, 2 blue; 3 green, 8 red; 2 blue, 1 red, 4 green; 2 blue, 10 red, 9 green; 7 green, 1 blue, 18 red".to_string(),
        "Game 30: 13 red, 3 blue; 3 blue, 1 green, 10 red; 15 red, 3 blue; 1 green, 1 red, 1 blue; 16 red, 1 green, 3 blue".to_string(),
        "Game 31: 5 red, 8 blue, 3 green; 5 green, 7 blue, 13 red; 9 red, 3 green, 10 blue; 15 red, 1 green, 7 blue; 5 green, 12 blue, 2 red; 6 blue, 13 red".to_string(),
        "Game 32: 2 blue, 8 red, 1 green; 3 green, 2 blue, 11 red; 2 green, 6 red; 13 red, 3 green, 2 blue; 6 red".to_string(),
        "Game 33: 5 blue, 5 red; 8 red, 1 green, 7 blue; 1 green, 6 red".to_string(),
        "Game 34: 3 blue; 3 green, 2 blue, 2 red; 3 green, 1 blue, 3 red; 3 blue".to_string(),
        "Game 35: 4 red, 2 blue, 6 green; 4 blue, 9 red, 10 green; 3 blue, 8 green, 1 red; 3 red, 1 green, 4 blue; 4 green, 7 blue; 8 red, 8 green, 2 blue".to_string(),
        "Game 36: 1 red, 3 blue, 12 green; 16 green, 7 blue, 1 red; 1 blue, 1 red, 9 green; 2 blue, 2 green; 8 green, 2 red".to_string(),
        "Game 37: 2 green, 8 red; 3 blue, 1 red, 2 green; 15 red, 7 blue; 1 green, 16 red, 15 blue; 13 red, 9 blue".to_string(),
        "Game 38: 9 red, 9 blue, 5 green; 3 red, 19 blue, 8 green; 15 blue, 11 red, 6 green; 10 red, 19 blue, 5 green; 8 blue, 7 green, 6 red; 7 red, 6 green, 10 blue".to_string(),
        "Game 39: 8 blue, 13 green, 2 red; 16 blue, 9 green; 19 blue, 1 green; 1 red, 3 blue, 9 green; 1 green, 18 blue".to_string(),
        "Game 40: 6 red, 5 blue; 11 green, 15 blue, 7 red; 10 blue, 5 green, 10 red; 13 blue, 9 red, 11 green; 2 green, 14 blue, 12 red; 6 red, 6 green".to_string(),
        "Game 41: 10 green, 1 red, 1 blue; 1 red, 9 green; 1 green; 6 green, 1 blue, 2 red; 1 blue, 8 green, 1 red; 9 green".to_string(),
        "Game 42: 13 green, 2 blue; 10 blue, 1 red; 10 red, 10 green, 8 blue; 16 green, 8 blue, 6 red; 9 red, 18 green; 10 red, 15 blue, 1 green".to_string(),
        "Game 43: 3 red, 16 blue, 6 green; 1 red, 17 blue, 12 green; 19 blue, 2 red, 16 green; 12 green, 7 blue, 1 red; 8 green, 7 blue, 2 red; 12 green, 9 blue".to_string(),
        "Game 44: 4 red, 3 green, 2 blue; 18 blue, 3 green; 7 red, 7 blue, 4 green".to_string(),
        "Game 45: 1 green, 3 blue, 7 red; 9 green, 8 red, 2 blue; 5 green, 3 blue, 6 red".to_string(),
        "Game 46: 18 blue; 4 blue, 1 red, 5 green; 2 red, 15 blue, 7 green".to_string(),
        "Game 47: 17 red, 4 green, 12 blue; 6 green, 1 red, 2 blue; 3 blue, 13 green, 4 red".to_string(),
        "Game 48: 11 red, 2 green; 8 red, 3 green; 2 green, 5 blue, 9 red; 3 green, 2 blue, 5 red".to_string(),
        "Game 49: 2 green, 12 blue, 9 red; 1 green, 12 red; 1 green, 2 blue, 18 red; 8 blue, 19 red; 1 green, 5 blue; 3 blue, 10 red, 1 green".to_string(),
        "Game 50: 5 green, 1 red; 7 red, 3 blue, 9 green; 15 blue, 4 green, 4 red".to_string(),
        "Game 51: 12 green, 14 blue; 2 red, 5 green, 16 blue; 4 red, 17 blue, 16 green; 6 blue, 16 green, 2 red; 17 blue, 13 green, 5 red".to_string(),
        "Game 52: 7 green, 10 red, 2 blue; 6 green, 12 red, 3 blue; 10 red, 3 blue, 8 green; 3 blue, 1 green, 8 red; 6 green, 5 blue, 3 red".to_string(),
        "Game 53: 8 blue, 3 green; 7 green, 11 blue, 1 red; 1 red, 7 blue, 9 green; 1 blue, 1 green; 4 green, 1 red; 1 red, 8 blue".to_string(),
        "Game 54: 1 blue, 1 green, 4 red; 1 red, 1 blue, 13 green; 11 red, 11 green, 1 blue".to_string(),
        "Game 55: 5 blue, 4 red, 11 green; 13 green, 9 blue, 3 red; 3 red, 7 green, 8 blue; 2 red, 20 blue, 2 green; 3 red, 10 blue, 1 green; 12 green, 5 red, 8 blue".to_string(),
        "Game 56: 17 red, 2 green, 1 blue; 13 blue, 8 green, 6 red; 1 green, 9 blue, 6 red; 2 blue".to_string(),
        "Game 57: 9 green, 1 red, 9 blue; 15 green, 10 blue, 1 red; 5 blue, 3 red, 10 green".to_string(),
        "Game 58: 14 red, 2 blue, 14 green; 17 red, 7 blue, 10 green; 4 green, 13 red, 11 blue; 3 green, 13 red, 5 blue; 13 red, 6 blue; 1 red, 7 green, 2 blue".to_string(),
        "Game 59: 16 blue, 7 red, 2 green; 7 green, 10 red, 12 blue; 4 red, 9 green, 14 blue; 8 blue, 11 green, 1 red; 3 blue, 5 red, 11 green".to_string(),
        "Game 60: 1 blue; 9 red, 4 green; 3 green, 3 blue, 1 red; 3 red, 1 blue".to_string(),
        "Game 61: 2 green, 15 red, 12 blue; 9 green, 1 blue, 10 red; 14 blue, 17 red, 2 green; 12 red, 6 blue, 3 green; 8 green, 10 blue, 10 red; 2 green, 10 red, 2 blue".to_string(),
        "Game 62: 12 red, 6 blue, 1 green; 2 red, 1 green, 4 blue; 10 blue, 12 red, 4 green; 5 green, 8 red, 8 blue".to_string(),
        "Game 63: 3 green, 3 red; 7 red; 2 green, 1 blue, 7 red; 5 red, 1 green".to_string(),
        "Game 64: 5 green, 11 red; 4 green, 2 blue, 7 red; 7 red, 11 blue, 3 green; 8 blue, 5 green, 5 red; 8 red, 4 blue".to_string(),
        "Game 65: 5 red, 5 blue; 15 green, 3 blue; 3 blue, 3 red, 8 green; 1 blue, 3 red, 5 green".to_string(),
        "Game 66: 8 green, 5 blue, 12 red; 10 red, 5 blue, 11 green; 12 red, 3 blue, 2 green; 5 green, 1 blue, 10 red; 15 red, 5 green, 3 blue; 2 red, 8 blue".to_string(),
        "Game 67: 12 blue, 3 red; 4 blue, 4 red, 1 green; 9 green, 14 blue, 3 red; 2 red, 13 blue, 6 green; 17 blue, 5 green".to_string(),
        "Game 68: 1 blue, 4 red, 11 green; 11 green, 4 red, 7 blue; 11 green, 7 blue; 14 green, 2 blue, 1 red; 2 blue, 4 red".to_string(),
        "Game 69: 4 red, 1 green; 5 red, 2 green, 3 blue; 1 red, 7 blue; 8 red, 6 blue, 1 green; 2 green, 6 red, 1 blue; 6 red, 8 blue, 2 green".to_string(),
        "Game 70: 6 blue, 2 green, 4 red; 1 green, 5 blue; 1 blue, 3 red; 2 red; 2 red, 17 blue".to_string(),
        "Game 71: 9 blue, 2 green, 1 red; 7 blue, 2 green, 3 red; 12 red, 13 blue; 15 blue, 1 green, 1 red".to_string(),
        "Game 72: 15 blue, 16 red, 18 green; 16 red, 12 blue, 14 green; 3 blue, 12 red, 4 green; 8 green, 17 blue, 15 red; 15 blue, 18 green, 4 red; 5 blue, 3 red, 10 green".to_string(),
        "Game 73: 17 blue, 3 red, 19 green; 10 blue, 15 green, 18 red; 4 green, 15 red; 1 green, 17 blue, 14 red; 16 red, 1 green, 4 blue".to_string(),
        "Game 74: 6 green, 2 blue, 5 red; 1 blue, 9 green; 5 red, 1 blue, 10 green; 4 green, 11 red, 1 blue".to_string(),
        "Game 75: 4 blue; 4 green, 6 blue; 2 green, 2 blue, 4 red".to_string(),
        "Game 76: 5 blue; 5 green, 5 red; 9 red, 1 blue, 1 green; 5 green; 3 green, 6 red, 1 blue".to_string(),
        "Game 77: 2 red, 10 blue, 6 green; 1 red, 6 blue, 6 green; 9 blue, 2 green, 8 red; 12 blue, 7 green, 18 red".to_string(),
        "Game 78: 2 red, 5 blue, 2 green; 2 blue, 4 green, 6 red; 4 blue, 4 green, 3 red; 3 red, 5 green; 2 red, 4 green, 4 blue".to_string(),
        "Game 79: 14 red, 6 blue, 1 green; 6 blue, 18 red, 2 green; 1 green; 8 red, 5 green; 1 blue, 7 red, 6 green; 11 red, 1 blue".to_string(),
        "Game 80: 5 blue, 4 red; 19 blue, 7 red; 6 red, 1 green, 12 blue; 1 green, 8 red".to_string(),
        "Game 81: 7 green, 6 red, 9 blue; 14 blue, 8 green; 15 green, 6 red, 4 blue; 1 red, 7 blue, 19 green".to_string(),
        "Game 82: 1 red, 4 blue; 3 blue, 1 red, 5 green; 3 blue, 5 green, 12 red; 17 red, 2 blue; 4 blue, 1 red".to_string(),
        "Game 83: 6 blue, 11 green, 18 red; 11 red, 7 blue, 2 green; 13 red, 14 blue, 14 green; 1 red, 3 blue, 16 green".to_string(),
        "Game 84: 2 red, 5 blue, 3 green; 9 red, 7 blue, 2 green; 4 green, 9 red, 3 blue; 1 blue, 1 green, 5 red".to_string(),
        "Game 85: 1 red, 10 green, 15 blue; 9 green, 1 red; 1 red, 2 green, 12 blue".to_string(),
        "Game 86: 1 green, 5 blue, 8 red; 10 green, 8 red, 9 blue; 6 green, 3 red, 8 blue; 9 red, 3 green, 8 blue; 2 red, 6 blue, 1 green".to_string(),
        "Game 87: 13 red, 12 green; 6 blue, 5 green, 3 red; 10 green, 1 blue, 17 red; 9 green, 6 blue, 2 red; 1 blue, 9 green, 14 red".to_string(),
        "Game 88: 4 green, 1 blue, 7 red; 6 green, 2 red, 1 blue; 13 red, 7 green".to_string(),
        "Game 89: 2 blue, 7 green, 10 red; 6 green, 5 blue; 12 red, 4 blue, 5 green; 15 red, 8 blue; 6 blue, 8 red, 3 green; 14 red, 11 green, 16 blue".to_string(),
        "Game 90: 8 green, 8 red; 5 green, 1 blue, 13 red; 3 blue, 1 green, 3 red; 11 red, 2 green; 9 red, 7 green, 1 blue".to_string(),
        "Game 91: 4 green, 13 red, 10 blue; 11 blue, 4 red; 10 blue, 9 green; 9 green, 4 blue, 12 red; 7 green, 4 red, 1 blue".to_string(),
        "Game 92: 6 blue; 10 green, 1 red, 11 blue; 5 blue, 5 green; 6 green, 1 red; 1 red, 6 green".to_string(),
        "Game 93: 2 red, 15 blue, 4 green; 13 red, 11 green; 6 green, 1 blue, 6 red; 6 red, 5 blue, 10 green; 2 blue, 11 green, 18 red".to_string(),
        "Game 94: 2 red, 13 blue, 3 green; 15 blue, 4 red, 2 green; 4 green, 9 blue, 7 red; 12 blue, 6 red, 11 green; 20 blue, 13 red, 11 green".to_string(),
        "Game 95: 6 blue, 1 red, 10 green; 10 red, 5 blue, 7 green; 9 red, 13 green, 10 blue; 11 blue, 9 red, 8 green".to_string(),
        "Game 96: 2 red, 7 green, 16 blue; 20 green, 2 red, 14 blue; 5 red, 15 green, 15 blue; 4 blue, 6 red, 15 green; 6 green, 6 red, 10 blue".to_string(),
        "Game 97: 1 red, 1 blue, 14 green; 10 green, 12 red, 1 blue; 10 red, 2 green, 1 blue; 1 blue, 3 green, 14 red; 3 red, 2 blue, 13 green; 1 blue, 3 green, 13 red".to_string(),
        "Game 98: 13 blue, 1 green; 18 green, 6 red, 3 blue; 11 blue, 7 red, 9 green; 4 red, 6 green, 11 blue; 12 blue, 6 red, 8 green".to_string(),
        "Game 99: 4 blue; 1 red, 2 green, 11 blue; 12 blue, 1 green, 1 red; 11 blue, 6 green; 1 red, 7 green, 8 blue".to_string(),
        "Game 100: 10 blue, 5 green; 4 green, 3 red, 6 blue; 2 green, 4 red, 1 blue".to_string(),
    ]
}
