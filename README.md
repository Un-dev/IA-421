# IA-421

This is our final project for the course of Mrs Karami at the Catholic University of Lille.
It is an adaptation of the [421](<https://fr.wikipedia.org/wiki/421_(jeu)>) dice game with the Qlearning algorithm.

Ceci est notre projet final en apprentissage renforcé, un cours donné par Mme KARAMI.
Il s'agit d'une adaptation du jeu du [421](<https://fr.wikipedia.org/wiki/421_(jeu)>) avec l'algorithme du Qlearning


## Authors

- [Denis D'Almeida](https://github.com/denisjunior)
- [François Lannoy](https://github.com/Un-dev)

# la fonction "print_q_table"
  elle permet d'afficher les résultats de l'apprentissage de l'agent IA
# la fonction "reward"
  cette fonction prend en paramètre un état et la dernière action, elle permet d'attribuer une récompense au dernier "Roll"
# la fonction "transition"
  elle retourne l'état suivant en fonction du l'état et de l'action passés
# la fonction "epsilon_greedy"
  elle choisi d'explorer ou d'exploiter le tableau en fonction du parametre epsilon
# la fonction "learn_episode"
  c'est la fonction qui permet à l'agent d'apprendre, en fonction du round, la fonction permet à l'agent de faire un "explore" ou un "exploit" en fonction de "epsilon_greedy"
# la fonction "explore"
  choisi un nombre aléatoirement entre 0 et 7 qui est le nombre d'action possible par dé puissance nombre de dé. L'action choisi sera donc exécuté, ensuite l'état suivant est changé et le "q_table est mise à jour
# la fonction "exploit"
  celle ci choisi la meilleure action par dans la Qtable par rapport au state actuel.
