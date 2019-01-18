import numpy as np
import random
import scipy.stats as ss

def distance(p1, p2):
    """Returns the distance between point p1 and point p2"""
    return np.sqrt(np.sum(np.power(p1 - p2, 2)))
    
def majority_vote(votes):
    """
    Returns the most common element in votes
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
            
    max_counts = max(vote_counts.values())
    winners = []
    for vote, count in vote_counts.items():
        if count == max_counts:
            winners.append(vote)
            
    return random.choice(winners)

def majority_vote_short(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

# lets try the distance function
p1 = np.array([1,1])
p2 = np.array([4,4])
distance(p1, p2)

# lets try majority_vote
votes = [1,2,3,1,2,3,1,2,3,3,3,3]
vote_counts = majority_vote(votes)

