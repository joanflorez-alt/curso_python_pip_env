import utils
import read_csv
import charts
import pandas as pd

def run():
  
  """
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  """
  
  # generamos el siguient gráfico: charts.generate_pie_chart(countries, percentages) con pandas
  # df= dataframe
  df = pd.read_csv("data.csv")  #aplicamos el metodo de lectura y el nombre del archivo y no ahorramos el algoritmo de read_csv.py
  
  # la linea de filtrar por continente: data = list(filter(lambda item : item['Continent'] == 'South America',data))
  #la podemos hacer con pandas
  df = df[df['Continent'] == 'Africa']
  countries = df['Country'].values  #obtenemos los paises
  percentages = df['World Population Percentage'].values #obtenemos los porcentajes
  charts.generate_pie_chart(countries, percentages)  #generamos el gráfico de pastel
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country"], labels, values)


if __name__ == '__main__':
  run()