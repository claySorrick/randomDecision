from abc import abstractmethod
from random_fetcher import Random_Client

# R_S = '0062980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'
R_S = '5362980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'

class Random_Decider:
    name = ''
    alive = False
    true_count = 0
    false_count = 0
    decisions = []
    result = None

    def __init__(self):
        pass
    
    @abstractmethod
    def decide(self):
        pass

    def is_alive(self):
        return self.alive

    def die(self):
        self.alive = False

    def add(self, res):
        if res:
            self.true_count += 1
        else:
            self.false_count += 1
        self.decisions.append(res)

    def make_result(self):
        self.result = self.true_count > self.false_count
        self.die()

#even
class Jack(Random_Decider):

    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Jack'
        self.alive = True
        self.digits = digits
        
    def decide(self):
        for i in range(len(self.digits)):
            res = False
            if int(self.digits[i]) % 2 == 0:
                res = True
            self.add(res)
        self.make_result()

#odd
class Jamy(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Jamy'
        self.alive = True
        self.digits = digits
        
    def decide(self):
        for i in range(len(self.digits)):
            res = False
            if int(self.digits[i]) % 2 != 0:
                res = True
            self.add(res)
        self.make_result()

#one mod two even
class Carl(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Carl'
        self.alive = True
        self.digits = digits
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            if i == len(self.digits) - 1:
                b = int(self.digits[0]) + 1
            else:
                b = int(self.digits[i+1]) + 1
            res = (a % b) % 2 == 0
            self.add(res)
        self.make_result()

#one mod two odd
class Chip(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Chip'
        self.alive = True
        self.digits = digits
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            if i == len(self.digits) - 1:
                b = int(self.digits[0]) + 1
            else:
                b = int(self.digits[i+1]) + 1
            res = (a % b) % 2 != 0
            self.add(res)
        self.make_result()

#one gt two
class Tom(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Tom'
        self.alive = True
        self.digits = digits
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            if i == len(self.digits) - 1:
                b = int(self.digits[0])
            else:
                b = int(self.digits[i+1])
            res = a > b
            self.add(res)
        self.make_result()

#one lt two
class Tim(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Tim'
        self.alive = True
        self.digits = digits
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            if i == len(self.digits) - 1:
                b = int(self.digits[0])
            else:
                b = int(self.digits[i+1])
            res = a < b
            self.add(res)
        self.make_result()

#sum even
class Sam(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Sam'
        self.alive = True
        self.digits = digits
        self.sum = 0
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            self.sum += a
            res = self.sum % 2 == 0
            self.add(res)
        self.make_result()

#sum odd
class Sara(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Sara'
        self.alive = True
        self.digits = digits
        self.sum = 0
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            self.sum += a
            res = self.sum % 2 != 0
            self.add(res)
        self.make_result()

#sum mod n+1 even
class Dan(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Dan'
        self.alive = True
        self.digits = digits
        self.sum = 0
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            if i == len(self.digits) - 1:
                b = int(self.digits[0]) + 1
            else:
                b = int(self.digits[i+1]) + 1
            self.sum += a
            res = (self.sum % b) % 2 == 0
            self.add(res)
        self.make_result()
        
#sum mod n+1 odd
class Don(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Don'
        self.alive = True
        self.digits = digits
        self.sum = 0
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            if i == len(self.digits) - 1:
                b = int(self.digits[0]) + 1
            else:
                b = int(self.digits[i+1]) + 1
            self.sum += a
            res = (self.sum % b) % 2 != 0
            self.add(res)
        self.make_result()

#sum gt prod
class Will(Random_Decider):
    
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Will'
        self.alive = True
        self.digits = digits
        self.sum = 0
        self.prod = 1
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            self.sum += a
            if a == 0:
                self.prod = 1
            else:
                self.prod *= a
            res = self.sum > self.prod
            self.add(res)
        self.make_result()

#sum lt prod
class Wayn(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Wayn'
        self.alive = True
        self.digits = digits
        self.sum = 0
        self.prod = 1
        
    def decide(self):
        for i in range(len(self.digits)):
            a = int(self.digits[i])
            self.sum += a
            if a == 0:
                self.prod = 1
            else:
                self.prod *= a
            res = self.sum < self.prod
            self.add(res)
        self.make_result()

class Decision_Manager():
    
    def __init__(self):
        self.deciders = []
        self.reset()
    
    def reset(self):
        digs = self.get_digits()
        self.deciders = []
        self.deciders.append(Jack(digs))
        self.deciders.append(Jamy(digs))
        self.deciders.append(Chip(digs))
        self.deciders.append(Carl(digs))
        self.deciders.append(Sam(digs))
        self.deciders.append(Sara(digs))
        self.deciders.append(Tom(digs))
        self.deciders.append(Tim(digs))
        self.deciders.append(Will(digs))
        self.deciders.append(Wayn(digs))
        self.deciders.append(Dan(digs))
        self.deciders.append(Don(digs))


    def get_digits(self):
        rc = Random_Client()
        numbers = rc.get_numbers()
        return numbers

    def get_decision(self):
        trues, falses = 0, 0
        for decider in self.deciders:
            decider.decide()
            if decider.result:
                trues += 1
            else:
                falses += 1
        return (trues, falses)


if __name__ == "__main__":
    #Jack,Jamy,Chip,Carl,Sam,Sara,Tom,Tim,Will,Wayn,Dan,Don
    dm = Decision_Manager()
    print(dm.get_decision())