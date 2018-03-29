import random
from random import randint
import string
random.choice(string.ascii_letters + string.digits)

cat = ['car', 'utl', 'mot']

nomes = ['Antonella', 'Pedro Henrique', 'Sophia', 'Arthur', 'Helena', 'Bernardo', 'Valentina', 'Lavinia',
 'Laura', 'Davi', 'Isabella', 'Lorenzo', 'Manuela', 'Maria Julia', 'Julia', 'Pedro', 'Heloisa', 'Gabriel',
  'Luiza', 'Maria Luiza', 'Matheus', 'Lorena', 'Lucas', 'Livia', 'Benjamin', 'Giovanna', 'Nicolas',
   'Maria Eduarda', 'Guilherme', 'Beatriz', 'Rafael', 'Maria Clara', 'Joaquim', 'Cecilia', 'Samuel', 
   'Enzo Gabriel', 'Jose', 'Antonio', 'Maria', 'Pablo', 'Victor', 'Vitor', 'Ana', 'Ana Lucia', 'Bruno',
    'Vanessa', 'Marcelo', 'Gustavo']


sobrenomes = ['da Silva', 'Souza', 'Costa', 'dos Santos', 'de Oliveira', 'Pereira', 'Rodrigues', 'Almeida', 
	'Nascimento', 'Lima', 'Araujo', 'Fernandes', 'Carvalho', 'Gomes', 'Martins', 'Rocha', 'Ribeiro', 'Alves',
	 'Monteiro', 'Mendes', 'Barros', 'de Freitas', 'Barbosa', 'Rosa', 'Pinto', 'Ramos', 'Moura', 'Cavalcanti',
	  'Dias', 'Castro', 'Campos', 'Cardoso', 'Orleans', 'Bourbon', 'Savick', 'Muniz', 'Marques', 'Vasconcelos',
	   'Montenegro', 'Drummond', 'Figueiredo', 'Resende', 'Sampaio', 'Fernandes', 'Cavalcante', 'Arantes',
	    'Lombardi', 'Dieckmann', 'Menezes', 'Liberato', 'Alencar', 'Olimpia', 'Henrique']


usedCnh = []

def getCnh():
	while True:
		cnh = randint(10000000000, 99999999999)
		if cnh not in usedCnh:
			usedCnh.append(cnh)
			return str(cnh)	



usedCPF = []
def getCPF():

	while True:
		cpf = []
		soma = 0
		for x in range(10, 1, -1):
			aux = randint(0, 9)
			cpf.append(aux)
			soma += x*aux
		
		rest = soma%11
		d1 = 0
		if rest > 1:
			d1 = 11-rest

		# print('soma1')
		# print(soma)
		cpf.append(d1)
		soma = 0

		for x in range(11,1, -1):
			soma += cpf[11-x]*x

		rest = soma%11
		d2 = 0
		if rest > 1:
			d2 = 11-rest
		# print('soma2')
		# print(soma)
		cpf.append(d2)
		final_cpf = ''
		for x in cpf:
			final_cpf += str(x)
		if final_cpf not in usedCPF:
			usedCPF.append(final_cpf)
			return final_cpf



usedCard = []
def getCartao():
	while True:
		card = randint(1000000000000000, 9999999999999999)
		return str(card), str(randint(100, 999)), str(randint(20, 35))+'-'+str(randint(1, 12))+'-1'


clientesCadastrados = []

def clientesGenerator(maximo, fSaida):
	
	for x in range(maximo):
		n = random.choice(nomes)
		ns = randint(2, 4)
		s = random.sample(sobrenomes, ns)
		for x in s:
			n+=' ' + x


		dn = str(randint(1960, 1999))+'-'+str(randint(1, 12))+'-'+str(randint(1, 28))
		
		cnh = getCnh()

		card, numConf, dt = getCartao()


		# print(n + ' ' +dn + ' ' +cnh)
		cpf = getCPF()

		saida = '\n\nBEGIN;\nINSERT INTO cliente (cnh, nome, cpf, dtNascimento) VALUES ("'+cnh+'", "'+n+'", "'+cpf + '", "'+dn+'");'
		saida += '\nINSERT INTO cartao (numero, codSeguranca, validade, cnh) VALUES("'+card+'", "'+numConf+'", "'+dt+'", "'+ cnh+'");\nCOMMIT;'
		# print(saida)
		fSaida.write(saida)

		clientesCadastrados.append(cnh+':0000-00-00:0')


