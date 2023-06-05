tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def exibir_tarefas():
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        print("Lista de tarefas:")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")

def marcar_tarefa_concluida():
    exibir_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa concluída: "))
    if numero_tarefa <= len(tarefas):
        tarefa_concluida = tarefas.pop(numero_tarefa - 1)
        print(f"A tarefa '{tarefa_concluida}' foi marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

while True:
    print("\n----- Lista de Tarefas -----")
    print("1. Adicionar nova tarefa")
    print("2. Exibir tarefas")
    print("3. Marcar tarefa como concluída")
    print("0. Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        exibir_tarefas()
    elif opcao == "3":
        marcar_tarefa_concluida()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")
