def filter_by_sexo(cnes: int = None, equipe: int = None):
    where_clause = ""
    if cnes is not None:
        where_clause += f"""            where 
               e.codigo_unidade_saude = {cnes}
        """
        if equipe and equipe is not None:
            where_clause += f"  and e.codigo_equipe = {equipe} "

    return f"""
        with cidadaos as (
            select
                distinct p.sexo, p.cidadao_pec
            from
                pessoas p
            join equipes e on e.cidadao_pec = p.cidadao_pec
            {where_clause}
        )
        select 
            lower(sexo),
            count(*) total 
        from cidadaos
        group by 1
    """
