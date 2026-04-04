from ..utils.vector import Vector, up, down, left, right, noop
from .base_snake import BaseSnake


def move(self, gamestate):
    current_vector = gamestate.me.current_direction
    if current_vector != noop:
        return current_vector

    head = gamestate.me.head
    l_wall = (0, head.y)           # Кортеж вместо Vector
    r_wall = (gamestate.board_width-1, head.y)
    t_wall = (head.x, 0)
    b_wall = (head.x, gamestate.board_width-1)

    # Придётся изменить метод farthest, чтобы он работал с кортежами
    # Или преобразовать векторы в кортежи
    walls_as_vectors = [Vector(x, y) for (x, y) in [l_wall, r_wall, t_wall, b_wall]]
    farthest = head.farthest(walls_as_vectors)

    # Преобразуем farthest в кортеж для сравнения
    farthest_tuple = (farthest.x, farthest.y)

    return {
        l_wall: left,
        r_wall: right,
        t_wall: up,
        b_wall: down,
    }.get(farthest_tuple, up)

class Snake0(BaseSnake):

    def move(self, gamestate):

        current_vector = gamestate.me.current_direction
        if current_vector != noop:
            return current_vector

        head = gamestate.me.head
        l_wall = Vector(0, head.y)
        r_wall = Vector(gamestate.board_width-1, head.y)
        t_wall = Vector(head.x, 0)
        b_wall = Vector(head.x, gamestate.board_width-1)
def move(self, gamestate):
    current_vector = gamestate.me.current_direction
    if current_vector != noop:
        return current_vector

    head = gamestate.me.head
    l_wall = (0, head.y)           # Кортеж вместо Vector
    r_wall = (gamestate.board_width-1, head.y)
    t_wall = (head.x, 0)
    b_wall = (head.x, gamestate.board_width-1)
    
    # Придётся изменить метод farthest, чтобы он работал с кортежами
    # Или преобразовать векторы в кортежи
    walls_as_vectors = [Vector(x, y) for (x, y) in [l_wall, r_wall, t_wall, b_wall]]
    farthest = head.farthest(walls_as_vectors)

    # Преобразуем farthest в кортеж для сравнения
    farthest_tuple = (farthest.x, farthest.y)

    return {
        l_wall: left,
        r_wall: right,
        t_wall: up,
        b_wall: down,
    }.get(farthest_tuple, up)
        # farthest = head.farthest([l_wall, r_wall, t_wall, b_wall])
        # return {
        #     l_wall: left,
        #     r_wall: right,
        #     t_wall: up,
        #     b_wall: down,
        # }.get(farthest, up)

    def name(self):
        return "Training Snake 0"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass
