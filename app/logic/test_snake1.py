from ..utils.test import build_test_gamestate
from ..logic import Eat, PathDistances
from ..snakes import *
from ..snakes.base_snake import *

# def test_eat_closest():
#     class EatingSnake(BaseSnake, Eat, PathDistances):
#         pass
#
#     gs = build_test_gamestate(3,3, me=[(1, 1), (2, 1)], food=[(0, 0), (1, 2)])
#     move = EatingSnake().move(gs)
#     assert move == "up"
# def test_snake0_left_wall():
#     gs = build_test_gamestate(11,11, me=[(0, 0), (0, 1)], food=[(0, 0), (1, 2)])
#     move = Snake0().move(gs)
#     assert move.direction() in [ "up","left"]
#
# def test_snake0_left_wall():
#     gs = build_test_gamestate(11,11, me=[(1, 11), (1, 10)], food=[(0, 0), (1, 2)])
#     move = Snake0().move(gs)
#     assert move.direction() in [ "up","left"]

def test_left_wall():
    # class EatingSnake(BaseSnake, Eat, PathDistances):
    #     pass
    """Змея у левой стены (x=0) - нельзя двигаться влево"""
    you = [(0, 1), (0, 2), (0, 3)]
    gs = build_test_gamestate(11,11, me=you, food=[])
    #gs = create_minimal_game_state(you, [])  # Пустой список других змей
    # snake = Snake0()
    snake = get_snake('snake1')

    # Вызываем метод на экземпляре
    move = snake.move(gamestate=gs)




    # Безопасные направления: вправо, вверх, вниз
    assert move.direction() in ["right", "up", "down"]
    assert move.direction() != "left"  # Явно проверяем, что не в стену

# def test_right_wall():
#     """Змея у правой стены (x=10 при width=11) - нельзя двигаться вправо"""
#     width = 11
#     height = 11
#     you = [(width-1, 1), (width-1, 2), (width-1, 3)]
#     gs = create_minimal_game_state(you, [])
#     m = move(gs)
#
#     # Безопасные направления: влево, вверх, вниз
#     assert m["move"] in ["left", "up", "down"]
#     assert m["move"] != "right"

# def test_top_wall():  # y=10 это верх
#     you = [(5, 10), (5, 9), (5, 8)]  # y=10
#     other_snakes = [(10, 10), (10, 9), (10, 8)]  # далеко, не мешают
#
#     gs = create_minimal_game_state(you, other_snakes)
#     m = move(gs)
#     assert m["move"] in ["down", "left", "right"]
#     assert m["move"] != "up"
#
# def test_bottom_wall():  # y=0 это низ
#     you = [(5, 0), (5, 1), (5, 2)]  # y=0
#     other_snakes = [(10, 10), (10, 9), (10, 8)]  # далеко, не мешают
#
#     gs = create_minimal_game_state(you, other_snakes)
#     m = move(gs)
#     assert m["move"] in ["up", "left", "right"]
#     assert m["move"] != "down"
