class Point():

    def __init__(self,n, size):
        self.x = int(n % size)
        self.y = int(n / size)
    
    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    def distance(self, other):
        return(abs(self.x - other.x) + abs(self.y - other.y))