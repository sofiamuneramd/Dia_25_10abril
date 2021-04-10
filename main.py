# Importamos la libreria pandas y por facilidad la abreviamos como pd

import pandas as pd

# Leer el archivo de excel subido

File=pd.ExcelFile('Libro1.xls')

# Se lee el contendio de la Hoja1

hoja1=File.parse('Hoja1')

# Vemos que si funciona con print(hoja1)

# Ahora imprimimos las columnas con print(hoja1.columns)

# Vamos a establecer una variable que contenga los valores de la columna Nombre y apellido

nombres=hoja1['Nombre'].values
apellido=hoja1['Apellido'].values

# Vemos que se almacena en una lista con print(nombres)

# Importamos ExcelWriter para crear una hoja nueva y escribir en ella

from pandas import ExcelWriter

# Creamos con Dateframe el nombre de las columnas de nuestra hoja de calculo (Nombre, Primer Apellido, Segundo Apellido) 

# Tambien se introduce la lista de datos de cada columna, algunas importadas de Libro1 otras se introducen directamente

copia1=pd.DataFrame({ 'Nombre' : nombres, 'Primer Apellido' : apellido, 'Segundo Apellido' : ['Medina', 'Montoya', 'Peña' ]})

# Introduciomos la siguiente linea para que las columnas queden en un orden especifico

copia1=copia1[['Nombre','Primer Apellido','Segundo Apellido']]

# Ahora creamos y guardamos el archivo. Index=False es para evitar que se cree una columna adicional con numeracion

archivo=ExcelWriter('copia1.xls')
copia1.to_excel(archivo,'Hoja Copia',index=False)
archivo.save()



