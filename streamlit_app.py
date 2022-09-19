from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import joblib
import os
from sklearn.preprocessing import RobustScaler, StandardScaler, MinMaxScaler

bairros = ['Abranches', 'Água Verde' ,'Ahú' ,'Alto Boqueirão' ,'Alto da Glória' ,'Alto da XV' ,'Alto da Rua XV' ,'Atuba' ,'Augusta' ,'Bacacheri' ,'Bairro Alto' ,'Barigui' ,'Barreirinha' ,'Batel' ,'Bigorrilho' ,'Boa Vista' ,'Bom Retiro' ,'Boqueirão' ,'Butiatuvinha' ,'Cabral' ,'Cachoeira' ,'Cajuru' ,'Campina do Siqueira' ,'Campo Comprido' ,'Campo de Santana' ,'Capão da Imbuia' ,'Capão Raso' ,'Cascatinha' ,'Centro' ,'Centro Histórico' ,'Caximba' ,'Centro Cívico' ,'Champagnat' ,'Cidade Industrial' ,'Cristo Rei' ,'Ecoville' ,'Fanny' ,'Fazendinha' ,'Ganchinho' ,'Guabirotuba' ,'Guaíra' ,'Hauer' ,'Hugo Lange' ,'Jardim Botânico' ,'Jardim Social' ,'Jardim das Américas' ,'Juvevê' ,'Lamenha Pequena' ,'Lindoia' ,'Mercês' ,'Mossunguê' ,'Novo Mundo' ,'Orleans' ,'Parolin' ,'Pilarzinho' ,'Pinheirinho' ,'Portão' ,'Prado Velho' ,'Rebouças' ,'Riviera' ,'Santa Cândida' ,'Santa Felicidade' ,'Santa Quitéria' ,'Santo Inácio' ,'São Braz' ,'São Francisco' ,'São João' ,'São Lourenço' ,'São Miguel' ,'Seminário' ,'Sítio Cercado' ,'Taboão' ,'Tarumã' ,'Tatuquara' ,'Tingui' ,'Uberaba' ,'Umbará' ,'Vila Izabel' ,'Vista Alegre' ,'Xaxim' ,'Neoville']

path1 = os.access("KNN.mod", os.F_OK)
print("Exists the path:", path1)

with open("KNN.mod", 'rb') as fo:  
    knn = joblib.load(fo)
with open("scaler_knn.mod", 'rb') as fo:  
    scaler_knn = joblib.load(fo)
with open("scaler_preco_knn.mod", 'rb') as fo:  
    scaler_preco_knn = joblib.load(fo)

"""
# Calculadora de Imóveis em Curitiba

O valor aproximado é obtido a partir do treinamento de modelos de machine learning com dados de imóveis obtidos a partir de scraping da internet.

Os algoritmos são experimentais, não garantindo nenhuma precisão do resultado.
"""

col1, col2 = st.columns(2)

with col1:
   """
   ### Dados
   """
   area = st.number_input('Área Construida (m²)')
   banheiros = st.number_input('Banheiros', step=1)
   quartos = st.number_input('Quartos', step=1)
   vagas = st.number_input('Vagas', step=1)
   bairro = st.selectbox('Bairro',bairros)
   botao = st.button('Calcular')

with col2:
   """
   ### Resultado
   """
   
   if botao:
      """
      
      
      """
      b = index(bairro)
      st.write('**KNN**:')
      valores = scaler_knn.transform([[area, quartos, garagens, vagas, b]])
      casa = knn.predict(valores)
      st.write("Preço estimado {m}: R$".format(m="KNN"), scaler_preco_knn.inverse_transform(casa.reshape(-1,1))[0][0])

