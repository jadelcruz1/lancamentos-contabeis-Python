# esse codigo foi criado para gerar lancamentos contabeis. em outro momento iremos criar um app para importar planilha de excel

Debito = int(input('Digite a conta debito:')) # aqui será inserido conta cotábil débito (ATIVO OU DESPESA)
Credito = int(input('Digite a conta credito:')) # aqui será inserido conta cotábil crédito (passivo OU receita)
Valor = float(input('Digite o valor:'))# o valor

if (Debito != Credito):
    print( 'Debito {}' .format(Debito))
    print('Credito {}' .format(Credito))
    print('R$ {}' .format(Valor))
else:
    print('conta debito não pode ser igual a debito')

