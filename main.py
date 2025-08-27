from src.extract import buscar_todos_dados_commodities
from src.load import salvar_no_postgres

commodities = ['CL=F','GC=F','SI=F']
if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados,schema='public')