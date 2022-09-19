from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

bairros = ['Abranches', 'Água Verde' ,'Ahú' ,'Alto Boqueirão' ,'Alto da Glória' ,'Alto da XV' ,'Alto da Rua XV' ,'Atuba' ,'Augusta' ,'Bacacheri' ,'Bairro Alto' ,'Barigui' ,'Barreirinha' ,'Batel' ,'Bigorrilho' ,'Boa Vista' ,'Bom Retiro' ,'Boqueirão' ,'Butiatuvinha' ,'Cabral' ,'Cachoeira' ,'Cajuru' ,'Campina do Siqueira' ,'Campo Comprido' ,'Campo de Santana' ,'Capão da Imbuia' ,'Capão Raso' ,'Cascatinha' ,'Centro' ,'Centro Histórico' ,'Caximba' ,'Centro Cívico' ,'Champagnat' ,'Cidade Industrial' ,'Cristo Rei' ,'Ecoville' ,'Fanny' ,'Fazendinha' ,'Ganchinho' ,'Guabirotuba' ,'Guaíra' ,'Hauer' ,'Hugo Lange' ,'Jardim Botânico' ,'Jardim Social' ,'Jardim das Américas' ,'Juvevê' ,'Lamenha Pequena' ,'Lindoia' ,'Mercês' ,'Mossunguê' ,'Novo Mundo' ,'Orleans' ,'Parolin' ,'Pilarzinho' ,'Pinheirinho' ,'Portão' ,'Prado Velho' ,'Rebouças' ,'Riviera' ,'Santa Cândida' ,'Santa Felicidade' ,'Santa Quitéria' ,'Santo Inácio' ,'São Braz' ,'São Francisco' ,'São João' ,'São Lourenço' ,'São Miguel' ,'Seminário' ,'Sítio Cercado' ,'Taboão' ,'Tarumã' ,'Tatuquara' ,'Tingui' ,'Uberaba' ,'Umbará' ,'Vila Izabel' ,'Vista Alegre' ,'Xaxim' ,'Neoville']

"""
# Calculadora de Imóveis em Curitiba

O valor aproximado é obtido a partir do treinamento de modelos de machine learning com dados de imóveis obtidos a partir de scraping da internet.

Os algoritmos são experimentais, não garantindo nenhuma precisão do resultado.

### Dados
"""

col1, col2 = st.columns(2)

with col1:
   area = st.number_input('Área Construida (m²)')
   banheiros = st.number_input('Banheiros', step=1)

with col2:
   quartos = st.number_input('Quartos', step=1)
   vagas = st.number_input('Vagas', step=1)



bairro = st.selectbox('Bairro',bairros)
    
    