def getTelefone():
	n1 = randint(20000000, 99999999)
	return str(n1)

emailExt = ['@bol.com', '@gmail.com', '@outlook.com', '@hotmail.com']

emails = []

def getEmail(n):
	n = n.replace(" ", "_")
	i = 0
	while True:
		for x in emailExt:
			email = n+str(i)+x
			if email not in emails:
				emails.append(email)
				return email
			i +=1


funcionarioCadastrados = []

def funcionario(maximo, fSaida):
	for idFunc in range(1, maximo):
		n = random.choice(nomes)
		ns = randint(2, 3)
		s = random.sample(sobrenomes, ns)
		for x in s:
			n+=' ' + x
		dn = str(randint(1950, 1999))+'-'+str(randint(1, 12))+'-'+str(randint(1, 28))
		
		email = getEmail(n)

		cnh = getCnh()

		card, numConf, dt = getCartao()

		telefone = getTelefone()

		cel = ''
		if random.random() > 0.7:
			cel = '9'+getTelefone()

		cpf = getCPF()

		# print(n + ' ' +dn + ' ' +cnh)

		saida = '\n\nBEGIN;\nINSERT INTO funcionario (idFuncionario, cpf, nome, email, telefone, celular, dtNascimento) VALUES ("'+str(idFunc)+'", "'+cpf + '", "' +n+'", "'+email+'", "'+telefone+'", "'+cel+'", "'+dn+'");\nCOMMIT;'
		# print(saida)
		fSaida.write(saida)
		funcionarioCadastrados.append(idFunc)





cores = ['azul', 'amarelo', 'preto', 'branco', 'vermelho', 'prata', 'chumbo', 'verde']
potencia = ['1.0','1.6', '1.8', '2.0']

comb = ['gasolina', 'alcool']

carros = ['COUPE:Chevrolet:Camaro:3.2', 'SUV:Chevrolet:Captiva:3.2','HATCH:Chevrolet:Agile','HATCH:Chevrolet:Celta', 
	'HATCH:Chevrolet:Onix', 'SEDAN:Chevrolet:Prisma', 'HATCH:Chevrolet:Prisma:2012:3.2',
	'SEDAN:Chevrolet:Prisma:2012:3.2', 'SEDAN:Volkswagen:Bora:1.8', 'PICKUP:Volkswagen:Amarok:3.2',
	'SEDAN:Volkswagen:CC:2.0', 'SEDAN:Volkswagen:CC:2.0', 'HATCH:Volkswagen:Fox', 'HATCH:Volkswagen:Golf',
	'SEDAN:Volkswagen:Jetta:2.0','SUV:Volkswagen:Tiguan:3.2','HATCH:Fiat:Uno:1.0','HATCH:Fiat:Palio:1.0',
	'HATCH:Fiat:Stilo','HATCH:Fiat:Uno:1.0', 'HATCH:Ford:KA', 'SEDAN:Ford:KA', 'HATCH:Ford:Fiesta', 'SEDAN:Ford:Fiesta',
	'HATCH:Ford:Focus','SEDAN:Ford:Fusion:2.0','SUV:Ford:Ecosport:2.0','SUV:Ford:Edge:2.0','COUPE:Ford:Mustang:5.2',
	'PICKUP:Ford:Ranger:3.0', 'SEDAN:Honda:City:2.0', 'SUV:Honda:CR-V:2.0', 'HATCH:Honda:Fit', 'SEDAN:Toyota:Corolla:2.0',
	'SEDAN:Toyota:Avalon:2.0', 'SEDAN:Toyota:Camry:2.0', 'HATCH:Toyota:Etios', 'PICKUP:Toyota:Hilux',
	'SEDAN:Hyundai:Azera:2.0', 'SEDAN:Hyundai:Elantra:2.0', 'SEDAN:Hyundai:Genesis:2.0', 'COUPE:Hyundai:Genesis:2.0',
	'HATCH:Hyundai:HB-20', 'HATCH:Hyundai:i30:2.0', 'SUV:Hyundai:IX35:3.2', 'SUV:Hyundai:Tucson:3.2', 'SUV:Hyundai:Santa Fe:3.2',
	'HATCH:Hyundai:Veloster:2.0', 'SUV:Hyundai:Veracruz:3.2']


