import pyexcel_ods3
import os

def Types():
    typ_calc = input('''
    1 >>> Régulateur
    2 >>> Transistor
    >>> ''')

    if typ_calc == '1':
        Calcul_reg()
    elif typ_calc == '2':    
        Calcul_TR()
    else:
        Types()    









def Calcul_TR():
    # Caractéristique du transistor
    print('\n')
    print("_____ Caractéristiques du transistor _____")
    print('\n')
    U_in = float(input("U in MAX... "))
    U_out = float(input("U out... "))
    Ic = float(input("I out... "))
    Vce_sat = float(input("Vce(sat)... "))

    Vce = (U_in - U_out) - Vce_sat
    Pdiss = (Vce*Ic)

    print("Datasheet : Operating junction temperature")
    Tj = float(input("Température max de fonctionnement... "))

    Ta = float(input("Température air ambiant... "))
    print("Datasheet : Thermal Resistance Junction-case")

    Rth_jc = float(input("Résistance thermique jonction - boitier... "))
    print("Datasheet : Thermal Resistance Junction-anbient")

    Rth_ja = float(input("Résistance thermique jonction - air ambient... "))
    print('\n')

    # Calcul de Ta max

    Ta_max = Tj - (Pdiss*Rth_ja)

    # Calcul de Rth dissipateur

    Pdiss_mrg = (Pdiss + (Pdiss/4))
    Rth_diss = ((Tj - Ta)/Pdiss_mrg) - (Rth_jc + 0.5)

    print("_____ Resultats _____")
    print('\n')
    print(f"Température ambient max sans radiateur: {round(Ta_max, 2)} °C")
    print(f"Résistance thermique min du dissipateur: {round(Rth_diss, 2)} °C/W")
    print('\n')


    # SAVE
    Suite = input('''
    1 >>> Enregistrer les résultats
    2 >>> Enregister les résultats + Graphe Ta et C/W_Diss pour I
    3 >>> Recalculer
    >>> ... ''')

    if Suite == '1' or Suite =='2':
        os.chdir('C:/Users/Utilisateur/Desktop')

        name_brut = input("Nom du document... ")
        nametxt = str(name_brut+'.txt')
        nameods = str(name_brut+'.ods')

        file = open(nametxt, 'a', encoding='utf-8')
        file.write('\n')
        file.write('_____ Caracteristiques du transistor _____'+'\n')

        file.write('Vce(sat): '+str(Vce)+' V'+'\n')
        file.write('Ic: '+str(Ic)+' A'+'\n')
        file.write('Temperature max de jonction: '+str(Tj)+ ' \u00b0C'+'\n')
        file.write('Temperature air ambient: '+str(Ta)+' \u00b0C'+'\n')
        file.write('Resistance thermique jonction - air ambient: '+str(Rth_ja)+' \u00b0C/W'+'\n')
        file.write('Resistance thermique jonction - boitier: '+str(Rth_jc)+' \u00b0C/W'+'\n')
        file.write('\n')

        file.write('_____ Resultats _____'+'\n')

        file.write('Puissance dissipee: '+str(Pdiss)+' W'+'\n')
        file.write('Temperature ambiente max sans radiateur: '+str(round(Ta_max, 2))+' \u00b0C'+'\n')
        file.write('Resistance thermique min du dissipateur: '+str(round(Rth_diss, 2))+' \u00b0C/W'+'\n')

        file.close()


    if Suite == '2':
        # Création du tableur
        title_spe = ["Vce", "Tj", "Rth_jc", "Rth_ja"]
        value_spe = [str(Vce), str(Tj), str(Rth_jc), str(Rth_ja)]
        titles = ["Intensité(A)", "Ta_max", "Rth_Diss"]
        data = []
        data.append(title_spe)
        data.append(value_spe)
        data.append("")
        data.append(titles)
        ic = 0.2
        while ic < 15.2:
            Pdiss = (Vce*ic)
            Ta_max = Tj - (Pdiss*Rth_ja)
            Pdiss_mrg = (Pdiss + (Pdiss/4))
            Rth_diss = ((Tj - Ta)/Pdiss_mrg) - (Rth_jc + 0.5)
            
            row = [ic, Ta_max, Rth_diss]
            data.append(row)
            ic += 0.2

        pyexcel_ods3.save_data(str('Graph_tr_' + nameods), {"Ta_max__Rth_Diss pour Ic":data})


    elif Suite == '3':
        Types()
    else:
        exit() 















