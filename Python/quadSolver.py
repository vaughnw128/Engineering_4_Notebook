import math

def quadSolver(a, b, c):
    discriminant = (b*b) - (4*a*c)
    if discriminant < 0:
        return None
    roots = [0,0]
    roots[0] = (-b + math.sqrt(discriminant))/(2*a)
    roots[1] = (-b - math.sqrt(discriminant))/(2*a)
    return roots

print('Quadratic Solver')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
arrRoots = quadSolver(a , b, c)
if(arrRoots == None):
    print('No Real Roots')
else:
    print('Roots: ' + str(arrRoots[0]) + ', ' + str(arrRoots[1]))
