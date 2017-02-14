class Bin:
    """
    bin class holds bin items
    """
    def __init__(self, a_bin):
        self.name = a_bin
        self.contents = []
        
    def add(self, item):
        for con in self.contents:
   
            
    def __str__(self):
        s = "Bin {0}:".format(self.name)
        for item in self.contents:
            s += "\n  {0}".format(item)
        return s

class BinItem:
    """
    this is an item from the warehouse
    """
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity
    
    def __str__(self):
        return "SKU {0}: {1}".format(self.sku, self.quantity)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests03.txt")
