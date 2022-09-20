class Node :
    data = None
    left = None
    right = None
    center = None

    def __init__(self, data) :
        init = data[0]
        #  switch(init) {
        #      case 'Q':
        #          this.data = String.valueOf(init);
        #          this.left = null;
        #          this.right = null;
        #          this.center = new Node(data.substring(1));
        #          return;
        #      case 'L':
        #          this.data = String.valueOf(init);
        #          this.left = null;
        #          this.right = null;
        #          this.center = new Node(data.substring(1));
        #          return;
        #      default:
        #  }
        if (init.isdigit()) :
            self.data = init
            self.left = None
            self.right = None
            self.center = None
            return
        if (init.isalpha()) :
            if (not init.isupper()) :
                variable = init
                finishVariable = True
                i = 0
                while finishVariable:
                    if(data[i+1] == "!"):
                        variable+=data[i+1]
                        finishVariable = False
                        break
                    variable+=data[i+1]
                    i=i+1
                
                self.data = variable
                self.left = None
                self.right = None
                self.center = None
                return
        else :
            self.data = init
            self.left = Node(data[1:])
            finishVariable = True
            i = 1
            if(data[1].isalpha()):
                while finishVariable:
                    if(data[i+1] == "!"):
                        finishVariable = False
                        i=i+1
                        break
                    i=i+1
            self.right = Node(data[i+1:])
            # if ((not data[1].isupper())):                                
            #     self.right = Node(data[2:])
            # else :
            #     count = 0
            #     isRight = 0
            #     i = 1
            #     while (len(data) > i) :
            #         if (not data[i-1].isupper()):                        
            #             count += 1
            #         else :
            #             isRight += 1
            #         if (isRight == count) :
            #             self.right = Node(data[i:])
            #             break
            #         i += 1
            self.center = None
            return
    

    def  nodeToString(self) :
        var = self.data
        if (self.center != None) :
            var = var + self.center.nodeToString()
        if (self.left != None) :
            var = var + self.left.nodeToString()
        if (self.right != None) :
            var = var + self.right.nodeToString()
        return var

    def  showNode(self) :
        var = self.data
        if (self.center != None) :
            var = var + "(" + self.center.showNode() + ")"
        if (self.left != None) :
            var = var + "(" + self.left.showNode() + ")"
        if (self.right != None) :
            var = var + "(" + self.right.showNode() + ")"
        return var

    