# projeto iniciando em pytho par ou impar
# 0.2.4.6.8.10...  (pares)
# 1.3.5.7.9.... (impares)

while True:
     try:
         valor = int(input('Digite um valor '))
         if valor %2 == 0:
            print('Número par')
         else:
            print('Número ímpar')
     except:
        print('Digite apenas números')

            
                