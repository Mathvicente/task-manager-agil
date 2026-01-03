tasks = []
_next_id = 1

def reset_tasks():
    global tasks, _next_id
    tasks = []
    _next_id = 1

def criar_tarefa(titulo, descricao, prioridade="Média"):
    global _next_id
    tarefa = {
        "id": _next_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente",
        "prioridade": prioridade
    }
    tasks.append(tarefa)
    _next_id += 1
    return tarefa

def listar_tarefas():
    return tasks

def atualizar_tarefa(id, prioridade=None, status=None):
    for tarefa in tasks:
        if tarefa["id"] == id:
            if prioridade:
                tarefa["prioridade"] = prioridade
            if status:
                tarefa["status"] = status
            return tarefa
    return None
