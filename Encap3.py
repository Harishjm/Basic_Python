class Robot(object):
   def __init__(self):
      self.__version = 22
      print(self.__encap())   ###inside the class you can access

   def getVersion(self):
      print(self.__version)
   def __encap(self):
       return "Encapsulating"

   def setVersion(self, version):
      self.__version = version

obj = Robot()
obj.getVersion()  ##print the version
obj.setVersion(23)  ###changed it using setter
obj.getVersion()
##obj.__encap()  you cant access
