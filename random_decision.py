

R_S = '0062980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'
#R_S = '5362980566143536201066017731944112043166104289330456701626650503804970856884726105184658629518811375'

        
class Decision_Maker:

    def __init__(self, digits):
        self.digits = digits
        self.index = 0
        self.true_count = 0
        self.false_count = 0
        self.decisions = []
        self.sum = 0
        self.prod = 1
        sm = 0
        for i in range(7):
            sm += int(digits[i])
        sm = sm % 7
        if sm == 0:
            print('even or odd')
            self.even()
        elif sm == 1:
            print('one mod two')
            self.one_mod_two()
        elif sm == 2:
            print('one gt two')
            self.one_gt_two()
        elif sm == 3:
            print('one lt two')
            self.one_lt_two()
        elif sm == 4:
            print('sum even')
            self.sum_even()
        elif sm == 5:
            print('sum mod n1')
            self.sum_mod_n1()
        elif sm == 6:
            print('sum gt prod')
            self.sum_gt_prod()
        self.result = self.true_count > self.false_count
            
#    takes a string of random digits
#    uses string to determine which function to run
#    run function over string of digits
    def even(self):
        res = False
        if int(self.digits[self.index]) % 2 == 0:
            res = True
        self.index += 1
        self.add(res)
        if self.index < len(self.digits):
            self.even()

    def one_mod_two(self):
        a = int(self.digits[self.index]) + 1
        self.index += 1
        if self.index == len(self.digits):
            b = int(self.digits[0]) + 1
        else:
            b = int(self.digits[self.index]) + 1
        res = (a % b) % 2 == 0
#        print(str(a) + ' % ' + str(b) + ' = ' + str(res))
        self.add(res)
        if self.index < len(self.digits):
            self.one_mod_two()
        
    def one_gt_two(self):
        a = int(self.digits[self.index])
        self.index += 1
        if self.index == len(self.digits):
            b = int(self.digits[0])
        else:
            b = int(self.digits[self.index])
        res = a > b
        self.add(res)
        if self.index < len(self.digits):
            self.one_gt_two()
        
    def one_lt_two(self):
        a = int(self.digits[self.index])
        self.index += 1
        if self.index == len(self.digits):
            b = int(self.digits[0])
        else:
            b = int(self.digits[self.index])
        res = a < b
        self.add(res)
        if self.index < len(self.digits):
            self.one_lt_two()
        
    def sum_even(self):
        a = int(self.digits[self.index])
        self.index += 1
        self.sum += a
        res = self.sum % 2 == 0
        self.add(res)
        if self.index < len(self.digits):
            self.sum_even()
        
    def sum_mod_n1(self):
        a = int(self.digits[self.index])
        self.index += 1
        if self.index == len(self.digits):
            b = int(self.digits[0]) + 1
        else:
            b = int(self.digits[self.index]) + 1
        self.sum += a
        res = (self.sum % b) % 2 == 0
        self.add(res)
        if self.index < len(self.digits):
            self.sum_mod_n1()
        
    def sum_gt_prod(self):
        a = int(self.digits[self.index])
        self.index += 1
        self.sum += a
        if a == 0:
            self.prod = 1
        else:
            self.prod *= a
        res = self.sum > self.prod
        self.add(res)
        if self.index < len(self.digits):
            self.sum_gt_prod()

    def add(self, res):
        if res:
            self.true_count += 1
        else:
            self.false_count += 1
        self.decisions.append(res)



    
dm = Decision_Maker(R_S)
print(dm.true_count)
print(dm.false_count)
print(dm.true_count + dm.false_count)
print(dm.result)

#dm = Decision_Manager()
#for i in range(len(R_S)):
#    dm.one_mod_two()
#print(dm.true_count)
#print(dm.false_count)
#print(dm.true_count + dm.false_count)
#
#
#dm = Decision_Manager()
#for i in range(len(R_S)):
#    dm.one_gt_two()
#print(dm.true_count)
#print(dm.false_count)
#print(dm.true_count + dm.false_count)
#
#dm = Decision_Manager()
#for i in range(len(R_S)):
#    dm.one_lt_two()
#print(dm.true_count)
#print(dm.false_count)
#print(dm.true_count + dm.false_count)
#
#dm = Decision_Manager()
#for i in range(len(R_S)):
#    dm.sum_even()
#print(dm.true_count)
#print(dm.false_count)
#print(dm.true_count + dm.false_count)
#
#dm = Decision_Manager()
#for i in range(len(R_S)):
#    dm.sum_mod_n1()
#print(dm.true_count)
#print(dm.false_count)
#print(dm.true_count + dm.false_count)
#
#dm = Decision_Manager()
#for i in range(len(R_S)):
#    dm.sum_gt_prod()
#print(dm.true_count)
#print(dm.false_count)
#print(dm.true_count + dm.false_count)
