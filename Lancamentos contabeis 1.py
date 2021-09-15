# esse codigo foi criado para gerar lancamentos contabeis. em outro momento iremos criar um app para importar planilha de excel

Debito = int(input('Digite a conta debito:')) # aqui será inserido conta cotábil débito (ATIVO OU DESPESA)
Credito = int(input('Digite a conta credito:')) # aqui será inserido conta cotábil crédito (passivo OU receita)
Valor = float(input('Digite o valor:'))# o valor será o expresso em documento fiscal ou contabil

if (Debito != Credito): # essa condição foi para demonstrar o lançamento contábil. Daqui poderá extratir os livros razão e Diario.
    print( 'Debito {}' .format(Debito))
    print('Credito {}' .format(Credito))
    print('R$ {}' .format(Valor))
else:  # aqui essa condição foi para que as contas debito e credito não sejam iguai, pois o balancete irá ter ATIVO diferente de Passivo.
    print('conta debito não pode ser igual a debito')

