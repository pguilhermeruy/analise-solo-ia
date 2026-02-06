# 🌱 AgriTech AI - Análise de Solo Inteligente

Um sistema de Machine Learning desenvolvido para auxiliar agrônomos e produtores na tomada de decisão sobre a viabilidade do solo para plantio.

## Objetivo
Classificar automaticamente se uma amostra de solo é **Fértil** ou **Deficiente** com base em três parâmetros fundamentais:
- Nível de Nitrogênio
- Nível de Potássio
- Percentual de Umidade

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Streamlit:** Para construção da interface web interativa.
- **Scikit-Learn:** Para implementação do algoritmo de Regressão Logística.
- **Pandas:** Para manipulação e estruturação do dataset sintético.

## Como Funciona
O modelo foi treinado com um dataset sintético que simula diferentes condições de solo. Ele aprendeu padrões de equilíbrio nutricional (ex: alto nitrogênio sem umidade resulta em solo impróprio) e aplica essa lógica para novas amostras inseridas pelo usuário.

## Como Executar Localmente
1. Clone o repositório.
2. Instale as dependências:
   ```bash
3. Execute a aplicação:
   ```bash
   streamlit run agricola.md
