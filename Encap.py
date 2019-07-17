class encap:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed=100
        self.__name="Verna"

    def display(self):
        print(self.__maxspeed)

    #__maxspeed = 89

    def set(self,speed):
        self.__maxspeed=speed



car1=encap()              ##in python you cannot achive properly the encapsulation
#print(car1.__maxspeed)   ##but you can show your intenctions

car1.display()  ###but you can use that inside the classs achieved using double underscore

### if you want to change the value of the that private you need to use the setter method



car1.set(500)
car1.display()