placas = []


veiculosTimeLine = []

def getPlaca():
	while True:
		placa = ''
		for x in range(3):
			placa += random.choice(string.ascii_uppercase)
		placa.lower()
		placa += '-'
		for x in range(4):
			placa += random.choice(string.digits)

		if placa not in placas:
			placas.append(placa)
			return placa




def carrosCreator(maximo, fSaida):
	for x in range(maximo):
		car = random.choice(carros)
		car = car.split(':')
		pot = 0

		vd = 100.0

		if len(car) == 3:
			pot = random.choice(potencia)
		else:
			pot = car[3]
			vd+=100.0


		tipo = car[0]
		marca = car[1]
		modelo = car[2]

		kmRodado = randint(0, 30000)

		cor = random.choice(cores)
		combustivel = random.choice(comb)

		ano = randint(2015, 2018)
		if ano == 2018:
			vd += 50.0


		np = 0

		if tipo == 'SUV' or tipo == 'SEDAN':
			np = 4

		if tipo == 'COUPE':
			np = 2
			vd += 100.0
		
		if tipo == 'HATCH':
			if random.random() > 0.7:
				np = 2
			else:
				np = 2
			


		placa = getPlaca()
		# print(placa)


		saida = '\n\nBEGIN;\nINSERT INTO veiculo(placa, marca, modelo, kmRodado, statusVeiculo, ano, tipo, combustivel, cor, vlDiaria) VALUES'
		saida += '("'+placa+'", "'+marca+'", "'+modelo+'", "'+str(kmRodado)+'", "disponivel", "'+str(ano)+'", "car", "'+combustivel+'", "'+cor+'", "'+str(vd)+'");'
		saida += '\nINSERT INTO carro (placa, potencia, tipo, numPortas) VALUES ("'+placa+'", "'+pot+'", "'+tipo+'", "'+str(np)+'");\nCOMMIT;'

		# print(saida)
		fSaida.write(saida)

		reg = str(ano)+':'+placa+':0000-00-00'
		veiculosTimeLine.append(reg)





motos = ['Honda:CB:300:R', 'Honda:CB:400', 'Honda:CB:400:Four', 'Honda:CB:400:SuperFour', 'Honda:CB:500',
	'Honda:CB:500:Four', 'Honda:CB:1000:R', 'Honda:Hornet:600', 'Honda:CB:250:R', 'Honda:CB:250',
	'Honda:CG:150:R', 'Honda:CG:150:R', 'Honda:CBR:250', 'Honda:CBR:250:R', 'Yamaha:YBR:125', 'Yamaha:YZF:600',
	'Yamaha:YZF:600:R', 'Yamaha:YZF:750', 'Yamaha:YZF:750:R', 'Yamaha:YS:150:Fazer', 'Yamaha:YS:250:Fazer',
	'BMW:RR:1000:S', 'BMW:GTL:1600:K', 'BMW:R:1000:S', 'BMW:B:1600:S', 'BMW:S:1000:XR']

def motosCreator(maximo, fSaida):
	for x in range(maximo):
		moto = random.choice(motos)
		moto = moto.split(':')
		pot = moto[2]

		vd = 100.0

		marca = moto[0]
		modelo = moto[1]

		vd += random.random()*100

		versao = ''
		if len(moto) == 4:
			versao = moto[3]

		
		kmRodado = randint(0, 30000)

		cor = random.choice(cores)
		combustivel = random.choice(comb)

		ano = randint(2015, 2018)
		if ano == 2018:
			vd += 50.0


		placa = getPlaca()
		# print(placa)


		saida = '\n\nBEGIN;\nINSERT INTO veiculo(placa, marca, modelo, kmRodado, statusVeiculo, ano, tipo, combustivel, cor, vlDiaria) VALUES'
		saida += '("'+placa+'", "'+marca+'", "'+modelo+'", "'+str(kmRodado)+'", "disponivel", "'+str(ano)+'", "mot", "'+combustivel+'", "'+cor+'", "'+str(vd)+'");'
		saida += '\nINSERT INTO motocicleta (placa, cilindradas, partida, versao) VALUES ("'+placa+'", "'+pot+'", "eletrica", "'+versao+'");\nCOMMIT;'

		fSaida.write(saida)
		# print(saida)
		reg = str(ano)+':'+placa+':0000-00-00'
		veiculosTimeLine.append(reg)



