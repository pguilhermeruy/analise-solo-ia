# 🌱 AgriTech AI - Análise de Solo Inteligente & Data Pipeline
🔗 **Acesse o Projeto Online:** [Clique aqui para testar](https://solo-ia-guilhermeruy.streamlit.app/)

Um sistema Full-Stack de Dados desenvolvido para auxiliar agrônomos na tomada de decisão, integrando Inteligência Artificial com persistência de dados e Business Intelligence.

## Objetivo
O sistema vai além da predição simples, atuando em três frentes:
1. **Classificar (IA):** Identificar se o solo é **Fértil** ou **Deficiente** com base em Nitrogênio, Potássio e Umidade.
2. **Registrar (SQL):** Armazenar automaticamente cada análise realizada em um banco de dados relacional para histórico.
3. **Analisar (BI):** Fornecer massa de dados estruturada para dashboards de performance no Power BI.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Streamlit:** Interface web interativa para input de dados.
- **Scikit-Learn:** Algoritmo de Regressão Logística para o motor de decisão.
- **SQLite3:** Banco de dados SQL embutido para persistência do histórico (Back-end).
- **Pandas:** Manipulação de DataFrames e exportação de relatórios.
- **Power BI:** Conectado via exportação CSV para visualização de KPIs e dispersão de dados.

## Como Funciona
1. **Treinamento:** O modelo aprende padrões de equilíbrio nutricional com um dataset sintético inicial.
2. **Predição:** O usuário insere os níveis de nutrientes na interface.
3. **Persistência:** O sistema classifica a amostra e **salva o resultado automaticamente** no banco de dados `agritech.db`.
4. **Exportação:** Um botão dedicado permite extrair todo o histórico acumulado para CSV, pronto para análise no Power BI/Excel.

## Como Executar Localmente
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Execute a aplicação:
   ```bash
   streamlit run agricola.py

## 📊 Prints do Dashboard
**Monitoramento de KPIs e Análise de Dispersão**



<img width="317" height="317" alt="dashboard-kpi" src="https://github.com/user-attachments/assets/4416ce4f-c571-43ed-99a6-ac6dbc01963f" /> 
<img width="317" height="317" alt="dashboard-dispersao" src="https://github.com/user-attachments/assets/6d454177-96b8-49c3-927d-178c8568e7e3" />

