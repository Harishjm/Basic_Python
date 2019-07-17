class Poly:
    def __init__(self,name):
        self.name=name

    def dance(self):
        print(self.name ,"Is dancing")

    def dance(self):
        print(self.name ,"Is dancing2")

    def dance(self):
        print(self.name ,"Is dancing332")


obj1=Poly("Babe")

obj1.dance()  ###this will not consider the method overloding but which defined last that will print first


