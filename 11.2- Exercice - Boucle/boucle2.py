# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

def trier(B):
    A = []
    for item in B:
        index = len(A) # Dans le cas où l'item est le plus grand nombre de la liste provisoire A, on insère à la fin du tableau
        for i in range(len(A)):
            if A[i] > item:
                index = i
                break
        A.insert(index, item)
    return A

print(B)
print(trier(B))
