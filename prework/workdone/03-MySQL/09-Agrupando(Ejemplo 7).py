# -*- coding: utf-8 -*-
# Agrupando(Ejemplo 7).py  



import sys
print(sys.version[:100])                # version del sistema (actual 3.7.2)
from sqlalchemy import create_engine    # conexion mysql  
import pandas as pd                     # dataframe
pd.set_option('display.max_rows', 50)   # numero de filas y columnas que se muestran
pd.set_option('display.max_columns', 9)



motor=create_engine('mysql+mysqlconnector://admin:password@localhost:3306/Apps')   # motor de enlace

cnx=motor.raw_connection()     # conexion

datos=pd.read_sql("""SELECT price
                     FROM Ratings 
                     GROUP BY price
                     ORDER BY price ASC""", cnx)                      # selecciona datos desde mysql

print ('Datos leidos desde MySQL.')

print (datos)
