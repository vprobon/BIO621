# This module implements a very simple class describing 'Genome' objects

class Genome:
    genetic_code = "standard" ## This is a "class variable"

    def __init__(self, species):
        self.__name = species
        self.__private_attribute = "Private attribute"
        self._protected_attribute = "Protected attribute"
        self.species = species ## This is an object attribute/variable ("instance variable")
        self.genes = []
        
        
    def add_gene(self, gene):
        self.genes.append(gene)

    def gene_count(self):
        return len(self.genes)

    def __str__(self):
        return(f"Genome of {self.__name}\n"
               f"with {self.gene_count()} genes\n"
               f"Private: {self.__private_attribute}\n"
               f"Protected: {self._protected_attribute}")
