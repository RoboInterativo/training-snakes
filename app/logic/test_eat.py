from ..utils.test import build_test_gamestate
from ..logic import Eat, PathDistances
from ..snakes import *


# def test_eat_closest():
#     class EatingSnake(BaseSnake, Eat, PathDistances):
#         pass
#
#     gs = build_test_gamestate(3,3, me=[(1, 1), (2, 1)], food=[(0, 0), (1, 2)])
#     move = EatingSnake().move(gs)
#     assert move == "up"
def test_snake0_left_wall():
    gs = build_test_gamestate(11,11, me=[(0, 0), (0, 1)], food=[(0, 0), (1, 2)])
    move = Snake0().move(gs)
    assert move.direction() in [ "up","left"]

def test_snake0_left_wall():
    gs = build_test_gamestate(11,11, me=[(1, 11), (1, 10)], food=[(0, 0), (1, 2)])
    move = Snake0().move(gs)
    assert move.direction() in [ "up","left"]
