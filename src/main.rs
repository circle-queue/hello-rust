pub mod rust;
use rust::d1::*;

fn main() {
    let sample_input = false;

    // Evaluate task #1 and check result
    let input1 = if sample_input {
        sample_input1()
    } else {
        full_input1()
    };
    let sol1 = solve1(input1);
    println!("{sol1}");
    assert!(if sample_input {
        sol1 == "142"
    } else {
        sol1 == "56042"
    });

    // Evaluate task #2 and check result
    let input2 = if sample_input {
        sample_input2()
    } else {
        full_input2()
    };
    let sol2 = solve2(input2);
    println!("{sol2}");
    assert!(if sample_input {
        sol2 == "281"
    } else {
        sol2 == "55358"
    });
}
