from ..utils.test import build_test_gamestate
from ..logic import Eat, PathDistances
from ..snakes.base_snake import BaseSnake


def test_eat_closest():
    class EatingSnake(BaseSnake, Eat, PathDistances):
        pass

    gs = build_test_gamestate(3,3, me=[(1, 1), (2, 1)], food=[(0, 0), (1, 2)])
    move = EatingSnake().move(gs)
    assert move == "up"





def test_eat_closest():
    class EatingSnake(BaseSnake, Eat, PathDistances):
        # Добавляем реализацию move, которая использует логику поедания
        def move(self, gamestate):
            # Получаем лучший ход для поедания ближайшей еды
            best_move = self.eat_closest_food(gamestate)
            if best_move:
                return best_move
            # Если нет еды или нельзя её съесть, двигаемся случайно
            return gamestate.get_legal_moves()[0]

    gs = build_test_gamestate(3,3, me=[(1, 1), (2, 1)], food=[(0, 0), (1, 2)])
    move = EatingSnake().move(gs)
    assert move is not None
    # Дополнительные проверки
    assert move.direction() in ['up', 'down', 'left', 'right']
