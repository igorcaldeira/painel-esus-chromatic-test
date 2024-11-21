# pylint: disable=E0401,C0301,W0612,W0611
import os
import subprocess
from pathlib import Path

from src.data.use_cases.create_bases.create_bases_usecase import CreateBasesUseCase
from src.env import env
from src.errors.logging import logging
from src.infra.create_base.create_autorreferido_base_repository import (
    CreateAutorreferidoBaseRepository,
)
from src.infra.create_base.create_diabetes_bases_repository import (
    CreateDiabetesBasesRepository,
)
from src.infra.create_base.create_equipes_base_repository import (
    CreateEquipesBaseRepository,
)
from src.infra.create_base.create_hypertension_bases_repository import (
    CreateHypertensionBasesRepository,
)
from src.infra.create_base.create_nominal_lists_bases_repository import (
    CreateDiabetesNominalListRepository,
    CreateHypertensionNominalListRepository,
)
from src.infra.create_base.create_oral_health_bases_repository import (
    CreateOralHealthBasesRepository,
)
from src.infra.create_base.create_pessoas_base_repository import (
    CreatePessoasBaseRepository,
)
from src.infra.create_base.create_smoking_bases_repository import (
    CreateSmokingBasesRepository,
)
from src.infra.create_base.create_structure_base_repository import (
    CreateStructureBaseRepository,
)
from src.infra.create_base.create_units_base_repository import CreateUnitsBaseRepository
from src.infra.create_base.polars import (
    CreateAcompCidadaosVinculadosBaseRepository,
    CreateAtendIndivBaseRepository,
    CreateAtendOdontoBaseRepository,
    CreateCadDomiciliarBaseRepository,
    CreateCadIndividualBaseRepository,
    CreateCidacaoPecBaseRepository,
    CreateCidadaoBaseRepository,
    CreateCidCiapExplodeAtendimentosRepository,
    CreateDimEquipesBaseRepository,
    CreateDimRacaCorBaseRepository,
    CreateEquipeBaseRepository,
    CreateFamiliaTerrBaseRepository,
    CreateIndicadoresCriancasRepository,
    CreateIndicadoresEquipeRepository,
    CreateIndicadoresIdososRepository,
    CreateProcedAtendBaseRepository,
    CreateTipoEquipeBaseRepository,
    CreateUnidadesSaudeBaseRepository,
    CreateVacinacaoBaseRepository,
    CreateVisistaDomiciliarBaseRepository,
)


class CreateBasesController:

    def create_bases(self):
        if os.getenv("ENV") == "instalador":
            path = "painel_esus.db"
        else:
            path = os.getcwd()
            path = Path(path.split("/painel-esus")[0])
            path = os.path.join(path, "painel_esus.db")
            path = os.path.relpath(path)
        # os.remove(path)
        if "GENERATE_BASE" not in env or env["GENERATE_BASE"] == "True":
            logging.info("Starting structure generation")
            CreateStructureBaseRepository().create_base()
            logging.info("Starting base generation")
            _list = [
                CreatePessoasBaseRepository(),
                CreateEquipesBaseRepository(),
                # CreateDimEquipesBaseRepository(),
                CreateUnidadesSaudeBaseRepository(),
                CreateAtendIndivBaseRepository(),
                CreateAtendOdontoBaseRepository(),
                CreateCadIndividualBaseRepository(),
                CreateVacinacaoBaseRepository(),
                CreateCidacaoPecBaseRepository(),
                CreateProcedAtendBaseRepository(),
                CreateFamiliaTerrBaseRepository(),
                CreateCidadaoBaseRepository(),
                CreateCadDomiciliarBaseRepository(),
                CreateDimRacaCorBaseRepository(),
                CreateTipoEquipeBaseRepository(),
                CreateAcompCidadaosVinculadosBaseRepository(),
                CreateVisistaDomiciliarBaseRepository(),
                CreateCidCiapExplodeAtendimentosRepository(),
                CreateIndicadoresIdososRepository(),
                CreateIndicadoresCriancasRepository(),
                CreateUnitsBaseRepository(),
                CreateAutorreferidoBaseRepository(),
                CreateDiabetesBasesRepository(),
                CreateHypertensionBasesRepository(),
                CreateDiabetesNominalListRepository(),
                CreateHypertensionNominalListRepository(),
            ]
            usecase = CreateBasesUseCase(bases_generators=_list)
            usecase.create_bases()
            
            current_dir = os.path.dirname(os.path.abspath(__file__))

            script_path = os.path.abspath('parquet_db.py')
            resultado = subprocess.run(
                    ['python', script_path],
                    check=True,             # Levanta uma exceção se o comando falhar
                    stdout=subprocess.PIPE, # Captura a saída padrão
                    stderr=subprocess.PIPE, # Captura a saída de erro
                    text=True               # Retorna a saída como string
                )
            print("Script conversao de parquet realizado com sucesso:")
            print(resultado.stdout)
        else:
            logging.info("Skipping base generation")
