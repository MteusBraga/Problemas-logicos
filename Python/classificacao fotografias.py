'''Henrique gosta de fotografar a natureza, em especial aves. Henrique fez um programa para extrair características de fotos automaticamente, mas ele precisa de um segundo programa para classificar essas fotos de acordo com essas características.

As fotos serão classificadas em 4 categorias:

Para imprimir (Quando a foto ficou tão boa que deve ser feita uma cópia física dela) Boa Marromeno Lixo As características que serão analisadas para determinar a categoria, são:

A relação sinal-ruído de pico da imagem (ou PSNR) que é uma medida objetiva da qualidade da foto, que pode variar de 0 à 100 Enquadramento (pode ser ruim, bom ou excelente) Exposição (subexposto, bem exposto ou superexposto)

Se o PSNR estiver entre 80 e 90, a foto pode ser considerada "marromeno", "boa" ou "para imprimir".

Se o enquadramento estiver bom ou excelente e a exposição estiver bem exposta, ela será considerada "Para imprimir".

Se o enquadramento estiver bom ou excelente mas a foto estiver subexposta ou superexposta, ela será considerada "boa". Em qualquer outro caso, ela será considerada "marromeno".

Se o PSNR estiver entre 50 e 80, a foto será "boa" se estiver com enquadramento excelente e bem exposta. Caso contrário será "marromeno".

Se o PSNR estiver abaixo de 50, a foto só será "marromeno" se estiver com enquadramento excelente e bem exposta. Caso contrário será "lixo".'''

psnr=int(input())
enq=input() #enquadramento
exposicao=input()
if psnr >=80 and psnr <=90: 
    if enq == 'bom' or enq=='excelente' and exposicao =='bem exposta':
        print('para imprimir')
    elif enq=='bom' or enq=='excelente' and exposicao =='subexposta' or exposicao =='superexposta':
        print('boa')
    else:
        print('marromeno')

elif psnr >=50 and psnr < 80:
    if enq=='excelente' and exposicao=='bem exposta':
        print('boa')
    else:
        print('marromeno')
        

elif psnr < 50:
    if enq=='excelente' and exposicao=='bem exposta':
        print('marromeno')
    else:
        print('lixo')
    