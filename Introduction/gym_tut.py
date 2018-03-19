import gym
import time


env = gym.make('CartPole-v0')
# env = gym.make('MountainCar-v0')
# env = gym.make('MsPacman-v0')
# env = gym.make('Hopper-v1')

env.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample()) # take a random action
#     time.sleep(0.01)

print(env.action_space)
#discrete(2) {0, 1} => {left, right}
print(env.observation_space)
#box(4,)


q_table=np.zeros((2, 4))

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        time.sleep(0.1)
        env.render()

        #what is observed(states)
        print(observation)
        action = env.action_space.sample()
        
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break


# from gym import spaces
# space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}

# x = space.sample()

# assert space.contains(x)
# assert space.n == 8