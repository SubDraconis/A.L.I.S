import numpy as np

class QLearningAgent:
    def __init__(self, states, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.q_table = np.zeros((states, actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.actions = actions

    def choose_action(self, state):
        if np.random.random() < self.exploration_rate:
            # Eksploracja: losowa akcja
            return np.random.choice(self.actions)
        else:
            # Wykorzystanie: akcja z najwyższą wartością Q
            return np.argmax(self.q_table[state, :])

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state, action]
        target = reward + self.discount_factor * np.max(self.q_table[next_state, :])
        self.q_table[state, action] += self.learning_rate * (target - predict)

# Przykład użycia (uproszczony system walki)
states = 10 # Przykładowo, 10 stanów zdrowia
actions = 2 # 0 - atak, 1 - obrona - ZMIENIONO: teraz liczba akcji
agent = QLearningAgent(states, actions)

# Pętla uczenia
episodes = 1000
for episode in range(episodes):
    state = np.random.randint(0, states) # Początkowy stan
    done = False
    while not done:
        action = agent.choose_action(state)
        # Symulacja środowiska (tutaj trzeba by zaimplementować logikę walki)
        if action == 0: # Atak
            reward = 1 if np.random.random() > 0.5 else -1 # Losowa nagroda za atak
            next_state = min(states - 1, state + 1) if reward > 0 else max(0, state -1)
        else: # Obrona
            reward = 0.5 # Mała nagroda za obronę
            next_state = state
        agent.learn(state, action, reward, next_state)
        state = next_state
        if state == 0 or state == states -1:
            done = True

print(agent.q_table)