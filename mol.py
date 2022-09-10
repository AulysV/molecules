prefixe = ["0", "méth", "éth", "prop", "but", "pent", "hex", "hept", "oct"]
suffixe = ["an", "yl"]

# On définit la function principale du programme : on va l'appeller quand on aura tout défnit
def main():
    # On définit toutes les valeurs par défaut ici
    nb_c = False
    r_rami = False
    nb_rami = False
    r_gc = False
    ui = False
    n_prefixe = 0

    # On définit une valeur qui indique si la boucle doit se répéter, on peut la changer plus tard si besoin
    repeat = True

    while repeat:
        # On récupère le nombre de C dans la molécule

        # On check si la valeur est celle par défaut
        if nb_c == False:
            nb_c = int(input("Combien de C dans la molécule ? "))

        # Si la valeur n'est pas correct
        if nb_c > 8 or nb_c < 1:
            # On dit que la valeur est pas bonne et on la remet à sa valeur par défaut
            print("Nombre incorrect, réessayer.")
            nb_c = False
            pass

        radical = prefixe[nb_c] + suffixe[0]
        print(f"Radical : {radical}")

        # On récupère le nombre de ramification

        # On répète le même principe avec r_rami
        if r_rami == False:
            r_rami = int(
                input("Quel est le rang de la ramification (0 pour pas de rami) ? ")
            )

        if r_rami < 0 or r_rami > nb_c:
            print("Nombre incorrect, réessayer.")
            r_rami = False
            pass

        # On récupère le nombre de C dans la ramification si besoin

        if r_rami != 0:
            # On répète le même principe avec nb_rami
            if nb_rami == False:
                nb_rami = int(
                    input("Combien de C dans la ramification ? ")
                )

            if nb_rami < 1:
                print("Nombre incorrect, réessayer.")
                nb_rami = False
                pass

        # On calcule
        
        if r_rami != 0:
            n_prefixe = prefixe[r_rami] + suffixe[1]
            print(f"{r_rami}-{n_prefixe}{radical}")

        elif r_rami == 0 or nb_rami == 0:
            n_prefixe = 0

        else:
            print("Erreur")
            pass

        # On récupère le rang du groupe caractéristique

        if r_gc == False:
            r_gc = int(
                input("Quel est le rang du groupe caractéristique ? ")
            )

        if r_gc < 0 or r_gc > nb_c:
            print("Nombre incorrect, réessayer.")
            r_gc = False
            pass

        elif r_gc == 1:
            if ui == False:
                ui = int(
                    input("Est-ce que le gc est toujours en position 1 ? 1 pour oui, 2 pour non : ")
                )

            if ui not in [1, 2]:
                print("Erreur")
                ui == False
                pass
            
            # j'ai juste supprimé un arrêt de la boucle inutile ici

        # On arrête la boucle mais pas le script
        repeat = False
    
    # Ici j'ai juste remplacé la fonction par le contenu de cette dernière : ce bout n'est utilisé qu'une seule fois

    # J'ai juste modifié le style ici car je trouvais que ça prennait trop de place : si tu veux tout changer hésite pas
    print("Choisissez un nombre, en fonction du groupe caractéristique de la molécule étudiée :")
    print("1. Hydroxyle : C liaison OH")
    print("Carbonyles :")
    print("    2 : Aldéhyde : C double liaison O, et C lisaion simple H (en fin de chaine)")
    print("    3 : Cétone : C double liason O (en milieu ou fin de chaine)")
    print("    4. Carboxyle : C double liaison O, et C lisaion simple OH (en fin de chaine)")

    # On réindique qu'on repeat de nouveau la boucle
    repeat = True

    while repeat:
        choix = int(
            input("Choisissez : 1, 2, 3, ou 4 : ")
        )

        t = ["0", "ol", "al", "one", "oïque"]

        if choix not in [1, 2, 3, 4]:
            print("Choix incorrect")
            pass

        elif choix == (1 or 2 or 3):

            if n_prefixe == 0:
                print(f"{radical}-{r_gc}-{t[choix]}")

            elif (
                (n_prefixe == 0)
                and (r_gc == 1)
                and (ui == 1)
            ):
                print(f"{radical}{t[choix]}")

            else:
                print(
                    f"{r_rami}-{n_prefixe}{radical}-{r_gc}-{t[choix]}"
                )

        # je l'ai juste mis en else car le choix ne peut être que "4"
        else:
            if (r_rami == 0) or (n_prefixe == 0):
                print(f"Acide {radical}{t[4]}")

            else:
                print(
                    f"Acide-{r_rami}-{n_prefixe}{radical}{t[4]}"
                )
        
        # On stop la boucle
        repeat = False

main()