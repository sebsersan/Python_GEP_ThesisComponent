import random
from random import Random
from evalTree import evalTree
from Node import Node
from Algorithm import Algorithm

class main:

    @staticmethod
    def run(self):
        GENERATIONS = 200
        POPULATIONSIZE = 10

        # nodeTest = Node("-+1+11-11")
        # context = [["a0!","result"],["2","180"]]
        # evaluator = evalTree()
        # algorithm = Algorithm(context)

        # print("Nodo creado str: " + nodeTest.nodeToString())
        # print("Nodo creado: " + nodeTest.showNode())
        # print("Resultado : " + str(evaluator.evalT(nodeTest, context)))

        # nodeTestString = nodeTest.nodeToString()

        # mutatedStringNode =algorithm.mutateNode(nodeTestString,context)
        # mutatedNode = Node(mutatedStringNode)

        # print("Nodo mutado str: " + mutatedStringNode)
        # print("Nodo mutado: " + mutatedNode.showNode())
        # print("Resultado: " + str(evaluator.evalT(mutatedNode, context)))
        # return 

        context = self.createContext()

        #context = [["a", "b", "c", "d", "h", "result"], ["3", "4", "5", "12", "80", "1245"]] # Context given
        index = len(context[1])

        obtainResults = [0 for _ in range(POPULATIONSIZE)]
        fitness = [0 for _ in range(POPULATIONSIZE)]

        realResult = float(context[1][index-1])

        algorithm = Algorithm(context)
        nodes = [None for _ in range(POPULATIONSIZE)]

        evaluator = evalTree()

        betterDistance = 9000
        bestNode = Node("0")


        initPopulation = algorithm.createPopulation(POPULATIONSIZE)
        i = 0
        while POPULATIONSIZE> i:

            nodes[i] = algorithm.chromosomeToNode(initPopulation[i])

            print("-----")
            print("Node " + str(i))
            print(nodes[i].showNode())
            print("-----")

            print("Evaluation:")
            obtainResults[i] = evaluator.evalT(nodes[i], context)
            print(obtainResults[i])
            print("-----><-----")

            fitness[i] = -abs(realResult - obtainResults[i])

            if abs(obtainResults[i] - realResult) < betterDistance:
                betterDistance = abs(obtainResults[i] - realResult)
                bestNode = nodes[i]
            i += 1
        print("Generation: " + str(0))
        print("Context: ")
        print((context[0]))
        print((context[1]))
        print("Better Global node:")
        print(bestNode.showNode())
        betterScore = evaluator.evalT(bestNode, context)
        print("Evaluation: "+str(betterScore))
        print("Goal: "+ str(realResult))
        print("Distance: " + str(betterDistance))
        if betterDistance == 0.0:
            print("! Result found !")
            print(bestNode.showNode())
            print(bestNode.nodeToString())
            print("end program")
            return
        iterator = 0
        while GENERATIONS> iterator:

            # sort nodes
            i = 0
            while i < len(fitness):
                j = i + 1
                while j < len(fitness):
                    if fitness[i] > fitness[j]:
                        tempfitness = fitness[i]
                        tempnodes = nodes[i]
                        fitness[i] = fitness[j]
                        nodes[i] = nodes[j]
                        fitness[j] = tempfitness
                        nodes[j] = tempnodes
                    j += 1
                i += 1

            iter2 = 0
            while POPULATIONSIZE> iter2:
                iterDouble = iter2
                probability = ((100*(1+iterDouble)/POPULATIONSIZE) - 1.21) # Probability to mutate current node 21% (I think so?)
                rand = Random()
                if not(rand.random() < probability/100):
                    if rand.random() < 0.22:    # probability of 22% to create new chromosome in generation (I Think So?)
                        print("NodeBeforCreated: " + nodes[iter2].nodeToString())
                        nodes[iter2] = algorithm.chromosomeToNode(algorithm.creatChromosome())
                    else:
                        print("NodeBeforMutated: " + bestNode.nodeToString())
                        mutatedStringBetterNode = algorithm.mutateNode(bestNode.nodeToString(), context)
                        print("NodeAfterMutated: " + mutatedStringBetterNode)
                        nodes[iter2] = Node(mutatedStringBetterNode)
                    print("Contexto: "+str(context) + " Nodo: " + nodes[iter2].nodeToString())
                    obtainResults[iter2] = evaluator.evalT(nodes[iter2], context)       #Problema aqui
                    fitness[iter2] = -abs(realResult - obtainResults[iter2])
                    if abs(obtainResults[iter2] - realResult) < betterDistance:
                        betterDistance = abs(obtainResults[iter2] - realResult)
                        bestNode = nodes[iter2]
                else:
                    print("NodeBefor2: " + nodes[iter2].nodeToString())
                    mutatedStringNode = algorithm.mutateNode(nodes[iter2].nodeToString(), context)
                    print("NodeAfter2: " + mutatedStringNode)
                    nodes[iter2] = Node(mutatedStringNode)
                    print("Contexto2: "+str(context) + " Nodo2: " + nodes[iter2].nodeToString())
                    obtainResults[iter2] = evaluator.evalT(nodes[iter2], context)       #Mismo problema que el anterior
                    fitness[iter2] = -abs(realResult - obtainResults[iter2])
                    if abs(obtainResults[iter2] - realResult) < betterDistance:
                        betterDistance = abs(obtainResults[iter2] - realResult)
                        bestNode = nodes[iter2]

                print("-----")
                print("Node " + str(iter2))
                print(nodes[iter2].showNode())
                print("-----")

                print("Evaluation:")
                obtainResults[iter2] = evaluator.evalT(nodes[iter2], context)
                print(obtainResults[iter2])
                print("-----><-----")
                iter2 += 1
            
            print("Generation: " + str(iterator+2)+ "/" + str(GENERATIONS))
            print("Context: ")
            print((context[0]))
            print((context[1]))
            print("Better Global node:")
            print(bestNode.showNode())
            print(bestNode.nodeToString())
            betterScore = evaluator.evalT(bestNode, context)
            print("Evaluation: " + str(betterScore))
            print("Goal: " + str(realResult))
            print("Distance: " + str(betterDistance))
            if betterDistance == 0.0:
                print("! Result found ¡")
                print("Generation: " + str(iterator+2) + "/" + str(GENERATIONS))
                print(bestNode.showNode())
                print(bestNode.nodeToString())
                print("end program")
                return
            iterator+=1
    

    def createContext():


        # Im not sure what i did next (08/30/2022)

        # I think this generate a random 

        # featuresVector1 = [[177, 165],[155, 146]]

        # lengthFV1 = len(featuresVector1) # Length of Features Vector 
        # lengthFVV1 = len(featuresVector1[0]) # Length of Features Values Vector 

        # context = [[],[]]

        # bool1 = 0
        # allFV = []
        # allFVV = []

        # while bool1 <lengthFV1//2:

        #     b1 = False
        #     b2 = False
        #     while not(b1 and b2):
        #         randomLengthFV = random.randint(0,lengthFV1-1)
        #         randomLengthFVV = random.randint(0,lengthFVV1-1)
        #         b1 = not(randomLengthFV in allFV)
        #         b2 = not(randomLengthFVV in allFVV)

        #     allFV.append(randomLengthFV)
        #     allFVV.append(randomLengthFVV)

        #     value = featuresVector1[randomLengthFV][randomLengthFVV]
        #     label = "a" + str(bool1) + "!"
        #     context[0].append(label)
        #     context[1].append(value)

        #     bool1+=1

        context = [["a0!", "a1!", "a2!", "a3!", "a4!", "result"], ["3", "4", "5", "12", "80", "1245"]] # Context given
        return context



# Main function added by Java to Python Converter:

if __name__ == "__main__":
    main().run(main)
