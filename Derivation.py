from sympy import *
import os
import platform

# This part is used to detect the OS you use and clear the console.
OperatingSystem = platform.system() 

if OperatingSystem == "Windows":
        os.system('cls')
else:
        os.system('clear')

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

print("======================[Derivator]======================")
print("Pour dériver en python, il faut savoir comment s'écrivent les équations.")
print("---------------------------------")
print("Voilà comment elles s'écrivent :")
print("2x -> 2*x")
print("x^n -> x**n")
print("cos(x) -> cos(x)")
print("sin(x) -> sin(x)")
print("ln(x) -> ln(x)")
print("e^x -> exp(x)")
print("---------------------------------")
print("Les inconnues à utiliser sont x, y et z.")

# Partie préparation de sympy
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/


# Partie dérivation
print("Entrez votre équation :")
f = input()
print("Avant la dérivation : ")
print(f)
f_prime = diff(f, x)
print("Après la dérivation : ")
print(f_prime)

# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/