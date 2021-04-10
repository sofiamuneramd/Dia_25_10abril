# Importamos la libreria pandas y por facilidad la abreviamos como pd

import pandas as pd

# Leer el archivo de excel subido

File=pd.ExcelFile('Libro1.xls')

# Se leer el contendio de la Hoja1

hoja1=File.parse('Hoja1')
print(hoja1)
print(hoja1.columns)
nombres=hoja1['Nombre'].values
print(nombres)


from pandas import ExcelWriter

df=pd.DataFrame({'Nombre':nombres})
df=df[['Nombre']]
writer=ExcelWriter('copia1.xls')
df.to_excel(writer,'Hoja Copia',index=False)
writer.save()