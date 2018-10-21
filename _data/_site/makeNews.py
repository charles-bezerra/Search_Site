import json

class News:
	def __init__(self, titulo, resumo, link, id = ''):
		self.titulo = titulo
		self.resumo = resumo
		self.link = link

		if(id == ''):
			js0 = ''
			count = 0

			file = open('NewsPesquisa.json', 'r')
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
    
    file = open('NewsPesquisa.json', 'r')
    data = file.read()
    file.close()
    
    if(data != ''):
        js0 = json.loads(data)
    
    js.extend(js0)
    aux = json.dumps(js) #
    
    with open('NewsPesquisa.json', 'w') as file:
        file.write(aux)
    
    print(js0[0]['id'])
    return 0

js = []

if __name__ == '__main__':
   	count = 0
   	id_a = 0
   	quit = ''
   	while quit != "s":
   		count += 1
   		titulo = input("Titulo da noticia: ")
   		resumo = input("Um breve resumo para noticia: ")
   		link = input("Link da noticia no portal: ")

   		if(count == 1):
   			news = News(titulo, resumo, link)
   			id_a = news.id
   			js.append(news.__dict__)
   		else:
   			news = News(titulo, resumo, link, id_a + count)
   			js.append(news.__dict__)
   		quit = input('Salvar? s/n: ')

   	saveOnFile(js)
		
