class Fraction:
    def __init__(self,ss,mm) :
        #properties
        self.s = ss
        self.m = mm

    #methods
    def sum(s1,m1,s2,m2):
        result_s=s1*m2+s2*m1
        result_m=m1*m2
        return result_s,result_m

    def mul(s1,m1,s2,m2):
        result_s=s1*s2
        result_m=m1*m2
        
        return result_s , result_m

    def fraction_to_number(s1,m1):
        if m1 != 0 :
            result = s1/m1
            return result
        else:
            return "Connot divide by zero"
