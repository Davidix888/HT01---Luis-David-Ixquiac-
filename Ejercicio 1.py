import re
import pandas as pd
from PyPDF2 import PdfReader
import os

rutaArchivo = 'Analisis Anual 2018 ETAS.pdf'
document = PdfReader(rutaArchivo)
pagina = document.pages[4]
texto = pagina.extract_text()
print(texto)

patron = r'\n(\d+)\s+(\d+)\s+(.+?(?:\n.+?)?)\s{2,}(.+?)\s{2,}(-|.+?)\s+(\d+)'


datos = re.findall(patron, texto)
print(datos)

etas = pd.DataFrame(datos, columns=['No', 'SE', 'AreaSalud', 'ETA', 'Fuente', 'Casos'])

print(etas)





