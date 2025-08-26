# multi-threading 

from threading import *
from time import sleep
class VIT(Thread):
    def run(self):
        for i in range(50):
            print("VIT")

class CSE(Thread):
    def run(self):
        for i in range(50):
            print("CSE")

class stu(Thread):
    def run(self):
        for i in range(50):
            print("AIML")
t1=VIT()
t2=CSE()
t3=stu()
t1.start()
t2.start()
t3.start()
print("Students")
