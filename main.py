from Agents import AgentEpsilonGreedy;
from TestBeds import EpsilonGreedyTestBed;
from TestBeds import SoftmaxTestBed
import utils
if __name__ == "__main__":
      
    numberOfBandits = 2000;  
    numberOfIterations = 1000;
    epsilon = 0.1
    temperature = 0.5
    testBed = SoftmaxTestBed(numberOfBandits, epsilon, temperature);
    rewards1 = []
    for i in range(0, numberOfIterations):
        testBed.learn()
        rewards1 += [testBed.getAverageReward()]

    utils.plot(rewards1)

#   myBanditTestbed = NArmBanditTestbed(banditClass =NArmBanditEpsilonGreedy, nBandits = 1000, epsilon = 0.1)
#   avg_rewards1 = myBanditTestbed(1000)
# myBanditTestbed2 = NArmBanditTestbed(banditClass =NArmBanditSoftmax, nBandits = 1000, epsilon = 0.1, temperature = 0.5)
# avg_rewards2 = myBanditTestbed2(1000)

# # myBanditTestbed.reset(0.01)
# # avg_rewards2 = myBanditTestbed(1000)
# # myBanditTestbed.reset(0.0)
# # avg_rewards3 = myBanditTestbed(1000)
# # myBanditTestbed.reset()

# # nBanditTestbed2 = nBanditTestbed(nBandits = 2000, epsilon = 0.01, banditClass =NArmBanditSoftmax)
# # avg_rewards2 = nBanditTestbed2()

