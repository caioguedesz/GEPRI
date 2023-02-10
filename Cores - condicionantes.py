cor1 = str(input('Digite a primeira cor: '))
cor2 = str(input('Digite a segunda cor: '))

if (cor1 == cor2 ):
 print('A cor resultante dessa mistura é ' + cor1)
elif (cor1 == 'vermelho' and cor2 == 'azul' or cor1 == 'azul' and cor2 == 'vermelho'):
    print('A cor resultante dessa mistura é magenta')
elif  (cor1 =='vermelho' and cor2 == 'verde' or cor1 == 'verde' and cor2 == 'vermelho'):
    print('A cor resultante dessa mistura é amarelo')
elif (cor1 == 'verde' and cor2 == 'azul' or cor1 == 'azul' and cor2 == 'verde'):  
    print('A cor resultante dessa mistura é Ciano')
 
#concluded the other colors for training
