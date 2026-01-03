import src.task_service as service

def test_criar_tarefa_com_prioridade():
    tarefa = service.criar_tarefa("Estudar", "Revisar matéria", prioridade="Alta")
    assert tarefa["prioridade"] == "Alta"

def test_listar_tarefas():
    tarefas = listar_tarefas()
    assert len(tarefas) >= 1

def test_atualizar_prioridade():
    atualizar_tarefa(1, prioridade="Baixa")
    tarefas = listar_tarefas()
    assert tarefas[0]["prioridade"] == "Baixa"
