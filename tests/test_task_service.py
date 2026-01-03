import src.task_service as service

def setup_function():
    service.reset_tasks()

def test_criar_tarefa_com_prioridade():
    tarefa = service.criar_tarefa("Estudar", "Revisar matéria", prioridade="Alta")
    assert tarefa["prioridade"] == "Alta"

def test_listar_tarefas():
    service.criar_tarefa("Exemplo", "Teste")
    tarefas = service.listar_tarefas()
    assert len(tarefas) == 1

def test_atualizar_prioridade():
    service.criar_tarefa("A", "B")
    service.atualizar_tarefa(1, prioridade="Baixa")
    tarefas = service.listar_tarefas()
    assert tarefas[0]["prioridade"] == "Baixa"
