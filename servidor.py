# coding: utf-8

import json
from flask import Flask, render_template, make_response
from flask import Flask
from flask import request
from jinja2 import Environment
from jinja2 import PackageLoader
import xml.etree.cElementTree as ET
import os
import shutil

path = u'/home/aluno/Documents/teste/'

app = Flask(__name__)
env = Environment(loader=PackageLoader(__name__, 'templates'))

@app.route('/diretorio/<string:opcoes>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def apiArquivos(opcoes):
	
	listaArquivos = os.listdir(path)

	# ************************************ Requisição GET ************************************
	if request.method == 'GET':

		if opcoes == 'json':
			return json.dumps({'descricao': listaArquivos})

		elif opcoes == 'xml':
				template = render_template('diretorio.xml', listaDeArquivos=listaArquivos)
				response = make_response(template)
				response.headers['Content-Type'] = 'application/xml'
				
				return response

		else:
			nomeArquivo = opcoes
			for line in listaArquivos:
				if nomeArquivo == line:
					arq = open(path + nomeArquivo, 'r')
					res = arq.read()
					arq.close()
					#return res.encode('utf-8')
					return res

	# ************************************ Requisição DELETE ************************************
	elif request.method == 'DELETE':

		if opcoes == 'ALL':
			for op in listaArquivos:
				if os.path.isfile(path + op) == True: 
					os.remove(path + op)
				else:
					shutil.rmtree(path + op)	

		if opcoes in listaArquivos:
			# Verificando se é uma pasta ou diretório.
			if os.path.isfile(path + opcoes) == True:
				os.remove(path + opcoes)
				return 'Arquivo deletado'
			else:
				shutil.rmtree(path + opcoes)
				return 'Diretório deletado'
		else:
			 return 'Arquivo ou diretório não encontrado'

@app.route('/diretorio/<string:arquivo>/<string:conteudo>', methods=['PUT'])
def cria_atualiza_arquivo(arquivo, conteudo):

	cont = []
	try:
		with open(path + arquivo, 'r') as arq:
			cont = arq.readlines()
			arq.close()
	except IOError:
		print 'Arquivo não encontrado'

	cont.append(conteudo)
	arq = open(path + arquivo, 'w')
	arq.write(conteudo)
	arq.close()

	if arquivo in os.listdir(path):
		return 'Arquivo atualizado com sucesso'
	
	return 'Arquivo criado com sucesso'


if __name__ == "__main__":
	app.run(debug=True)

if __name__ == "__main__":
	app.run(debug=True)

