"""Given a list of points as a tuple (x, y) and an integer k, find the k closest points to the origin (0, 0).

Here's an example and some starter code:

def closest_points(points, k):
  # Fill this in.

print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]"""


def pClosest(points, K):
 
    points.sort(key = lambda K: K[0]**2 + K[1]**2)
 
    return points[:K]
 
# Driver program
points = [[3, 3], [5, -1], [-2, 4]]
 
K = 2
 
print(pClosest(points, K))
