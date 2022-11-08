import requests

BD = "https://bancodedadosteste-7ea86-default-rtdb.firebaseio.com/"

def cadastrar(nome, cpf, email, senha):
    if(buscaChave(email,senha)!=None):
        print("Usuario ja cadastrado!")
        return;
    usuario = '{"Nome": '+f'"{nome}"'+', "CPF": '+f'"{cpf}"'+', "Email": '+f'"{email}"'+', "Senha": '+f'"{senha}"'+'}'
    requisicao = requests.post(BD+'.json', data=usuario)
    if(requisicao.status_code!=200):
        print("Erro ao cadastrar!")
        return;
    print("Usuario cadastrado com sucesso!")

def alterar(nome, cpf, email, senha):
    chave = buscaChave(email,senha)
    if(chave!=None):
        alteracao = '{"Nome":'+f'"{nome}"'+', "CPF":'+f'"{cpf}"'+'}'
        requisicao = requests.patch(BD+chave+".json", data=alteracao)
        print("Usuario alterado com sucesso!")
        return;
    print("Usuario ou senha incorretos!")

def deletar(email,senha):
    chave = buscaChave(email,senha)
    if(chave!=None):
        requisicao = requests.delete(BD+chave+".json")
        print("Usuario deletado com sucesso!")
        return;
    print("Usuario ou senha incorretos!")

def login(email,senha):
    if(buscaChave(email,senha)!=None):
        print("Logado com sucesso!")
        return;
    print("Usuario ou senha incorretos!")

def buscaChave(email,senha):
    requisicao = requests.get(BD+'.json')
    dic = requisicao.json()
    for i,values in enumerate(dic.values()):
        if(values['Email']==email and values['Senha']==senha):
            chave = list(dic.keys())[i]
            return chave
    return None

#cadastrar("Jubileu", "01010101010", "jubileu@email.com", "senha123")
#login("jubileu@email.com", "senha123")
#alterar("Jubilinho", "02020202020", "jubileu@email.com", "senha123")
#deletar("jubileu@email.com", "senha123")
#print(buscaChave("jubileu@email.com", "senha123"))

