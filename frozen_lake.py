import gymnasium as gym

env = gym.make("FrozenLake-v1", is_slippery = False, render_mode="human")
env.reset()

episode_number  = 100
timestep_number = 100
directory = './video'

for episode in range(episode_number):
    print(observation)
    for timestep in range(timestep_number):

        env.render()
        action = env.action_space.sample()
        observation, reward, done, info, _ = env.step(action)

        if done:
            print('Episode : {:02d} | Timestep : {:02d} | Rewards : {:02.0f}'.format(episode + 1, timestep + 1, reward))
            break
env.render()

env.close()
