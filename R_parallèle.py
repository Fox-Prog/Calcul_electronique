
def Calcul():
    resistances = [10,12,15,18,22,27,33,39,47,56,68,82,100,120,150,180,220,270,330,390,470,560,680,820]


    RE = float(input("Valeur RE..."))
    mrg = float(input("Marge..."))

    Solution = {}
    var = 0
    s = 1


    Diff = float('inf')
    Bi = -1
    Bj = -1


    if RE in resistances:               # Valeur standard ? ___________________________________________________
        Solution[f'S{var}'] = {'R1':RE}
        var = var + 1


    for i in range(len(resistances)): # 1ere passe ___________________________________________________
        r1 = resistances[i]

        for j in range(len(resistances)):
            r2 = resistances[j]
            re_calculee = (r1*r2)/(r1+r2)
            diff = abs(RE - re_calculee)

            if diff < Diff:
                Diff = diff

                Solution[f'S{var}'] = {'R1':resistances[i], 'R2':resistances[j], 'Val':re_calculee}
            
    var = var + 1


    def ctrl(R1, R2):                    # CTRL DOUBLONS ___________________________________________________
        for el in range(len(Solution)):
            if (R1 + R2) == (Solution[f'S{el}']['R1'] + Solution[f'S{el}']['R2']):
                return False
            
        return True


    for i in range(len(resistances)):   # 2eme passe ___________________________________________________
        r1 = resistances[i]

        for j in range(len(resistances)):
            r2 = resistances[j]
            re_calculee = (r1*r2)/(r1+r2)
            diff = abs(RE - re_calculee)

            if diff <= Diff + mrg or diff == Diff:
                Doublon = ctrl(resistances[i], resistances[j])

                if Doublon == True:
                    Solution[f'S{var}'] = {'R1':resistances[i], 'R2':resistances[j], 'Val':re_calculee}
                    var = var + 1

    print('\n')

    for solus in Solution:
        print(f"Solution {s}: R1= {Solution[solus]['R1']} ohms // R2= {Solution[solus]['R2']} ohms // Valeur précise = {Solution[solus]['Val']}")
        s = s + 1

    print('\n')

Calcul()

Restart = input("Recalculer ?... Y... ")

while Restart == 'Y':
    Calcul()
    Restart = input("Recalculer ?... Y... ")