utilitarios = ['12:Renault:Master:Executiva', '12:Renault:Master', '12:Mercedes Benz:Sprinter', '8:Jinbei:Van', '14:Fiat:Ducato:Multijet',
'14:Fiat:Ducato', '5000:Hyundai:HR', '5000:Hyundai:HR:Bau', '5000:Iveco:Daily', '5000:Iveco:Daily:Refrigerador']

def utilitariosCreator(maximo, fSaida):
	for x in range(maximo):
		utl = random.choice(utilitarios)
		utl = utl.split(':')

		vd = 300.0

		marca = utl[1]
		modelo = utl[2]
		carga = 0
		pas = 0

		if len(utl[0]) > 2:
			carga = utl[0]
			vd += random.random()*200
		else:
			pas = utl[0]
			vd += random.random()*50

		versao = ''
		if len(utl) == 4:
			versao = utl[3]

		
		kmRodado = randint(0, 30000)

		cor = random.choice(cores)
		combustivel = random.choice(comb)

		ano = randint(2015, 2018)
		if ano == 2018:
			vd += 50.0


		placa = getPlaca()
		# print(placa)

		saida = '\n\nBEGIN;\nINSERT INTO veiculo(placa, marca, modelo, kmRodado, statusVeiculo, ano, tipo, combustivel, cor, vlDiaria) VALUES'
		saida += '("'+placa+'", "'+marca+'", "'+modelo+'", "'+str(kmRodado)+'", "disponivel", "'+str(ano)+'", "mot", "'+combustivel+'", "'+cor+'", "'+str(vd)+'");'
		saida += '\nINSERT INTO utilitario (placa, numPassageiros, carga) VALUES ("'+placa+'", "'+str(pas)+'", "'+str(carga)+'");\nCOMMIT;'


		fSaida.write(saida)
		reg = str(ano)+':'+placa+':0000-00-00'
		veiculosTimeLine.append(reg)
		# print(saida)



descricaoAcidente = ['reparos na pintura', 'Reparo em amassados e pintura', 
'Troca de elementos da suspensao, reparos na lataria e pintura', 'Troca de vidro e reparos na pintura', 
'Substituicao de pneus furados']
descricaoManutencaoSimples = ['Limpeza no interior e exterior', 'Troca de pneus, oleo e balanceamento. Limpeza no interior e exterior',
	'Troca de oleo', 'Polimento e limpeza interna e externa']


existOPR = []

# def permitidaOP(veiculo, cliente):
# 	v = veiculo.split(':')
# 	placa = v[1]
# 	for x in existOPR:
# 		if x[0] == 'v' or x[0] == 'm':
# 			if placa in x and cliente in x:
# 				return False
# 	return True


revisoes = []


def getFuncionario():
	return random.choice(funcionarioCadastrados)


def incluiRevisao(data, placa):
	idFunc = getFuncionario()
	arm = str(idFunc)+':'+placa+':'+data
	revisoes.append(arm)
	# print('idFunc: placa: dtManutencao')
	# print(arm)



# def atualizaOperacoes(dia, mes, ano):
# 	data = str(ano)+'-'+str(mes)+'-'+str(dia)
# 	for x in range(len(existOPR)-1):
# 		dado = existOPR[x]
# 		dtFim = dado.split(':')[5]
# 		if not dado[0] == 'f':
# 			if dado[0] == 'm':
# 				print('finalizou\n'+dtFim)
# 				new = list(dado)
# 				new[0] = 'f'
# 				dado = ''.join(new)
# 			if(dtFim == data):
# 				print('manutencao\n'+dtFim)
# 				incluiRevisao(data, dado.split(':')[2])
# 				new = list(dado)
# 				new[0] = 'm'
# 				dado = ''.join(new)
# 			existOPR[x] = dado
# 			print(existOPR[x])

