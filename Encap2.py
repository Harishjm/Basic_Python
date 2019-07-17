class Django:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30


    def pry(self):
        print(self.__c)

    def setValues(self,newer):
        self.__c=newer


obj1=Django()
print(obj1.a)   ###No encap
print(obj1._b)   ###Trying  to achieve but still we can acccess
#print(obj1.__c)
print(obj1.pry())
obj1.setValues(2555)
###You cant access
print(obj1.pry())