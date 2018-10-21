import json
import sys
class Projeto(object):
    def  __init__(self, nome, alunos, aluno_bols, coordenador, coordenador_bols, resumo, ano, edital, grupo, campus, id=''):
        self.nome = nome
        self.alunos = alunos
        self.aluno_bols = aluno_bols
        self.coordenador = coordenador
        self.coordenador_bols = coordenador_bols
        self.resumo = resumo
        self.ano = ano
        self.edital = edital
        self.grupo = grupo
        self.campus = campus

        if(id == ''):
            js0 = ''
            count = 0

            file = open('fileProjects-pesquisa.json', 'r')
            data = file.read()
            file.close()

            if(data != ''):
                js0 = json.loads(data)

            for i in js0:
                count += 1

            self.id = count + 1

        else:
            self.id = id



def saveOnFile(js):

    js0 = ''

    file = open('fileProjects-pesquisa.json', 'r')
    data = file.read()
    file.close()

    if(data != ''):
        js0 = json.loads(data)

    js.extend(js0)


    aux = json.dumps(js)

    with open('fileProjects-pesquisaf.json', 'w') as file:
        file.write(aux)



    print(js0[14]['id'])
    return 0

class main(object):
    js = []
    if __name__ == "__main__":
        count = 0
        id_a = 0
        quit = ''
        while quit != "s":
            count += 1
            nome = input("Nome: ")
            aluno_bols = input("Aluno Bolsita: ")
            alunos = input("Demais alunos participantes: ").split(', ')
            coordenador_bols = input("Coordenador bolsista: ")
            coordenador = input("Coordenador: ").split(', ')
            resumo = input("Resumo: ")
            ano = input("Ano: ")
            edital = input("Forneca as informacoes do edital: ")
            campus = input("Campus: ")
            if(count == 1):
                p = Projeto(nome, alunos, aluno_bols, coordenador, coordenador_bols, resumo, ano, edital, grupo, campus)
                id_a = p.id
                js.append(p.__dict__)
            else:
                p = Projeto(nome, alunos, aluno_bols, coordenador, coordenador_bols, resumo, ano, edital, campus, id_a + count)
                js.append(p.__dict__)

            quit = input('Salvar? s/n: ')

        saveOnFile(js)
