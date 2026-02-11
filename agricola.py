import streamlit as st
import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="AgriTech", page_icon="🌱")
st.title("I.A. para medição de qualidade de solo") 
st.write("Sistema de Inteligência Artificial para análise de viabilidade de plantio baseado em níveis de nutrientes.")

def init_db():
    conn = sqlite3.connect('agritech.db') 
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            nitrogenio INTEGER,
            potassio INTEGER,
            umidade INTEGER,
            resultado TEXT
        )
    ''')
    conn.commit() 
    conn.close()  
init_db()

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
        resultado_texto = "Aprovado"
        st.success("✅ Solo ótimo para Plantio.")
    else:
        resultado_texto = "Reprovado"
        st.error("❌ Solo necessita mais atenção.")
        
    conn = sqlite3.connect('agritech.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO historico (nitrogenio, potassio, umidade, resultado) VALUES (?, ?, ?, ?)", 
              (input_nitrogenio, input_potassio, input_umidade, resultado_texto))
    
    conn.commit()
    conn.close()  
    
    st.toast("Dados salvos no Banco de Dados com sucesso!")
    
    st.write("---")
    st.write("👀 O que o SQL está enxergando:")
    conn = sqlite3.connect('agritech.db')
    df_banco = pd.read_sql_query("SELECT * FROM historico", conn)
    st.dataframe(df_banco.tail(5)) 
    conn.close()

@st.cache_data
def converter_para_csv(df):
    return df.to_csv(index=False).encode('utf-8')


conn = sqlite3.connect('agritech.db')
df_completo = pd.read_sql_query("SELECT * FROM historico", conn)
conn.close()

if not df_completo.empty:
    st.write("---")
    st.subheader("📊 Business Intelligence")
    st.write("Baixe os dados históricos para analisar no Power BI ou Excel:")
    
    csv = converter_para_csv(df_completo)
    
    st.download_button(
        label="📥 Baixar Base de Dados (CSV)",
        data=csv,
        file_name='dados_agritech.csv',
        mime='text/csv',
    )
