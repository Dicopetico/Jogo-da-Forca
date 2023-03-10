import random
from os import system, name
listaPalavras = {'Frutas': ['Banana', 'Abacaxi', 'Quiui', 'Melancia', 'Tomate', 'Goiaba'],
                 'Filmes': ['Zootopia', 'Gato de botas', 'Interestelar', 'Avatar'],
                 'Séries': ['Stranger things', 'Lost', 'The walking dead'],
                 'Animais': ['Coelho', 'Rapoza', 'Tartaruga', 'Galinha', 'Avestruz', 'Zebra',
                             'Lobo', 'Cachorro', 'Gato', 'Rato']}

categorias = list(listaPalavras.keys())

categoriaEscolhida = random.choice(categorias)

palavraEscolhida = random.choice(list(listaPalavras[categoriaEscolhida]))
palavras = palavraEscolhida.split(' ')
quantidadePalavras = len(palavras)
quantidadeEspaco = quantidadePalavras - 1
quantidadeLetra = len(palavraEscolhida) - quantidadeEspaco

listaLetras = []
tentativa = 5


def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')


def PalavraTracos():
    palavraHifen = ['_']*len(palavras[0])
    if quantidadePalavras > 1:
        for i in range(1, quantidadePalavras):
            tamanhoPalavra_n = len(palavras[i])
            palavraHifen += [' '] + ['_'] * tamanhoPalavra_n
    return palavraHifen


def InputUsuario(listaL):
    while True:
        letra = input("Digite uma letra: ").lower()
        try:
            float(letra)
        except ValueError:
            if len(letra) > 1:
                print("Você não digitou somente uma letra!")
                continue
            elif letra in listaL:
                print('Você já digitou essa letra!')
                continue
            else:
                break
        else:
            print('Você digitou um número!')
            continue
    return letra


def VerificarSeEncaixa(letra, tentativa, palavraH, qL):
    contador = 0
    plvrlow = palavraEscolhida.lower()
    if letra in plvrlow:
        for i in plvrlow:
            if i == ' ':
                contador += 1
                continue
            if i == letra:
                palavraH[contador] = i
                qL -= 1
                if contador == 0:
                    palavraH[0] = palavraH[0].upper()
            contador += 1
    else:
        if tentativa == 0:
            pass
        tentativa -= 1
    return tentativa, palavraH, qL


def EnforcarJorge():
    if tentativa == 5:
        print(forca_1)
    elif tentativa == 4:
        print(forca_2)
    elif tentativa == 3:
        print(forca_3)
    elif tentativa == 2:
        print(forca_4)
    elif tentativa == 1:
        print(forca_5)
    elif tentativa == 0:
        print(forca_6)
    elif tentativa == -1:
        print(forca_7)


string1, string2, string3, string4 = 'Bem-vindo', 'Esse é o Jogo da Forca!', 'Parabéns! Você ganhou!',\
    'A categoria do jogo é'

forca_1 = '   __________\n' \
        '   |        |       Um certo dia...\n' \
        '   |        |       Um pequeno rapaz foi condenado\n' \
        '   |                por um crime que não cometeu\n' \
        '   |                o nome desse rapaz é Jorge\n' \
        '   |\n' \
        '   |______          Por favor, ajude Jorge!'
forca_2 = '   __________\n' \
        '   |        |\n' \
        '   |        |        Concentração, eu confio em você!\n' \
        '   |       (°°)          \n' \
        '   |\n' \
        '   |\n' \
        '   |______'
forca_3 = '   __________\n' \
        '   |        |\n' \
        '   |        |\n' \
        '   |      (°.°)        Pobre Jorge!\n' \
        '   |        I\n' \
        '   |    \n' \
        '   |______'
forca_4 = '   __________\n' \
        '   |        |\n' \
        '   |        |\n' \
        '   |      (°-°)\n' \
        '   |        I\\       Não deixe o Jorge morrer!\n' \
        '   |\n' \
        '   |______'
forca_5 = '   __________\n' \
        '   |        |\n' \
        '   |        |\n' \
        '   |      (°_°)\n' \
        '   |       /I\\\n' \
        '   |                 \"Eu consigo ver a luz...\"\n' \
        '   |______'
forca_6 = '   __________\n' \
        '   |        |\n' \
        '   |        |\n' \
        '   |      (0o0)\n' \
        '   |       /I\\\n' \
        '   |         \\     \"Será esse o meu fim?\"\n' \
        '   |______'
forca_7 = '   __________\n' \
        '   |        |\n' \
        '   |        |\n' \
        '   |      (*0*)\n' \
        '   |                     Jorge está morto TT\n' \
        '   |       /I\\\n' \
        '   |______ / \\'
forcaVitoria = '   __________\n' \
        '   |        |       ________________________________\n' \
        '   |        |      / Parabens amigo! Você me salvou!\\\n' \
        '   |        |      | Agora eu posso ir jogar LOL!   |\n' \
        '   |              /\\________________________________/ \n' \
        '   |          (°¬°)    \n' \
        '   |           /I\\   \n' \
        '   |______     / \\'


palavraHifen = PalavraTracos()
palvhifen = ''.join(palavraHifen)

while True:
    limpa_tela()
    print(f'{string1:=^50}')
    print(f'{string2:-^50}')
    print(f'{string4:=^50}\n')
    print(f'{categoriaEscolhida:-^50}')
    print(f'\nLetras utilizadas: {listaLetras}\n')
    if palvhifen == palavraEscolhida:
        print(forcaVitoria)
        print('\nParabens! Você ganhou!')
        print('O Jorge pode ser \"feliz\" de novo!')
        break
    EnforcarJorge()
    print(f'{palvhifen:^50}')
    print(f'\nQuantidade de letras restantes: {quantidadeLetra}')
    if tentativa == 5:
        print(f'\nVocê tem um total de {tentativa+1} tentativas')
    elif tentativa >= 1:
        print(f'\nVocê tem mais {tentativa+1} tentativas')
    elif tentativa == 0:
        print(f'\nVocê tem apenas mais {tentativa+1} tentativa')
    elif tentativa == -1:
        print(f'A palavra era {palavraEscolhida}')
        print('Você não tem mais nenhuma tentativa! TT')
        continuar = False
        break
    letra = InputUsuario(listaLetras)
    listaLetras += letra
    tentativa, palavraHifen, quantidadeLetra = VerificarSeEncaixa(letra, tentativa, palavraHifen, quantidadeLetra)
    palvhifen = ''.join(palavraHifen)
