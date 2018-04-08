import argparse
import os
import shutil
import sys

# Parse arguments
parser = argparse.ArgumentParser(description="Run simulator with specified agent and environment.")
parser.add_argument('agent', choices=['AgentRandom', 'AgentQ'], help='the agent to simulate')
parser.add_argument('game', choices=['explore'], help='the game to simulate')
parser.add_argument('num_training_games', type=int, help='the number of training games to play')
parser.add_argument('output_dir', help='the directory to save simulation results')
args = parser.parse_args()

# Output directory
shutil.rmtree(args.output_dir, ignore_errors=True)
os.makedirs(args.output_dir)

# Initialize agent
if args.agent == 'AgentRandom':
    from agents.AgentRandom import AgentRandom
    agent1 = AgentRandom()
    agent2 = None
elif args.agent == 'AgentQ':
    from agents.AgentQ import AgentQ
    agent1 = AgentQ()
    agent2 = None
elif args.agent == 'AgentShootOut':
    from agents.AgentShootOut import AgentShootOut
    agent1 = AgentShootOut()
    agent2 = AgentShootOut()
else:
    print("Agent type '{0}' is not available.".format(args.agent))
    sys.exit(0)

# Initialize environment
if args.game == 'explore':
    from games.ExploreGame import ExploreGame
    if args.agent == 'AgentShootOut':
        game = ExploreGame(agent1=agent1, agent2=agent2)
    else:
        game = ExploreGame(agent1=agent1)
else:
    print("Game type '{0}' is not available.".format(args.game))
    sys.exit(1)

# Simulation loop:
# Train for specified number of games:
for step in range(args.num_training_games):
    game.reset()
    for step in range(game.num_steps_in_game):
        # agent1
        game.step(1)
        # agent2
        if agent2:
            game.step(2)

# Reset and render one game:
agent1.training = False
if agent2:
    agent2.training = False
game.reset()
for step in range(game.num_steps_in_game):
    # agent1
    game.step(1)
    # agent2
    if agent2:
        game.step(2)

    add_obstacle = 0
    if args.agent == 'AgentShootOut':
        add_obstacle = 1
    game.env.render('{0}/step_{1}.png'.format(args.output_dir, step), add_obstacle)
