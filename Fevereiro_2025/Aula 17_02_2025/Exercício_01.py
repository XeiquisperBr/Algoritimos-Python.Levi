# Lista de tarefas
tarefas = ["Estudar Python", "Estudar JavaScript"]

#Definindo uma função para adicionar uma tarefa
def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    return tarefas

#Chamando a função para adicionar uma nova tarefa
nova_tarefa = "Lavar a louça"
resultadofinal = adicionar_tarefa(nova_tarefa)

# Imprimindo a lista de tarefas atualizada
print(resultadofinal) #Saída:  ['Estudar Python', 'Estudar JavaScript', 'Lavar a louça']