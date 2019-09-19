# Le generateur ne garderai pas en mémoire les résultats lorsque l'on itère dessus. Il lit calclue et oublie.

# Une fonction qui retoune un générateur. Ce code ne sera lue que lorsque l'on va itérer sur le générateur.
def creerGenerateur():
    print("Générateur créé")
    myList = range(3)
    for item in myList:
        yield item*item #permet de retourner un générateur. C'est ce qui fait que le compilateur comprends que c'est un generateur.

# A la différence, cette fonction va être lue a chaque fois que l'on l'appel.
def functTest():
    print("Code fonction test lue")
    return 2

generateur  = creerGenerateur()
generateur2 = creerGenerateur()
generateur3 = creerGenerateur()
generateur4 = creerGenerateur()

for i in generateur:
    print(i)
# après avoir été utilisé le generateur est vidé. Le code ci-dessous n'affichera rien
for i in generateur:
    print(i)

test = functTest()