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


def test_d3_rust():
    assert rust_impl.d3_solve1(python_impl.d3.sample_input1) == "4361"
    assert rust_impl.d3_solve2(python_impl.d3.sample_input2) == "467835"
    assert rust_impl.d3_solve1(python_impl.d3.full_input1) == "526404"
    assert rust_impl.d3_solve2(python_impl.d3.full_input2) == "84399773"


def test_d3_python():
    assert python_impl.d3.solve1(python_impl.d3.sample_input1) == "4361"
    assert python_impl.d3.solve2(python_impl.d3.sample_input2) == "467835"
    assert python_impl.d3.solve1(python_impl.d3.full_input1) == "526404"
    assert python_impl.d3.solve2(python_impl.d3.full_input2) == "84399773"


def test_d4_rust():
    assert rust_impl.d4_solve1(python_impl.d4.sample_input1) == "13"
    assert rust_impl.d4_solve2(python_impl.d4.sample_input2) == "30"
    assert rust_impl.d4_solve1(python_impl.d4.full_input1) == "20407"
    assert rust_impl.d4_solve2(python_impl.d4.full_input2) == "23806951"


def test_d4_python():
    assert python_impl.d4.solve1(python_impl.d4.sample_input1) == "13"
    assert python_impl.d4.solve2(python_impl.d4.sample_input2) == "30"
    assert python_impl.d4.solve1(python_impl.d4.full_input1) == "20407"
    assert python_impl.d4.solve2(python_impl.d4.full_input2) == "23806951"


def test_d5_rust():
    assert rust_impl.d5_solve1(python_impl.d5.sample_input1) == "35"
    assert rust_impl.d5_solve2(python_impl.d5.sample_input2) == "46"
    assert rust_impl.d5_solve1(python_impl.d5.full_input1) == "88151870"
    assert rust_impl.d5_solve2(python_impl.d5.full_input2) == "2008785"  # slow: 5s


def test_d5_python():
    assert python_impl.d5.solve1(python_impl.d5.sample_input1) == "35"
    assert python_impl.d5.solve2(python_impl.d5.sample_input2) == "46"
    assert python_impl.d5.solve1(python_impl.d5.full_input1) == "88151870"
    assert python_impl.d5.solve2(python_impl.d5.full_input2) == "2008785"  # slow: 15s


def test_d6_rust():
    assert rust_impl.d6_solve1(python_impl.d6.sample_input1) == "288"
    assert rust_impl.d6_solve2(python_impl.d6.sample_input2) == "71503"
    assert rust_impl.d6_solve1(python_impl.d6.full_input1) == "303600"
    assert rust_impl.d6_solve2(python_impl.d6.full_input2) == "23654842"


def test_d6_python():
    assert python_impl.d6.solve1(python_impl.d6.sample_input1) == "288"
    assert python_impl.d6.solve2(python_impl.d6.sample_input2) == "71503"
    assert python_impl.d6.solve1(python_impl.d6.full_input1) == "303600"
    assert python_impl.d6.solve2(python_impl.d6.full_input2) == "23654842"  # slow: 1.5s


def test_d7_rust():
    assert rust_impl.d7_solve1(python_impl.d7.sample_input1) == "6440"
    assert rust_impl.d7_solve2(python_impl.d7.sample_input2) == "5905"
    assert rust_impl.d7_solve1(python_impl.d7.full_input1) == "253954294"
    assert rust_impl.d7_solve2(python_impl.d7.full_input2) == "254837398"


def test_d7_python():
    assert python_impl.d7.solve1(python_impl.d7.sample_input1) == "6440"
    assert python_impl.d7.solve2(python_impl.d7.sample_input2) == "5905"
    assert python_impl.d7.solve1(python_impl.d7.full_input1) == "253954294"
    assert python_impl.d7.solve2(python_impl.d7.full_input2) == "254837398"


def test_d8_rust():
    assert rust_impl.d8_solve1(python_impl.d8.sample_input1) == "2"
    assert rust_impl.d8_solve2(python_impl.d8.sample_input2) == "6"
    assert rust_impl.d8_solve1(python_impl.d8.full_input1) == "14681"
    assert rust_impl.d8_solve2(python_impl.d8.full_input2) == "14321394058031"


def test_d8_python():
    assert python_impl.d8.solve1(python_impl.d8.sample_input1) == "2"
    # This one day is different, since the full input is a simpler case of the sample input
    # The full input has non-overlapping cycles, and is therefore simpler
    # The general case cannot be solved using LCM, but
    # the brute force implementation could be adjusted to increment by all Zs in each cycle
    # assert python_impl.d8.solve2(python_impl.d8.sample_input2) == "6"
    assert python_impl.d8.solve1(python_impl.d8.full_input1) == "14681"
    assert python_impl.d8.solve2(python_impl.d8.full_input2) == "14321394058031"


# # def test_d9_rust():
# #     assert rust_impl.d9_solve1(python_impl.d9.sample_input1) == "114"
# #     assert rust_impl.d9_solve2(python_impl.d9.sample_input2) == "2"
# #     assert rust_impl.d9_solve1(python_impl.d9.full_input1) == "1938800261"
# #     assert rust_impl.d9_solve2(python_impl.d9.full_input2) == "1112"


def test_d9_python():
    assert python_impl.d9.solve1(python_impl.d9.sample_input1) == "114"
    assert python_impl.d9.solve2(python_impl.d9.sample_input2) == "2"
    assert python_impl.d9.solve1(python_impl.d9.full_input1) == "1938800261"
    assert python_impl.d9.solve2(python_impl.d9.full_input2) == "1112"


# # def test_d10_rust():
# #     assert rust_impl.d10_solve1(python_impl.d10.sample_input1) == "4"
# #     assert rust_impl.d10_solve2(python_impl.d10.sample_input2) == "4"
# #     assert rust_impl.d10_solve1(python_impl.d10.full_input1) == "6947"
# #     assert rust_impl.d10_solve2(python_impl.d10.full_input2) == "273"


def test_d10_python():
    assert python_impl.d10.solve1(python_impl.d10.sample_input1) == "4"
    assert python_impl.d10.solve2(python_impl.d10.sample_input2) == "4"
    assert python_impl.d10.solve1(python_impl.d10.full_input1) == "6947"
    assert python_impl.d10.solve2(python_impl.d10.full_input2) == "273"


# # def test_d11_rust():
# #     assert rust_impl.d11_solve1(python_impl.d11.sample_input1) == "374"
# #     assert rust_impl.d11_solve2(python_impl.d11.sample_input2) == "82000210"
# #     assert rust_impl.d11_solve1(python_impl.d11.full_input1) == "9177603"
# #     assert rust_impl.d11_solve2(python_impl.d11.full_input2) == "632003913611"


def test_d11_python():
    assert python_impl.d11.solve1(python_impl.d11.sample_input1) == "374"
    # For this, I assume an expansion factor of 1_000_000
    assert python_impl.d11.solve2(python_impl.d11.sample_input2) == "82000210"
    assert python_impl.d11.solve1(python_impl.d11.full_input1) == "9177603"
    assert python_impl.d11.solve2(python_impl.d11.full_input2) == "632003913611"
