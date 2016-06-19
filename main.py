from nArmBanditTestbed import NArmBanditTestbed
from nArmBanditEpsilonGreedy import NArmBanditEpsilonGreedy
import matplotlib.pyplot as plt
from nArmBanditSoftmax import NArmBanditSoftmax

if __name__ == "__main__":
  myBanditTestbed = NArmBanditTestbed(banditClass =NArmBanditEpsilonGreedy, nBandits = 1000, epsilon = 0.1)
  avg_rewards1 = myBanditTestbed(1000)
  myBanditTestbed2 = NArmBanditTestbed(banditClass =NArmBanditSoftmax, nBandits = 1000, epsilon = 0.1, temperature = 0.5)
  avg_rewards2 = myBanditTestbed2(1000)
  
  # # myBanditTestbed.reset(0.01)
  # # avg_rewards2 = myBanditTestbed(1000)
  # # myBanditTestbed.reset(0.0)
  # # avg_rewards3 = myBanditTestbed(1000)
  # # myBanditTestbed.reset()

  # # nBanditTestbed2 = nBanditTestbed(nBandits = 2000, epsilon = 0.01, banditClass =NArmBanditSoftmax)
  # # avg_rewards2 = nBanditTestbed2()


  t = range(1,len(avg_rewards1)+1)
  plt.plot(t, avg_rewards1,t, avg_rewards2)
  plt.ylabel('avg_rewards')
  plt.show()

