import os
import sqlite3
import customtkinter as ctk
import time
from PIL import Image

Base_Dir = os.path.dirname(os.path.abspath(__file__))
Image_Path = os.path.join(Base_Dir, 'assets', 'images', 'emoji.png')
imagem = ctk.CTkImage(Image.open(Image_Path),size=(300, 300))

conexao = sqlite3.connect("Dados.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Dados_Usuario(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha INTEGER NOT NULL )
               """)
conexao.commit()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("340x520")
app.title("Sistema de Contas")
app.resizable(False, False)

MenuPrincipal = ctk.CTkFrame(app, width=600, height=535, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
MenuPrincipal.pack(padx=5 ,pady=15)

def MenuLogin():
        MenuPrincipal.forget()
        MenuDeLogin = ctk.CTkFrame(app, width=600, height=535, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
        MenuDeLogin.pack(padx=5 ,pady=15)
        EntradaUsuario = ctk.CTkEntry(MenuDeLogin, width=200,height=50, placeholder_text="Nome de Usuario...", bg_color="#222222")
        EntradaUsuario.place(x=65, y=75)
        EntradaSenha = ctk.CTkEntry(MenuDeLogin, width=200,height=50, placeholder_text="Digite sua senha...", bg_color="#222222", show="*")
        EntradaSenha.place(x=65, y=150)
        TituloLogin = ctk.CTkLabel(MenuDeLogin, text="Login:", font=("arial", 25, "bold"), bg_color="transparent",fg_color="#222222")
        TituloLogin.place(x=10, y=25)
        def Login():
                Usuario = EntradaUsuario.get()
                Senha = EntradaSenha.get()
                EntradaUsuario.delete(0,"end")
                EntradaSenha.delete(0,"end")
                cursor.execute("SELECT * FROM Dados_Usuario WHERE nome = ? AND senha = ? ", (Usuario, Senha))
                resultado = cursor.fetchone()
                if resultado:
                        MenuDeLogin.forget()
                        MenuRegistrado = ctk.CTkFrame(app, width=600, height=535, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
                        MenuRegistrado.pack(padx=5 ,pady=15)
                        MensagemLogin = ctk.CTkLabel(MenuRegistrado, text=f"Bem vindo {Usuario}!", font=("arial", 25, "bold"), bg_color="transparent",fg_color="#222222")
                        MensagemLogin.place(x=10, y=25)
                        ImagemBemVindo = ctk.CTkLabel(MenuRegistrado,image=imagem,text="")
                        ImagemBemVindo.place(x=15, y=75)
                else:
                        MensagemErro = ctk.CTkLabel(MenuDeLogin, text="Conta não encontrada!", font=("arial", 25, "bold"), bg_color="transparent",fg_color="#222222")
                        MensagemErro.place(x=10, y=250)
        BotaoFazerLogin = ctk.CTkButton(MenuDeLogin, width=150, height=75, text="Fazer Login",command=Login, bg_color="#222222", fg_color="#0058CC", border_color="black", border_width=4)
        BotaoFazerLogin.place(x=75, y=300)



def MenuCadastro():
        MenuPrincipal.forget()
        MenuDeCadastro = ctk.CTkFrame(app, width=600, height=535, bg_color="#222222", fg_color="transparent", border_color="black", border_width=4)
        MenuDeCadastro.pack(padx=5 ,pady=15)
        EntradaUsuario = ctk.CTkEntry(MenuDeCadastro, width=200,height=50, placeholder_text="Nome de Usuario...", bg_color="#222222")
        EntradaUsuario.place(x=65, y=75)
        EntradaSenha = ctk.CTkEntry(MenuDeCadastro, width=200,height=50, placeholder_text="Digite sua senha...", bg_color="#222222", show="*")
        EntradaSenha.place(x=65, y=150)
        TituloCadastro = ctk.CTkLabel(MenuDeCadastro, text="Cadastro:", font=("arial", 25, "bold"), bg_color="transparent",fg_color="#222222")
        TituloCadastro.place(x=10, y=25)
        def Cadastro():
                Usuario = EntradaUsuario.get()
                Senha = EntradaSenha.get()
                EntradaUsuario.delete(0,"end")
                EntradaSenha.delete(0,"end")
                cursor.execute("INSERT INTO Dados_Usuario (nome, senha) VALUES (?, ?)", (Usuario, Senha))
                conexao.commit()
                time.sleep(1)
                app.destroy()
        BotaoFazerCadastro = ctk.CTkButton(MenuDeCadastro, width=150, height=75, text="Fazer Cadastro",command=Cadastro, bg_color="#222222", fg_color="#0058CC", border_color="black", border_width=4)
        BotaoFazerCadastro.place(x=75, y=300)      

def Menu():
        TituloMenu = ctk.CTkLabel(MenuPrincipal, text="SELECIONE SUA OPÇÃO:", font=("arial", 25, "bold"), bg_color="transparent",fg_color="#222222")
        TituloMenu.place(x=10, y=50)
        BotaoLogin = ctk.CTkButton(MenuPrincipal, width=150, height=75, text="Login",command=MenuLogin, bg_color="#222222", fg_color="#0058CC", border_color="black", border_width=4)
        BotaoLogin.place(x=100, y=200)
        BotaoCadrastro = ctk.CTkButton(MenuPrincipal, width=150, height=75, text="Cadastro",command=MenuCadastro, bg_color="#222222", fg_color="#0058CC", border_color="black", border_width=4)
        BotaoCadrastro.place(x=100, y=300)


Menu()
app.mainloop()