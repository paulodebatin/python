create database vendas;

CREATE SEQUENCE public.pessoa_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

CREATE SEQUENCE public.produto_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

CREATE TABLE public.pessoa (
	id serial NOT NULL DEFAULT nextval('pessoa_id_seq'::regclass),
	nome varchar(255) NOT NULL,
	endereco varchar(255) NULL,
	numero varchar(20) NULL,
	bairro varchar(255) NULL,
	cidade varchar(255) NULL,
	uf bpchar(2) NULL,
	receber_noticias bool NULL,
	fumante bool NULL,
	cep varchar(8) NULL,
	data_nascimento date NULL,
	CONSTRAINT pessoa_pkey PRIMARY KEY (id)
);

CREATE TABLE public.produto (
	id serial NOT NULL DEFAULT nextval('produto_id_seq'::regclass),
	nome varchar(255) NOT NULL,
	quantidade int8 NULL,
	preco numeric(10,2) NULL,
	CONSTRAINT produto_pkey PRIMARY KEY (id)
);