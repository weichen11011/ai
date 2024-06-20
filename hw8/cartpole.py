# -*- coding: utf-8 -*-
"""
Created on Sun May  5 06:13:01 2024

@author: yan10
"""
# 修改至 https://github.com/ccc112b/py2cs/blob/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-%E5%BC%B7%E5%8C%96%E5%AD%B8%E7%BF%92/01-%E5%BC%B7%E5%8C%96%E5%AD%B8%E7%BF%92/01-gym/04-run/cartpole_human_run.py
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
