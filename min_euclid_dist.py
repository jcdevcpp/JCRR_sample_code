'''
You have an array p of points on a Cartesian plane. Find and return the minimum possible Euclidian distance between two points with different indices in p.

Example

For p = [[0, 11], [-7, 1], [-5, -3]], the output should be
closestPointPair(p) = 4.472135955.

Input/Output

    [execution time limit] 5.5 seconds (py3)

    [input] array.array.integer p

    Every inner array p[i] contains exactly 2 integers: the x and y coordinates of the ith point.

    Guaranteed constraints:
    2 ≤ p.length ≤ 2 · 104,
    p[i].length = 2,
    |p[i][j]| ≤ 107.

    [output] float

    The minimum possible distance between two points with different indices in p.

    Your answer will be considered correct if its absolute error doesn't exceed 10-5.
'''

from math import sqrt

def one_dim_dist(p1, p2):
    return abs(p1,p2)

def euclid_dist(pa, pb):
    ''' calculate distance between two points
        pa=[xc,yc], pb=[xc,yc]
    '''
    xd=abs(pa[0]-pb[0])
    yd=abs(pa[1]-pb[1])
    return sqrt(xd**2+yd**2)

def find_min_distance(p_array):
    distlist=[]
    for midx, refp in enumerate(p_array):
        print(f'{refp = }')
        for idx in range(midx+1,len(p_array)):
            print(f'-----------------{p_array[idx]  = }')
            d=euclid_dist(refp,p_array[idx])
            print(f'distancia {d}')
            distlist.append(d)
    return min(distlist)

if __name__=="__main__":
    d=find_min_distance([[0,11], 
        [-7,1], 
        [-5,-3]])
    print(d)




