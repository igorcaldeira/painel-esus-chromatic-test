def filter_by_localidade(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
               e.codigo_unidade_saude = {cnes}
        """
        if equipe and equipe is not None:
            where_clause += f"  and e.codigo_equipe = {equipe} "

    return f"""WITH cidadaos as (
select
    distinct p.*,
    case 
        when LOWER(tipo_localidade) is null then 'nao_definido'
        when LOWER(tipo_localidade) = 'zona rural' then 'rural'
        when LOWER(tipo_localidade) is not null  and LOWER(tipo_localidade) != 'zona rural' then 'urbano'
    end tipo    
from
    pessoas p
join equipes e on e.cidadao_pec = p.cidadao_pec
{where_clause}
)
select tipo, count(*) total  from cidadaos group by 1;"""
