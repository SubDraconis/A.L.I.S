import random
import numpy as np

# Klasa agenta Q-learning
class QLearningAgent:
    # Inicjalizacja agenta
    def __init__(self, states, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.2):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.states = states
        self.actions = actions

    # Wybór akcji na podstawie stanu
    def choose_action(self, state):
        if random.random() < self.exploration_rate:
            return random.choice(range(self.actions))
        else:
            if state in self.q_table and self.q_table[state]:
                return max(self.q_table[state], key=self.q_table[state].get)
            else:
                return random.choice(range(self.actions))

    # Uczenie się agenta
    def learn(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {}
        if action not in self.q_table[state]:
            self.q_table[state][action] = 0

        if next_state not in self.q_table:
            self.q_table[next_state] = {}

        old_value = self.q_table[state][action]
        next_max = max(self.q_table[next_state].values()) if self.q_table[next_state] else 0

        new_value = (1 - self.learning_rate) * old_value + self.learning_rate * (reward + self.discount_factor * next_max)
        self.q_table[state][action] = new_value

states = 10
actions = 3
agent = QLearningAgent(states, actions)

episodes = 1000
for episode in range(episodes):
    state = np.random.randint(0, states)
    done = False
    while not done:
        action = agent.choose_action(state)
        if action == 0:
            reward = 1 if np.random.random() > 0.5 else -1
            next_state = min(states - 1, state + 1) if reward > 0 else max(0, state -1)
        elif action == 1:
            reward = 0.5
            next_state = state
        else:
            reward = -0.5
            next_state = max(0, state - 1)
        agent.learn(state, action, reward, next_state)
        state = next_state
        if state == 0 or state == states -1:
            done = True

print(agent.q_table)