from optfunc import Optimization

def simplex(obj: Optimization, x0, initStep=0.025, stepCoeff=1.025, eps=1e-4, alpha=1, gamma=2, rho=0.5):
    n = len(x0)
    pond = [x0]
    fVals = [obj.f(x0)]
    it = 0

    for i in range(n):
        xTemp = x0.copy()
        if xTemp[i] == 0:
            xTemp[i] += initStep
        else:
            xTemp[i] *= stepCoeff
        pond.append(xTemp)
        fVals.append(obj.f(xTemp))

    while True:
        it += 1

        sortedInd = sorted(range(len(fVals)), key=lambda i: fVals[i])
        pond = [pond[i] for i in sortedInd]
        fVals = [fVals[i] for i in sortedInd]

        x_m = [sum([pond[i][j] for i in range(len(pond) - 1)]) / n for j in range(n)]

        x_r = [x_m[j] + alpha * (x_m[j] - pond[-1][j]) for j in range(n)]
        y_r = obj.f(x_r)

        if fVals[0] <= y_r < fVals[-2]:
            pond[-1], fVals[-1] = x_r, y_r
        elif y_r < fVals[0]:
            x_e = [x_m[j] + gamma * (x_m[j] - pond[-1][j]) for j in range(n)]
            y_e = obj.f(x_e)
            if y_e < y_r:
                pond[-1], fVals[-1] = x_e, y_e
            else:
                pond[-1], fVals[-1] = x_r, y_r
        else:
            x_c = [x_m[j] + rho * (pond[-1][j] - x_m[j]) for j in range(n)]
            y_c = obj.f(x_c)
            if y_c < fVals[-1]:
                pond[-1], fVals[-1] = x_c, y_c
        
        xErr = max([sum((pond[i][j] - pond[0][j]) ** 2 for j in range(n)) ** 0.5 for i in range(1, len(pond))])
        yErr = abs(fVals[0] - fVals[-1])

        if xErr < eps and yErr < eps:
            break

    return pond[0], fVals[0], it
