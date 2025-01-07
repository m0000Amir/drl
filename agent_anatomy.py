import random
from typing import List


class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over!")
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0

    def step(self, env: Environment) -> None:
        cur_ob = env.get_observation()
        print(f'Cur ob: {cur_ob}')
        actions = env.get_actions()
        print(f'Actions: {actions}')
        reward = env.action(random.choice(actions))
        print(f'Reward: {reward}')
        self.total_reward += reward
        print(f'    Total reward:   {self.total_reward}')


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print(f'Total reward got: {agent.total_reward:.4f}')

    print('DONE!')
