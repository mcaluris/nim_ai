AI that teaches itself to play Nim through reinforcement learning(Q-learning).

Markov Decision Processes

Reinforcement learning can be viewed as a Markov decision process, having the following properties:

    Set of states S
    Set of actions Actions(S)
    Transition model P(s’ | s, a)
    Reward function R(s, a, s’)


Q-Learning

Q-Learning is one model of reinforcement learning, where a function Q(s, a) outputs an estimate of the value of taking action a in state s.

The model starts with all estimated values equal to 0 (Q(s,a) = 0 for all s, a). When an action is taken and a reward is received, the function does two things: 1) it estimates the value of Q(s, a) based on current reward and expected future rewards, and 2) updates Q(s, a) to take into account both the old estimate and the new estimate. This gives us an algorithm that is capable of improving upon its past knowledge without starting from scratch.

Q(s, a) ⟵ Q(s, a) + α(new value estimate - Q(s, a))

The updated value of Q(s, a) is equal to the previous value of Q(s, a) in addition to some updating value. This value is determined as the difference between the new value and the old value, multiplied by α, a learning coefficient. When α = 1 the new estimate simply overwrites the old one. When α = 0, the estimated value is never updated. By raising and lowering α, we can determine how fast previous knowledge is being updated by new estimates.

The new value estimate can be expressed as a sum of the reward (r) and the future reward estimate. To get the future reward estimate, we consider the new state that we got after taking the last action, and add the estimate of the action in this new state that will bring to the highest reward. This way, we estimate the utility of making action a in state s not only by the reward it received, but also by the expected utility of the next step. The value of the future reward estimate can sometimes appear with a coefficient gamma that controls how much future rewards are valued. We end up with the following equation:

Q Learning Formula

A Greedy Decision-Making algorithm completely discounts the future estimated rewards, instead always choosing the action a in current state s that has the highest Q(s, a).

This brings us to discuss the Explore vs. Exploit tradeoff. A greedy algorithm always exploits, taking the actions that are already established to bring to good outcomes. However, it will always follow the same path to the solution, never finding a better path. Exploration, on the other hand, means that the algorithm may use a previously unexplored route on its way to the target, allowing it to discover more efficient solutions along the way. For example, if you listen to the same songs every single time, you know you will enjoy them, but you will never get to know new songs that you might like even more!

To implement the concept of exploration and exploitation, we can use the ε (epsilon) greedy algorithm. In this type of algorithm, we set ε equal to how often we want to move randomly. With probability 1-ε, the algorithm chooses the best move (exploitation). With probability ε, the algorithm chooses a random move (exploration).

Another way to train a reinforcement learning model is to give feedback not upon every move, but upon the end of the whole process. For example, consider a game of Nim. In this game, different numbers of objects are distributed between piles. Each player takes any number of objects from any one single pile, and the player who takes the last object looses. In such a game, an untrained AI will play randomly, and it will be easy to win against it. To train the AI, it will start from playing a game randomly, and in the end get a reward of 1 for winning and -1 for losing. When it is trained on 10,000 games, for example, it is already smart enough to be hard to win against it.

This approach becomes more computationally demanding when a game has multiple states and possible actions, such as chess. It is infeasible to generate an estimated value for every possible move in every possible state. In this case, we can use a function approximation, which allows us to approximate Q(s, a) using various other features, rather than storing one value for each state-action pair. Thus, the algorithm becomes able to recognize which moves are similar enough so that their estimated value should be similar as well, and use this heuristic in its decision making.

$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.