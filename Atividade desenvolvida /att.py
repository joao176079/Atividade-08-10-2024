import os
from dataclasses import dataclass

# João victor agapio modesto mendes

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def situacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade de primeiro grau"
    elif 35 <= imc < 40:
        return "Obesidade grau de 2 grau"
    else:
        return "Obesidade grau de 3 grau"

def cadastrar_usuarios():
    usuarios = []
    while True:
        logoSenai()
        nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")

        if nome.lower() == 'sair':
            break
        
        sobrenome = input("Digite o sobrenome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        altura = float(input("Digite a altura do usuário em metros: "))
        peso = float(input("Digite o peso do usuário em quilogramas: "))

        usuario = {
            'nome': nome,
            'sobrenome': sobrenome,
            'idade': idade,
            'altura': altura,
            'peso': peso
        }
        usuarios.append(usuario)
    
    return usuarios

def exibir_usuarios(usuarios):
    logoSenai()
    print("\nDados dos usuários:")
    i = 1
    for usuario in usuarios:
        imc = calcular_imc(usuario['peso'], usuario['altura'])
        situacao = situacao_imc(imc)
        print(f"Usuário {i}:")
        print(f"Nome completo: {usuario['nome']} {usuario['sobrenome']}")
        print(f"Idade: {usuario['idade']} anos")
        print(f"Altura: {usuario['altura']} metros")
        print(f"Peso: {usuario['peso']} quilogramas")
        print(f"IMC: {imc:.2f}")
        print(f"Situação: {situacao}\n")
        i += 1

usuarios = cadastrar_usuarios()
exibir_usuarios(usuarios)