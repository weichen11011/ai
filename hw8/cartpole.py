# -*- coding: utf-8 -*-
"""
Created on Sun May  5 06:13:01 2024

@author: yan10
"""

import gymnasium as gym
env = gym.make("CartPole-v1", render_mode="human") # 若改用這個，會畫圖
# env = gym.make("CartPole-v1", render_mode="rgb_array")
observation, info = env.reset(seed=42)
score = 0
def action(observation):
    if observation[3]>0:
        action = 1
    else:
        action = 0
    return action
for _ in range(1000):
   env.render()
   observation, reward, terminated, truncated, info = env.step(action(observation))
   #print('observation=', observation)
   score += reward
   if terminated or truncated:
      observation, info = env.reset()
      print('done, score=', score)
      score = 0
env.close()
