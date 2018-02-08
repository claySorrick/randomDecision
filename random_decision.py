

#R_S = '0062980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'
R_S = '5362980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'


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
        self.sum = 0
        self.prod = 1


    def is_even(self):
        res = False
        if int(R_S[self.index]) % 2 == 0:
            res = True
        self.index += 1
        return res

    def is_odd(self):
        return not self.is_even()

    def even_odd(self):
        res = self.is_even()
        self.add(res)

    def one_mod_two(self):
        a = int(R_S[self.index]) + 1
        self.index += 1
        if self.index == len(R_S):
            b = int(R_S[0]) + 1
        else:
            b = int(R_S[self.index]) + 1
        res = (a % b) % 2 == 0
#        print(str(a) + ' % ' + str(b) + ' = ' + str(res))
        self.add(res)
        
    def add(self, res):
        if res:
            self.true_count += 1
        else:
            self.false_count += 1
        self.decisions.append(res)
        
    def one_gt_two(self):
        a = int(R_S[self.index])
        self.index += 1
        if self.index == len(R_S):
            b = int(R_S[0])
        else:
            b = int(R_S[self.index])
        res = a > b
        self.add(res)
        
    def one_lt_two(self):
        a = int(R_S[self.index])
        self.index += 1
        if self.index == len(R_S):
            b = int(R_S[0])
        else:
            b = int(R_S[self.index])
        res = a < b
        self.add(res)
        
    def summ(self):
        a = int(R_S[self.index])
        self.index += 1
        self.sum += a
        res = self.sum % 2 == 0
        self.add(res)
        
    def sum_mod_n1(self):
        a = int(R_S[self.index])
        self.index += 1
        if self.index == len(R_S):
            b = int(R_S[0]) + 1
        else:
            b = int(R_S[self.index]) + 1
        self.sum += a
        res = (self.sum % b) % 2 == 0
        self.add(res)
        
    def sum_gt_prod(self):
        a = int(R_S[self.index])
        self.index += 1
        self.sum += a
        if a == 0:
            self.prod = 1
        else:
            self.prod *= a
        res = self.sum > self.prod
        self.add(res)

dm = Decision_Manager()
for i in range(len(R_S)):
    dm.even_odd()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)

dm = Decision_Manager()
for i in range(len(R_S)):
    dm.one_mod_two()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)


dm = Decision_Manager()
for i in range(len(R_S)):
    dm.one_gt_two()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)

dm = Decision_Manager()
for i in range(len(R_S)):
    dm.one_lt_two()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)

dm = Decision_Manager()
for i in range(len(R_S)):
    dm.summ()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)

dm = Decision_Manager()
for i in range(len(R_S)):
    dm.sum_mod_n1()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)

dm = Decision_Manager()
for i in range(len(R_S)):
    dm.sum_gt_prod()
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)
