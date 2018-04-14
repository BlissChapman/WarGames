import argparse
import os
import shutil
import sys 

# Parse arguments
parser = argparse.ArgumentParser(description="Run simulator with specified agent and environment.")
parser.add_argument('game', choices=['explore'], help='the game to simulate')
parser.add_argument('num_training_games', type=int, help='the number of training games to play')
parser.add_argument('output_dir', help='the directory to save simulation results')
args = parser.parse_args()

# Output directory
shutil.rmtree(args.output_dir, ignore_errors=True)
os.makedirs(args.output_dir)

from agents.AgentQ import AgentQ
agentA = AgentQ()
agentB = AgentQ()

# Initialize environment
if args.game == 'explore':
    from games.PrisonerDilemma import PrisonerDilemma
    game = PrisonerDilemma(agentA=agentA, agentB=agentB)
else:
    print("Game type '{0}' is not available.".format(args.game))
    sys.exit(1)

# Simulation loop:
# Train for specified number of games:
for step in range(args.num_training_games):
    game.reset()
    for step in range(game.num_steps_in_game):
        game.step()

# Reset and render one game:
agentA.training = False
agentB.training = False
game.reset()
for step in range(game.num_steps_in_game):
    game.step()
    game.env.render('{0}/step_{1}.png'.format(args.output_dir, step))

print(agentA.Q)
print(agentB.Q)