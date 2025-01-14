import os
import time

def supprimer_fichiers_obsoletes(dossier, delai_secondes):
    maintenant = time.time()
    
    for nom_fichier in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, nom_fichier)
        if os.path.isfile(chemin_fichier):
            derniere_modification = os.path.getmtime(chemin_fichier)
            if maintenant - derniere_modification > delai_secondes:
                os.remove(chemin_fichier)
                print(f"Fichier supprimé : {chemin_fichier}")

# Exemple d'utilisation
dossier_a_verifier = "deleteTest/"
supprimer_fichiers_obsoletes(dossier_a_verifier, 60)  # Délai de 5 secondes

while True:
    print("Vérification des fichiers...")
    supprimer_fichiers_obsoletes(dossier_a_verifier, 60)  # Délai de 5 secondes
    time.sleep(60)