import random

class Genes:
    value = ""

    def __init__(self, type, context):

        if type == "var":
            index = len(context[0]) -1
            rand = random.randint(0,index-1) # Last element is the result thats why "index-1" 
            self.value = context[0][rand]
            return
        elif type == "op":
            randOP = random.randint(0,4)
            if randOP in (0,1):
                self.value = "+"
                return
            elif randOP in (2,3):
                self.value = "-"
                return
            elif (randOP == 4):
                self.value = "*"
                return
        elif type == "const":
            randConst = random.randint(0,2)
            if randConst in (0,1):
                self.value = "1"
                return
            elif (randConst == 2):
                self.value = "2"
                return
        return

    def get(self):
        return self.value
