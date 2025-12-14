from datetime import datetime as dt

current_id = 0
db_task = []

# Classe
class Task:
    def __init__(self, current_id, description, create_data, status, deadline):
        self.current_id = current_id
        self.description = description
        self.create_data = create_data
        self.status = status
        self.deadline = deadline


# Funções
# Essa função retorna a data atual da transação
def current_date(): 
    """Retorna a data e hora atual."""
    return dt.now()

# Essa função cria uma nova função da lista de tarefas
def create_new_task():
    """Cria uma nova tarefa e adiciona à lista."""

    global current_id
    
    while True:
        current_id += 1

        print(f"\n--- Criando tarefa #{current_id} ---")
        description = input("Digite a descrição da sua tarefa: ")
        create_data = current_date()
        status = input("Digite o status da tarefa: ")
        deadline = input("Digite o prazo final da tarefa: ")
        stop = int(input("Digite 0 para sair e 1 para continuar: "))

        task_new = Task(current_id, description, create_data, status, deadline)
        db_task.append(task_new)

        print("\n✅ Tarefa criada com sucesso!")
        print(f"ID: {task_new.current_id}")
        print(f"Descrição: {task_new.description}")
        print(f"Data de criação: {task_new.create_data}")
        print(f"Status: {task_new.status}")
        print(f"Prazo: {task_new.deadline}")
    
        if stop == 0:
            break
        else:
            continue


# Essa função conculta as tarefas já criadas
def consult_tasks():
    """Consulta e exibe uma tarefa pelo ID."""

    which_task = int(input("Qual o ID da tarefa para consulta: "))
    try:
        for tsk in db_task:
            if tsk.current_id == which_task:
                print("\n✅ Tarefa encontrada!")
                print(f"ID: {tsk.current_id}")
                print(f"Descrição: {tsk.description}")
                print(f"Data de criação: {tsk.create_data}")
                print(f"Status: {tsk.status}")
                print(f"Prazo: {tsk.deadline}")
                return
    except TypeError:
        print("Insira uma das opções acima.")
    
    
    print("Nenhuma tarefa encontrada com esse ID.")

# Essa função marca uma tabela como concluída
def completed_task():
    """Marca uma tarefa como concluída pelo ID."""

    op = (input("Digite o ID da tarefa que deseja marcar como concluída: "))

    for tsk in db_task:
        if tsk.current_id == op:
            tsk.status = "Concluída"
            print("Tarefa marcada como concluída.")
            return

    print("Nenhuma tarefa encontrada com esse ID.")


# Essa função deleta uma tarefa
def delete_task():
    """Remove uma tarefa da lista pelo ID."""

    op = int(input("Digite o ID da tarefa que deseja excluir: "))

    for tsk in db_task:
        if tsk.current_id == op:
            db_task.remove(tsk)
            print("Tarefa excluída com sucesso.")
            return
        
    print("Nenhuma tarefa encontrada com esse ID.")


# Menu para selecionar as funções
# Menu principal
while True:
    print("""
          ==== Menu ====
    1 - Criar nova tarefa
    2 - Consultar tarefa criada
    3 - Marcar como concluída
    4 - Excluir tarefa
    0 - Sair do sistema
    """)

    op = int(input("Insira a opção: "))

    if op == 1:
        create_new_task()
    elif op == 2:   
        consult_tasks()
    elif op == 3:
        completed_task()
    elif op == 4:
        delete_task()
    elif op == 0:
        print("Até mais!")
        break
    else:
        print("Opção inválida!")

current_date()
