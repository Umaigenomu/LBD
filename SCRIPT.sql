DROP DATABASE rents;
CREATE DATABASE rents;
USE rents;
CREATE TABLE funcionario(
	idFuncionario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefone VARCHAR(255) NOT NULL,
    cpf CHAR(11) NOT NULL,
    celular VARCHAR(255),
    dtNascimento DATE NOT NULL
);

CREATE TABLE veiculo(
	placa CHAR(8) PRIMARY KEY NOT NULL,
    marca VARCHAR(255) NOT NULL,
    modelo VARCHAR(255) NOT NULL,
    kmRodado FLOAT NOT NULL,
    statusVeiculo VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    tipo CHAR(3),
    combustivel VARCHAR(255),
    cor VARCHAR(255),
    vlDiaria FLOAT NOT NULL
);
CREATE TABLE motocicleta(
	placa CHAR(8) PRIMARY KEY REFERENCES veiculo(placa) ON DELETE CASCADE ,
    cilindradas INT NOT NULL,
    partida VARCHAR(255),
    versao VARCHAR(255)
    );
CREATE TABLE carro(
	placa CHAR(8) PRIMARY KEY REFERENCES veiculo(placa) ON DELETE CASCADE,
	potencia char(8),
    tipo VARCHAR(255),
    numPortas INT
);
CREATE TABLE utilitario(
	placa CHAR(8) PRIMARY KEY REFERENCES veiculo(placa) ON DELETE CASCADE ,
    numPassageiros INT,
    carga INT
);

CREATE TABLE revisao(
	codRevisao INT AUTO_INCREMENT PRIMARY KEY,
	placa CHAR(8) ,
    dtRevisao DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    FOREIGN KEY (placa) REFERENCES veiculo(placa) ON DELETE CASCADE
);
CREATE TABLE cliente(
	cnh CHAR(11) PRIMARY KEY NOT NULL,
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(255),
    dtNascimento DATE NOT NULL
);
CREATE TABLE cliente_premium(
	cnh CHAR(11) PRIMARY KEY REFERENCES cliente(cnh) ON DELETE CASCADE,
    categoria VARCHAR(255) NOT NULL
);
CREATE TABLE cartao(
	numero CHAR(16) NOT NULL,
    codSeguranca INT NOT NULL,
    validade DATE NOT NULL,
    cnh CHAR(11),
    FOREIGN KEY (cnh) REFERENCES cliente(cnh) ON DELETE CASCADE
);
CREATE TABLE cupom(
	idCupom INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    precoPonto INT NOT NULL,
    desconto FLOAT NOT NULL,
    categoria VARCHAR(255)
);
CREATE TABLE lista_cupom(
	cnh CHAR(11),
    idCupom INT,
    FOREIGN KEY (idCupom) REFERENCES cupom(idCupom) ON DELETE CASCADE,
    FOREIGN KEY (cnh) REFERENCES cliente(cnh) ON DELETE CASCADE,
    primary key(idCupom, cnh)
);
CREATE TABLE acidente(
	codAcidente INT AUTO_INCREMENT PRIMARY KEY,
	placa CHAR(8) ,
    dtAcidente DATE NOT NULL,
    cnh CHAR(11),
    FOREIGN KEY (cnh) REFERENCES cliente(cnh) ON DELETE CASCADE,
    FOREIGN KEY (placa) REFERENCES veiculo(placa) ON DELETE CASCADE
);
CREATE TABLE infracao(
	codInfracao INT AUTO_INCREMENT PRIMARY KEY,
	placa CHAR(8),
    dtEmissao DATE NOT NULL,
    valor FLOAT NOT NULL,
    cnh CHAR(11),
    FOREIGN KEY (cnh) REFERENCES cliente(cnh) ON DELETE CASCADE,
    FOREIGN KEY (placa) REFERENCES veiculo(placa) ON DELETE CASCADE
);
CREATE TABLE aluguel(
	codAluguel INT AUTO_INCREMENT PRIMARY KEY,
	placa CHAR(8) REFERENCES veiculo(placa) ON DELETE CASCADE,
    dtRetirada DATE NOT NULL,
    dtDevolucao DATE,
    kmRodado INT,
    cnh CHAR(11) NOT NULL,
    FOREIGN KEY (cnh) REFERENCES cliente(cnh) ON DELETE CASCADE,
    FOREIGN KEY (placa) REFERENCES veiculo(placa) ON DELETE CASCADE
);

