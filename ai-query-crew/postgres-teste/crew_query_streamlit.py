import streamlit as st
import os
import pandas as pd
from crew_query import SQLQueryCrew
from postgres_connection import PostgresConnection  # Certifique-se de que está importando a conexão corretamente
from postgres_databases import PostgresDatabases

# Configuração do caminho do schema
root = os.path.dirname(os.path.abspath(__file__))

# Instanciando o agente de consulta SQL
sql_crew = SQLQueryCrew()

# Configuração da interface do Streamlit
st.title("🔍 AI-Query")

# Entrada do usuário
st.sidebar.header("Configuração da Consulta")

# Seleção do tipo de banco de dados
database_type = st.sidebar.selectbox("Tipo de Banco de Dados", ["Postgres", "MySQL", "SQLite"], index=0)

# Seleção do nome do banco de dados
database_name = st.sidebar.selectbox("Nome do Banco", ["ecommerce", "clinica"], index=0)

# Atualiza o caminho do schema conforme o banco selecionado
schema_path = os.path.join(root, "schemas",f"schema_{database_name}.yaml")

# Área de texto para que o usuário insira a consulta
user_request = st.text_area("Digite sua solicitação:", 
                            "")

# Checkbox para exibir gráfico
exibir_grafico = st.checkbox("📊 Exibir resultados em gráfico")

# Botão para executar a consulta
if st.button("Executar Consulta"):
    if not user_request.strip():
        st.warning("⚠️ A solicitação não pode estar vazia. Por favor, insira um comando.")
    else:
        inputs = {
            "database_type": database_type,
            "database_name": database_name,
            "yaml_path": schema_path,
            "user_request": user_request,
            "json_output": False
        }

        sql_query = sql_crew.kickoff(inputs)  # O resultado vem em JSON

        # Exibir a consulta SQL gerada
        st.subheader("🔍 Consulta SQL Gerada:")


        # Verifica se há dados no resultado e converte para DataFrame
        if sql_query:
                        
            ecommerce_database = PostgresDatabases.get_database_uri(database_name)

            conn = PostgresConnection(database_uri=ecommerce_database)
            conn.connect()

            cursor = conn.cursor
            cursor.execute(sql_query)
            # Obtendo os resultados
            results = cursor.fetchall()

            colunas = conn.get_colunas()

            df = pd.DataFrame(results, columns=colunas)
                
            st.subheader("📊 Resultado da Consulta:")

            if exibir_grafico:
                # Se houver pelo menos uma coluna numérica, exibir o gráfico
                for col in df.columns:
                    try:
                        df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "."))  # Conversão explícita
                    except ValueError:
                        pass  # Se não puder converter, mantém o valor original

                
                numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
                
                if len(numeric_columns) >= 1:
                    st.bar_chart(df.set_index(df.columns[0]))  # Primeiro campo vira índice no gráfico
                else:
                    st.warning("⚠️ Os dados retornados não possuem colunas numéricas para exibir um gráfico.")
            
            st.dataframe(df)  # Exibe os dados como tabela interativa
        else:
            st.warning("⚠️ Nenhum dado encontrado para essa consulta.")
