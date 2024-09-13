from tabulate import tabulate

etudiants = []

# Fonction pour vérifier si un numéro de téléphone est unique
def verifier_telephone_unique(telephone):
    return not any(e['telephone'] == telephone for e in etudiants)

def obtenir_note(message):
    while True:
        try:
            note = float(input(message))
            if 0 <= note <= 20:
                return round(note, 2)
            print("La note doit être entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer une note valide.")



# Fonction pour ajouter un étudiant
def ajouter_etudiant():
    while True:
        telephone = input("Téléphone : ")
        if len(telephone) == 10 and telephone.isdigit() and verifier_telephone_unique(telephone):
            break
        print("Téléphone invalide ou déjà utilisé. Essayez encore.")
    
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    classe = input("Classe : ")

    note_devoir = obtenir_note("Note de devoir : ")
    note_projet = obtenir_note("Note de projet : ")
    note_examen = obtenir_note("Note d'examen : ")

    moyenne = round((note_devoir + note_projet + note_examen) / 3, 2)

    etudiants.append({
        'telephone': telephone,
        'nom': nom,
        'prenom': prenom,
        'classe': classe,
        'note_devoir': note_devoir,
        'note_projet': note_projet,
        'note_examen': note_examen,
        'moyenne': moyenne
    })

    

# Fonction pour afficher tous les étudiants
def afficher_tous():
    if etudiants:
        print(tabulate(etudiants, headers="keys"))
    else:
        print("Aucun étudiant enregistré.")

# Fonction pour trier et afficher les étudiants
def trier_et_afficher():
    if etudiants:
        etudiants_triees = sorted(etudiants, key=lambda x: x['moyenne'], reverse=True)
        print(tabulate(etudiants_triees, headers="keys"))
    else:
        print("Aucun étudiant enregistré.")

# Fonction pour rechercher un étudiant selon un critère
def rechercher_etudiant():
    critere = input("Rechercher par (téléphone, nom, prénom, classe) : ").lower()
    valeur = input(f"Entrez la valeur pour {critere} : ").lower()
    resultats = [e for e in etudiants if str(e.get(critere, '')).lower() == valeur]

    if resultats:
        print(tabulate(resultats, headers="keys"))
    else:
        print(f"Aucun étudiant trouvé avec {critere} = {valeur}")




# Fonction pour modifier les notes d'un étudiant
def modifier_notes():
    telephone = input("Entrez le téléphone de l'étudiant : ")
    etudiant = next((e for e in etudiants if e['telephone'] == telephone), None)
    
    if etudiant:
        etudiant['note_devoir'] = obtenir_note("Nouvelle note de devoir : ")
        etudiant['note_projet'] = obtenir_note("Nouvelle note de projet : ")
        etudiant['note_examen'] = obtenir_note("Nouvelle note d'examen : ")
        etudiant['moyenne'] = round((etudiant['note_devoir'] + etudiant['note_projet'] + etudiant['note_examen']) / 3, 2)
        print("Notes mises à jour.")
    else:
        print("Étudiant non trouvé.")




# Fonction principale pour afficher le menu et gérer les actions
def afficher_menu():
    options = {
        '1': afficher_tous,
        '2': trier_et_afficher,
        '3': rechercher_etudiant,
        '4': modifier_notes,
        '5': lambda: print("Au revoir!") or exit()
        
    }
    
    while True:
        print("\nMenu:")
        print("1. Afficher tout")
        print("2. Trier et afficher (par moyenne décroissante)")
        print("3. Rechercher selon un critère")
        print("4. Modifier les notes d'un étudiant")
        print("5. Sortir")
        
        choix = input("Choisissez une option : ")
        action = options.get(choix)
        if action:
            action()
        else:
            print("Option invalide, veuillez réessayer.")



# Exécution du programme
if __name__ == "__main__":
    while True:
        ajouter_etudiant()
        if input("Voulez-vous ajouter un autre étudiant ? (oui/non) : ").lower() != 'oui':
            break

    afficher_menu()
