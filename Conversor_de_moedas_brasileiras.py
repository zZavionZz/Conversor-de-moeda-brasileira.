
def conversor_de_reais(reais):
    return reais / 3.45

def tratamento_de_texto(texto: str):
    texto = texto.replace(',', '.').lower()
    
    caracteres_indesejaveis = [
        'r$','us$',
        'r', 'us',
        '$', 'reais',
        'dolar', 'dollar'
        ]
    
    for i in caracteres_indesejaveis:
        texto = texto.replace(i, '')
        
    return texto
    
def conversor_float(texto: str) -> float:
    while True:
        try:
            texto = float(texto)
            break
        except ValueError:
            print('erro')
            
            texto = input('digite novamente: ')
            texto = tratamento_de_texto(texto)
            
    return texto

def pontuação_br(numero: float):
    f_string = f'{numero:_.2f}'
    f_string = f_string.replace('.', ',').replace('_', '.')
    
    return f_string
    
while True:
    reais = input('quantos reais você tem na carteira? (0 para sair!) ')
    if reais == '0':
        break
    
    reais_formatado = tratamento_de_texto(reais)
    reais_float = conversor_float(reais_formatado)
    reais_br = pontuação_br(reais_float)
    
    soma = conversor_de_reais(reais_float)
    print(f'a quantia de dinheiro que você tem é de R${reais_br} e você tera {soma:.2f}dolares.')
