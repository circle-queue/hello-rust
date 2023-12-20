#![allow(unused)]
pub mod rust_impl;

fn main() {
    // For debugging in pure rust
    #[allow(unused_variables)]
    use rust_impl::d10 as d;
    let sample_input = false;

    // Evaluate task #1 and check result
    let input1 = if sample_input {
        d::sample_input1()
    } else {
        d::full_input1()
    };
    let sol1 = d::solve1(input1);
    println!("{sol1}");
    assert!(if sample_input {
        sol1 == "4"
    } else {
        sol1 == "6947"
    });

    // Evaluate task #2 and check result
    let input2 = if sample_input {
        d::sample_input2()
    } else {
        d::full_input2()
    };
    let sol2 = d::solve2(input2);
    println!("{sol2}");
    assert!(if sample_input {
        sol2 == "4"
    } else {
        sol2 == "273"
    });
}
