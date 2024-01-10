# %%
import pandas as pd
from ydata_profiling import ProfileReport

ruta_archivo_origen = 'dataset.csv'

df = pd.DataFrame(pd.read_csv(ruta_archivo_origen))

reporte = ProfileReport(df,title="Reporte segunda parte")

reporte.to_file('reporte.html')



