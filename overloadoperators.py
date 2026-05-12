class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "Both are equal"
        else:
            return "Not equal"
    def __eq__(self, other):
        if(self.a==other.a):
          return "They are equal"
        else:
            return "Not equal"   
ob1=A(2)
ob2=A(3)
print("Passed Values",ob1.a,ob2.a)
print(ob1<ob2)
ob3=A(3)
ob4=A(3)
print("Passed Values",ob3.a,ob4.a)
print(ob3==ob4)