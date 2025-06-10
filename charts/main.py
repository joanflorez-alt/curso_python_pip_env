#importamos charts 

import charts

#creamos una función run como la principal que va a llamar a función creada en charts

def run():
    charts.generate_pie_chart()
    
# como queremos que funcione como un script

if __name__ == "__main__":
    run()

