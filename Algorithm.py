import random
import math
from typing import Any
from Chromosome import Chromosome

from Genes import Genes
from Node import Node

class Algorithm:
    context = [[]]

    def __init__(self, ctx):
        self.context = ctx 

    def creatChromosome(self):

        g1 = None
        genes = []
        c1 = Chromosome(None)
        geneCount = 0

        j = 0
        while geneCount>=j:
            rand = random.randint(0,7)
            type = ""
            if rand in (1,2,3):
                type = "var"
            elif rand in (0,4,5):
                type = "op"
                geneCount+=2
            elif rand in (6,7):
                type = "const"
            g1 = Genes(type,self.context)
            genes.append(g1)
            j += 1
        c1 = Chromosome(genes)

        return c1

    def createPopulation(self, ind):

        c1 = Chromosome(None)
        cS = [None for _ in range(ind)]

        i = 0
        while ind> i:
            c1 = self.creatChromosome()
            cS[i] = c1
            i += 1
        return cS


    def mutateNode(self, cs, context):
        
        lenghtCS = len(cs)
        randomMutate = random.randint(0,6)
        if randomMutate in (0,1,2,3): 
            # mutate by changing random chart (len(context[0])-1)
            randomIndexChart = random.randint(0,lenghtCS-1)
            randConst = random.randint(0,6)
            if ((cs[randomIndexChart]).isdigit() and not(self.isPartOfVariable(cs,randomIndexChart))):
                print("Reemplazar digito: ")
                if randConst in (0,1,2):
                    cs= cs[:randomIndexChart] + "1" + cs[randomIndexChart+1:]
                elif randConst in (4,5):
                    cs= cs[:randomIndexChart] + "2" + cs[randomIndexChart+1:]
                elif randConst in (6,3): # Mutate by changing a random chart by a random var
                    randomIndexContextCost = random.randint(0,(len(context[0])-2))
                    cs= cs[:randomIndexChart]+context[0][randomIndexContextCost]+cs[randomIndexChart+1:]
            elif(self.isVariable(cs[randomIndexChart])):
                print("Reemplazar variable: ")
                gap = self.lenOfVariable(cs,randomIndexChart)
                if randConst in (0,1,2):
                    cs= cs[:randomIndexChart] + "1" + cs[randomIndexChart+gap:]
                elif randConst in (4,5):
                    cs= cs[:randomIndexChart] + "2" + cs[randomIndexChart+gap:]
                elif randConst in (6,3): # Mutate by changing a random chart by a random var
                    randomIndexContextCost = random.randint(0,(len(context[0])-2))
                    print("Problema")
                    print(cs)
                    print(context[0][randomIndexContextCost])
                    print(randomIndexChart)
                    print(randomIndexChart+gap)
                    cs= cs[:randomIndexChart]+context[0][randomIndexContextCost]+cs[randomIndexChart+gap:]
                    print("->"+cs)
            elif(cs[randomIndexChart] == "+" or cs[randomIndexChart] == "-" or cs[randomIndexChart] == "*"):
                print("Reemplazar operación: ")
                if randConst in (0,1,2):
                    cs= cs[:randomIndexChart]+ "+" + cs[randomIndexChart+1:]
                elif randConst in (3,4,5):
                    cs= cs[:randomIndexChart]+ "-" + cs[randomIndexChart+1:]
                elif randConst == 6:
                    cs= cs[:randomIndexChart]+ "*" + cs[randomIndexChart+1:]
            else:
                self.mutateNode(cs, context)
        elif randomMutate in (4,5):
            # mutate by adding or subbing 1, 2 or random var
            randConstOp = random.randint(0,7)
            if randConstOp in (0,1,2):
                randAdd = random.randint(0,2)

                if(randAdd in (0,1)): # 66% odds to add +1, 33% to add random var
                    cs= "+1" + cs
                else:
                    randConstVar = random.randint(0,len(context[0]) -2)
                    cs= "+"+ context[0][randConstVar] + cs
            elif randConstOp in (3,4,5):
                randAdd = random.randint(0,2)

                if(randAdd in (0,1)): # 66% odds to sustract 1, 33% to sustract random var
                    cs= "-1" + cs
                else:
                    randConstVar = random.randint(0,len(context[0]) -2)
                    cs= "-"+ context[0][randConstVar] + cs
            elif randConstOp == 6:
                randAdd = random.randint(0,2)

                if(randAdd in (0,1)):
                    cs= "+2" + cs
                else:
                    randConstVar = random.randint(0,len(context[0]) -2)
                    cs= "+"+ context[0][randConstVar] + cs
            elif randConstOp == 7:
                randAdd = random.randint(0,2)

                if(randAdd in (0,1)):
                    cs= "-2" + cs
                else:
                    randConstVar = random.randint(0,len(context[0]) -2)
                    cs= "-"+ context[0][randConstVar] + cs
        elif randomMutate == 6:
            # CREATE NEW CHROMOSOME 
            chromosomeCreated = self.creatChromosome()
            newNode = self.chromosomeToNode(chromosomeCreated)
            newStringNode = newNode.nodeToString()

            #cs = newStringNode[:len(newStringNode)-1] + cs  # works only on 1-length variables
            if(newStringNode[len(newStringNode)-1] == "!"):   # Add new Chromosome without last var or digit to the old Chromosome
                i = 1
                finishVariable = True
                while finishVariable:
                    if(newStringNode[len(newStringNode)-(1+i)] == "a"):
                        finishVariable = False
                        break
                    i=i+1
                cs = newStringNode[:len(newStringNode)-(1+i)] + cs
            else:
                cs = newStringNode[:len(newStringNode)-1] + cs

        return cs

    def chromosomeToNode(self, c):

        chromosomeStrInfo = ""
        allGenes = c.getAllGenes()

        j = 0
        while len(allGenes)> j:
            if chromosomeStrInfo is None:
                chromosomeStrInfo = allGenes[j].get()
            else:
                chromosomeStrInfo = chromosomeStrInfo + allGenes[j].get()
            j += 1
        node = Node(chromosomeStrInfo)
        return node

    def isVariable(self, var):
        bool1 = False
        if(var[0].isalpha()):
            bool1 = True
        return bool1
    
    def isPartOfVariable(self, data, index):
        bool1 = False

        i=index
        while i > 0:
            if(data[i-1] == "a"):
                bool1=True
                i=0
                break
            i=i-1
        return bool1

    def lenOfVariable(self, data, index):
        gap = index
        i=1
        finishVariable = True
        while finishVariable:
            if(data[gap+i] == "!"):
                i = i+1
                finishVariable = False
                break
            i=i+1

        return i

