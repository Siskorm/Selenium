from asyncio.windows_events import NULL

import json
import time
import pandas as pd
#from objPlantilla import ObjElement
#from objPlantilla import ObjPlantilla
from Cselenium1 import CSelenium
#from classpandas import Classpanda
#from classmatplotlib import ClassMatplotlib

path_file = r'Plantilla.json'
#mt = ClassMatplotlib()
#pa = Classpanda()
sl = CSelenium()

plantilla = ObjPlantilla().GetObjects(path_file)
print(plantilla[0])
books =[]
count = 0


for obj in plantilla:
    print(obj.navegator)
    drive = sl.navegador(obj.navegator)
    sl.ventana(drive,obj.url)
    time.sleep(10)
    for element in obj.acciones:
        if element.accion != "leer_tala":
            sl.FindByAndAction(element.type, element.selector, element.accion, element.valor)
            continue




        print("Creando Dataframe")
        df = sl.ReadTable(element.type_th,element.selector_th, element.type_tb, element.selector_tb)
        print(count)
        books = pa.new_csv(df,count)
        count += 1
        print("LISTO \n")



    drive.close()
    print("GRAFICANDO...")
    mt.set_graph(books,obj.readTable.chart)
    print("FIN.")
    pass


class actividad1():
    def __init__(self):
        pass