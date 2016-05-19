#Author: Sudhanshu Mittal
import numpy as np

class NArmBanditTestbed:
	bandits = []
	def __init__(self, banditClass, nArms = 10, nBandits = 10, epsilon = 0.1):
		self.nBandits = nBandits;
		self.bandits = [banditClass(nArms, epsilon) for i in range(0,self.nBandits)]

	# def reset(self, epsilon):
	# 		[self.bandits[i].reset(epsilon=epsilon) for i in range(0,self.nBandits)]
	def __call__(self):
		rewards = zip(*[self.bandits[i]() for i in range(0,self.nBandits)])
		avg_rewards =  [np.mean(results) for results in rewards]
		return avg_rewards


