#SIMULADOR DE USUÁRIO E SENHA realizado pelo aluno Jackson.

nome = input("Informe seu nome: " )
senha = input("Informe sua senha: ")

while(senha == nome):
    print("A senha não pode ser igual ao nome")
    nome = input("Informe seu nome: ")
    senha = input("Informe sua senha: ")
if(nome != senha):
    print("Login efetuado com sucesso!")
