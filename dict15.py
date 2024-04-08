def ex1(key = "Limão",value = "R$ 1.99"):
    '''
        Escreva um programa que crie um dicionário vazio e adicione elementos a ele, onde as chaves são nomes de frutas e os valores são os preços dessas frutas.
    '''
    d = {}
    d["banana"] = "R$ 4.99"
    d["maça"] = "R$ 2.99"
    d["uva"] = "R$ 10.99"
    d["tomate"] = "R$ 5.99"
    d["maracujá"] = "R$ 20.99"
    d[key] = value
    for i in list(d.keys()):
        print(f"{i}: {d[i]}")


def ex2():
    '''
        Crie um dicionário com informações sobre você, como nome, idade, e cidade onde mora. Imprima essas informações.
    '''

    d = {
        "Nome": "João Paulo",
        "Idade": 19,
        "Cidade": "Cotia"
    }

    for i in list(d.keys()):
        print(f"{i}: {d[i]}")

def ex3(l = []):
    '''
        Dada a lista de frutas ['maçã', 'banana', 'laranja', 'maçã', 'banana', 'maçã'], crie um dicionário que contenha cada fruta como chave e o número de ocorrências como valor.
    '''
    from collections import Counter
    # Para este tipo de exercício eu também poderia usar o método count das listas
    if not isinstance(l,list) or len(l) == 0:
        l = ['maçã', 'banana', 'laranja', 'maçã', 'banana', 'maçã']
    count = Counter(l)
    print(dict(count))

def ex4():
    '''
        Escreva um programa que solicite ao usuário que digite uma frase e conte quantas vezes cada palavra aparece na frase, armazenando o resultado em um dicionário.
    '''
    from collections import Counter 
    # Para este tipo de exercício eu também poderia usar o método count das listas
    phrase = input("Digite uma frase qualquer: ")
    words = phrase.split(" ")
    count = Counter(words)
    print(dict(count))
def ex5():
    '''
        Crie um dicionário contendo nomes de países como chaves e suas capitais como valores. Em seguida, peça ao usuário que digite o nome de um país e imprima a capital correspondente.
    '''
    d = {
        "Estados Unidos": "Washington D.C",
        "Brasil": "Brasília",
        "Canadá": "Ottawa",
        "México": "Cidade do México",
        "Ucrânia": "Kiev"
    }

    text = input("Digite um país: ")

    if text in d.keys():
        print(d[text])
    else:
        print("Este país não foi encontrado na lista de capitais")

def ex6(d: dict):
    '''
        Escreva uma função que receba um dicionário e retorne uma lista contendo apenas as chaves cujos valores são números pares.
    '''

    toReturn = []
    for i in d.keys():
        val = d[i]
        if isinstance(val,int) and val % 2 == 0:
            toReturn.append(i)
    
    print(toReturn)
    return toReturn

def ex7():
    '''
        Crie um programa que leia o nome e a idade de três pessoas e armazene essas informações em um dicionário onde o nome é a chave e a idade é o valor. Em seguida, imprima a média das idades.
    '''
    dList = []

    for _ in range(3):
        d = {}
        name = input("Digite o seu nome: ")
        age = int(input("Digite a sua idade: "))
        d["name"] = name
        d["age"] = age
        dList.append(d)

    av = 0
    for d in dList:
        av+= d["age"]
    print(f"Média = {av/3}")

def ex8(d1,d2):
    '''
        Escreva uma função que receba dois dicionários como entrada e retorne um novo dicionário contendo apenas as chaves que estão presentes em ambos dicionários e seus valores correspondentes concatenados como uma lista.
    '''
    resultDict = {}

    for key in d1.keys():
        if key in d2:
            resultDict[key] = [d1[key],d2[key]]
    print(resultDict)
    
def ex9(d):
    '''
        Dado um dicionário que mapeia nomes de produtos a preços, escreva uma função que receba o dicionário como entrada e retorne o produto mais caro.
    '''
    expensive = ""
    maxValue = 0
    for key in d.keys():
        if d[key] > maxValue:
            maxValue = d[key]
            expensive = key
    print(f"O Produto mais caro é {expensive}")

