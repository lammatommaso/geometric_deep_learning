from numpy import array
from scipy.linalg import lu

a = array([[2,-1,0,-1,1],[1,2,-1,0,-1],[0,-1,2,-1,-1],[-1,0,-1,2,1],[1,-1,-1,1,2]])

pl, u = lu(a, permute_l=True)

print(u)
