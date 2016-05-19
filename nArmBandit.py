#Author: Sudhanshu Mittal
import random
import matplotlib.pyplot as plt
import numpy as np
class NArmBandit:
    mu = 0.0;
    sigma = 1.0;    
    def __init__(self, nArms = 10, epsilon= 0.1):
        self.epsilon = epsilon
        self.nArms = nArms
        self.best_arm = 0;
        self.nIterations = 1000
        self.av_estimates = np.zeros(self.nArms);
        self.action_values = np.random.normal(self.mu,self.sigma, self.nArms);

    # def reset(self, epsilon= 0.1):
    #   self.epsilon = epsilon
    #   self.best_arm = 0;
    #   for i in range(0,self.nArms):
    #       self.arm_selection_count[i] = 0.0;
    #       self.av_estimates[i] = 0.0;
    def print_state(self):
        print self.action_values 
        print self.av_estimates
        print "\n"
    
    def get_reward(self, arm):
        return np.random.normal(self.action_values[arm],self.sigma);

    #to be overridden
    def choose_action(self):
        return 0;

    #to be overridden
    def get_alpha(self, arm):
        return 0;
    
    def update_arm_value_estimate(self, arm, reward):
        self.av_estimates[arm] = self.av_estimates[arm] + self.get_alpha(arm)*(reward - self.av_estimates[arm])
        if ( self.av_estimates[arm] > self.av_estimates[self.best_arm]):
            self.best_arm = arm;
    
    def __call__(self):
        rewards = [] 
        for i in range(0,self.nIterations):
            arm = self.choose_action();
            reward = self.get_reward(arm);  
            self.update_arm_value_estimate(arm, reward);
            rewards.append(reward);
        return rewards; 


