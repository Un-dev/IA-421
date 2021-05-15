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
def print_q_table():
  line ="     "
  for i in range(0, len(STATES)):
    line += str(STATES[i][0]) + str(STATES[i][1]) + str(STATES[i][2]) +"   "
  line += "11x   xxx  else"
  print(line)
  print("    ----------------------------------------------------------")
  for i in range(0, len(q_table.keys())):
    line = str(i) + " | "
    for j in range(0, len(q_table[i])):
      if (int(q_table[i][j]) < 1000):
        line += " "
      if (int(q_table[i][j]) < 100):
        line += " "
      if (int(q_table[i][j]) < 10):
        line += " "

      line += str(int(q_table[i][j]))+", "
    print(line)

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
  next_state = [None] * 3
  for i, item in enumerate(action):
    if (item == True):
      next_state[i] = random.randint(1,6)
    else:
      next_state[i] = state[i]

  return sorted(next_state)

#chooses whether to explore or exploit
def epsilon_greedy(e):
  #exploitation
  if random.uniform(0, 1) > e:
    return False
  #exploration
  else:
    return True

#avec l'etat 456 je relance le dé 2 et 3

def learn_episode():
  # an episode is composed of 3 rounds
  # first round where we roll every dices
  current_state = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6)])
  # two more rounds
  for i in range(0, 2):
    if (epsilon_greedy(EPSILON)):
      # if e_greedy returns true we explore
      current_state = sorted(explore(current_state, i==1))
    else: 
      # otherwise we exploit
      current_state = sorted(exploit(current_state))
  return current_state
    

# plays a random action and updates Q_table 
def explore(state, last):
  # chooses random number between 0 and 7, that will be our action to execute
  action = ACTIONS[random.randint(0,7)]
  # changes the state
  next_state = transition(state, action)

  # updates q_table
  update_q_table(state, action, next_state, last)
  return next_state

# chooses the best action according to Q_table
def exploit(state):
  # takes the given state and iterates over q_table's corresponding index
  state_idx = index_of_state(state)
  state_actions_values = [None] * len(q_table)
  for i in range(0, len(q_table)):
    state_actions_values[i] = [q_table[i][state_idx]]
  # finds the index of the best action
  best_action_index = state_actions_values.index(max(state_actions_values))
  # plays it 
  action_to_play = ACTIONS[best_action_index]
  next_state = transition(state,action_to_play)
  return next_state

# finds index in STATES of the given state
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

# finds index in ACTIONS of the given action
def index_of_action(action):
  for i, item in enumerate(ACTIONS):
    if(ACTIONS[i][0] == action[0] and ACTIONS[i][1] == action[1] and ACTIONS[i][2] == action[2]):
      return i

# finds the index of the best action in q_table for given state
def best_action_index(state):
  # takes the given state and iterates over q_table's corresponding index
  state_idx = index_of_state(state)
  state_actions_values = [q_table[0][state_idx]]
  for i in range(0, len(q_table)):
    state_actions_values = [q_table[i][state_idx]]
  # finds the index of the best action
  return  state_actions_values.index(max(state_actions_values))


# changes the value of q_table for state/action couple
def update_q_table(state, action, next_state, last):
  best_next_action= best_action_index(next_state)
  state_index = index_of_state(state)
  action_index = index_of_action(action)
  Qvalue = (1-learning_rate) * q_table[action_index][state_index] + learning_rate * (reward(state, last) + GAMMA*q_table[best_next_action][index_of_state(next_state)])
  q_table[action_index][state_index] = Qvalue

def play_n_episodes(n):
  for i in range(0, n):
    learn_episode()



# play_n_episodes(10)
play_n_episodes(300000)
print_q_table()

def play_a_game():
  current_state = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6)])
  for i in range(0, 2):
    current_state = sorted(exploit(current_state))
  return reward(current_state, True)

def play_n_game(n):
  mean_score = 0
  for i in range(0, n):
    # print(play_a_game())
    mean_score += play_a_game()
  return mean_score/n

n = 10000
print("mean score of "+str(n)+" games : ")
print(play_n_game(10000))

print(reward([1,1,1], True))
