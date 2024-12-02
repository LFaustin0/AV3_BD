import bcrypt
import msvcrt

def senha1(prompt="Senha: "):
    senha = ""
    print(prompt, end="", flush=True)

    while True:
        char = msvcrt.getch()
        if char in {b"\r", b"\n"}: 
            break
        elif char == b"\x08":  
            if len(senha) > 0:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        else:
            senha += char.decode("utf-8")
            print("*", end="", flush=True)
    print()
    return senha

def funcao_admin():
    usuarios = {
        'email': 'lucasfaustino@gmail.com',
        'senha': bcrypt.hashpw('12345'.encode(), bcrypt.gensalt()) 
    }

    print("Digite o email e senha do administrador para acessar o sistema.")
    email = input("Email: ")
    senha = senha1("Senha: ")  


    if email == usuarios['email'] and bcrypt.checkpw(senha.encode(), usuarios['senha']):
        print("Acesso concedido.")
        return True
    else:
        print("Acesso negado.")
        return False
