from Bandits import MultiArmedBandit;
from Agents import AgentEpsilonGreedy, AgentSoftmax
from utils import generateActionValues

class TestBed:
    def __init__(self, bandits, agents):
        assert(len(bandits) > 0)
        assert(len(bandits) == len(agents))
        self.numberOfBandits = len(bandits);
        self.bandits = bandits;
        self.agents = agents;
        
    def learn(self):
        for agent in self.agents:
            agent.learn();
    
    def getAverageReward(self):
        reward = 0;
        for agent in self.agents:
            reward += agent.getReward(agent.bestArm) 
        return reward / self.numberOfBandits;
    
class EpsilonGreedyTestBed(TestBed):
    numberOfArms = 10;
    def __init__(self, numberOfBandits, epsilon):
        assert(numberOfBandits > 0)

        bandits = [MultiArmedBandit(self.numberOfArms, generateActionValues(self.numberOfArms)) for _ in range(0, numberOfBandits)]
        agents = [AgentEpsilonGreedy(bandits[i], self.numberOfArms, epsilon) for i in range(0, numberOfBandits)]
        TestBed.__init__(self, bandits, agents);
        
class SoftmaxTestBed(TestBed):
    numberOfArms = 10;
    def __init__(self, numberOfBandits, epsilon, temperature):
        assert(numberOfBandits > 0)
        bandits = [MultiArmedBandit(self.numberOfArms, generateActionValues(self.numberOfArms)) for _ in range(0, numberOfBandits)]
        agents = [AgentSoftmax(bandits[i], self.numberOfArms, epsilon, temperature) for i in range(0, numberOfBandits)]
        TestBed.__init__(self, bandits, agents);
    