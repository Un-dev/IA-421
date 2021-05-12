# coding=utf-8

import gameGrid6
import random 

current_state = "s1"
q_table = {
  "up": [0,0,0,0,0,0],
  "down": [0,0,0,0,0,0],
  "right": [0,0,0,0,0,0],
  "left": [0,0,0,0,0,0],
}


learning_rate = 0.1
actions= ["up", "down", "right", "left"]

def transitions(state, action):
    next_state = state
    if (state == "s0" and action == "down") :
        next_state= "s4"
    elif (state == "s1" and action == "down") :
        next_state= "s3"
    elif (state == "s1" and action == "up") :
        next_state= "s5"
    elif (state == "s2" and action == "left") :
        next_state= "s3"
    elif (state == "s3" and action == "left") :
        next_state= "s4"
    elif (state == "s3" and action == "up") :
        next_state= "s1"
    elif (state == "s3" and action == "right") :
        next_state= "s2"
    elif (state == "s4" and action == "down") :
        next_state= "s5"
    elif (state == "s4" and action == "right") :
       next_state= "s3"
    elif (state == "s4" and action == "up") :
       next_state= "s0"

    return next_state

#chooses whether to explore or exploit
def epsilonGreedy(e):
  #exploitation
  if random.uniform(0, 1) > e:
    return 0
  #exploration
  else:
    return 1

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
  print("exploitation vers : "+action)
  value = newQValue(Q, state, action )
  Q = updateQtable(value, action, state, Q)
  return transitions(state, action)


#given an index, return the name of an action
def action_from_index(index):
  if (index == 0):
    return "up"
  elif (index == 1):
    return "down"
  elif (index == 2):
    return "right"
  elif (index == 3):
    return "left"

#given an index, return the name of a state
def stateIndex(state):

  if (state == "s0"):
    return 0
  elif (state == "s1"):
    return 1
  elif (state == "s2"):
    return 2
  elif (state == "s3"):
    return 3
  elif (state == "s4"):
    return 4
  else:
    return 5

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


