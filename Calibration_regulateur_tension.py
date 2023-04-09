
# Caractéristiques du régulateur

U_out = float(input("Tension de sortie... "))
U_in_max = float(input("Tension d'entrée min... "))
I_max = float(input("Intenstié max en sortie... "))

tr = input("Montage avec transistor ? ...Y/n... ")

if tr == 'Y':
    I_max_reg = float(input("Intenstié max pour le régulateur... "))
    Hfe = int(input("Hfe transistor... "))
    Vbe = float(input("Vbe transistor... "))

# Calcul
    
# U_in minimum ______________________________________________
U_in = (1.4*U_out)

# C1 ______________________________________________
C1 = 20000/(U_in_max/I_max)

# C4 ______________________________________________
C4 = C1/10

if tr == 'Y':
    # R1 ______________________________________________
    Ib = I_max/Hfe
    I_R1 = I_max_reg - Ib
    R1 = Vbe/I_R1
    W_R1 = (I_R1*I_R1)*R1

    # R2 ______________________________________________
    R2 = Vbe/I_max

print('\n')

print(f"Tension d'entrée minimum: {round(U_in, 3)} ( A comfirmer...)")
print(f"C1: {round(C1)} uF  (min)")
print(f"C4: {round(C4)} uF  (min)")

if tr == 'Y':
    print(f"R1: {round(R1, 3)} ohms, {round(W_R1, 3)} watt")
    print(f"R2: {round(R2, 3)} ohms, 3 watt")

print('\n')

stop = input("For exit --> Press enter... ")
