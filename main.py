# Projeto: Analisador Profissional de Força de Senhas

# PONTUAÇÃO MÁXIMA: 9 pontos

# analisando criterios de segurança:

def avaliar_comprimento(senha):
    if len(senha) >= 12:
        return 4
        return pontuacao
    elif len(senha) >= 8:
        return 2
    else:
        return 0

def verificar_maiuscula(senha):
    # caracteres maiusculos ( verifica se existe ao menos um:)
    if any(c.isupper() for c in senha):
        return 1
    else:
        return 0

def verificar_minuscula(senha):
    # caracteres minusculos verifica se existe ao menos um:
    if any(c.islower() for c in senha):
        return 1
    else:
        return 0

def verificar_numero(senha):
    #caracteres númericos:
    if any(c.isdigit() for c in senha):
        return 1
    else:
        return 0

def verificar_especial(senha):
    # caracteres especiais ( Se não for apenas letras e números:
    if not senha.isalnum():
        return 2
    else:
        return 0

# classificação:

def classificar_pontuacao(pontos):

    if pontos <= 3:
        return "Fraca"
    elif pontos >= 4 and pontos <= 6:
        return "Média"
    elif pontos >= 7 and pontos <= 8:
        return "Forte"
    else:
        return "Muito Forte"

# executando o código:

senha_usuario = input("Digite sua senha: ")

pontos = (avaliar_comprimento(senha_usuario) + verificar_maiuscula(senha_usuario) + verificar_minuscula(senha_usuario) + verificar_numero(senha_usuario) + verificar_especial(senha_usuario))

nivel = classificar_pontuacao(pontos)

print(f"Pontuação: {pontos}")
print(f"Nivel: {nivel}")
