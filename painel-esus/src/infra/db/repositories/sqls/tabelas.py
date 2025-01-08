TABELAS = [
    "DROP TABLE IF EXISTS pessoas;",
    "DROP TABLE IF EXISTS diabetes;",
    "DROP TABLE IF EXISTS diabetes_nominal;",
    "DROP TABLE IF EXISTS equipes;",
    "DROP TABLE IF EXISTS hipertensao;",
    "DROP TABLE IF EXISTS hipertensao_nominal;",
    "DROP TABLE IF EXISTS autorreferidos;",
    "DROP TABLE IF EXISTS crianca;",
    "DROP TABLE IF EXISTS idoso;",
    "DROP TABLE IF EXISTS status_records;",
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
			possui_fci BOOLEAN,
			possui_fcdt BOOLEAN,
			dt_ultima_atualizacao_cidadao DATE,
			diferenca_ultima_atualizacao_cidadao BIGINT,
			dt_atualizacao_fcd DATE,
			diferenca_ultima_atualizacao_fcd BIGINT,
			codigo_equipe_vinculada BIGINT,
			codigo_unidade_saude BIGINT,
			acompanhamento TEXT,
            status_cadastro TEXT,
            nu_micro_area_domicilio TEXT,
            nome_equipe TEXT,
            nome_unidade_saude TEXT,
            fci_att_2anos BOOLEAN,
            fcdt_att_2anos BOOLEAN,
            alerta_status_cadastro BOOLEAN,
            alerta BOOLEAN,
            tipo_ident_cpf_cns BOOLEAN,
            faixa_etaria TEXT,
            st_recusa_cadastro BOOLEAN,
			CONSTRAINT pk_pessoas PRIMARY KEY (co_cidadao)
		);
	""",
    'CREATE INDEX ix_pessoas_index ON pessoas ("index");',
    """CREATE TABLE status_records (
        "index" BIGINT, 
		tipo TEXT,
		codigo_equipe BIGINT,
		codigo_unidade_saude BIGINT,
		quantidade BIGINT
    );""",
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
		ultima_data_hemoglobina_glicada TEXT, 
		alerta_ultima_hemoglobina_glicada BOOLEAN,
		FOREIGN KEY(co_fat_cidadao_pec) REFERENCES pessoas(cidadao_pec)
	);""",
    'CREATE INDEX ix_diabetes_nominal_index ON diabetes_nominal ("index");',
    """CREATE TABLE idoso (
	"index" BIGINT, 
	cidadao_pec TEXT, 
	atendimentos_medicos FLOAT, 
	data_ultimo_atendimento_medicos DATE, 
	indicador_atendimentos_medicos INTEGER, 
	medicoes_peso_altura FLOAT, 
	data_ultima_medicao_peso_altura DATE, 
	indicador_medicoes_peso_altura INTEGER, 
	imc FLOAT, 
	categoria_imc TEXT, 
	registros_creatinina FLOAT, 
	data_ultimo_registro_creatinina DATE, 
	indicador_registros_creatinina INTEGER, 
	indicador_visitas_domiciliares_acs INTEGER, 
	visitas_domiciliares_acs FLOAT, 
	data_ultima_visita_domiciliar_acs DATE, 
	vacinas_influenza FLOAT, 
	data_ultima_vacina_influenza TEXT, 
	indicador_vacinas_influenza INTEGER, 
	atendimentos_odontologicos FLOAT, 
	data_ultimo_atendimento_odontologico DATE, 
	indicador_atendimento_odontologico INTEGER,
  		FOREIGN KEY(cidadao_pec) REFERENCES pessoas(cidadao_pec)
	);""",
    """	CREATE INDEX ix_idoso_index ON idoso ("index");""",
    """CREATE TABLE crianca (
	"index" BIGINT, 
	cidadao_pec BIGINT, 
	indicador_atendimentos_medicos_enfermeiros INTEGER, 
	data_ultimo_atendimento_medico_enfermeiro DATE, 
	atendimentos_medicos_enfermeiros_8d_vida FLOAT, 
	atendimentos_medicos_enfermeiros_puericult FLOAT, 
	data_ultimo_atendimento_medicos_enfermeiros_puericult DATE, 
	indicador_atendimentos_medicos_enfermeiros_puericult INTEGER, 
	medicoes_peso_altura_ate2anos FLOAT, 
	data_ultima_medicao_peso_altura_ate2anos DATE, 
	indicador_medicoes_peso_altura_ate2anos INTEGER, 
	data_ultima_visita_domiciliar_acs DATE, 
	indicador_visitas_domiciliares_acs INTEGER, 
	visitas_domiciliares_acs FLOAT, 
	teste_pezinho FLOAT, 
	indicador_teste_pezinho INTEGER, 
	data_ultimo_teste_pezinho TEXT, 
	n_penta FLOAT, 
	n_polio FLOAT, 
	n__triplici FLOAT, 
	data_ultima_vacina_penta DATE, 
	data_ultima_vacina_polio DATE, 
	data_ultima_vacina_triplici DATE, 
	indicador_vacinas_penta_polio_triplici INTEGER, 
	atendimentos_odontologicos FLOAT, 
	data_ultimo_atendimento_odontologico TEXT, 
	indicador_atendimentos_odontologicos FLOAT, 
	n_medicos FLOAT, 
	n_enfer FLOAT, 
	n_fono FLOAT, 
	n_psicol FLOAT, 
	n_educ_fisica FLOAT, 
	n_assist_social FLOAT, 
	n_tera_ocup FLOAT, 
	n_farmac FLOAT, 
	n_fisio FLOAT, 
	n_nutric FLOAT, 
	n_ciru_dent FLOAT, 
	n_outros FLOAT, 
	total FLOAT,
   			FOREIGN KEY(cidadao_pec) REFERENCES pessoas(cidadao_pec)
		);""",
    """	CREATE INDEX ix_crianca_index ON crianca ("index");	""",
]
