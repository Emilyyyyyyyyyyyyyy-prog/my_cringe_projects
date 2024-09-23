import numpy as np
from abc import ABC, abstractmethod


class WorldOptions(object):
    pass


options = WorldOptions()
options.board_rows = 3
options.board_cols = 4
options.win_state = (2, 3)
options.lose_state = (1, 3)
options.start_state = (0, 0)
options.obstacles = [(1, 1), (1, 2)]
options.deterministic = False


class GridWorld:
    def __init__(self, world_options):
        self.board = np.zeros([world_options.board_rows, world_options.board_cols])
        self.obstacles = world_options.obstacles
        for obs in self.obstacles:
            self.board[obs[0], obs[1]] = -1

        self.action_dict = {"up": (1, 0),
                            "down": (-1, 0),
                            "left": (0, -1),
                            "right": (0, 1)
                            }
        self.start_state = world_options.start_state
        self.state = self.start_state
        self.is_terminal_state = False
        self.win_state = world_options.win_state
        self.lose_state = world_options.lose_state
        self.deterministic = world_options.deterministic

    # Определяет вознаграждение согласно текущему состоянию
    def give_reward(self):
        if self.state == self.win_state:
            return 1
        elif self.state == self.lose_state:
            return -1
        else:
            return 0

    # Проверяет, лежит ли состояние state в границах игрового поля
    def is_within_bounds(self, state):
        return 0 <= state[0] < self.board.shape[0] and 0 <= state[1] < self.board.shape[1]

    # Возвращает валидное следущее состояние в зависимости от выбранного действия action
    def next_position(self, action, move=True):
        if not self.deterministic:
            if action == "up":
                action_dst = np.random.choice(["up", "left", "right"], p=[0.8, 0.1, 0.1])
            if action == "down":
                action_dst = np.random.choice(["down", "left", "right"], p=[0.8, 0.1, 0.1])
            if action == "left":
                action_dst = np.random.choice(["left", "up", "down"], p=[0.8, 0.1, 0.1])
            if action == "right":
                action_dst = np.random.choice(["right", "up", "down"], p=[0.8, 0.1, 0.1])
        else:
            action_dst = action

        next_state = tuple(self.state[i] + self.action_dict[action_dst][i] for i in range(2))

        if not self.is_within_bounds(next_state) or next_state in self.obstacles:
            next_state = self.state

        if move:
            self.state = next_state

            # Определяет, является ли текущее состояние state терминальным
            if (self.state == self.win_state) or (self.state == self.lose_state):
                self.is_terminal_state = True

        return next_state

    # возвращает игру в исходное состояние
    def reset(self):
        self.state = self.start_state
        self.is_terminal_state = False

    # Выводит игровое поле
    def show_board(self):
        for row_id in reversed(range(np.size(self.board, 0))):
            print('-----------------')
            out = '| '
            for col_id in range(np.size(self.board, 1)):
                if self.board[row_id, col_id] == -1:
                    token = 'X'
                if self.board[row_id, col_id] == 0:
                    token = '0'
                if (row_id, col_id) == self.win_state:
                    token = 'W'
                if (row_id, col_id) == self.lose_state:
                    token = 'L'
                if (row_id, col_id) == self.start_state:
                    token = '*'
                out += token + ' | '
            print(out)
        print('-----------------')


class Agent(ABC):

    def __init__(self, env_options):
        self.actions = ["up", "down", "left", "right"]  # множество допустимых действий

        self.learning_rate = 0.2  # показатель степени для вычисления кумулятивного вознаграждения # learning rate - \alpha
        self.exploration_rate = 0.3  # exploration rate - вероятность "попробовать пойти не туда"
        self.reward_discount = 0.9  # показатель степени для вычисления кумулятивного вознаграждения (gamma)

        self.env = GridWorld(env_options)  # интерфейс взаимодействия со средой
        self.env.show_board()

        self.traj_states = []  # последовательный набор кортежей состояние-действие, траектория
        self.init_state_values()

    # абстрактные метод для реализации в классах-наследниках
    @abstractmethod
    def init_state_values(self):  # инициализация нулями V-function или Q-function
        pass

    @abstractmethod
    def update_state_values(self):  # пересчёт значений V-function или Q-function в соответствии с алгоритмом обучения
        pass

    @abstractmethod
    def extract_value(self, action):  # чтение текущего значения V-function или Q-function
        pass

        # Выбирает лучшее действие для текущего состояния

    def choose_action(self):
        max_next_reward = 0
        action = "up"

        # Добавляем элемент случайности, чтобы агент не ходил всегда по одному пути
        if np.random.uniform(0, 1) <= self.exploration_rate:
            action = np.random.choice(self.actions)
        else:
            for a in self.actions:
                next_reward = self.extract_value(a)

                if next_reward >= max_next_reward:
                    action = a
                    max_next_reward = next_reward
        return action

    # Возвращает следующее состояние, соответствующее действию action
    def take_action(self, action):
        position = self.env.next_position(action, move=True)
        return

        # стирает информацию о пройденной агентом траектории и ставит его на стартовую позицию

    def reset(self):
        self.env.reset()
        self.traj_states = []

        # В течение нескольких раундов производим обновление значений, соответствующих каждому состоянию

    def play(self, roundsCount=10):
        round_id = 0

        while round_id < roundsCount:
            # Конец раунда
            if self.env.is_terminal_state:
                self.append_state_to_traj(self.env.state, None)

                # обновление state_values в конце раунда (из конца траектории в начао)
                self.update_state_values()

                self.reset()
                round_id += 1
            else:
                action = self.choose_action()

                prev_state = self.env.state
                # Переходим в следущее состояние, выполняя действие
                self.take_action(action)

                # Добавляем состояние к текущей траектории
                self.append_state_to_traj(prev_state, action)

    # Выводит текущие значения для всех состояний
    def show_values(self):
        for row_id in reversed(range(np.size(self.state_values, 0))):
            print('----------------------------------')
            out = '| '
            for col_id in range(np.size(self.state_values, 1)):
                out += str(self.state_values[(row_id, col_id)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')


class Agent_V(Agent):
    def init_state_values(self):
        self.state_values = np.zeros(np.shape(self.env.board))

    def append_state_to_traj(self, state, action):
        self.traj_states.append(state)

    def update_state_values(self):
        reward = self.env.give_reward()
        self.state_values[self.env.state] = reward

        for state in reversed(self.traj_states):
            reward = self.state_values[state] + self.learning_rate * (reward - self.state_values[state])  # формула (1)
            self.state_values[state] = round(reward, 3)

    def extract_value(self, action):
        next_state = self.env.next_position(action, move=False)
        return self.state_values[next_state]
