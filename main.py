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
  0: [0,0,0,0,0,0,0,0,0,0],
  1: [0,0,0,0,0,0,0,0,0,0],
  2: [0,0,0,0,0,0,0,0,0,0],
  3: [0,0,0,0,0,0,0,0,0,0],
  4: [0,0,0,0,0,0,0,0,0,0],
  5: [0,0,0,0,0,0,0,0,0,0],
  6: [0,0,0,0,0,0,0,0,0,0],
  7: [0,0,0,0,0,0,0,0,0,0],

}

GAMMA = 0.9
EPSILON = 0.1
learning_rate = 0.1

def reward(state, last):
  # reward is given only for the last rolls
  if (last == False):
    return 0
  else:
    for i, item in enumerate(STATES):
      # if state is part of the STATES constant we just return the reward
      if(STATES[i][0] == state[0] and STATES[i][1] == state[1] and STATES[i][2] == state[2]): 
        return STATES[i]["Récompense"]
    # else it means we are in special cases
    if (state[0] == 1 and state[1] == 1):
      # 11x -> 400 pts + x
      return 400+state[2]
    elif (state[0] == state[1] and state[1] == state[0]):
      # xxx -> 300 + x
      return 300 + state[0]
    else: 
      # else 100 + highest dice
      return 100+state[2]
    

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

def learn_episode():
  # an episode is composed of 3 dice rolls
  current_state = 0
  for i in range(0, 3):
    if (epsilon_greedy(EPSILON)):
      # if e_greedy returns true we explore
      explore()
    else: 
      # otherwise we exploit
      current_state = exploit()
    return current_state
    

# plays a random action and updates Q_table 
def explore(state):
  # chooses random number between 0 and 7, that will be our action to execute
  action = ACTIONS[random.randint(0,7)]
  print("exploitation vers : "+action)
  # changes the state
  next_state = transition(state, action)
  state_index = index_of_state(state)
  action_index = index_of_action(action)
  # updates q_table
  update_q_table(state_index, action_index, next_state)

  pass

# chooses the best action according to Q_table
def exploit(state):
  # takes the given state and iterates over q_table's corresponding index
  state_idx = index_of_state(state)
  state_actions_values = [q_table[0][state_idx]]
  for i in range(0, len(q_table)):
    state_actions_values = [q_table[i][state_idx]]
  # finds the index of the best action
  best_action_index = state_actions_values.index(max(state_actions_values))
  # plays it 
  action_to_play = ACTIONS[best_action_index]
  next_state = transition(state,action_to_play)
  return next_state

def index_of_state(state):
  for i, item in enumerate(STATES):
    if(STATES[i][0] == state[0] and STATES[i][1] == state[1] and STATES[i][2] == state[2]):
      return i
  if (state[0] == 1 and state[1] == 1):
    return 7
  elif (state[0] == state[1] and state[1] == state[0]):
    return 8
  else: 
    return 9

def index_of_action(action):
  for i, item in enumerate(ACTIONS):
    if(ACTIONS[i][0] == action[0] and ACTIONS[i][1] == action[1] and ACTIONS[i][2] == action[2]):
      return i

def best_action_index(state):
  # takes the given state and iterates over q_table's corresponding index
  state_idx = index_of_state(state)
  state_actions_values = [q_table[0][state_idx]]
  for i in range(0, len(q_table)):
    state_actions_values = [q_table[i][state_idx]]
  # finds the index of the best action
  return  state_actions_values.index(max(state_actions_values))


def update_q_table(state, action, next_state):
  # change the value of q_table for state/action couple
  best_next_action= best_action_index(next_state)
  Qvalue = (1-learning_rate) * q_table[state][action] + learning_rate(reward(STATES[state],ACTIONS[action]) + GAMMA*q_table[next_state][best_next_action])

  return Qvalue