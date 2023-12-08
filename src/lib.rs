#![allow(dead_code)]

pub mod rust;

use pyo3::prelude::*;

#[pyfunction]
fn d1_solve_task_1(input: Vec<String>) -> PyResult<String> {
    Ok(rust::d1::solve1(input))
}

#[pyfunction]
fn d1_solve_task_2(input: Vec<String>) -> PyResult<String> {
    Ok(rust::d1::solve2(input))
}

/// A Python module implemented in Rust.
#[pymodule]
fn hello_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(d1_solve_task_1, m)?)?;
    m.add_function(wrap_pyfunction!(d1_solve_task_2, m)?)?;
    Ok(())
}
