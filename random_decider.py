from abc import abstractmethod

# R_S = '0062980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'
R_S = '5362980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'

class Random_Decider:
    name = ''
    finished = False
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

    def is_finished(self):
        return self.finished

    def finish(self):
        self.finished = True
        self.die()

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
class James(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'James'
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
class Wayne(Random_Decider):
    
    def __init__(self, digits):
        Random_Decider.__init__(self)
        self.name = 'Wayne'
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

        

def p_result(a):
    print()
    print(a.name)
    print(a.true_count)
    print(a.false_count)
    print(a.result)

if __name__ == "__main__":
    #Jack,James,Chip,Carl,Sam,Sara,Tom,Tim,Will,Wayne,Dan,Don
    j = Jack(R_S)
    j.decide()
    p_result(j)
    j = James(R_S)
    j.decide()
    p_result(j)
    j = Chip(R_S)
    j.decide()
    p_result(j)
    j = Carl(R_S)
    j.decide()
    p_result(j)
    j = Sam(R_S)
    j.decide()
    p_result(j)
    j = Sara(R_S)
    j.decide()
    p_result(j)
    j = Tom(R_S)
    j.decide()
    p_result(j)
    j = Tim(R_S)
    j.decide()
    p_result(j)
    j = Will(R_S)
    j.decide()
    p_result(j)
    j = Wayne(R_S)
    j.decide()
    p_result(j)
    j = Dan(R_S)
    j.decide()
    p_result(j)
    j = Don(R_S)
    j.decide()
    p_result(j)