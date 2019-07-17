# try:
#     print(n)
#
# except NameError:
#     print("Its a name error")
# except :
#     print("Something else")


###this whole procedure for Finding name error


try:
    print("Hello")

except Exception as e:
    print(e)

else:
    print("There is no exceptions")


finally:
    print("It will execute for the all the conditions")