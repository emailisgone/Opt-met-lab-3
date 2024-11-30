from imports import datetime, math, np, sp, plt, scp
from optfunc import Optimization
from penalty import minPen
print(f"{datetime.now()}\n")

obj = Optimization()

print("----------------------[VALUES AT 0,0,0]-----------------------------------------------------")
point = [0,0,0]
#a, b, c = obj.f(point), obj.g(point), obj.h(point)
#print(f"f(X) = {a}, g(X) = {b}, h(X) = {c}")
#print(minPen(obj, point))
saved = minPen(obj, point)
for i in saved:
    print(saved[i])
obj.reset()

print("----------------------[VALUES AT 1,1,1]-----------------------------------------------------")
point = [1,1,1]
#a, b, c = obj.f(point), obj.g(point), obj.h(point)
#print(f"f(X) = {a}, g(X) = {b}, h(X) = {c}")
#print(minPen(obj, point))
saved = minPen(obj, point)
for i in saved:
    print(saved[i])
obj.reset()

print("----------------------[VALUES AT 0.1,0.5,0.7]-----------------------------------------------------")
point = [0.1,0.5,0.7]
#a, b, c = obj.f(point), obj.g(point), obj.h(point)
#print(f"f(X) = {a}, g(X) = {b}, h(X) = {c}")
#print(minPen(obj, point))
saved = minPen(obj, point)
for i in saved:
    print(saved[i])
obj.reset()