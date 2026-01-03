import src.task_service as service

def setup_function():
    service.tasks.clear()
    service.counter = 1


def test_criar_tarefa_com_prioridade():
    tarefa = service.criar_tarefa("Estudar", "Revisar matéria", prioridade="Alta")
    assert tarefa["prioridade"] == "Alta"
    assert tarefa["id"] == 1


def test_listar_tarefas():
    service.criar_tarefa("Tarefa A", "Desc")
    tarefas = service.listar_tarefas()
    assert len(tarefas) == 1


def test_atualizar_prioridade():
    service.criar_tarefa("Tarefa B", "Desc")
    service.atualizar_tarefa(1, prioridade="Baixa")
    tarefas = service.listar_tarefas()
    assert tarefas[0]["prioridade"] == "Baixa"


def test_remover_tarefa():
    service.criar_tarefa("Tarefa C", "Desc")
    service.remover_tarefa(1)
    tarefas = service.listar_tarefas()
    assert len(tarefas) == 0
