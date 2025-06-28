import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


#creamos una instancia de esta aplicación FastAPI
# Esta es la aplicación FastAPI que se encargará de manejar las peticiones HTTP

app= FastAPI()

#agregamos una sintaxis que es un decorador, donde agregamos una ruta a nuestra aplicación
# Este decorador indica que la función `get_list` se ejecutará cuando se haga una petición GET a la ruta raíz "/"

@app.get("/")

#creemos nuestro primer recurso, una función que retorna una lista (de números por ejemplo)

def get_list():
    return [1,2,3]

# podemos crear otro recurso, una función que retorna un mensaje del nombre (información de la empresa)

@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola soy una pagina web</h1>
    <p>Esta es una página de contacto</p>
    <p>Mi nombre es Tienda de Ropa</p>
    """





def run():
    store.get_categories()  # Llamamos a la función para obtener las categorías

if __name__ == "__main__":
    run()  # Ejecutamos la función principal al iniciar el script