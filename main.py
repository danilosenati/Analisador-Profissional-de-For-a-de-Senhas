código da etapa 1:

# Projeto: Analisador Profissional de Força de Senhas

# PONTUAÇÃO MÁXIMA: 9 pontos

pontuacao = 0

senha_usuario = input("Digite sua senha: ")

# analisando criterios de segurança:

if len(senha_usuario) >= 12:
    pontuacao = 4

if len(senha_usuario) >= 8:
    pontuacao = 2
else:
    pontuacao = 0

# caracteres maiusculos ( verifica se existe ao menos um:)
if any(c.isupper() for c in senha_usuario):
    pontuacao += 1

# caracteres minusculos verifica se existe ao menos um:
if any(c.islower() for c in senha_usuario):
    pontuacao += 1

#caracteres númericos:
if any(c.isdigit() for c in senha_usuario):
    pontuacao += 1

# caracteres especiais ( Se não for apenas letras e números:
if not senha_usuario.isalnum():
    pontuacao += 2

# classificação:

print(f"{pontuacao} pontos")

if pontuacao <= 3:
     print("Fraca")
elif pontuacao >= 4 and pontuacao <= 6:
    print("Média")
elif pontuacao >= 7 and pontuacao <= 8:
    print("Forte")
else:
    print("Muito Forte")
