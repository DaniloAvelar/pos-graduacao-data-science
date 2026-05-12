import plotly.express as px
import pandas as pd

# Exemplo de dados consolidados
df_satisfacao = pd.DataFrame({
    "Status": ["Promotores", "Neutros", "Detratores"],
    "Quantidade": [450, 200, 150]
})

fig = px.pie(df_satisfacao, values='Quantidade', names='Status',
             color='Status',
             color_discrete_map={'Promotores':'green', 'Neutros':'yellow', 'Detratores':'red'},
             hole=.4, title="Nível de Satisfação da Rede Social")
fig.show()