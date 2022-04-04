CREATE DATABASE biblioteca;
USE biblioteca;
#DROP DATABASE biblioteca;

CREATE TABLE tbl_clientes (
	codigo_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(45) NOT NULL,
    cpf_cliente VARCHAR(45) NOT NULL UNIQUE,
    nasc_cliente DATE NOT NULL,
    email VARCHAR(45) NOT NULL
);

CREATE TABLE tbl_categoria(
	codigo_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(45) NOT NULL
);

CREATE TABLE tbl_editora (
	codigo_editora INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome_editora VARCHAR(45) NOT NULL,
    cnpj VARCHAR(45) UNIQUE NOT NULL,
    email VARCHAR(45) NOT NULL
);

CREATE TABLE tbl_autor (
	codigo_autor INT PRIMARY KEY AUTO_INCREMENT,
    nome_autor VARCHAR(45) NOT NULL,
    nasc_autor DATE NOT NULL,
    nascionalidade VARCHAR(45) NOT NULL
);

CREATE TABLE tbl_livros (
	codigo_livro INT PRIMARY KEY AUTO_INCREMENT,
    nome_livro VARCHAR(45) NOT NULL,
    data_publicacao DATE NOT NULL,
    paginas INT NOT NULL,
    valor_unitario DECIMAL(6,2) NOT NULL,
    fk_categoria INT NOT NULL,
    fk_editora INT NOT NULL
);

CREATE TABLE autor_livros (
	fk_autor INT,
    fk_livro INT
);

CREATE TABLE tbl_bibliotecario (
	codigo_bibliotecario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_bibliotecario VARCHAR(45) NOT NULL,
    nasc_bibliotecario DATE NOT NULL,
    telefone VARCHAR(45) NOT NULL,
    fk_bibliotecario_responsavel INT
);

CREATE TABLE tbl_emprestimos (
	codigo_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    retirada timestamp NOT NULL,
    devolução timestamp NOT NULL,
    fk_bibliotecario INT NOT NULL,
    fk_cliente INT NOT NULL
);

CREATE TABLE livro_emprestimo (
	fk_livro INT NOT NULL,
    fk_emprestimo INT NOT NULL
);

ALTER TABLE tbl_bibliotecario
ADD foreign key (fk_bibliotecario_responsavel) 
REFERENCES tbl_bibliotecario(codigo_bibliotecario);

ALTER TABLE tbl_livros
ADD foreign key (fk_categoria) 
REFERENCES tbl_categoria(codigo_categoria);

ALTER TABLE tbl_livros
ADD foreign key (fk_editora) 
REFERENCES tbl_editora(codigo_editora);

ALTER TABLE autor_livros
ADD foreign key (fk_autor) 
REFERENCES tbl_autor(codigo_autor);

ALTER TABLE autor_livros
ADD foreign key (fk_livro) 
REFERENCES tbl_livros(codigo_livro);

ALTER TABLE tbl_emprestimos
ADD foreign key (fk_bibliotecario) 
REFERENCES tbl_bibliotecario(codigo_bibliotecario);

ALTER TABLE tbl_emprestimos
ADD foreign key (fk_cliente) 
REFERENCES tbl_clientes(codigo_cliente);

ALTER TABLE livro_emprestimo
ADD foreign key (fk_livro) 
REFERENCES tbl_livros(codigo_livro);

ALTER TABLE livro_emprestimo
ADD foreign key (fk_emprestimo) 
REFERENCES tbl_emprestimos(codigo_emprestimo);

