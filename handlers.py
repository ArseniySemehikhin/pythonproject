
class Poly:
    def __init__(self, *polinom):
        if len(polinom) == 0:
            self.polinom = [0]
        elif type(polinom[0]) == list:
            self.polinom = polinom[0]
        else:
            self.polinom = list(polinom)



    def __repr__(self):
        s="'Poly(("
        l=len(self.polinom)
        if l>1:
            s=s+str(self.polinom[0])+', '
            for i in range(1,l-1):
                s=s+str(self.polinom[i])+', '
        s=s+str(self.polinom[l-1])+"))'"
        return s




    def __str__(self):
        if all(coef == 0 for coef in self.polinom):
            return "0"
        Sum= ''
        flag=True
        flag1=False
        for power, coef in enumerate(self.polinom):
            k=''
            if coef == 0:
                continue

            if (power==0) and (coef !=0):
                k += str(abs(coef))
                flag= False if coef < 0 else True
                Sum=k
                flag1 = True

            if (abs(coef) != 1) and (power>0):
                if isinstance(coef, float):
                   coef = round(coef, 3)
                k=str(abs(coef))+('x^'+ str(power) if power > 1 else "x")
                if flag:
                    a='+'
                else:
                    a='-'
                if flag1:
                 Sum=k+' '+a+' '+Sum
                else:
                    Sum=k
                    flag1 = True
                flag = False if coef < 0 else True
            if (abs(coef) == 1) and (power>0):
                if isinstance(coef, float):
                    round(coef,3)
                k=('x^'+ str(power) if power > 1 else "x")
                if flag:
                    a='+'
                else:
                    a='-'
                if flag1:
                 Sum=k+' '+a+' '+Sum
                else:
                    Sum=k
                flag = False if coef < 0 else True
        if flag:
         return Sum
        else:
            return '-'+Sum

    def __radd__(self, other):
        return self + other

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        a = []
        k = Poly(a)
        if len(self.polinom) < len(other.polinom):
            n = len(self.polinom)
        else:
            n = len(other.polinom)
        for i in range(n):
            a.append(self.polinom[i] + other.polinom[i])
        if len(self.polinom) > n:
            a += self.polinom[n::]
        else:
            a += other.polinom[n::]
        k.polinom = a

        return k

    def __rsub__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        a = []
        d = Poly(a)
        if len(self.polinom) < len(other.polinom):
            n = len(self.polinom)
        else:
            n = len(other.polinom)
        for i in range(n):
            a.append(-self.polinom[i] + other.polinom[i])
        if len(self.polinom) > n:
            a += self.polinom[n::]
        else:
            a += other.polinom[n::]
        d.polinom = a
        return d

    def __sub__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        a = []
        d = Poly(a)
        if len(self.polinom) < len(other.polinom):
            n = len(self.polinom)
        else:
            n = len(other.polinom)
        for i in range(n):
            a.append(self.polinom[i] - other.polinom[i])
        if len(self.polinom) > n:
            a += self.polinom[n::]
        else:
            a += other.polinom[n::]
        d.polinom = a
        return d
    def __eq__(self, other):
        if not isinstance(other, Poly):
                other = Poly(other)
        return self.polinom == other.polinom

poly1 = Poly([1,4,0.3654,-6,-1,0])
poly2 = Poly()
poly3 = Poly(1)
poly4 = Poly(1,-2,-3.12345)
print(poly1-poly2)
print(poly1-poly3)
print(poly1-poly4)
print(poly2-poly3)
print(poly1-poly1)
print(poly1-4)
print(3.5-poly2)