class Chromosome:
    genes = []

    def __init__(self, g):

        self.genes = []
        self.genes = g

    def getGenes(self, index):
        return self.genes[index]

    def getAllGenes(self):
        return self.genes
