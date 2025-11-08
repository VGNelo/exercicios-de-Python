def validar_senha(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"
    if not any(c.isupper() for c in senha):
        return False, "A senha deve ter pelo menos uma letra maiúscula"
    if not any(c.isdigit() for c in senha):
        return False, "A senha deve ter pelo menos um número"
    
    return True, "Senha válida"

# Exemplo de uso
senha = input("Digite sua senha: ")
valida, mensagem = validar_senha(senha)
print(mensagem)
