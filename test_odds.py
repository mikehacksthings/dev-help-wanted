import main

def test_odds():
    assert main.remove_odds(set()) == set()
    assert main.remove_odds({2, 4, 6}) == {2, 4, 6}
    assert main.remove_odds({1, 3, 5}) == set()
    assert main.remove_odds({1, 2, 3, 4, 5}) == {2, 4}
    assert main.remove_odds({0, -1, -2, -3, -4}) == {0, -2, -4}