from optfunc import Optimization
from simplex import simplex

def penalty(obj: Optimization, x, r):
    bX = 0
    bX += obj.g(x)**2

    for h in obj.h(x):
        bX += max(0, h)**2

    return obj.f(x) + (1/r)*bX

def minPen(obj: Optimization, x0, initR=0.1, rDec=0.5, eps=1e-4, maxIter=1000, maxOutIter=10):
    # r - baudos koeficientas
    # maxOutIter - maksimalus sk. kartu kiek dalinam r pusiau, UNLESS minimum is found
    results = {
        "solutions": [],
        "funcVals": [],
        "niter": [],
        "neval": []
    }

    current_x = x0
    r = initR

    for _ in range(maxOutIter):
        class PenaltyObjective:
            def f(self, x):
                return penalty(obj, x, r)

        penalty_obj = PenaltyObjective()

        solution, func_val, iterations = simplex(penalty_obj, current_x, eps=eps, maxIter=maxIter)

        results["solutions"].append(solution)
        results["funcVals"].append(func_val)
        results["niter"].append(iterations)
        results["neval"].append(Optimization.counter)

        if sum([obj.g(solution)**2] + [max(0, h)**2 for h in obj.h(solution)]) < eps:
            break

        r *= rDec

        obj.reset()
        current_x = solution

    return results

