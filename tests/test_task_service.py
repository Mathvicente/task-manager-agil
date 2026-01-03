from src.task_service import *

def test_criar_tarefa():
    tarefa = criar_tarefa("Estudar", "Revisar matéria")
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Estudar"
    assert tarefa["status"] == "To Do"

def test_listar_tarefas():
    tarefas = listar_tarefas()
    assert len(tarefas) >= 1

def test_atualizar_tarefa():
    tarefa = atualizar_tarefa(1, status="In Progress")
    assert tarefa["status"] == "In Progress"

def test_remover_tarefa():
    remover_tarefa(1)
    tarefas = listar_tarefas()
    assert len(tarefas) == 0
