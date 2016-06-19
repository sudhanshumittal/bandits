#Author: Sudhanshu Mittal
import numpy as np

class NArmBanditTestbed:
    bandits = []
    def __init__(self, banditClass, nBandits = 10, **params):
        print params
        self.nBandits = nBandits;
        self.bandits = [banditClass(**params) for i in range(0, nBandits)]

    # def reset(self, epsilon):
    #       [self.bandits[i].reset(epsilon=epsilon) for i in range(0,self.nBandits)]
    def __call__(self,nIterations = 1000):
        rewards = zip(*[self.bandits[i](nIterations) for i in range(0,self.nBandits)])
        avg_rewards =  [np.mean(results) for results in rewards]
        return avg_rewards
    
    def reset(self):
        [bandit.reset() for bandit in self.bandits]

    def set_params(**params):
        [bandit.set_params(**params) for bandit in self.bandits]

