from scipy.optimize import bisect, newton

def f(x):
    return x**5 + 5.25*x**4 + 4.125*x**3 - 9.125*x**2 - 14.625*x - 5.625

def df(x):
    return 5*x**4 + 21*x**3 + 12.375*x**2 - 18.25*x - 14.625

r1 = bisect(f, -4.0, -3.5)
r2 = bisect(f, -1.5, -0.5)
r3 = bisect(f, 1.0, 2.0)

n1 = newton(f, -4.0, fprime=df)
n2 = newton(f, -1.2, fprime=df)
n3 = newton(f, 2.0, fprime=df)

print("raices para biseccion")
print(f"x1 = {r1:.10f}")
print(f"x2 = {r2:.10f}")
print(f"x3 = {r2:.10f}")  
print(f"x4 = {r2:.10f}")  
print(f"x5 = {r3:.10f}")

print("\nraices para newton")
print(f"x1 = {n1:.10f}")
print(f"x2 = {n2:.10f}")
print(f"x3 = {n2:.10f}")  
print(f"x4 = {n2:.10f}")  
print(f"x5 = {n3:.10f}")