# def getVeiculoOP():
# 	return random.choice(veiculosTimeLine)


# def getCliente():
# 	return random.choice(clientesCadastrados)


# def period(dia, mes, ano, duracao):
# 	dtInicio = str(ano)+'-'+str(mes)+'-'+str(dia)
# 	dn = dia
# 	mn = mes
# 	an = ano
# 	for x in range(duracao):
# 		dn += 1
# 		if dn == 29:
# 			dn = 1
# 			mn += 1
# 			if mn == 13:
# 				mn = 1
# 				an += 1

# 	dtFim = str(an)+'-'+str(mn)+'-'+str(dn)
# 	return dtInicio, dtFim


# def criarAluguelRevisao():
# 	i = 0
# 	for ano in range(2015,2016):
# 		for mes in range(1,2):
# 			for dia in range(1,29):
# 				print('\n\n---------------------------------')
# 				print(str(ano)+'-'+str(mes)+'-'+str(dia))
# 				atualizaOperacoes(dia, mes, ano)
# 				qtd = randint(5, 10)
# 				for interacoes in range (qtd):
# 					veiculo = getVeiculoOP()
# 					cliente = getCliente()
# 					v = veiculo.split(':')
# 					v = int(v[0])
# 					if v <= ano:
# 						if permitidaOP(veiculo, cliente):
# 							duracao = randint(1, 60)
# 							dtInicio, dtFim = period(dia, mes, ano, duracao)
# 							v = veiculo.split(':')
# 							v = v[1]
# 							inclusao = ''
# 							inclusao = 'v:'+str(i) +':'+v + ':' + cliente + ':' + dtInicio + ':' +dtFim
# 							i+=1

# 							existOPR.append(inclusao)
					 
			


def period2(dia, mes, ano, duracao, manutencao):
	dtInicio = str(ano)+'-'+str(mes)+'-'+str(dia)
	dn = dia
	mn = mes
	an = ano
	for x in range(duracao):
		dn += 1
		if dn == 29:
			dn = 1
			mn += 1
			if mn == 13:
				mn = 1
				an += 1

	dtFim = str(an)+'-'+str(mn)+'-'+str(dn)

	for x in range(manutencao):
		dn += 1
		if dn == 29:
			dn = 1
			mn += 1
			if mn == 13:
				mn = 1
				an += 1
	dtManutencao = str(an)+'-'+str(mn)+'-'+str(dn)
	
	return dtInicio, dtFim, dtManutencao


def permitidaOP2(data, v, cliente):
	ano, mes, dia = data.split('-')
	for x in veiculosTimeLine:
		anoV, placa, dt = x.split(':')
		if(placa == v):
			a, m, d = dt.split('-')
			if ano < a:
				return False
			if mes < m:
				return False
			if dia < d:
				return False

	for x in clientesCadastrados:
		cnh, dt, score = x.split(':')
		if(cnh == cliente):
			a, m, d = dt.split('-')
			if ano < a:
				return False
			if mes < m:
				return False
			if dia < d:
				return False

	return True

def atualizaClienteVeiculo(veiculoIndex, dtManutencao, clienteIndex, dtFim):
	c = clientesCadastrados[clienteIndex]
	cnh, dt, score = c.split(':')
	
	clientesCadastrados[clienteIndex] = cnh+':'+dtFim+':' + str(int(score)+300)
	
	car = veiculosTimeLine[veiculoIndex]
	ano, placa, dt = car.split(':')

	veiculosTimeLine[veiculoIndex] = ano+':'+placa+':'+dtManutencao
	

	# for x in range(len(clientesCadastrados)):
	# 	c = clientesCadastrados[x]
	# 	cnh, dt, score = c.split(':')
	# 	if cnh == cliente:
	# 		print('cnh: dtFim')
	# 		print(c)

	# for x in range(len(veiculosTimeLine)):
	# 	car = veiculosTimeLine[x]
	# 	ano, placa, dt = car.split(':')
	# 	if placa == v:
	# 		print('ano: placa: dtManutencao')
	# 		print(car)


