from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Calculadora de Imóveis em Curitiba

O valor aproximado é obtido a partir do treinamento de modelos de machine learning com dados de imóveis obtidos a partir de scraping da internet.

Os algoritmos são experimentais, não garantindo nenhuma precisão do resultado.

### Dados
"""


with st.echo(code_location='below'):
    area = st.number_input('Área Construida (m²)')
    quartos = st.number_input('Quartos', step=1)
    banheiros = st.number_input('Banheiros')
    vagas = st.number_imput('Vagas')
    
    
