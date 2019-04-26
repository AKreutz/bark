# Copyright (c) 2019 fortiss GmbH
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from modules.runtime.scenario.scenario_generation.scenario_generation import ScenarioGeneration
from modules.runtime.viewer.pygame_viewer import PygameViewer
from modules.runtime.viewer.matplotlib_viewer import MPViewer
from modules.runtime.commons.parameters import ParameterServer
import time


param_server = ParameterServer()

viewer = PygameViewer(params=param_server, x_range=[-200,0], y_range=[-100,100])

sim_step_time = param_server["simulation"]["step_time",
                                        "Step-time used in simulation",
                                        1]
sim_real_time_factor = param_server["simulation"]["real_time_factor",
                                                "execution in real-time or faster",
                                                1]
scenario_generation = ScenarioGeneration()
scenario_generation.load_scenario_list(filename="examples/scenarios/test.bark_scenarios")


for _ in range(0,5): # run 5 scenarios in a row, repeating after 3
    scenario = scenario_generation.get_next_scenario()
    world_state = scenario.get_world_state()
    for _ in range(0, 3): # run each scenario for 3 steps
        world_state.step(sim_step_time)
        viewer.drawWorld(world_state)
        viewer.show(block=False)
        time.sleep(sim_step_time/sim_real_time_factor)