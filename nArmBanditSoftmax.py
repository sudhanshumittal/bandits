#Author: Sudhanshu Mittal
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from nArmBandit import NArmBandit

class NArmBanditSoftmax(NArmBandit):
    def __init__(self, nArms = 10, epsilon= 0.1, temperature = 0.5, **params ):
        set_params(nArms, termperature, **params)
        NArmBandit.__init__(self,nArms, epsilon);
        self.reset(epsilon = epsilon, termperature = temperature)

        #overridden
    def set_params(self, nArms = 10, temperature= 0.5, **params):
        self.temperature = temperature;
        NArmBandit.set_params(self, nArms, **params)

    def reset(self):
        NArmBandit.reset(self)
        self.arm_selection_count = np.zeros(self.nArms);

    def get_alpha(self, arm):
        self.arm_selection_count[arm]+=1
        return 1.0/self.arm_selection_count[arm];

    def weighted_choice(self, choices):
        total = sum(choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(range(0,len(choices)), choices):
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

    def choose_action(self):
        choices = [math.exp(q/self.temperature) for q in self.av_estimates ]
        total_sum = sum(choices)
        choices = [i/total_sum for i in choices]
        return self.weighted_choice(choices)