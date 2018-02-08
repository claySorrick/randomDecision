

R_S = '0062980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'

class Decision_Result:

    def __init__(self, decision):
        self.decision = decision

class Decision_Manager:

    def __init__(self):
        self.id = ''
        self.index = 0
        self.true_count = 0
        self.false_count = 0
        self.decisions = []

    def is_even(self):
        res = False
        if int(R_S[self.index]) % 2 == 0:
            res = True
        self.index += 1
        return res

    def is_odd(self):
        return not self.is_even()

    def even_odd(self):
        self.decisions.append(self.is_even())

    def one_mod_two(self):
        
        
    # def one_gt_two(self):
        
    # def one_lt_two(self):
        
    # def sum(self):
        
    # def sum_mod_n1(self):
        
    # def sum_gt_prod(self):

dm = Decision_Manager()
for i in range(100):
    dm.even_odd()
print(dm.decisions)