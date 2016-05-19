#Author: Sudhanshu Mittal
import numpy as np
import random
import matplotlib.pyplot as plt

from nArmBandit as NArmBandit

class NArmBanditSoftmax(NArmBandit):
	def __init__(self, nArms = 10, epsilon= 0.1, temperature = 1.0):
		self.temperature = 1.0;
		supoer.__init__(nArms, epsilon);

	def weighted_choice(self, choices):
		total = sum(w for c, w in choices)
		r = random.uniform(0, total)
		upto = 0
		for c, w in choices:
			if upto + w >= r:
				return c
			upto += w
		assert False, "Shouldn't get here"

	def choose_action(self):
		choices = [math.exp(1e, q/self.temperature) for q in self.av_estimates ]
		choices = [i/sum(choices) for i in choices]
		return = weighted_choice(choices):
		
	
class nBanditTestbed:
	bandits = []
	def __init__(self, nBandits = 10, epsilon = 0.1):
		self.nBandits = nBandits;
		self.bandits = [nArmBandit(epsilon=epsilon) for i in range(0,self.nBandits)]
	def reset(self, epsilon):
			[self.bandits[i].reset(epsilon=epsilon) for i in range(0,self.nBandits)]
	def __call__(self):
		rewards = zip(*[self.bandits[i]() for i in range(0,self.nBandits)])
		avg_rewards =  [np.mean(results) for results in rewards]
		return avg_rewards
