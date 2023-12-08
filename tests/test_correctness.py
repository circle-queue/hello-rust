from hello_rust import python_impl, rust_impl


def test_d1_rust():
    assert rust_impl.d1_solve1(python_impl.d1.sample_input1) == "142"
    assert rust_impl.d1_solve2(python_impl.d1.sample_input2) == "281"
    assert rust_impl.d1_solve1(python_impl.d1.full_input1) == "56042"
    assert rust_impl.d1_solve2(python_impl.d1.full_input2) == "55358"


def test_d1_python():
    assert rust_impl.d1_solve1(python_impl.d1.sample_input1) == "142"
    assert python_impl.d1.solve1(python_impl.d1.sample_input1) == "142"
    assert python_impl.d1.solve2(python_impl.d1.sample_input2) == "281"
    assert python_impl.d1.solve1(python_impl.d1.full_input1) == "56042"
    assert python_impl.d1.solve2(python_impl.d1.full_input2) == "55358"


def test_d2_rust():
    assert rust_impl.d2_solve1(python_impl.d2.sample_input1) == "8"
    assert rust_impl.d2_solve2(python_impl.d2.sample_input2) == "2286"
    assert rust_impl.d2_solve1(python_impl.d2.full_input1) == "1867"
    assert rust_impl.d2_solve2(python_impl.d2.full_input2) == "84538"


def test_d2_python():
    assert python_impl.d2.solve1(python_impl.d2.sample_input1) == "8"
    assert python_impl.d2.solve2(python_impl.d2.sample_input2) == "2286"
    assert python_impl.d2.solve1(python_impl.d2.full_input1) == "1867"
    assert python_impl.d2.solve2(python_impl.d2.full_input2) == "84538"
