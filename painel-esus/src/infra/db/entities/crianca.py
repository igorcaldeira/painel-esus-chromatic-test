# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from src.infra.db.entities.pessoas import Pessoas
from src.infra.db.settings.base import Base


class Crianca(Base):
    __tablename__ = "crianca"
    index = Column(Integer, primary_key=True, autoincrement=True)
    cidadao_pec = Column(Integer, ForeignKey("pessoas.cidadao_pec"))
    pessoa: Mapped[Pessoas] = relationship("Pessoas", uselist=False, lazy="subquery")
    
    atendimentos_medicos = Column(Integer) 
    data_ultimo_atendimento_medicos = Column(Date) 
    indicador_atendimentos_medicos = Column(Integer)
    medicoes_peso_altura = Column(Integer)
    data_ultima_medicao_peso_altura = Column(Date) 
    indicador_medicoes_peso_altura = Column(Integer)
    registros_creatinina = Column(Integer) 
    data_ultimo_registro_creatinina = Column(Date) 
    indicador_registros_creatinina = Column(Integer)
    vacinas_influenza = Column(Integer) 
    data_ultima_vacina_influenza = Column(Date)  
    indicador_vacinas_influenza = Column(Integer)
    atendimentos_odontologicos = Column(Integer) 
    data_ultimo_atendimento_odontologico = Column(Date) 
    indicador_atendimento_odontologico = Column(Integer)
    visitas_domiciliares_acs = Column(Integer) 
    data_ultima_visita_domiciliar_acs = Column(Date)  
    indicador_visitas_domiciliares_acs = Column(Integer)
