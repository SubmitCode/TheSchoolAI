import numpy as np
import gym
import matplotlib.pyplot as plt


# parameters = np.random.rand(4)
#action = 0 if np.matmul(parameters, observation) < 0 else 1 

env = gym.make("CartPole-v0")


def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0

    for _ in range(200):
        action = 0 if np.matmul(parameters, observation) < 0 else 1 
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    
    return totalreward


#################
## Random Search
#################


goal_reached_at = []
for _ in range(25):
    bestparams = None
    bestreward = 0
    for i in range(1000):
        parameters = np.random.rand(4) * 2 - 1
        reward = run_episode(env, parameters)
        if reward > bestreward:
            bestreward = reward
            bestparams = parameters
            if reward == 200:
                goal_reached_at.append(i)
                print("goal reached at {}".format(i))
                break

print("average episodes needed with random search is {}".format(np.mean(goal_reached_at)))





#################
## Hill Climbing
#################

noise_scaling = 0.1
goal_reached_at = []
for _ in range(25):
    parameters = np.random.rand(4) * 2 - 1
    bestreward = 0
    for i in range(10000):

        # if i % 100 == 0:
        #     print("i={}".format(i))
        newparams = parameters + (np.random.rand(4) * 2 - 1) * noise_scaling
        reward = 0
        reward = run_episode(env, parameters)
        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            if reward == 200:
                print("goal reached at {}".format(i))
                break


print("average episodes needed with Hill Climbing is {}".format(np.mean(goal_reached_at)))
