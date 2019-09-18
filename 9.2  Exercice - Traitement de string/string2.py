# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

print(texte.count("exemple"))
texte = texte.replace("exemple", "représente")

print(texte)

print(texte[::-1]) # Pour inversre le sens de lecture