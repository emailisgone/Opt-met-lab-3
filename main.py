'''
Kokia turėtų būti stačiakampio gretasienio formos dėžė, kad vienetiniam paviršiaus plotui jos tūris būtų maksimalus?

1. Aprašykite tikslo funkciją f(X), lygybinio ir nelygybinių apribojimų funkcijas gi(X) ir hi(X) taip, kad optimizavimo uždavinys būtų formuluojamas min f(X), gi(X)=0, hi(X)≤0.
2. Apskaičiuokite funkcijų f(X), gi(X), hi(X) reikšmes taškuose X0=(0,0,0), X1=(1,1,1) ir Xm=(1/10,5/10,7/10).
3. Aprašykite kvadratinę baudos funkciją, apimančią tikslo funkciją ir apribojimus.
4. Patyrinėkite baudos daugiklio įtaką baudos funkcijos reikšmėms.
5. Minimizuokite baudos funkciją praeitame laboratoriniame darbe sukurtu optimizavimo be apribojimų algoritmu sprendžiant optimizavimo uždavinių seką su mažėjančia parametro r seka, kai pirmasis sekos uždavinys optimizuojamas pradedant iš taškų X_0, X_1 ir X_m, o kiekvieno paskesnio uždavinio pradinis taškas yra ankstesnio uždavinio sprendinys. 
6. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius priklausomai nuo pradinio taško.
'''
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