












class ScenarioGeneration:
    def __init__(self, params, num_scenarios, random_seed=None):
        self.params = params
        self.num_scenarios = num_scenarios
        self.random_seed = random_seed
        self.current_scenario_idx = 0
        self.scenario_list = self.create_scenarios(params, num_scenarios, random_seed)

    def get_next_scenario(self):
        if self.current_scenario_idx >= self.num_scenarios:
            self.current_scenario_idx = 0
            print("Resetting scenario index to zero")
        scenario = self.get_scenario(self.current_scenario_idx)
        self.current_scenario_idx += 1
        return scenario

    def get_scenario(self, idx):
        return self.scenario_list[idx]

    def create_scenarios(self, params, num_scenarios, random_seed):
        """ Creates a list of scenario class instances which should be deterministically reproducible given the random seed, the params and the number of scenarios
        
        Arguments:
            params {[bark.common.ParameterServer]} -- [provides additional parameters]
            num_scenarios {[int]} -- [how many scenarios should be created]
            random_seed {[unsigned int]} -- [a seed used to make scenario generation based on random factors reproducible]
        
        Returns:
            scenario_list {[a list of instances of type scenario class]} -- [each scenario in this list defines one initial world condition]
        """
        raise NotImplementedError("Implement this function in a subclass")