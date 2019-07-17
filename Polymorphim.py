class Engineers:
    def __init__(self,name):
        self.name=name

    def Engineering(self):
        print("Enineers can work on Engineering")

    def Hospital(self):
        print("Engineers can't provide treatement")

class Doctors:
    def __init__(self,name):
        self.name=name

    def Engineering(self):
        print("doctors can't work on Engineering")

    def Hospital(self):
        print("Doctors can provide treatement")




def Coding_Test(student):
    student.Engineering()


harry=Engineers("Harry")
vena=Doctors("Venne")

Coding_Test(harry)
Coding_Test(vena)
