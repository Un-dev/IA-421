# IA-421

This is our final project for the course of Mrs Karami at the Catholic University of Lille.
It is an adaptation of the [421](<https://fr.wikipedia.org/wiki/421_(jeu)>) dice game with the Qlearning algorithm.

## Authors

- [Denis D'Almeida](https://github.com/denisjunior)
- [François Lannoy](https://github.com/Un-dev)

# la fonction "print_q_table"
  elle permet d'afficher les résultats de l'apprentissage de l'agent IA
  ![resultat](https://user-images.githubusercontent.com/50630269/118365405-f54e3100-b59c-11eb-9a53-4f5e58a949e5.jpg)

  
# la fonction "reward"
  cette fonction prend en paramètre un état et la dernière action, elle permet d'attribuer une récompense au dernier "Roll"
# la fonction "transition"
  elle retourne la probabilité d'atteindre une un état St+1 en faisant une action depuis un état S
# la fonction "epsilon_greedy"
# la fonction "learn_episode"
  c'est la fonction qui permet à l'agent d'apprendre, en fonction du round, la fonction permet à l'agent de faire un "explore" ou un "exploit" en fonction de "epsilon_greedy"
# la fonction "explore"
  choisi un nombre aléatoirement entre 0 et 7 qui est le nombre d'action possible par dé puissance nombre de dé. L'action choisi sera donc exécuté, ensuite l'état suivant est changé et le "q_table" est mise à jour
# la fonction "exploit"
  celle ci choisi la meilleur action par rapport au "q_table", elle prend un état en paramètre et itère sur la "q_table" pour trouver l'index correspondant.
