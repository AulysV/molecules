prefixe = ["0", "méth", "éth", "prop", "but", "pent", "hex", "hept", "oct"]
suffixe = ["an", "yl"]


while True:
    nb_c = int(input("Combien de C dans la molécule ? "))

    while True:
        if nb_c > 8 or nb_c < 1:
            print("Nombre incorrect, réessayer.")

        else:
            radical = prefixe[nb_c] + suffixe[0]
            print(f"Radical : {radical}")

            r_rami = int(
                input("Quel est le rang de la ramification (0 pour pas de rami) ? ")
            )

            while True:
                if r_rami < 0 or r_rami > nb_c:
                    print("Nombre incorrect, réessayer.")

                else:
                    nb_rami = int(
                        input(
                            "Combien de C dans la ramification ? (0 pour pas de rami) "
                        )
                    )

                    while True:
                        if nb_rami < 0:
                            print("Nombre incorrect, réessayer.")

                        else:
                            if r_rami != 0:
                                n_prefixe = prefixe[r_rami] + suffixe[1]
                                print(f"{r_rami}-{n_prefixe}{radical}")

                            elif r_rami == 0 or nb_rami == 0:
                                n_prefixe = 0

                            else:
                                print("Erreur")
                                pass

                            r_gc = int(
                                input("Quel est le rang du groupe caractéristique ? ")
                            )

                            while True:

                                def fonc():
                                    print(
                                        "Choisissez un nombre, en fonction du groupe caractéristique de la molécule étudiée :"
                                    )
                                    print("1. Hydroxyle : C liaison OH")
                                    print("Carbonyles :")
                                    print(
                                        "    2 : Aldéhyde : C double liaison O, et C lisaion simple H (en fin de chaine)"
                                    )
                                    print(
                                        "    3 : Cétone : C double liason O (en milieu ou fin de chaine)"
                                    )
                                    print(
                                        "4. Carboxyle : C double liaison O, et C lisaion simple OH (en fin de chaine)"
                                    )

                                    while True:
                                        choix = int(
                                            input("Choisissez : 1, 2, 3, ou 4 : ")
                                        )

                                        t = ["0", "ol", "al", "one", "oïque"]

                                        if choix not in [1, 2, 3, 4]:
                                            print("Choix incorrect")

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

                                        elif choix == 4:

                                            if (r_rami == 0) or (n_prefixe == 0):
                                                print(f"Acide {radical}{t[4]}")

                                            else:
                                                print(
                                                    f"Acide-{r_rami}-{n_prefixe}{radical}{t[4]}"
                                                )
                                        quit()

                                if r_gc < 0 or r_gc > nb_c:
                                    print("Nombre incorrect, réessayer.")

                                elif r_gc == 1:
                                    ui = int(
                                        input(
                                            "Est-ce que le gc est toujours en position 1 ? 1 pour oui, 2 pour non : "
                                        )
                                    )

                                    while True:
                                        if ui not in [1, 2]:
                                            print("Erreur")
                                        else:
                                            fonc()
                                            quit()
                                else:
                                    fonc()
                                    quit()