def ex10(word):
    '''
        Escreva um programa que receba uma frase do usuário e conte quantas vezes cada letra aparece, armazenando o resultado em um dicionário. Ignore espaços e diferenciação entre maiúsculas e minúsculas.
    '''

    from collections import Counter
    w = word.lower().replace(" ", "")
    lettersCount = Counter(list(w))

    for key in lettersCount:
        print(f"Letra {key} aparece {lettersCount[key]} vezes")
  
def ex11(studentList):
    '''
        Escreva uma função que receba uma lista de dicionários contendo informações sobre alunos (nome, nota1, nota2, nota3) e retorne um novo dicionário onde as chaves são os nomes dos alunos e os valores são as médias das notas.
    '''
    result = {}

    for student in studentList:
        av = (student["nota1"] + student["nota2"] + student["nota3"]) / 3
        result[student["nome"]] = av
    
    for key in result.keys():
        print(f"O Estudante {key} tem a média {result[key]}")

def ex12(word):
    '''
        Crie um programa de dicionário de tradução que traduza palavras de inglês para espanhol. O programa deve ter um dicionário com algumas palavras em inglês e suas traduções em espanhol. Em seguida, peça ao usuário para digitar uma palavra em inglês e imprima sua tradução correspondente em espanhol. 
    '''
    trad = {
        "stone": "piedra",
        "orange": "naranja",
        "black": "negro",
        "hat": "sombrero",
        "bomb": "bomba"
    }

    w = word.lower()

    if w in trad:
        print(f"The translation for {w} in spanish is {trad[w]}")
    else:
        print("The word you typed in isn't on the translated dictionary")

    pass
def ex13():
    '''
    Escreva uma função que receba um dicionário contendo o nome de cada pessoa e a quantidade de livros que ela possui. A função deve retornar o nome da pessoa com mais livros.
    '''
    d = {
        "João": 4,
        "Linda": 3,
        "Larry": 20,
        "Thamires": 90
    }

    values = list(d.values())

    maxOwner = list(d.keys())[values.index(max(values))]
    print("O Maior possuidor de livros é: ", maxOwner)

def ex14(word):
    '''
        Crie um programa que simule um dicionário simples de palavras em inglês. O programa deve permitir que o usuário consulte o significado de uma palavra digitada. Você pode usar um dicionário Python com algumas palavras e seus significados como base para o programa.
    '''
    words = {
        "Orange": "A spherical-shaped fruit which it's outside being usually green and it's inside being orange",
        "Computer": "A programmable machine invented by humans that can do repetitive tasks for us",
        "Stone": "Stones can be found in nature and have different colors,shapes, and properties, and when refined are the base of all human crafts",
        "Game": "A Game it's a funny challenge that humans usually do when they have nothing better to do.",
        "Language": "Its the set of sound that humans produce to communicate with each other"
    }

    if word in words:
        print(f"The meaning of {word} is {words[word]}")
    else:
        print(f"{word} is not on the dictionary")

def ex15(products):
    '''
        Escreva uma função que receba um dicionário onde as chaves são nomes de produtos e os valores são seus preços, e retorne um novo dicionário com os produtos ordenados pelo preço em ordem crescente.
    '''

    from collections import OrderedDict


    result = OrderedDict(sorted(products.items(),key=lambda x:x[1]))

    for key,value in result.items():
        print(f"Product: {key}, Price: {value}")

#Utilize help(ex<n>) para obter uma descrição detalhada sobre o problema, inclusive quais parâmetros cada um recebe

# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6({"a": 10, "b": 5})
# ex7()
# ex8({"a": 10, "b": 20}, {"a": 15, "c": 30})
# ex9({"Banana": 10.99, "Limão": 2.99})
# ex10("Banana")
# ex11([
#     {"nome": "Jota", "nota1": 1, "nota2": 2, "nota3": 3},
#     {"nome": "Linda", "nota1": 10, "nota2": 10, "nota3": 10},
#     {"nome": "Marry", "nota1": 5, "nota2": 5, "nota3": 5}
# ])
# ex12("stone")
# ex13()
# ex14("Computer")
# ex15({
#     "banana": 10.99,
#     "laranja": 4.89,
#     "uva": 5.49
# })
