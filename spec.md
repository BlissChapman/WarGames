## Agents
#### Properties
`self.training`
- The training flag allows the run script to train an agent on a game and then switch to optimal play when rendering a simulated game.

#### Methods
`action(self, state, action_choices)`
- The action method is provided a representation of the state of the game. It must select an action to take from the action choices provided by the game. In learning agents, this choice will be based off previous experience.

`learn(self, state, action, chosen_next_state, reward_for_choice)`
- The learn method is called by the game after an agent's action has been simulated. It provides the original state, the action the agent selected, the resulting state, and the reward for being in the new state. A learning agent will typically adjust their internal decision-making state in this method call.

## Environments
#### Methods
`reset(self)`
- Restores the environment to the initial state.

`render(self, output_file)`
- Renders a graphical representation of the environment to the specified output file on disk.

## Games
Games simulate the interaction between the environment and an agent.

#### Methods
`reset(self)`
- Restores the game to the initial state. This is often as simple as resetting the underlying environment.

`step(self)`
- Moves the game one time step forward by requesting an action from the agent and simulating the impact of that action on the environment.
