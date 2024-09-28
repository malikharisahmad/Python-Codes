from random import *
class Polynomial:
    def __init__(self,var='x',deg=0,c=[]):
        self.__var=var
        self.__deg=deg
        self.__c=c


    @property
    def var(self):
        return self.__var
    @var.setter
    def var(self,d):
        self.__var=d

    @property
    def deg(self):
        return self.__deg
    @deg.setter
    def deg(self,d):
        self.__deg=d

    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self,d):
        self.__c=d

    def __str__(self):
        a=(self.c).copy()
        a.reverse()
        p=[]
        for i in range (len(a)):
            pol=''
            if a[i]==0:
                continue
            else:
                if (len(a)-i-1)!=0:
                    if a[i]==1:
                        if (len(a)-i-1)==1:
                            pol+=str(self.var)
                        else:
                            pol+=str(self.var)+'^'+str(len(a)-i-1)
                    elif a[i]==-1:
                        if (len(a)-i-1)==1:
                            pol+='-'+str(self.var)
                        else:
                            pol+='-'+str(self.var)+'^'+str(len(a)-i-1)
                    else:
                        if (len(a)-i-1)==1:
                            pol+=str(a[i])+str(self.var)
                        else:
                            pol+=str(a[i])+str(self.var)+'^'+str(len(a)-i-1)
                else:
                    pol+=str(a[i])
                (p).append(pol)
        q=' + ' .join(p)
        return q.replace('+ -','-')

    def __add__(self,self1):
        d=max(self.deg,self1.deg)
        l=[]
        b=(self.c).copy()
        c=(self1.c).copy()
        if len(b)>len(c):
            for i in range (len(b)-len(c)):
                c.append(0)
            
        elif len(b)<len(c):
            for i in range (len(c)-len(b)):
                b.append(0)
                
        for i in range (len(b)):
            l.append(b[i]+c[i])
        return Polynomial(self.var,d,l)

    def __mul__(self,self1):
         c = [0]*(len(self.c)+len(self1.c)-1)    
         for i in range (len(self.c)):           
             for j in range (len(self1.c)):      
                 c[i+j]+=(self.c[i]*self1.c[j])
         return Polynomial(self.var, self.deg+self1.deg, c)

    def __neg__(self):  
        n = []
        for i in range (len(self.c)):
            n.append(-1*self.c[i])      
        return Polynomial(self.var, self.deg, n)

    def __sub__(self,self1):
        return self + (-(self1))


def main():
    var1 = input("Enter variable of first polynomial: ")
    deg1 = int(input("Enter degree of first polynomial: "))
    c1 = []
    for i in range (deg1+1):
        c1.append(randint(-5,5))
    while c1[len(c1)-1]==0:
        c1[len(c1)-1]=randint(-5,5)
    pol1 = Polynomial (var1, deg1, c1)
    print (f'Pol1: {pol1}')
    print (f'Degree of Pol1: {pol1.deg}')

    var2 = input("Enter variable of second polynomial: ")
    deg2 = int(input("Enter degree of second polynomial: "))
    c2 = []
    for i in range (deg2+1):
        c2.append(randint(-5,5))
    while c2[len(c2)-1]==0:
        c2[len(c2)-1]=randint(-5,5)
    pol2 = Polynomial (var2, deg2, c2)
    print (f'Pol2: {pol2}')
    print (f'Degree of Pol2: {pol2.deg}')

    print (f'Pol1 + Pol2: {pol1+pol2}')
    print (f'Pol1 * Pol2: {pol1*pol2}')
    print (f'Pol1 - Pol2: {pol1-pol2}')
    
if __name__ == "__main__":
    main()
