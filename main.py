# coding=utf-8

import random
STATES = [
  {
    "Récompense": 800,
    "0": 1,
    "1": 2,
    "2": 4}, 
  {
    "Récompense": 700,
    "0": 1,
    "1": 1,
    "2": 1}, 
  {
    "Récompense": 203,
    "0": 1,
    "1": 2,
    "2": 3}, 
  {
    "Récompense": 204,
    "0": 2,
    "1": 3,
    "2": 4}, 
  {
    "Récompense": 205,
    "0": 3,
    "1": 4,
    "2": 5
  }, 
  {
    "Récompense": 206,
    "0": 4,
    "1": 5,
    "2": 6
  }, 
  {
    "Récompense": 0,
    "0": 1,
    "1": 2,
    "2": 2
  }]

# def reward(state, action):

def transition(state, action):
  # print(state["0"])
  for i, item in enumerate(action):
    if (item == True):
      state[str(i)] = random.randint(1,6)

  return state

#avec l'etat 456 je relance le dé 2 et 3

print(transition({"0": 4, "1": 5, "2": 6}, [False, True, True]))

