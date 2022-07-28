import funcoes

while True:
    print("""\nO que deseja fazer?
    [1] Cadastrar um novo cartão
    [2] Ver os cartões cadastrados
    [3] Excluir um cartão
    [4] Verificar Preço ideal para um produto""")

    while True:
        escolha = input('Escolha: ')
        try:
            escolha = int(escolha)
            break
        except ValueError as error:
            print('Digite um numero valido!')
        except Exception as error:
            print(f'Erro nao esperado. {error}')

    if escolha == 1:
        funcoes.add_cartao()

    if escolha == 2:
        try:
            print(funcoes.ver_cartoes())


        except Exception:
            print('Nao há cartoes registrados.')

    if escolha == 3:
        funcoes.remover_cartao()

    if escolha == 4:
        funcoes.venda()

    else:
        print('Escolha uma opcao valida!')
    close = 0
    while True:
        fechar_programa = input('Caso queira parar digite [S]im ou [N]ão : ').upper()
        if fechar_programa == 'S':
            close = 1
            break
        elif fechar_programa == 'N':
            break
        else:
            print('Opcao invalida')
    if close == 1:
        break