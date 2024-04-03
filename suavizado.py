import pandas as pd 
import matplotlib.pyplot as plt


# Defining the columns to read
usecols = ["date","value"]

# Read the CSV file
medicion = pd.read_csv("C:/Users/pc53/Downloads/archivo_ejc2.csv", index_col="date", usecols=usecols)
medicion = pd.read_csv("C:/Users/pc53/Downloads/archivo_ejc2.csv")


# grafica
x_horas = medicion['date']
y_dBA  = medicion['value']
plt.plot(x_horas,y_dBA)
plt.title('Mediciòn')
plt.grid()
plt.show()


suavizado = y_dBA.rolling(4000).mean()

# grafica
plt.plot(x_horas,suavizado)
plt.title('Mediciòn con suavizado')
plt.grid()
plt.show()
