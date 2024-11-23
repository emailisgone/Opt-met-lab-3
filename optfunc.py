class Optimization:
    counter = 0

    def __init__(self):
        pass

    def f(self, x):
        Optimization.counter += 1 
        return -(x[0]*x[1]*x[2])
    
    def gradF(self, x):
        Optimization.counter += 1
        return [-x[1]*x[2], -x[0]*x[2], -x[0]*x[1]]
    
    def g(self, x):
        Optimization.counter += 1 
        return 2*(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])-1
    
    def gradG(self, x):
        Optimization.counter += 1 
        return [2*(x[1]+x[2]), 2*(x[0]+x[2]), 2*(x[0]+x[1])]
    
    def h(self, x):
        Optimization.counter += 1 
        return [-x[0], -x[1], -x[2]]
    
    def gradH(self, x):
        Optimization.counter += 1 
        return [[-1, 0, 0],[0, -1, 0],[0, 0, -1]]
    
    def reset(self):
        Optimization.counter = 0