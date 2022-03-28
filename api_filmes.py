import requests
import json


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=b25bcf69&t='+titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexao')
        return None


def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Premios:', filme['Awards'])
    print('Poster:', filme['Poster'])
    print('')


sair = False
while not sair:
    op = input('Escreva o nome de um filme ou Finalizar para encerrar: ')

    if op == 'Finalizar':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
           print('Filme não encontrado')
        else:
            printar_detalhes(filme)