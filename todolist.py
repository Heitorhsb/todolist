import json

def listar(tarefas):
    print()
    if not tarefas:
        print('nenhuma tarefa para listar')
        return
    print("tarefas")
    for tarefa in tarefas:
        print(f'\t{tarefa}')
        
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f)
    print('Tarefas salvas com sucesso!')

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

tarefas = carregar_tarefas()
tarefas_refeitas = []
while True:
    
    print("Comandos: listar, desfazer, refazer")
    comando = input("Digite uma tarefa ou comando: ")
    

    if comando == 'listar':
        listar(tarefas)
    elif comando == 'desfazer':
        if not tarefas:
            print('não há tarefas para desfazer')
        else:
            tarefas_refeitas.append(tarefas.pop())
            salvar_tarefas(tarefas)
    elif comando == 'refazer':
        if not tarefas_refeitas:
            print('não há tarefas para refazer')
        else:
            tarefas.append(tarefas_refeitas.pop())
            salvar_tarefas(tarefas)
    else: 
        tarefas.append(comando)
        salvar_tarefas(tarefas)
