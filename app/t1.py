from utils.vector import Vector
# v=Vector(0,1)
# print(v)
from utils.snake import Snake
from utils.test import build_test_gamestate
d={'id': '654fb7ce-a615-403e-830b-3d56bff968d5',
 'name': 'sneke-sergvag77',
 'health': 98,
 'body': [{'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 1, 'y': 5}],
 'head': {'x': 0, 'y': 4},
 'length': 3,
 'latency': '40',
 'shout': '',
 'squad': '',
 'customizations': {'color': '', 'head': '', 'tail': ''}}
# snake=Snake(d)
# print (snake.coords[1])
# # print (snake._coords)
#
# _coords

gs = build_test_gamestate(1, 2, me=[(0, 1), (0, 2),(0,3)])

print (str(gs.me.neck ))
#     gs.me.neck== V(0, 2)
# gs=build_test_gamestate()
