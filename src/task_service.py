tasks = []
counter = 1

def criar_tarefa(titulo, descricao):
    global counter
    tarefa = {
        "id": counter,
        "titulo": titulo,
        "descricao": descricao,
        "status": "To Do"
    }
    tasks.append(tarefa)
    counter += 1
    return tarefa

def listar_tarefas():
    return tasks

def atualizar_tarefa(id, titulo=None, descricao=None, status=None):
    for tarefa in tasks:
        if tarefa["id"] == id:
            if titulo: tarefa["titulo"] = titulo
            if descricao: tarefa["descricao"] = descricao
            if status: tarefa["status"] = status
            return tarefa
    return None

def remover_tarefa(id):
    global tasks
    tasks = [t for t in tasks if t["id"] != id]
