from numpy import random;
class Arm:
    def draw(self):
        raise NotImplementedError("implement this method")

class NormalArm(Arm):
    def __init__(self, actionValue):
        self.actionValue = actionValue;
    
    def draw(self):
        return self.actionValue + random.normal();
        
class MultiArmedBandit:
    def __init__(self, numberOfArms, actionValueArray):
        assert(numberOfArms > 0);
        assert(len(actionValueArray) == numberOfArms);
        
        self.numberOfArms = numberOfArms;
        self.arms = [NormalArm(actionValueArray[i]) for i in range(0, numberOfArms)];
        
    def getReward(self, armPulled):
        assert(armPulled <= self.numberOfArms and armPulled >= 1), \
               "arm pulled=%s, number of arms=%s" % ( str(armPulled), str(self.numberOfArms));
        return self.arms[armPulled - 1].draw();
