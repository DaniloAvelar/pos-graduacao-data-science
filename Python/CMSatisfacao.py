import pandas as pd
import plotly.express as px
from datetime import datetime

# Simulando a chegada de comentários em tempo real
dados_reais = [
    {"usuario": "@joao", "comentario": "Fui contemplado! Magalu é top!", "sentimento": 1.0, "categoria": "Contemplação"},
    {"usuario": "@maria", "comentario": "Taxa de administração muito alta.", "sentimento": -0.5, "categoria": "Taxas"},
    {"usuario": "@jose", "comentario": "Como faço pra dar um lance?", "sentimento": 0.0, "categoria": "Dúvidas"},
    {"usuario": "@ana", "comentario": "Demora demais o atendimento no zap.", "sentimento": -0.8, "categoria": "Atendimento"}
]

df = pd.DataFrame(dados_reais)

# No Plotly, você usaria um gráfico de barras para medir o 'termômetro'
fig = px.bar(df, x='categoria', y='sentimento', color='categoria',
             title="Termômetro de Sentimento Consórcio Magalu (Tempo Real)",
             color_discrete_map={'Contemplação': 'green', 'Atendimento': 'red', 'Taxas': 'orange', 'Dúvidas': 'blue'})

fig.show()