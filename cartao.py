import json


class Cartao:
    def __init__(self):
        self._cartao = {}
        try:
            abrir = open('cartoes.json','x')
        except FileExistsError:
            pass
        except Exception:
            pass
        try:
            self.__converter_dados()
        except:
            pass

    @property
    def cartao(self):
        self.__converter_dados()
        cartoes = ''
        for x in self._cartao:
            cartoes += f'{x}, '
        return f'Os Cartoes Disponivels são: {cartoes[:-2]}'

    def add_cartao(self, cartao, porcentagem):
        novo_cartao = {cartao.title(): porcentagem}
        self._cartao.update(novo_cartao)
        self.salvar_json()

    def salvar_json(self):
        with open('cartoes.json', 'w') as arquivo:
            json.dump(self._cartao, arquivo, indent=4)

    def __converter_dados(self):
        with open('cartoes.json', 'r') as arquivo:
            self._cartao = json.load(arquivo)

    def excluir_cartao(self, nome):
        self.__converter_dados()
        try:
            self._cartao.pop(nome.title())
            self.salvar_json()
            return True
        except KeyError as e:
            print(f'{nome} é uma Key invalida')
        except Exception as e:
            print(f'Erro: {e}')
            pass

    def valor_venda(self, valor):
        media = 0
        for x,y in self._cartao.items():
            valor_novo = valor +(valor*y/100)
            media+= valor_novo
            print(f'Para o cartão: {x}  O preço ideal é de: {valor_novo:.2f}')
        try:
            media = media / len(self._cartao)
            print('\nDe Acordo com a porcentagem cobrada para cada cartão\n')
            print(f'\nO Preço médio ideal para o produto é de {media:.2f}')
        except ZeroDivisionError as error:
            print('sua lista de cartoes está vazia!')
            print('Use a opção cadastrar um novo cartão!')
            print('Selecione [N]ão e tente novamente.')
            pass



