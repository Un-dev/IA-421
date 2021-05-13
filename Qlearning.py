# coding=utf-8

import gameGrid6
import random 

current_state = "s1"


learning_rate = 0.1



#chooses a random action and plays it
def explore(state, Q):
  action = actions[random.randint(0,3)]
  print("exploration vers : "+action)
  value = newQValue(Q, state, action)
  Q = updateQtable(value, action, state, Q)
  return transitions(state, action)

#chooses the best action according to Q and plays it
def exploit(state, Q):
  stateIdx = stateIndex(state)
  s_actions = [Q["up"][stateIdx], Q["down"][stateIdx], Q["right"][stateIdx], Q["left"][stateIdx]]
  action = action_from_index(s_actions.index(max(s_actions)))
  value = newQValue(Q, state, action )
  Q = updateQtable(value, action, state, Q)
  return transitions(state, action)

#calculates new Q for given state and action pair
def newQValue(Q, state, action):
  new_value = gameGrid6.rewards(state, action) #+ GAAM*0
  return (1-learning_rate) * Q[action][stateIndex(state)] + learning_rate * (new_value)

def updateQtable(value, action, state, Q):
  state_idx = stateIndex(state)
  Q[action][state_idx] = value
  return Q

def learnEpisode(s, Q, e):
  current_state = s
  print("started at : " + current_state)
  while not gameGrid6.isEnd(current_state):
    #exploit
    if (epsilonGreedy(e) == 0):
      current_state = exploit(current_state, Q)
      print(current_state)
    #explore
    else:
      current_state = explore(current_state, Q)
      print(current_state)
  print("===========")
  print(Q["up"])
  print(Q["down"])
  print(Q["left"])
  print(Q["right"])
  return Q


