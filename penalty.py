from imports import np
from optfunc import Optimization
from simplex import simplex

def penalty(obj: Optimization, x, r):
    bX = 0
    bX += obj.g(x)**2

    for h in obj.h(x):
        bX += max(0, h)**2

    return obj.f(x) + (1/r)*bX

def minPen(obj: Optimization, x0, initR=10, eps=1e-6):
    # initR - baudos koeficientas
    results = {
        "points": [],
        "funcVals": [],
        "niter": [],
        "neval": []
    }

    class PenaltyObjectiveFunction:
        def f(self, x):
            return penalty(obj, x, r)

    penaltyObjFunc = PenaltyObjectiveFunction()
    currX = x0
    r = initR

    while True:
        point, funcVal, iterations = simplex(penaltyObjFunc, currX)

        results["points"].append(point)
        results["funcVals"].append(funcVal)
        results["niter"].append(iterations)
        results["neval"].append(Optimization.counter)

        if sum([obj.g(point)**2]+[max(0, h)**2 for h in obj.h(point)])<eps:
            break

        if np.linalg.norm(np.array(point)-np.array(currX))<eps:
            break

        r *= 0.5
        obj.reset()
        currX = point

    return results

