def add_tarefas():
    tarefa = list()
    taf = list()
    while True:
       taf.append(str(input('qual tarefa deseja adicionar? (digite 000 para encerrar) ')))
       if '000' in taf:
           taf.pop()
           break
       print(f'Adicionando --> {taf[-1]} <-- na lista de tarefas')
    tarefa = taf[:]
    return tarefa


def remover_tarefas():
    while True:
        c = 0
        for item in tarefas:
            print(f'digite {c} para remover {item}: ')
            c += 1
        d = int(input('qual opção deseja apagar? [000 para encerrar] '))
        if d == 000:
            break
        else:
            del tarefas[d]


tarefas = list()
print('GENCIADOR DE TAREFAS')
print('digite as numerações especificas para acionar as ferramentas.')
t = ('1 - para adicionar tarefas.\n'
      '2 - para remover tarefas.\n'
      '3 - visualizar tarefas.\n'
      '000 - para finalizar progrma: ')
while True:
    r = int(input(f'{t}\n qual funcionalidade escolher: ' ))
    if r == 1:
        tarefas = add_tarefas()
    elif r == 2:
        remover_tarefas()
    elif r == 3:
        print(f'a sua lista de tarefas final ficou {tarefas}: ')
    elif r == 4:
        break
    else:
        print('Codigo não definido, por favor tente novamente: ')
print('FIM')