def getVeiculoOP(dia, mes, ano):
	i = 0
	while i < 200:
		i+=1
		carIndex = randint(0, len(veiculosTimeLine)-1)
		car = veiculosTimeLine[carIndex]
		fab, placa, dt = car.split(':')
		# print('Escolheu:'+car+'\n')
		# print('Data:'+str(ano)+'-'+str(mes)+'-'+str(dia)+'\n\n')
		# print(int(fab))
		if int(fab) <= ano:
			a, m, d = dt.split('-')
			if not int(a) > ano:
				
				if not int(m) > mes:
					if not int(d) > dia:
					
						return carIndex
	return None

def generateSubList():
    return int(len(clientesCadastrados)/7)


def getCliente(dia, mes, ano):
	i = 0
	while i < 200:
		i+=1
		rad = random.random()

		clienteIndex = 0
		if rad > 0.70:

			clienteIndex = randint(0, len(clientesCadastrados)-1)
		else:
			# subList = [clientesCadastrados[index] for index in range(int(len(clientesCadastrados)/4))]
			clienteIndex = randint(0, subList)	
		# print('incluiu')
		# print('Escolheu:'+cliente+'\n')
		# print('Data:'+str(ano)+'-'+str(mes)+'-'+str(dia)+'\n\n')
		cnh, dt, score = clientesCadastrados[clienteIndex].split(':')		
		a, m, d = dt.split('-')
		if not int(a) > ano:
			if not int(m) > mes:
				if not int(d) > dia:
					
					return clienteIndex
	return None


def getMultas(dtInicio, veiculoIndex, clienteIndex):
	if random.random() > 0.2:
		cnh, dt, score = clientesCadastrados[clienteIndex].split(':')	
		score = int(score)
		score -= 50
		if score < 0:
			score = 0
		veiculo = veiculosTimeLine[veiculoIndex]
		fab, placa, dt = veiculo.split(':')
		clientesCadastrados[clienteIndex] = cnh+':'+dt+':'+str(score)
		query = '\nINSERT INTO infracao(placa, dtEmissao, valor, cnh)VALUES("'+placa+'", "'+dtInicio+'", "'+str(float(randint(50, 500)))+'", "'+cnh+'");\n'
		return query
	else:
		return '\n'	

def getAcidente(dtFim, veiculoIndex, clienteIndex):
	if random.random() > 0.02:
		cnh, dt, score = clientesCadastrados[clienteIndex].split(':')
		score = int(score)
		score -= 50
		if score < 0:	
			score = 0
		clientesCadastrados[clienteIndex] = cnh+':'+dt+':'+str(score)
		veiculo = veiculosTimeLine[veiculoIndex]
		fab, placa, dt = veiculo.split(':')
		query = '\nINSERT INTO acidente(placa, dtAcidente, cnh)VALUES("'+placa+'", "'+dtFim+'", "'+cnh+'");\n'
		return query, True
	else:
		return '\n', False



