class Optimization:
    counter = 0

    def __init__(self):
        pass

    def f(self, x):
        Optimization.counter += 1 
        return -(x[0]*x[1]*x[2])
    
    def g(self, x):
        return 2*(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])-1   # 2ab+2ac+2bc=1  =>  2(ab+ac+bc)-1=0  =>  gi(a,b,c)=0  - lygibinis apribojimas
    
    def h(self, x): 
        return [-x[0], -x[1], -x[2]]                 # a,b,c>0  => hi(a,b,c)>=0     - nelygibinis apribojimas
    
    def reset(self):
        Optimization.counter = 0