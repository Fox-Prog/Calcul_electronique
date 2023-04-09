

#  Caractéristique du régulateur
print('\n')
print(" _____ Caracteristique du regulateur _____ ")
Ues_max = float(input("Tension E-S max... "))
URs_min = float(input("Tension de sortie min du régulateur... "))

#  Caractéristique du montage
print('\n')
print(" _____ Caracteristique du montage _____ ")
U_out_min = float(input("U_out min... "))
U_out_max = float(input("U_out max... "))
I_max = float(input("Intenstié max en sortie... "))
R1 = 220

# Calcul base
U_in_min = (U_out_max * 1.2)
U_in_max = (U_out_max * 1.4)

R2_max = round((((U_out_max / URs_min)-1) * R1), 2)
R2_min = round((((U_out_min / URs_min)-1) * R1), 2)
Pot = round((R2_max - R2_min), 2)

print('\n')
print(" _____ Resultats _____ ")
print(f"R1 idéal: {R1} ohms")
print(f"R2 idéal: {R2_min} ohms")
print(f"Potentiomètre idéal: {Pot} ohms")
print('\n')

# Potentiomètre existant
Potex = [100,200,220,250,470,500,1000,2000,2200,2500,4700,5000,10000,20000,22000,25000,47000,50000,100000,220000,250000,470000,500000]
Diff = float('inf')

for p in range(len(Potex)):
    diff = abs(Pot - Potex[p])  

    if diff < Diff:
        Diff = diff
        PotR = Potex[p]

print(f"Potentiomètre existant: {PotR} ohms")
print('\n')

# Calcul de la tension out max sans toucher à la tension out min
U_out_max_reel = round(((((PotR + R2_min)/R1)+1)*URs_min), 2)

# Modification de R2_min pour avoir U_out_max fixe
R2_min_reel = round(((R1*((U_out_max/URs_min)-1))- PotR), 2)

# Calcul de la tension out min sans toucher à la tension out max
U_out_min_reel = round((((R2_min_reel/R1)+1)*URs_min), 2)

print(f"Solution 1: {U_out_min}v -- {U_out_max_reel}v (R2: {R2_min} ohms)")
print(f"Solution 2: {U_out_min_reel}v -- {U_out_max}v (R2: {R2_min_reel} ohms)")
print('\n')

# Calcul condensateur
C1 = round(20000/(U_in_max/I_max))
C3 = round(C1 / 10)
C5 = round(C1 / 10)

print(f"C1: {C1} uF")
print(f"C2: film / polyester - voir datasheet du régulateur")
print(f"C3: {C3} uF")
print(f"C4: film / polyester - voir datasheet du régulateur")
print(f"C5: {C5} uF")
print('\n')

save = input("Enregistrer les résultats ?...Y/n... ")