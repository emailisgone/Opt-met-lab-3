from optfunc import Optimization
from simplex import simplex

def penalty(obj: Optimization, x, r):
    bX = 0
    bX += obj.g(x)**2

    for h in obj.h(x):
        bX += max(0, h)**2

    return obj.f(x) + (1/r)*bX

def minPen(obj: Optimization, x0, initR=10, rDec=0.9, eps=1e-4):
    # r - baudos koeficientas
    # maxOutIter - maksimalus sk. kartu kiek dalinam r pusiau, UNLESS minimum is found
    results = {
        "solutions": [],
        "funcVals": [],
        "niter": [],
        "neval": []
    }

    currX = x0
    r = initR

    while True:
        class PenaltyObjectiveFunction:
            def f(self, x):
                return penalty(obj, x, r)

        penaltyObjFunc = PenaltyObjectiveFunction()

        solution, funcVal, iterations = simplex(penaltyObjFunc, currX)

        results["solutions"].append(solution)
        results["funcVals"].append(funcVal)
        results["niter"].append(iterations)
        results["neval"].append(Optimization.counter)

        if sum([obj.g(solution)**2] + [max(0, h)**2 for h in obj.h(solution)]) < eps:
            break

        r *= rDec

        obj.reset()
        currX = solution

    return results

