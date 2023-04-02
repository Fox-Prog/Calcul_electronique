
# Caractéristiques du régulateur

U_out = int(input("Tension de sortie... "))
I_max = float(input("Intenstié max en sortie... "))
I_max_reg = float(input("Intenstié max pour le régulateur... "))

Hfe = int(input("Hfe transistor... "))
Vbe = float(input("Vbe transistor... "))

# Calcul
    
# U_in minimum ______________________________________________
if U_out == 5:
    U_in = 9
elif U_out == 8:
    U_in = 12
else:
    U_in = (1.4*U_out)

# C1 ______________________________________________
C1 = 20000/(U_in/I_max)

# C4 ______________________________________________
C4 = C1/10

# R1 ______________________________________________
Ib = I_max/Hfe
I_R1 = I_max_reg - Ib
R1 = Vbe/I_R1
W_R1 = (I_R1*I_R1)*R1

# R2 ______________________________________________
R2 = Vbe/I_max

print('\n')

print(f"Tension d'entré minimum: {round(U_in, 3)}")
print(f"C1: {round(C1, 3)} uF")
print(f"C4: {round(C4, 3)} uF")
print(f"R1: {round(R1, 3)} ohms, {round(W_R1, 3)} watt")
print(f"R2: {round(R2, 3)} ohms")

print('\n')

stop = input("For exit --> Press enter... ")
