from db import criar_conexao

def cadastrar():
    conn=criar_conexao()
    if conn:
        cursor = conn.cursor()
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        cpf = int(input("Digite o  seu cpf:"))
        while True:
            sexo = input("Digite seu sexo 'M' ou 'F':").upper()
            if sexo in ('M','F'):
                break  
        
            print("Sexo invalido!Por favor digite entre 'M' ou 'F'")
        cursor.execute("INSERT INTO pacientes (nome, idade,cpf,sexo) VALUES (%s, %s,%s,%s)", (nome,idade,cpf,sexo))
        conn.commit()
        print("Paciente cadastrado com sucesso!")
        cursor.close()
        conn.close()


def listar_pacientes():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()
        for pacientes in pacientes:
            print(f"ID: {pacientes[0]}, Nome: {pacientes[1]}, Idade: {pacientes[2]},Cpf:{pacientes[3]},Sexo:{pacientes[4]}")
        cursor.close()
        conn.close()

def buscar():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        nome = input("Digite o nome do paciente: ")
        cursor.execute("SELECT * FROM pacientes WHERE nome ILIKE %s", (f"%{nome}%",))
        resultados = cursor.fetchall()
        if resultados:
            for paciente in resultados:
                print(f"ID: {paciente[0]}, Nome:{paciente[1]}, Idade:{paciente[2]},Cpf:{paciente[3]},Sexo:{paciente[4]}")
        else:
            print("Paciente não encontrado.")
        cursor.close()
        conn.close()

def excluir_consultas():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        consultas_id =input("Digite o ID da consulta que deseja excluir: ")
        cursor.execute("DELETE FROM consultas WHERE id = %s", (consultas_id))
        conn.commit()
        print("Consulta cancelada com sucesso!")
        cursor.close()
        conn.close()

def agendar_consultas():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        pacientes_id = int(input("Digite o ID do paciente: "))
        medicos_id = int(input("Digite o ID do médico: "))
        data_consulta = input("Digite a data da consulta (YYYY-MM-DD): ")
        cursor.execute(
            "INSERT INTO consultas (pacientes_id, medicos_id, data_consulta) VALUES (%s, %s, %s)",
            (pacientes_id,medicos_id, data_consulta)
        )
        conn.commit()
        print("Consulta agendada com sucesso!")
        cursor.close()
        conn.close()

def listar_consultas():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consultas")
        consultas = cursor.fetchall()
        for consulta in consultas:
            print(f"ID Consulta: {consulta[0]}, paciente_id: {consulta[1]},medico_id: {consulta[2]},data_consulta: {consulta[3]}")
        cursor.close()
        conn.close()

def adicionar_medico():
    conn =  criar_conexao()
    if conn:
        cursor = conn.cursor()
        nome = input("Digite o nome do médico: ")
        especialidade = input("Digite a especialidade do médico: ")
        crm = input("Digite seu crm:")
        cpf = input("Digite seu cpf:")
        while True:
            sexo = input("Digite seu sexo 'M' ou 'F':").upper()
            if sexo in ('M','F'):
                break  
        
            print("Sexo invalido!Por favor digite entre 'M' ou 'F'")
        cursor.execute("INSERT INTO medicos (nome, especialidade,crm,cpf,sexo) VALUES (%s, %s,%s,%s,%s)", (nome, especialidade,crm,cpf,sexo))
        conn.commit()
        print("Médico cadastrado com sucesso!")
        cursor.close()
        conn.close()

def medicos():
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicos")
        medicos = cursor.fetchall()
        for medico in medicos:
            print(f"ID: {medico[0]}, Nome: {medico[1]}, Especialidade: {medico[2]},Crm:{medico[3]},Cpf:{medico[4]}")
        cursor.close()
        conn.close()

def bio_med(nome_medico):
    conn = criar_conexao()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicos WHERE nome ILIKE %s", (f"%{nome_medico}%",))
        medico = cursor.fetchone()
        if medico:
            print(f"Nome: {medico[1]}, Especialidade: {medico[2]}")
        else:
            print("Médico não encontrado.")
        cursor.close()
        conn.close()
