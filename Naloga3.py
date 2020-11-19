import sys

premer = int(sys.argv[1])
polmer = premer / 2

obseg = 2 * 3.141592653589 * polmer
ploscina = 3.141592653589 * pow(polmer, 2)

print("Obseg je: ", obseg)
print("Ploscina je: ", ploscina)