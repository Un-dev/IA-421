# coding=utf-8

import random
STATES = [
  {
    "Récompense": 800,
    "1": 1,
    "2": 2,
    "3": 4}, 
  {
    "Récompense": 700,
    "1": 1,
    "2": 1,
    "3": 1}, 
  {
    "Récompense": 203,
    "1": 1,
    "2": 2,
    "3": 3}, 
  {
    "Récompense": 204,
    "1": 2,
    "2": 3,
    "3": 4}, 
  {
    "Récompense": 205,
    "1": 3,
    "2": 4,
    "3": 5
  }, 
  {
    "Récompense": 206,
    "1": 4,
    "2": 5,
    "3": 6
  }, 
  {
    "Récompense": 0,
    "1": 1,
    "2": 2,
    "3": 2
  }]

# def reward(state, action):

def transition(state, action):
  print(state[0])
  # for i in action.item
  #   if (item):
  #     state[i] = random.randint(1,6)
  # return state

#avec l'etat 456 je relance le dé 2 et 3
transition({"1": 4, "2": 5, "3": 6}, [False, True, True])