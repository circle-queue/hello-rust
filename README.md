# hello-rust
This package explores the intersection between Python and Rust. I implement solutions to adventofcode.com/2023, solving the problem in python, followed by rust, then adding rust bindings to python and solving them in python using the rust implementation.

# Setup
```sh
python -m venv venv
source ./venv/bin/activate
pip install maturin
maturin develop
pytest
```
This should return all greens after a while

# Bindings architecture
[Maturin](https://www.maturin.rs/) is a build tool for easily embedding rust binaries in python packages. It supports (among other) the [PyO3](https://pyo3.rs/) library for the bindings between rust and python. All the rust code is found in [src/rust_impl](src/rust_impl) and the python code is found in [src_python/hello_rust/python_impl](src_python/hello_rust/python_impl). They're linked via [src/lib.rs](src/lib.rs), which allows importing the two implementations simply by doing:
```python
from hello_rust import python_impl, rust_impl

assert rust_impl.d1_solve1(python_impl.d1.sample_input1) == "142"
assert python_impl.d1.solve1(python_impl.d1.sample_input1) == "142"
```

## Details
### Typing
PyO3 implements modules in a dynamic way, which is slightly messy. Sub-modules are [assigned](https://pyo3.rs/v0.14.0/module) to other modules. Furthermore, since the files are binary, IDEs and other tools are unable to infer the return types of these functions. To solve this, I implement `.pyi` files [as proposed by PyO3](https://pyo3.rs/v0.20.0/python_typing_hints).

### src-layout
[It's a good idea](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) to implement the src-layout over the flat-layout, which for maturin is done by [adding the following to pyproject.toml](https://www.maturin.rs/project_layout):
```toml
[tool.maturin]
python-source = "src_python"
```
