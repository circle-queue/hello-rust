import hello_rust as rust_impl
import hello_rust.python as python_impl


def test_d1_rust():
    assert rust_impl.d1_solve_task_1(python_impl.d1.sample_input1) == "142"
    assert rust_impl.d1_solve_task_2(python_impl.d1.sample_input2) == "281"
    assert rust_impl.d1_solve_task_1(python_impl.d1.full_input1) == "56042"
    assert rust_impl.d1_solve_task_2(python_impl.d1.full_input2) == "55358"


def test_d1_python():
    assert python_impl.d1.solve_task_1(python_impl.d1.sample_input1) == "142"
    assert python_impl.d1.solve_task_2(python_impl.d1.sample_input2) == "281"
    assert python_impl.d1.solve_task_1(python_impl.d1.full_input1) == "56042"
    assert python_impl.d1.solve_task_2(python_impl.d1.full_input2) == "55358"
