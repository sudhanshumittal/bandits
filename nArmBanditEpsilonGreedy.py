#Author: Sudhanshu Mittal
import numpy as np
import random
from nArmBandit import * 
class NArmBanditEpsilonGreedy(NArmBandit):
    def __init__(self, nArms, epsilon, **params):
        # print nArms
        # print 'epsilon=', epsilon
        set_params(nArms = nArms, epsilon = epsilon)
        NArmBandit.__init__(self, nArms, epsilon)
        self.reset(epsilon)

    #overridden
    def set_params(self, nArms = 10, epsilon= 0.1, **params):
        self.epsilon = epsilon
        NArmBandit.set_params(self, nArms, **params)
        
    #overridden
    def reset(self):
        NArmBandit.reset(self)
        self.arm_selection_count = np.zeros(self.nArms);
        
    def shouldExplore(self):
        return random.random() <= self.epsilon

    #overridden
    def choose_action(self):
        if self.shouldExplore():
            #chose one arm randomly
            return int(self.nArms*random.random())
        else:
            #chose best arm
            return self.best_arm;

    #overridden
    def get_alpha(self, arm):
        self.arm_selection_count[arm]+=1
        return 1.0/self.arm_selection_count[arm];


