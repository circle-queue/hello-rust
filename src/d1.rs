pub fn solve1() -> String {
    let data = vec!["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"];
    let mut total = 0;

    for ele in data {
        let mut digits_only: String = String::from("");
        for char in ele.chars() {
            if char.is_numeric() {
                digits_only = digits_only + &char.to_string()
            }
        }

        let first_ele = digits_only.chars().next().expect("1");
        let last_ele = digits_only.chars().last().expect("2");
        let grouped = String::from(first_ele) + &last_ele.to_string();
        let num: i32 = grouped.as_str().parse().expect("foo");
        total = total + num;
        dbg!(num);
    }
    total.to_string()
}

pub fn solve2() -> String {
    let data = vec![
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ];

    let conversions = [
        ("oneightwone", "1821"),
        ("oneighthree", "183"),
        ("oneightwo", "182"),
        ("eightwone", "821"),
        ("eighthree", "83"),
        ("nineight", "98"),
        ("eightwo", "82"),
        ("oneight", "18"),
        ("twone", "21"),
        ("eight", "8"),
        ("five", "5"),
        ("four", "4"),
        ("nine", "9"),
        ("one", "1"),
        ("seven", "7"),
        ("six", "6"),
        ("three", "3"),
        ("two", "2"),
    ];

    let mut total = 0;

    for ele in data {
        let mut converted: String = String::from(ele);
        for (k, v) in conversions {
            converted = converted.replace(k, v);
        }

        let mut digits_only = String::from("");
        for char in converted.chars() {
            if char.is_numeric() {
                digits_only = digits_only + &char.to_string()
            }
        }

        let first_ele = digits_only.chars().next().expect("1");
        let last_ele = digits_only.chars().last().expect("2");
        let grouped = String::from(first_ele) + &last_ele.to_string();
        let num: i32 = grouped.as_str().parse().expect("foo");
        total = total + num;
        dbg!(num);
    }
    total.to_string()
}
