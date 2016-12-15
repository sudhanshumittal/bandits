# Author: Sudhanshu Mittal
import math
import numpy as np
import random
import utils
from Bandits import MultiArmedBandit;
from sympy.physics.units import temperature


class Agent:
    bestArm = 1;  # indexed from 1
    def __init__(self, bandit, numberOfArms):
        assert(isinstance(bandit, MultiArmedBandit));
        self.bandit = bandit;
        self.numberOfArms = bandit.numberOfArms;
        self.actionValueEstimates = np.zeros(self.numberOfArms);
    def chooseArm(self):
        raise NotImplementedError('implement method chooseArm');

    def getReward(self, armChosen):
        return self.bandit.getReward(armChosen)

    def learn(self):
        armChosen = self.chooseArm();
        reward = self.getReward(armChosen);
        self.updateEstimate(armChosen, reward);
        
    def updateEstimate(self, arm, reward):
        raise NotImplementedError('implement method updateEstimate');

class AgentEpsilonGreedy(Agent):
    
    def __init__(self, bandit, numberOfArms, epsilon):
        Agent.__init__(self, bandit, numberOfArms);
        self.epsilon = epsilon;
        self.armSelectionCount = np.zeros(numberOfArms);
        
    def updateEstimate(self, arm, reward):
        self.actionValueEstimates[arm - 1] += self.getAlpha(arm) * (reward - self.actionValueEstimates[arm - 1])
        if (self.actionValueEstimates[arm - 1] > self.actionValueEstimates[self.bestArm - 1]):
            self.bestArm = arm;
    
    def chooseArm(self):
        chosenArm = None
        if self.shouldExplore():
            chosenArm = random.randint(1, self.numberOfArms)
        else:
            chosenArm = self.bestArm;
        self.armSelectionCount[chosenArm - 1] += 1;
        return chosenArm;

    def getAlpha(self, arm):
        return 1.0 / self.armSelectionCount[arm - 1];
    
    def shouldExplore(self):
        return random.random() <= self.epsilon

if __name__ == "__main__":
    actualActionValues = utils.generateActionValues(10);
    bandit = MultiArmedBandit(10, actualActionValues);
    agent = AgentEpsilonGreedy(bandit, 10, 0.1);
    mse = []
    for _ in range(0, 10000):
        agent.learn()
        mse += [np.mean(np.square(actualActionValues - agent.actionValueEstimates))];

    print actualActionValues;
    print agent.actionValueEstimates;
    utils.plot(mse);

class AgentSoftmax(Agent):
    
    def __init__(self, bandit, numberOfArms, epsilon, temperature):
        Agent.__init__(self, bandit, numberOfArms);
        self.epsilon = epsilon;
        self.temperature = temperature;
        self.armSelectionCount = np.zeros(numberOfArms);

    def getAlpha(self, arm):
        return 1.0 / self.armSelectionCount[arm - 1];

    def chooseArm(self):
        choices = [math.exp(q/self.temperature) for q in self.actionValueEstimates ]
        totalSum = sum(choices)
        choices = [i/totalSum for i in choices]
        chosenArm =  self.weightedChoice(choices)
        self.armSelectionCount[chosenArm - 1] += 1;
        return chosenArm;

    def weightedChoice(self, choices):
        total = sum(choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(range(1,len(choices)+1), choices):
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

    def updateEstimate(self, arm, reward):
        self.actionValueEstimates[arm - 1] += self.getAlpha(arm) * (reward - self.actionValueEstimates[arm - 1])
        if (self.actionValueEstimates[arm - 1] > self.actionValueEstimates[self.bestArm - 1]):
            self.bestArm = arm;

# class NArmBandit:
#     mu = 0.0;
#     sigma = 1.0;    
#     # to be overridden
#     def reset(self):
#         # self.epsilon = epsilon
#         self.best_arm = 0;
#         self.av_estimates = np.zeros(self.nArms);
# 
#     # to be overridden
#     def set_params(self, nArms=10, **params):
#         self.nArms = nArms
#     
#     def __init__(self, nArms):
#         self.set_params(nArms)
#         self.action_values = np.random.normal(self.mu, self.sigma, self.nArms);
#         self.reset()        
# 
#     def print_state(self):
#         print self.action_values 
#         print self.av_estimates
#         print "\n"
#     
#     def get_reward(self, arm):
#         return np.random.normal(self.action_values[arm], self.sigma);
# 
#     # to be overridden
#     def chooseArm(self):
#         return 0;
# 
#     # to be overridden
#     def getAlpha(self, arm):
#         return 0;
#     
#     def update_arm_value_estimate(self, arm, reward):
#         self.av_estimates[arm] = self.av_estimates[arm] + self.getAlpha(arm) * (reward - self.av_estimates[arm])
#         if (self.av_estimates[arm] > self.av_estimates[self.best_arm]):
#             self.best_arm = arm;
#     
#     def __call__(self, nIterations=1):
#         rewards = [] 
#         for i in range(0, nIterations):
#             arm = self.chooseArm();
#             reward = self.get_reward(arm);  
#             self.update_arm_value_estimate(arm, reward);
#             rewards.append(reward);
#         return rewards; 