def criarAluguelRevisao2(fSaida):
	i = 1
	for ano in range(2017,2019):
		for mes in range(1,13):
			for dia in range(1,29):
				print(type(ano))
				maxQtd = 12*(ano-2000) + dia*3
				qtd = randint(30, maxQtd)
				print('\n--------------------------------\n')
				print('Relacoes em: '+str(ano)+'-'+str(mes)+'-'+str(dia))
				print('\n***********************************\n')
				for interacoes in range (qtd):
					veiculoIndex = getVeiculoOP(dia, mes, ano)
					clienteIndex = getCliente(dia, mes, ano)

					if(veiculoIndex == None or clienteIndex == None):
						continue

					veiculo = veiculosTimeLine[veiculoIndex]
					cliente = clientesCadastrados[clienteIndex]

					anoV, placa, dt = veiculo.split(':')
					cnh, dt, score = cliente.split(':')

					duracao = randint(1, 5)
					kmRodado = randint(5, 80)*duracao
					manutencao = randint(2, 5)
					dtInicio, dtFim, dtManutencao = period2(dia, mes, ano, duracao, manutencao)


					multa = getMultas(dtInicio, veiculoIndex, clienteIndex)
					acidente, resp = getAcidente(dtFim, veiculoIndex, clienteIndex)
					inclusao = str(i) +':'+veiculo + ':' + cliente + ':' + dtInicio + ':' +dtFim
					existOPR.append(inclusao)
					incluiRevisao(dtManutencao, veiculo)
					atualizaClienteVeiculo(veiculoIndex, dtManutencao, clienteIndex, dtFim)
					# print('id: placa: cnh: dtInicio: dtFim')
					# print(inclusao)
					# print('\n--------------------------------\n')

					final = '\nBEGIN;\nINSERT INTO aluguel(placa, dtRetirada, dtDevolucao, kmRodado, cnh)VALUES("'+placa+'", "'+dtInicio+'", "'+dtFim+'", "'+str(kmRodado)+'", "'+cnh+'");'
					final += multa
					final += acidente
					
					revisaoQuery = ''

					if resp == True:
						revisaoQuery = '\nINSERT INTO revisao(placa, dtRevisao, valor, descricao)VALUES("'+placa+'", "'+dtManutencao+'", "'+str(float(randint(200, 2000)))+'", "'+random.choice(descricaoAcidente)+'");\n'
					else:
						revisaoQuery = '\nINSERT INTO revisao(placa, dtRevisao, valor, descricao)VALUES("'+placa+'", "'+dtManutencao+'", "'+str(float(randint(20, 100)))+'", "'+random.choice(descricaoManutencaoSimples)+'");\n'
					final += revisaoQuery
					final += '\nCOMMIT;\n\n'
					fSaida.write(final)
					i+=1



cupons = []
def criaCupons():
	fact = 50
	idC = 1
	for categoria in cat:
		for x in range(2, 10):
			query = '\nINSERT INTO cupom(idCupom, precoPonto, desconto, categoria)VALUES("'+str(idC)+'", "'+str(100*x+fact)+'", "'+str(x)+'", "'+categoria+'");\n'
			fSaida.write(query)
			cupons.append(str(idC)+':'+str(100*x+fact)+':'+categoria+':'+str(x))
			idC+=1
		fact +=400
		print('cupom_mais_caro:' + str(1600+fact))


# Modifique o local de armazenamento
path = '/home/maxtelll/Desktop/povoador_LBD.txt'

# for i in range(100000):
# 	print (getCPF())

fSaida = open(path, 'w+')


print('Cria clientes...')
clientesGenerator(30000, fSaida)
print('Cria funcionarios...')
funcionario(500, fSaida)
print('Cria carros...')
carrosCreator(3000, fSaida)
print('Cria motos...')
motosCreator(2000, fSaida)
print('Cria utilitarios...')
utilitariosCreator(1000, fSaida)

# print(clientesCadastrados)
# print(funcionarioCadastrados)
# print(veiculosTimeLine)

# fSaida.close()

# path = '/home/maxtelll/Desktop/teste_LBD.txt'

# # for i in range(100000):
# # 	print (getCPF())

# fSaida = open(path, 'w+')

print('Cria relacoes...')
subList = generateSubList()
criarAluguelRevisao2(fSaida)

print('Criando cupons')
criaCupons()


print('Premiuns')

i = 0
for p in clientesCadastrados:
	cnh, dt, score = p.split(':')
	print(score)
	score = int(score)

	if(score >= 3000):
		i += 1
		categoria = random.choice(cat)
		query = '\nINSERT INTO cliente_premium(cnh, categoria)VALUES("'+cnh+'", "'+categoria+'");\n'
		fSaida.write(query)
	# fSaida.write(p+'\n')
print(str(i)+' cadastrados')
print('\ncupom')
i = 0
for p in clientesCadastrados:
	cnh, dt, score = p.split(':')
	score = int(score)
	for cupom in cupons:
		idC, preco, categ, des = cupom.split(':')
		preco = int(preco)
		if score >= preco:
			i +=1
			query = '\nINSERT INTO lista_cupom(cnh, idCupom)VALUES("'+cnh+'", "'+idC+'");\n'
			fSaida.write(query)
print(str(i)+' cadastrados')


# for pr in cupons:
# 	print(pr)

# for p in existOPR:
# 	# print(p)
# 	fSaida.write(p+'\n')

# for p in revisoes:
# 	# print(p)
# 	fSaida.write(p+'\n')



fSaida.close()
