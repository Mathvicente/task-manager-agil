from src.task_service import *

def test_criar_tarefa_com_prioridade():
    tarefa = criar_tarefa("Estudar", "Revisar matéria", prioridade="Alta")
    assert tarefa["prioridade"] == "Alta"

def test_atualizar_prioridade():
    atualizar_tarefa(1, prioridade="Baixa")
    tarefas = listar_tarefas()
    assert tarefas[0]["prioridade"] == "Baixa"
