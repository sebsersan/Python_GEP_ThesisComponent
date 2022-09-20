import math

class evalTree:

    def evalT(self, root, context):
        if root == None:
            return 0
        left = self.evalT(root.left,context)
        right = self.evalT(root.right,context)
        center = self.evalT(root.center,context)

        if root.data == "+":
            return left + right
        elif (root.data == "-"):
            return left - right
        elif (root.data == "*"):
            return left * right
        elif (root.data == "/"):    #Not in used
            return left / right
        elif (root.data == "Q"):    #Not in used
            return math.sqrt(center)
        elif (root.data == "L"):    #Not in used
            return math.log(center)
        # elif (root.data.isdigit()):   #It can be use as alternative to adding any digit
        #     return int(root.data) 
        elif (root.data == "0"):    #Not sure that is in used
            return 0
        elif (root.data == "1"):
            return 1
        elif (root.data == "2"):
            return 2

        else:
            index = context[0].index(root.data)
            value = int(context[1][index])
            return value
