import requests    #importamos el modulo requests

def get_categories():
    r= requests.get('https://api.escuelajs.co/api/v1/categories') #hacemos una peticion get a la url, aqui obtenemos la información
    print(r.status_code) #imprimimos el codigo de estado de la peticion
    print(r.text) #imprimimos el texto de la respuesta
    print(type(r.text)) #imprimimos el tipo de dato del texto de la respuesta
    
#para obtener información especifica de la respuesta, podemos usar el metodo json() de la respuesta
    categories = r.json()
    for category in categories:
        print(category["name"]) #imprimimos el nombre de cada categoria