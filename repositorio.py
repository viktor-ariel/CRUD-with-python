personagens = {
    1:{
        "nome": "carlos",
        "raca": "bruxo",
        "casa": "leao",
        "altura": 1.70,
        "nascimento" : "31/10/2000",
        "imagem" : "..."
    },
    2: {
        "nome": "Sophia",
        "raca": "elfo",
        "casa": "grifo",
        "altura": 1.65,
        "nascimento": "15/04/1995",
        "imagem": "..."
    },
    3: {
        "nome": "Liam",
        "raca": "bruxo",
        "casa": "serpente",
        "altura": 1.75,
        "nascimento": "22/07/1998",
        "imagem": "..."
    },
    4: {
        "nome": "Aria",
        "raca": "humano",
        "casa": "coruja",
        "altura": 1.68,
        "nascimento": "03/12/2002",
        "imagem": "..."
    },
    5: {
        "nome": "Lucas",
        "raca": "elfo",
        "casa": "leão",
        "altura": 1.80,
        "nascimento": "10/09/1997",
        "imagem": "..."
    },
    6: {
        "nome": "Mia",
        "raca": "bruxo",
        "casa": "grifo",
        "altura": 1.63,
        "nascimento": "28/06/2001",
        "imagem": "..."
    },
    7: {
        "nome": "Ethan",
        "raca": "humano",
        "casa": "serpente",
        "altura": 1.70,
        "nascimento": "09/03/1996",
        "imagem": "..."
    },
    8: {
        "nome": "Olivia",
        "raca": "elfo",
        "casa": "coruja",
        "altura": 1.72,
        "nascimento": "14/01/1999",
        "imagem": "..."
    }
}

def gerar_id():
    id = len(personagens) + 1
    return id 

def createPersonagem(nome, raca, casa, altura, nascimento, imagem):
    personagens[gerar_id()] = {"nome" : nome, "raca": raca, "casa": casa, "altura": altura, "nascimento": nascimento, "imagem": imagem}


def returnPersonagens():
   return personagens

def returnPersonagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return { }

def updatePersonagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem

def removePersonagem(id:int):
    del personagens[id]

