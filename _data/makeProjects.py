import json
import sys
class Projeto(object):
    def __init__(self, nome, alunos, aluno_bols, coordenador, coordenador_bols, resumo, ano):
        self.nome = nome
        self.alunos = alunos
        self.aluno_bols = aluno_bols
        self.coordenador = coordenador
        self.coordenador_bols = coordenador_bols
        self.resumo = resumo
        self.ano = ano

def saveOnFile(js):

    js0 = ''

    file = open('fileProjects.json', 'r')
    data = file.read()
    file.close()

    if(data != ''):
        js0 = json.loads(data)

    js.extend(js0)


    aux = json.dumps(js)

    with open('fileProjects.json', 'w') as file:
        file.write(aux)
    return 0

class main(object):
    js = []
    if __name__ == "__main__":
        quit = ''
        while quit != "s":
            nome = input("Nome: ")
            aluno_bols = input("Aluno Bolsita: ")
            alunos = input("Demais alunos participantes: ").split(', ')
            coordenador_bols = input("Coordenador bolsista: ")
            coordenador = input("Coordenador: ").split(', ')
            resumo = input("Resumo: ")
            ano = input("Ano: ")
            p = Projeto(nome, alunos, aluno_bols, coordenador, coordenador_bols, resumo, ano)
            js.append(p.__dict__)

            quit = input('Salvar? s/n: ')

        saveOnFile(js)
