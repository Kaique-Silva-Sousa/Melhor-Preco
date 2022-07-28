from cartao import Cartao

chamar_funcao = Cartao()


def add_cartao():
    nome_cartao = input('Digite o nome do cartão: ')
    while True:
        porcentagem_cartao = input('Digite a porcentagem cobrada pelo cartão: ')
        try:
            porcentagem_cartao = float(porcentagem_cartao)
            break
        except:
            print('Digite um valor numerico valido')
    chamar_funcao.add_cartao(nome_cartao, porcentagem_cartao)
    print(f'Cartão : {nome_cartao} adicionado com sucesso!')


def remover_cartao():
    while True:
        nome_cartao = input('Digite o nome do cartao que deseja remover: ')
        try:
            if chamar_funcao.excluir_cartao(nome_cartao) == True:
                print(f'Cartão {nome_cartao} excluido com sucesso')
                break
        except KeyError as Error:
            print(Error)
            continue

def ver_cartoes():
    return chamar_funcao.cartao

def venda():
    while True:
        valor = input('Digite o valor que deseja para o produto: ').replace(',','.')
        try:
            valor = float(valor)
            break
        except ValueError:
            print('Digite um valor valido!')
        except Exception as error:
            print(f'Houve um erro inesperado! {error}')
    chamar_funcao.valor_venda(valor)

