from threading import *
from time import sleep
class VIT(Thread):
    def run(self):
        for i in range(50):
            print("VIT")
            sleep(5)

class CSE(Thread):  
    def run(self):
        for i in range(50):
            print("CSE")
           
class Stu(Thread):  
    def run(self):
        for i in range(50):
            print("AIML")
t1=VIT()
t2=CSE()
t3=Stu()
t1.start()
t2.start()
t3.start()
sleep(3)
print("Students of VIT")