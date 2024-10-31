TABELAS = [
    'DROP TABLE IF EXISTS pessoas;',
	'DROP TABLE IF EXISTS diabetes;',
	'DROP TABLE IF EXISTS diabetes_nominal;',
	'DROP TABLE IF EXISTS equipes;',
	'DROP TABLE IF EXISTS hipertensao;',
	'DROP TABLE IF EXISTS hipertensao_nominal;',
	"""
		CREATE TABLE pessoas (
			"index" BIGINT, 
			cidadao_pec BIGINT, 
			co_cidadao BIGINT, 
			raca_cor TEXT, 
			cpf TEXT, 
			cns TEXT, 
			nome TEXT, 
			nome_social TEXT, 
			data_nascimento DATE, 
			idade BIGINT,
			sexo TEXT, 
			identidade_genero TEXT, 
			telefone TEXT, 
			ultima_atualizacao_cidadao DATE, 
			ultima_atualizacao_fcd DATE, 
			tipo_endereco TEXT, 
			endereco TEXT, 
			complemento TEXT, 
			numero TEXT, 
			bairro TEXT, 
			cep TEXT, 
			tipo_localidade TEXT,
			CONSTRAINT pk_pessoas PRIMARY KEY (cidadao_pec)
		);
	""",	
	'CREATE INDEX ix_pessoas_index ON pessoas ("index");',
	"""CREATE TABLE hipertensao_nominal (
		"index" BIGINT, 
		co_fat_cidadao_pec BIGINT, 
		diagnostico TEXT, 
		cids TEXT, 
		ciaps TEXT, 
		min_date DATE, 
		data_ultima_visita_acs DATE, 
		alerta_visita_acs BOOLEAN, 
		total_consulta_individual_medico BIGINT, 
		total_consulta_individual_enfermeiro BIGINT, 
		total_consulta_individual_medico_enfermeiro BIGINT, 
		ultimo_atendimento_medico DATE, 
		ultimo_atendimento_enfermeiro DATE, 
		alerta_total_de_consultas_medico BOOLEAN, 
		ultimo_atendimento_medico_enfermeiro DATE, 
		alerta_ultima_consulta_medico BOOLEAN, 
		ultimo_atendimento_odonto DATE, 
		alerta_ultima_consulta_odontologica BOOLEAN, 
		ultima_data_afericao_pa DATE, 
		alerta_afericao_pa BOOLEAN, 
		ultima_data_creatinina DATE, 
		alerta_creatinina BOOLEAN,
		FOREIGN KEY(co_fat_cidadao_pec) REFERENCES pessoas(cidadao_pec)
	);""",
	'CREATE INDEX ix_hipertensao_nominal_index ON hipertensao_nominal ("index");',
	"""CREATE TABLE diabetes_nominal (
		"index" BIGINT, 
		co_fat_cidadao_pec BIGINT, 
		diagnostico TEXT, 
		cids TEXT, 
		ciaps TEXT, 
		min_date DATE, 
		data_ultima_visita_acs DATE, 
		alerta_visita_acs BOOLEAN, 
		total_consulta_individual_medico BIGINT, 
		total_consulta_individual_enfermeiro BIGINT, 
		total_consulta_individual_medico_enfermeiro BIGINT, 
		ultimo_atendimento_medico DATE, 
		ultimo_atendimento_enfermeiro DATE, 
		alerta_total_de_consultas_medico BOOLEAN, 
		ultimo_atendimento_medico_enfermeiro DATE, 
		alerta_ultima_consulta_medico BOOLEAN, 
		ultimo_atendimento_odonto DATE, 
		alerta_ultima_consulta_odontologica BOOLEAN, 
		ultima_data_afericao_pa DATE, 
		alerta_afericao_pa BOOLEAN, 
		ultima_data_glicemia_capilar DATE, 
		alerta_ultima_glicemia_capilar BOOLEAN, 
		ultima_data_hemoglobina_glicada TEXT, 
		alerta_ultima_hemoglobina_glicada BOOLEAN,
		FOREIGN KEY(co_fat_cidadao_pec) REFERENCES pessoas(cidadao_pec)
	);""",
	'CREATE INDEX ix_diabetes_nominal_index ON diabetes_nominal ("index");'
]
