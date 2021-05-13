# coding=utf-8

import random
STATES = [
  {
    "Récompense": 800,
    0: 1,
    1: 2,
    2: 4
  }, 
  {
    "Récompense": 700,
    0: 1,
    1: 1,
    2: 1
  }, 
  {
    "Récompense": 203,
    0: 1,
    1: 2,
    2: 3
  }, 
  {
    "Récompense": 204,
    0: 2,
    1: 3,
    2: 4}, 
  {
    "Récompense": 205,
    0: 3,
    1: 4,
    2: 5
  }, 
  {
    "Récompense": 206,
    0: 4,
    1: 5,
    2: 6
  }, 
  {
    "Récompense": 0,
    0: 1,
    1: 2,
    2: 2
  }]

ACTIONS = [
  [False, False, False],
  [False, False, True],
  [False, True, False],
  [False, True, True],
  [True, False, False],
  [True, False, True],
  [True, True, False],
  [True, True, True]
]
GAMMA = 0.9
EPSILON = 0.1

def reward(state, last):
  if (last == False):
    return 0
  else:
    for i, item in enumerate(STATES):
      if(STATES[i][0] == state[0] and STATES[i][1] == state[1] and STATES[i][2] == state[2]): 
        return STATES[i]["Récompense"]
    return 100+state[maxindex(state)]
    

def transition(state, action):
  for i, item in enumerate(action):
    if (item == True):
      state[i] = random.randint(1,6)

  return state

#avec l'etat 456 je relance le dé 2 et 3

print(transition([4, 5, 6], [False, True, True]))
print(reward(sorted([2, 4, 1]), True))
