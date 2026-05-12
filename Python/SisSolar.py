import plotly.express as px
import pandas as pd

# 1. Carregar os dados
df = pd.read_csv('dados_sistema_solar.csv')

# 2. Criar um gráfico interativo
fig = px.scatter(df,
                 x="Distancia_Sol_UA",
                 y="Periodo_Orbital_Anos_Terra",
                 size="Diametro_Equatorial_km",
                 color="Tipo",
                 hover_name="Corpo_Celeste",
                 log_x=False,
                 size_max=60,
                 title="Relação: Distância vs. Período Orbital no Sistema Solar")

# 3. Exibir
fig.show()