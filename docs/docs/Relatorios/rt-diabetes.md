# Relatório Temático Diabetes

Este relatório tem como objetivo:

- favorecer aumento da cobertura de identificação, manejo, acompanhamento transdisciplinar e promoção da saúde de pessoas com diabetes na Atenção Primária à Saúde
- monitorar e prevenir agravos, principalmente aqueles relacionados a internações por condições sensíveis à atenção primária (ICSAP)
- contribuir com ferramentas para ações de acompanhamento e monitoramento de pessoas com diabetes

## Tela v.0.9.1 (beta)

![Relatório Temático Diabetes](./img/rt-diabetes.png)

## Regras

1. Identificação das pessoas a partir da Ficha de atendimento individual: código CID10 e CIAP 2 E/OU problema/condição avaliada
    
    **E/OU**
    
    Identificação das pessoas a partir da Ficha de cadastro individual: questionário autorreferido de condições/ situações de saúde
    
    #17 statusTemDiabetes
    
    **Código AB**: ABP006
    
    **CIAP2**: T89; T90; **W85**
    
    **CID10**: E10, E100, E101, E102, E103, E104, E105, E106, E107, E108, E109, E11, E110, E111, E112, E113, E114, E115, E116, E117, E118, E119, **E12**, **E120, E121, E122, E123, E124, E125, E126, E127, E128, E129, E13, E130, E131, E132, E133, E134, E135, E136, E137, E138, E139**, E14, E140, E141, E142, E143, E144, E145, E146, E147, E148, E149, **O24, O240, O241, O242, O243, O244, O249, P702**
    
2. Estratificar por idade e sexo
3. Identificação de exames solicitados E/OU avaliados nos últimos 12 meses:
    1. Glicemia código SIGTAP: 02.02.01.029-5 / ABEX 026
    2. Hemoglobina glicada código SIGTAP: 02.02.01.050-3/ ABEX 008
    3. Retinografia código SIGTAP: 02.11.06.017-8 / ABEX 013
    4. Creatinina código SIGTAP: 02.02.01.031-7/ ABEX 003
    5. EAS/EQU (urina rotina) código SIGTAP: 02.02.01.001-7/ ABEX 027
4. Os exames devem ser classificados em 
    1. Sem solicitação ⇒ sem solicitação e sem avaliação
    2. Aguardando resultado ⇒ Com solicitação e sem avaliação
    3. Resultado registrado ⇒ com Avaliação e/ou com solicitação
5. Identificação de profissionais responsáveis por atendimentos - código CBO
    1. Enfermeiro 2235
    2. Técnico de enfermagem e auxiliar de enfermagem 3222
    3. Técnico Agente Comunitário de Saúde 3222
    4. Agente Comunitário de Saúde 5151
    5. Médico clínico 2251, 2252, 2253, 2231
    6. Cirugião Dentista 2232
    7. Farmacêutico 2234
    8. Fisioterapeuta 2236
    9. Profissional de Educação Física 2344, 2241
    10. Técnico em Saúde Bucal 3224
    11. Terapeuta Ocupacional 2239
    12. Nutricionista 2237
    13. Assistente Social 251605
    14. Psicólogo 251510
    15. Fonoaudiólogo 2238
    
6. Identificação de último registro peso / altura nos últimos 12 meses E cálculo de IMC E categorizar em 4 faixas
    1. Avaliação antropométrica: peso (kg) / altura (cm)
    2. Fórmula IMC: dividir o peso (em kg) pela altura ao quadrado (em metros)
        
        https://lh7-rt.googleusercontent.com/docsz/AD_4nXefz_oslD2JFFK7earbHlkxSfC30jhxsSw6fHlEZ3_TRwdg3k1e9gBXe_VF4qy4VzUsJWYVXua5fvOKBakDMPPW3KAWOqdTFrOP5FtzdMJugjKY2Vf5m2kqjqKNjcOYTSEyM43wkfgpxnjNScSId5rq5w?key=1AefdsQCaYLGYQiRhr0xJw
        
    3. Categorias / Faixas de IMC:
        1. < 18,5 Baixo peso
        2. 18,5 a 24,9 Peso adequado
        3. 25,0 a 29,9 Excesso de peso
        4. >= 30,0 Obesidade
        5. Não informado - quando não houver o peso e/ou altura

7. Identificar agravos relacionados a internações por condições sensíveis à atenção primária a partir de códigos CID10 e CIAP2 relacionados a:
8. Retinopatia diabética
(CID 10) H36.0/ (CIAP2) F83
9. Doença renal
(CID 10) I12, I12.9, I13, I13.0, I13.1, I13.2, I13.9, N08. 3, N17.9, N18, N18.0, N18.8, N18.9, N19 / (CIAP2) U14, U99, U88, U90
10. Doença coronariana 
(CID10) I24 , I24.8, I24.9, I25, I25.1, I25.8, I25.9, I51.8, I51.9, I11.0, I11.9, I13.0, I13.2, I50, I50.0, I50.9/
11. Doença cerebrovascular 
(CID10) G46, G46.8, I67, I67.8, I67.9, I68, I68.8, I69, I69.9/
12. Neuropatia 
(CID10) G57, G57.8, G57.9, G58, G59.0, G59.8, G61, G62.8, G62.9, G63, G63.2, G63.3/
13. Doença arterial oclusiva periférica 
(CID10) I73, I73.8, I73.9


## Tabelas 
tb_acomp_cidadaos_vinculados

tb_fat_atendimento_individual

tb_fat_familia_terriotrio

tb_fat_cidadao_pec

tb_fat_cad_domiciliar

tb_dim_tempo

tb_dim_cbo


## Variáveis
co_seq_fat_atd_ind
co_dim_tempo
nu_cns
nu_peso
nu_altura
co_dim_unidade_saude
co_dim_faixa_etaria
co_dim_sexo
co_dim_local_atendimento
co_fat_cidadao_pec
nu_cpf_cidadao
codigo
tipo
co_dim_cbo_1
no_cidadao
co_dim_tipo_localizacao
co_dim_tempo_nascimento
cbo
dt_registro
