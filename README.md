# 🔍 AI-Query Crew

CrewAI Logo  
*Sistema inteligente para geração de consultas SQL otimizadas através de linguagem natural*

## 🌟 Recursos Principais
- **🤖 Agente Especializado em SQL**  
  Interpretação de linguagem natural e geração de consultas SQL otimizadas
- **🎲 Suporte a Múltiplos Bancos**  
  Compatibilidade com PostgreSQL, MySQL e SQLite
- **📊 Visualização de Dados**  
  Exibição dos resultados em formato tabular e gráficos interativos
- **🔄 Integração Perfeita**  
  Conexão direta com bancos de dados para execução das consultas geradas
- **📝 Interface Amigável**  
  Interação simplificada via Streamlit para usuários sem conhecimento técnico
- **📤 Exportação de Resultados**  
  Visualização e análise dos dados obtidos de forma interativa

## 🏗️ Arquitetura do Sistema

### 👥 Componentes Principais
| Componente            | Função Principal                          | Tecnologias         |
|-----------------------|-------------------------------------------|---------------------|
| SQL Query Crew        | Geração de consultas SQL otimizadas       | CrewAI, LLM         |
| Database Connection   | Conexão com diferentes bancos de dados    | psycopg2            |
| Schema Generator      | Extração e formatação de esquemas         | YAML                |
| Query Executor        | Execução e recuperação de resultados      | SQL                 |
| Data Visualizer       | Visualização interativa dos dados         | Streamlit, Pandas   |

### 📋 Fluxo de Trabalho
```mermaid
graph TD
    A[Input do Usuário] --> B{SQL Query Crew}
    B --> C[Geração da Consulta SQL]
    C --> D[Execução no Banco]
    D --> E[Processamento dos Resultados]
    E --> F[Visualização dos Dados]
    F --> G[Exibição de Gráficos]
```

## 🛠️ Estrutura do Projeto

```
ai-query-crew/
├── postgres-teste/
│   ├── README.md
│   ├── clinica.sql                # Script SQL para banco clínica
│   ├── crew_query.py              # Core da geração de consultas
│   ├── crew_query_streamlit.py    # Interface Streamlit
│   ├── crew_query_test.py         # Testes de funcionalidade
│   ├── ecommerce.sql              # Script SQL para banco ecommerce
│   ├── postgres_connection.py     # Conexão com PostgreSQL
│   ├── postgres_databases.py      # Gerenciamento de bancos
│   ├── pyproject.toml             # Configuração do projeto
│   ├── schema_generator.py        # Gerador de esquemas YAML
│   ├── test_conn.py               # Teste de conexão
│   └── schemas/                   # Esquemas dos bancos
│       ├── schema_clinica.yaml
│       └── schema_ecommerce.yaml
└── schemas/
    ├── schema_clinica.yaml        # Esquema do banco clínica
    └── schema_ecommerce.yaml      # Esquema do banco ecommerce
```

## 📋 Pré-requisitos
- Python 3.12+
- PostgreSQL
- CrewAI 0.102.0+
- psycopg2 2.9.10+
- Streamlit 1.42.2+
- pandas 2.2.3+
- python-dotenv 1.0.1+

## 🚀 Começando

1. Clone o repositório:
```bash
git clone https://github.com/matheus896/ai-query-crew.git
```

2. Configure o ambiente virtual:
```bash
cd ai-query-crew/postgres-teste
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -e .
```

4. Configure as variáveis de ambiente no arquivo `.env`:
```env
DATABASE_URI=postgresql://usuario:senha@localhost:5432
```

## 🖥️ Como Usar (Interface Web)

1. Inicie o servidor Streamlit:
```bash
streamlit run crew_query_streamlit.py
```

2. Na interface:
   - Selecione o tipo de banco de dados
   - Escolha o banco específico (ecommerce, clinica)
   - Digite sua solicitação em linguagem natural
   - Marque a opção para visualizar em gráfico (opcional)
   - Clique em "Executar Consulta"

3. Visualize os resultados:
   - Consulta SQL gerada
   - Dados em formato tabular
   - Gráficos interativos (quando aplicável)

## 🔧 Configuração Avançada

### Adicionando Novos Bancos de Dados
Edite `postgres_databases.py` para:
- Registrar novos bancos de dados
- Configurar strings de conexão
- Definir aliases para acesso rápido

### Gerando Esquemas YAML
Use o `schema_generator.py` para:
```bash
python schema_generator.py
```
- Extrair automaticamente a estrutura do banco
- Definir colunas categóricas para análise
- Gerar arquivos YAML de esquema

## 🤝 Contribuindo
1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença
Distribuído sob licença MIT. Veja `LICENSE` para detalhes.

## 🙏 Reconhecimentos
- [CrewAI](https://crewai.com) - Framework de agentes
- [Streamlit](https://streamlit.io) - Interface web
- [PostgreSQL](https://www.postgresql.org/) - Sistema de banco de dados
- [Pandas](https://pandas.pydata.org/) - Análise de dados

---
