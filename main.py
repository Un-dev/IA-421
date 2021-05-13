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

q_table = {
  0: [0,0,0,0,0,0],
  1: [0,0,0,0,0,0],
  2: [0,0,0,0,0,0],
  3: [0,0,0,0,0,0],
  4: [0,0,0,0,0,0],
  5: [0,0,0,0,0,0],
  6: [0,0,0,0,0,0],
  7: [0,0,0,0,0,0],
}

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

#chooses whether to explore or exploit
def epsilon_greedy(e):
  #exploitation
  if random.uniform(0, 1) > e:
    return False
  #exploration
  else:
    return True

#avec l'etat 456 je relance le dé 2 et 3

print(transition([4, 5, 6], [False, True, True]))
print(reward(sorted([2, 4, 1]), last=True))

def learn_episode()
  # un episode est composé de 3 lancé
  for i in range(0, 3):
    if (epsilon_greedy(EPSILON)){
      # if e_greedy returns true we explore
      explore()
    } else {
      # otherwise we exploit
      exploit()
    }

# plays a random action and updates Q_table 
def explore()
  pass

# chooses the best action according to Q_table
def exploit()
  pass
