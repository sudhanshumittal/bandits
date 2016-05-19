#Author: Sudhanshu Mittal
import numpy as np
import random
from nArmBandit import * 
class NArmBanditEpsilonGreedy(NArmBandit):
    def __init__(self, nArms = 10, epsilon= 0.1):
        self.arm_selection_count = np.zeros(nArms);
        NArmBandit.__init__(self, nArms, epsilon)

    # def reset(self, epsilon= 0.1):
    #   self.epsilon = epsilon
    #   self.best_arm = 0;
    #   for i in range(0,self.nArms):
    #       self.arm_selection_count[i] = 0.0;
    #       self.av_estimates[i] = 0.0;

    def shouldExplore(self):
        return random.random() <= self.epsilon

    def choose_action(self):
        if self.shouldExplore():
            #chose one arm randomly
            return int(self.nArms*random.random())
        else:
            #chose best arm
            return self.best_arm;

    #to be overridden
    def get_alpha(self, arm):
        self.arm_selection_count[arm]+=1
        return 1.0/self.arm_selection_count[arm];

