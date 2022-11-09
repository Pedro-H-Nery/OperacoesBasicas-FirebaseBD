from tkinter import *
import FirebaseBD as bd

class InterfaceGrafica:
    def __init__(self, janela):
        self.modo = "cadastrar"

        janela.title("Tela de interação com Firebase")
        janela.geometry("600x600")
        self.containerTitulo = Frame(janela)
        self.containerTitulo['pady']=10
        self.containerTitulo.pack()
        self.containerOpcoes = Frame(janela)
        self.containerOpcoes['pady']=10
        self.containerOpcoes.pack()
        self.containerCampos1 = Frame(janela)
        self.containerCampos1['pady']=10
        self.containerCampos1.pack()
        self.containerCampos2 = Frame(janela)
        self.containerCampos2['pady']=10
        self.containerCampos2.pack()
        self.containerBotao = Frame(janela)
        self.containerBotao['pady']=10
        self.containerBotao.pack()
        self.containerMensagem = Frame(janela)
        self.containerMensagem['pady']=10
        self.containerMensagem.pack()

        self.titulo = Label(self.containerTitulo, text="Tela de interação com Firebase")
        self.titulo['font']=("Arial", "13", "bold")
        self.titulo.pack()

        self.btncadastro = Button(self.containerOpcoes, text="Cadastrar")
        self.btncadastro['font']=("Arial", "10")
        self.btncadastro['width']=12
        self.btncadastro['command']=self.cadastro
        self.btncadastro['bg']="lightgray"
        self.btncadastro.pack(side=LEFT)

        self.btnbusca = Button(self.containerOpcoes, text="Buscar")
        self.btnbusca['font']=("Arial", "10")
        self.btnbusca['width']=12
        self.btnbusca['command']=self.busca
        self.btnbusca['bg']="lightgray"
        self.btnbusca.pack(side=LEFT)

        self.btnalteracao = Button(self.containerOpcoes, text="Alterar")
        self.btnalteracao['font']=("Arial", "10")
        self.btnalteracao['width']=12
        self.btnalteracao['command']=self.alteracao
        self.btnalteracao['bg']="lightgray"
        self.btnalteracao.pack(side=LEFT)

        self.btndelete = Button(self.containerOpcoes, text="Deletar")
        self.btndelete['font']=("Arial", "10")
        self.btndelete['width']=12
        self.btndelete['command']=self.delete
        self.btndelete['bg']="lightgray"
        self.btndelete.pack(side=LEFT)

        self.nome = Label(self.containerCampos1,text="Nome :", width=10)
        self.nome.pack(side=LEFT)
        self.campoNome = Entry(self.containerCampos1)
        self.campoNome['width']=25
        self.campoNome.pack(side=LEFT)

        self.cpf = Label(self.containerCampos1,text="CPF :", width=10)
        self.cpf.pack(side=LEFT)
        self.campoCpf = Entry(self.containerCampos1)
        self.campoCpf['width']=25
        self.campoCpf.pack(side=LEFT)

        self.email = Label(self.containerCampos2,text="E-mail :", width=10)
        self.email.pack(side=LEFT)
        self.campoEmail = Entry(self.containerCampos2)
        self.campoEmail['width']=25
        self.campoEmail.pack(side=LEFT)

        self.senha = Label(self.containerCampos2,text="Senha :", width=10)
        self.senha.pack(side=LEFT)
        self.campoSenha = Entry(self.containerCampos2)
        self.campoSenha['width']=25
        self.campoSenha.pack(side=LEFT)

        self.botaoEscolha = Button(self.containerBotao, text="Cadastrar Usuário")
        self.botaoEscolha['font']=("Arial", "10")
        self.botaoEscolha['width']=25
        self.botaoEscolha['command']=self.cadastrar
        self.botaoEscolha['bg']="lightgray"
        self.botaoEscolha.pack(side=LEFT)

        self.mensagem = Label(self.containerMensagem, text="", font=("Arial", "10"))
        self.mensagem.pack()

        self.cadastro()

    def cadastro(self):
        self.desativarBotao(self.modo)
        self.modo="cadastrar"
        self.botaoEscolha['text']="Cadastrar Usuário"
        self.botaoEscolha['command']=self.cadastrar
        self.ativarBotao(self.modo)
    
    def busca(self):
        self.desativarBotao(self.modo)
        self.modo="buscar"
        self.botaoEscolha['text']="Buscar Usuário"
        self.botaoEscolha['command']=self.buscar
        self.ativarBotao(self.modo)
    
    def alteracao(self):
        self.desativarBotao(self.modo)
        self.modo="alterar"
        self.botaoEscolha['text']="Alterar Usuário"
        self.botaoEscolha['command']=self.alterar
        self.ativarBotao(self.modo)
    
    def delete(self):
        self.desativarBotao(self.modo)
        self.modo="deletar"
        self.botaoEscolha['text']="Deletar Usuário"
        self.botaoEscolha['command']=self.deletar
        self.ativarBotao(self.modo)

    def ativarBotao(self, botao):
        if(botao == "cadastrar"):
            self.btncadastro['bg']="black"
            self.btncadastro['fg']="white"
            self.btncadastro['state']=DISABLED
        elif(botao == "buscar"):
            self.btnbusca['bg']="black"
            self.btnbusca['fg']="white"
            self.btnbusca['state']=DISABLED
        elif(botao == "alterar"):
            self.btnalteracao['bg']="black"
            self.btnalteracao['fg']="white"
            self.btnalteracao['state']=DISABLED
        elif(botao == "deletar"):
            self.btndelete['bg']="black"
            self.btndelete['fg']="white"
            self.btndelete['state']=DISABLED
    
    def desativarBotao(self, botao):
        if(botao == "cadastrar"):
            self.btncadastro['bg']="lightgray"
            self.btncadastro['fg']="black"
            self.btncadastro['state']=NORMAL
        elif(botao == "buscar"):
            self.btnbusca['bg']="lightgray"
            self.btnbusca['fg']="black"
            self.btnbusca['state']=NORMAL
        elif(botao == "alterar"):
            self.btnalteracao['bg']="lightgray"
            self.btnalteracao['fg']="black"
            self.btnalteracao['state']=NORMAL
        elif(botao == "deletar"):
            self.btndelete['bg']="lightgray"
            self.btndelete['fg']="black"
            self.btndelete['state']=NORMAL
    
    def cadastrar(self):
        resposta = bd.cadastrar(self.campoNome.get(), self.campoCpf.get(), self.campoEmail.get(), self.campoSenha.get())
        self.mensagem["text"] = resposta

    def buscar(self):
        resposta = bd.buscar(self.campoEmail.get(), self.campoSenha.get())
        self.mensagem["text"] = resposta

    def alterar(self):
        resposta = bd.alterar(self.campoNome.get(), self.campoCpf.get(), self.campoEmail.get(), self.campoSenha.get())
        self.mensagem["text"] = resposta

    def deletar(self):
        resposta = bd.deletar(self.campoEmail.get(), self.campoSenha.get())
        self.mensagem["text"] = resposta

janela = Tk()
InterfaceGrafica(janela)
janela.mainloop()