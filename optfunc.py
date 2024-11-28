class Optimization:
    counter = 0

    def __init__(self):
        pass

    def f(self, x):
        Optimization.counter += 1 
        return -(x[0]*x[1]*x[2])
    
    def g(self, x):
        return 2*(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])-1
    
    def h(self, x): 
        return [-x[0], -x[1], -x[2]]
          
    def reset(self):
        Optimization.counter = 0