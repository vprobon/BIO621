class ExpressionGenome(Genome):
    '''This module needs debugging.'''

    data_type = "RNA-seq"

    def __init__(self, species)
        super().__init__(species)
        self.expression = []

    def add_expression(self, gene, value):
        self.expression[gene] = value

    def mean_expression()

        total = sum(self.expression.values())
        return total / len(self.expression)

    def highly_expressed(self, threshold):
        genes = []

        for gene, value in self.expression.items():
            if value > threshold:
                genes.append(value)

        return genes
