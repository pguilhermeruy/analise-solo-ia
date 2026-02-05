import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="AgriTech", page_icon="🌱")
st.title("I.A. para medição de qualidade de solo") 
st.write("Sistema de Inteligência Artificial para análise de viabilidade de plantio baseado em níveis de nutrientes.")


dados_solo = {
    'Nitrogênio': [85, 20, 90, 0, 22, 67, 90, 100, 3, 30, 100, 0, 50],
    'Potássio' : [70, 15, 80, 1, 49, 33, 87, 99, 9, 56, 0, 100, 0],
    'Umidade': [60, 10, 65, 56, 23, 77, 40, 8, 10, 30, 10, 5, 100],
    'Status': [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0] #1 = Um bom solo - 0 = um solo ruim
}
df = pd.DataFrame(dados_solo)


#DATAFRAME
x = df[['Nitrogênio', 'Potássio', 'Umidade']]
y = df['Status']


#TREINAMENTO DA IA
modelo = LogisticRegression()
modelo.fit(x, y)


#INTERFACE VIA STREAMLIT
input_nitrogenio = st.sidebar.slider("Nível de Nitrogênio", 0, 100, 50)
input_potassio = st.sidebar.slider("Nível de Potássio", 0, 100, 50)
input_umidade = st.sidebar.slider("Nível de Umidade", 0, 100, 50)

if st.button("Analisar Solo"):
    predicao = modelo.predict([[input_nitrogenio, input_potassio, input_umidade]])
    
    if predicao[0] == 1:
        st.success("Solo ótimo para Plantio.")
    else:
        st.error("Solo necessita mais atenção.")