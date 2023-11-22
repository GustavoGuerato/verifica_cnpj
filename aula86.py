import cnpj

cnpj1 = '50.235.200/0001-00'


if cnpj.valida(cnpj1):
    print(f'{cnpj1} é valido')
else:
    print(f'{cnpj1} é invalido')

