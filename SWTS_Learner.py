from TS_Learner import *

class SWTS_Learner(TS_Learner):
    def __init__(self,n_arms, window_size):
        super().__init__(n_arms)
        self.window_size = window_size
        self.pulled_arms = np.array([])

    def update(self,pulled_arm,reward):
        self.t+=1
        self.update_observations(pulled_arm, reward)
        self.pulled_arms = np.append(self.pulled_arms, pulled_arm)
        n_samples = np.sum(self.pulled_arms[-self.window_size:] == pulled_arm)
        cum_rew = np.sum(self.rewards_per_arm[pulled_arm][-n_samples:])

        self.beta_parameters[pulled_arm, 0] = cum_rew + 1.0
        self.beta_parameters[pulled_arm, 1] = n_samples - cum_rew + 1.0