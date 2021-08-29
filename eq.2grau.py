a = float(input('Digite o termo que antecede x²'))
b = float(input('Digite o termo que antecede x'))
c = float(input('Digite o termo idependente'))
d = b**2-4*a*c
x1 = (-b+d**(1/2))/2*a
X2 = (-b-d**(1/2))/2*a
if d < 0:
    print('Essa equação não tem solução no conjunto dos numeros reais')
else:
    print('Essa equção tem solução {} e {}'.format(x1,X2))

