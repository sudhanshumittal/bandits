from nArmBanditTestbed import NArmBanditTestbed
from nArmBanditEpsilonGreedy import NArmBanditEpsilonGreedy
import matplotlib.pyplot as plt

if __name__ == "__main__":
  myBanditTestbed1 = NArmBanditTestbed(banditClass =NArmBanditEpsilonGreedy, nBandits = 2000, epsilon = 0.1)
  avg_rewards1 = myBanditTestbed1()

  myBanditTestbed2 = NArmBanditTestbed(banditClass =NArmBanditEpsilonGreedy, nBandits = 2000, epsilon = 0.01)
  avg_rewards2 = myBanditTestbed2()

  # nBanditTestbed2 = nBanditTestbed(nBandits = 2000, epsilon = 0.01, banditClass =NArmBanditSoftmax)
  # avg_rewards2 = nBanditTestbed2()

  myBanditTestbed3 = NArmBanditTestbed(banditClass =NArmBanditEpsilonGreedy, nBandits = 2000, epsilon = 0.0)
  avg_rewards3 = myBanditTestbed3()

  t = range(1,len(avg_rewards1)+1)
  plt.plot(t, avg_rewards1,t, avg_rewards2,t, avg_rewards3)
  plt.ylabel('avg_rewards')
  plt.show()

