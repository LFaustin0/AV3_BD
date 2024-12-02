from cadastros import (
    listar_consultas,
    medicos,
    buscar,
    bio_med,
    excluir_consultas,
    agendar_consultas,
    cadastrar,
    listar_pacientes,
    adicionar_medico,
)
from adm import funcao_admin

usuario_logado = funcao_admin()    
if usuario_logado == True:

    while True:
        print('------------------------\n------------------------\n O que você deseja fazer? ')
        print('1. Cadastrar um(a) paciente')
        print('2. Listar pacientes')
        print('3. Buscar paciente')
        print('4. Agendar consulta')
        print('5. Listar consultas agendadas')
        print('6.Excluir consulta')
        print('7. Adicionar novo médico')
        print('8. Listar médicos disponíveis')
        print('9. Exibir biografia de um médico')
        print('10. Encerrar')
        print('------------------------\n------------------------')

        opcao = int(input('Opção? '))        

        if opcao == 1:
            cadastrar()    
        elif opcao == 2:
            listar_pacientes()  
        elif opcao == 3:
            buscar()  
        elif opcao == 4:
            agendar_consultas()
        elif opcao == 5:
            listar_consultas()  
        elif opcao == 6:
            excluir_consultas()   
        elif opcao == 7:
            adicionar_medico()  
        elif opcao == 8:
            medicos()  
        elif opcao == 9:
            nome_medico = input("Digite o nome do médico para exibir a biografia: ")
            bio_med(nome_medico)  
        elif opcao == 10:
            print('Saindo...')
            break  
        else:
            print('Opção inválida!')
