# coding: utf-8

import requests
import json
from lxml import etree

op = '0'
while op != '5':
	
	print '********** Operações **********\n'
	op = raw_input('1. Listar arquivos\n2. Exibir arquivo\n3. Remover arquivo/diretório' + 
		'\n4. Criar/Atualizar arquivo\n5. Sair\nEscolha: ')

	# ************************************ Listagem de arquivos ************************************
	if op == '1':
		print '\n********** Listar **********'
		tipo = raw_input('1. json\n2. xml\nEscolha: ')

		if tipo == '1':
			print '\n********** json *********\n'
			r = requests.get("http://localhost:5000/diretorio/json")

			dados = json.loads(r.text)

			for dado in dados["descricao"]:
				print u'' + dado
		
		elif tipo == '2':
			print '\n********** xml *********\n'
			r = requests.get("http://localhost:5000/diretorio/xml")
			#root = xml.getroot()

			conteudo = r.text
			arq = open('xm.xml', 'w')
			arq.write(conteudo.encode('utf8') )
			arq.close()

			xml = etree.parse('xm.xml')
			# Listando todos os elementos do XML
			for elemento in xml.iter():
				print elemento.text


	# ************************************ Exibição de arquivo ************************************
	elif op == '2':
		print '\n********** Exibir **********'
		arq = raw_input('Arquivo: ')
		r = requests.get("http://localhost:5000/diretorio/" + arq)
		print r.text.encode('utf-8')

	# ************************************ Remover arquivo ************************************
	elif op == '3':
		print '\n********** Deletar **********'
		arq = raw_input('Arquivo: ')
		r = requests.delete("http://localhost:5000/diretorio/" + arq)
		print r.text

	# ************************************ Criar e atualizar arquivo ************************************
	elif op == '4':
		print '\n********** Criar/Atualizar **********'
		arq = raw_input('Arquivo: ')
		conteudo = raw_input('Conteudo: ')
		r = requests.put("http://localhost:5000/diretorio/" + arq + '/' + conteudo)
		print r.text
