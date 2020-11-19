import sys

print("Vnesite 4 mestno stevilo!")
letnicaRojstva = int(sys.argv[1])

starost = 2020 - letnicaRojstva
print(starost)

if starost > 18:
    print("Stari ste", starost, "let. Lahko se udeležite volitev.")
else:
    print("Žal ste premladi. Volitev se lahko udeležite čez: ", 18 - starost, "let.")