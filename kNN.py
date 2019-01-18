import numpy as np

def distance(p1, p2):
    """Returns the distance between point p1 and point p2"""
    return np.sqrt(np.sum(np.power(p1 - p2, 2)))
    
    
    
p1 = np.array([1,1])
p2 = np.array([4,4])
distance(p1, p2)