def Calcul_reg():
    # Caractéristique du régulateur
    print('\n')
    print("_____ Caractéristiques du régulateur _____")
    print('\n')

    U_in = float(input("U in MAX... "))
    U_out = float(input("U out... "))
    I_out = float(input("I out... "))
    print("Datasheet : Operating junction temperature")
    Tj = float(input("Température max de fonctionnement... "))

    Ta = float(input("Température air ambiant... "))
    print("Datasheet : Thermal Resistance Junction-case")

    Rth_jc = float(input("Résistance thermique jonction - boitier... "))
    print("Datasheet : Thermal Resistance Junction-anbient")

    Rth_ja = float(input("Résistance thermique jonction - air ambient... "))
    print('\n')

    # Calcul I max sans dissipateur
    print("_____ Résultats _____")
    print('\n')

    Is = ((Tj - Ta)/Rth_ja) / (U_in - U_out)

    print(f"I max sans dissipateur: {round(Is, 2)} A")

    # Calcul Rth dissipateur

    Rth_diss = ((Tj-Ta)-(((U_in-U_out)*I_out)*Rth_jc)) / ((U_in-U_out)*I_out)

    print(f"Résistance thermique min du dissipateur: {round(Rth_diss, 2)} °C/W")

    print('\n')

    # SAVE
    Suite = input('''
    1 >>> Enregistrer les résultats simple
    2 >>> Enregister les résusltats + graph Imax pour T
    3 >>> Enregister les résusltats + graph Rth_diss pour U_in
    4 >>> Enregistrer tout
    5 >>> Recalculer
    >>> ... ''')

    if Suite == '1' or Suite == '2' or Suite == '3' or Suite == '4':
        os.chdir('C:/Users/Utilisateur/Desktop')

        # Création des fichiers
        name_brut = input("Nom du document... ")
        nametxt = str(name_brut+'.txt')
        nameods = str(name_brut+'.ods')

        file = open(nametxt, 'a', encoding='utf-8')
        file.write('\n')
        file.write('_____ Caracteristiques du regulateur _____'+'\n')

        file.write('Tension d\'entree max: '+str(U_in)+' V'+'\n')
        file.write('Tension de sortie (regulee): '+str(U_out)+' V'+'\n')
        file.write('Intensite max de sortie: '+str(I_out)+' A'+'\n')
        file.write('Temperature max de jonction: '+str(Tj)+ ' \u00b0C'+'\n')
        file.write('Temperature air ambient: '+str(Ta)+' \u00b0C'+'\n')
        file.write('Resistance thermique jonction - air ambient: '+str(Rth_ja)+' \u00b0C/W'+'\n')
        file.write('Resistance thermique jonction - boitier: '+str(Rth_jc)+' \u00b0C/W'+'\n')
        file.write('\n')

        file.write('_____ Resultats _____'+'\n')

        file.write('Intensite max de sortie sans dissipateur: '+str(round(Is, 2))+' A'+'\n')
        file.write('Resistance thermique min du dissipateur: '+str(round(Rth_diss, 2))+' \u00b0C/W'+'\n')

        file.close()

    if Suite == '2' or Suite == '4':
        # Création du tableur
        title_spe = ["U_in", "U_out", "Tj", "Rth_ja", "Rth_jc"]
        value_spe = [str(U_in), str(U_out), str(Tj), str(Rth_ja), str(Rth_jc)]
        titles = ["Ta(°C)", "Imax(A)", "Rth_diss(°C/W)"]
        data = []
        data.append(title_spe)
        data.append(value_spe)
        data.append("")
        data.append(titles)
        for t in range(-20, 61):
            Is = ((Tj - t)/Rth_ja) / (U_in - U_out)
            Is_calc = round(Is, 2)
            Rth_diss = ((Tj-t)-(((U_in-U_out)*I_out)*Rth_jc)) / ((U_in-U_out)*I_out)
            Rth_diss_calc = round(Rth_diss, 2)
            row = [t, Is_calc, Rth_diss_calc]
            data.append(row)

        pyexcel_ods3.save_data(str('Imax for Ta_' + nameods), {"Imax pour T":data})


    if Suite == '3' or Suite == '4':
        # Création du tableur
        title_spe = ["U_out", "I_out", "Tj", "Ta", "Rth_ja", "Rth_jc"]
        value_spe = [str(U_out), str(I_out), str(Tj), str(Ta), str(Rth_ja), str(Rth_jc)]
        titles = ["U_in", "Rth_diss(°C/W)"]
        data = []
        data.append(title_spe)
        data.append(value_spe)
        data.append("")
        data.append(titles)
        for u in range(9, 36):
            Rth_diss = ((Tj-Ta)-(((u-U_out)*I_out)*Rth_jc)) / ((u-U_out)*I_out)
            Rth_diss_calc = round(Rth_diss, 2)
            row = [u, Rth_diss_calc]
            data.append(row)

        pyexcel_ods3.save_data(str('Rth_diss for U_in_'+ nameods), {"Rth_diss pour U_in":data})



    elif Suite == '5':
        Types()
    else:
        exit()        

Types()