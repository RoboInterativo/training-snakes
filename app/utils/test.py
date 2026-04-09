from .game_state import GameState


def build_test_gamestate(width=3, height=3, me=[(0,0)], opponents=[], food=[]):

    def _tuples_to_snake(tuples):
        return {
        "body":   _tuples_to_coords(tuples),
        "health": 100,
        "id": "58a0142f-4cd7-4d35-9b17-815ec8ff8e70",
        "length": len(tuples),
        "name": "Sonic Snake"

      }

    def _tuples_to_coords(tuples):
        return [{
            "x": t[0],
            "y": t[1]
        } for t in tuples]
    data= {
    "turn": 0,
    "game":{

    },
    "board":
     {
      "food":  _tuples_to_coords(food),
       "snakes": [_tuples_to_snake(coords) for coords in opponents],
       "height": height,
        "width": width,

    },
    "you": _tuples_to_snake(me)
    }


    data["board"]["snakes"].append(data["you"])
    gs = GameState(data)
    return gs
