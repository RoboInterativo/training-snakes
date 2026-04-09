import json
str1 ="""
{
      "game": {
        "id": "a3f61692-8538-497e-b4dd-71e5e7ebe68b",
        "ruleset": {
          "name": "standard",
          "version": "v1.0.0",
          "settings": {
            "foodSpawnChance": 15,
            "minimumFood": 1,
            "hazardDamagePerTurn": 15,
            "royale": {
              "shrinkEveryNTurns": 0
            },
            "squad": {
              "allowBodyCollisions": false,
              "sharedElimination": false,
              "sharedHealth": false,
              "sharedLength": false
            }
          }
        },
        "timeout": 500,
        "map": "",
        "source": ""
      },
      "turn": 2,
      "board": {
        "height": 11,
        "width": 11,
        "food": [
          {
            "x": 2,
            "y": 6
          },
          {
            "x": 5,
            "y": 5
          }
        ],
        "snakes": [
          {
            "id": "654fb7ce-a615-403e-830b-3d56bff968d5",
            "name": "sneke-sergvag77",
            "health": 98,
            "body": [
              {
                "x": 0,
                "y": 4
              },
              {
                "x": 0,
                "y": 5
              },
              {
                "x": 1,
                "y": 5
              }
            ],
            "head": {
              "x": 0,
              "y": 4
            },
            "length": 3,
            "latency": "40",
            "shout": "",
            "squad": "",
            "customizations": {
              "color": "",
              "head": "",
              "tail": ""
            }
          },
          {
            "id": "876fc201-06c6-473a-89e9-603c2d49a7c6",
            "name": "robosnake",
            "health": 100,
            "body": [
              {
                "x": 10,
                "y": 6
              },
              {
                "x": 9,
                "y": 6
              },
              {
                "x": 9,
                "y": 5
              },
              {
                "x": 9,
                "y": 5
              }
            ],
            "head": {
              "x": 10,
              "y": 6
            },
            "length": 4,
            "latency": "39",
            "shout": "",
            "squad": "",
            "customizations": {
              "color": "",
              "head": "",
              "tail": ""
            }
          }
        ],
        "hazards": []
      },
      "you": {
        "id": "654fb7ce-a615-403e-830b-3d56bff968d5",
        "name": "sneke-sergvag77",
        "health": 98,
        "body": [
          {
            "x": 0,
            "y": 4
          },
          {
            "x": 0,
            "y": 5
          },
          {
            "x": 1,
            "y": 5
          }
        ],
        "head": {
          "x": 0,
          "y": 4
        },
        "length": 3,
        "latency": "40",
        "shout": "",
        "squad": "",
        "customizations": {
          "color": "",
          "head": "",
          "tail": ""
        }
      }
}"""
real_json1=json.loads(str1)
