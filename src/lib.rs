#![allow(dead_code)]

pub mod rust_impl;

use pyo3::prelude::*;

#[rustfmt::skip] #[pyfunction] fn d1_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d1::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d1_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d1::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d2_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d2::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d2_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d2::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d3_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d3::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d3_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d3::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d4_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d4::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d4_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d4::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d5_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d5::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d5_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d5::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d6_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d6::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d6_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d6::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d7_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d7::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d7_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d7::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d8_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d8::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d8_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d8::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d9_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d9::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d9_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d9::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d10_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d10::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d10_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d10::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d11_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d11::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d11_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d11::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d12_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d12::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d12_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d12::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d13_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d13::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d13_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d13::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d14_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d14::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d14_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d14::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d15_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d15::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d15_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d15::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d16_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d16::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d16_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d16::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d17_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d17::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d17_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d17::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d18_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d18::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d18_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d18::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d19_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d19::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d19_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d19::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d20_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d20::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d20_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d20::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d21_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d21::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d21_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d21::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d22_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d22::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d22_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d22::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d23_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d23::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d23_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d23::solve2(input)) }
#[rustfmt::skip] #[pyfunction] fn d24_solve1(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d24::solve1(input)) }
#[rustfmt::skip] #[pyfunction] fn d24_solve2(input: Vec<String>) -> PyResult<String> { Ok(rust_impl::d24::solve2(input)) }

/// A Python module implemented in Rust.
#[pymodule]
fn hello_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    let submod = PyModule::new(_py, "rust_impl")?;
    rust_impl(submod)?;
    m.add_submodule(submod)?;
    Ok(())
}

fn rust_impl(m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(d1_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d1_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d2_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d2_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d3_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d3_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d4_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d4_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d5_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d5_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d6_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d6_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d7_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d7_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d8_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d8_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d9_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d9_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d10_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d10_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d11_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d11_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d12_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d12_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d13_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d13_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d14_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d14_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d15_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d15_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d16_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d16_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d17_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d17_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d18_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d18_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d19_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d19_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d20_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d20_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d21_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d21_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d22_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d22_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d23_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d23_solve2, m)?)?;
    m.add_function(wrap_pyfunction!(d24_solve1, m)?)?;
    m.add_function(wrap_pyfunction!(d24_solve2, m)?)?;

    Ok(())
}
