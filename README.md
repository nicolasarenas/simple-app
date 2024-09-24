# simple-app

Simple App for testing connectivity between servers

## Descripción

`simple-app` es una aplicación sencilla diseñada para probar la conectividad entre servidores. Utiliza Flask para exponer una API que reenvía solicitudes a un servidor remoto y devuelve las respuestas en formato JSON.

## Requisitos

- Python 3.x
- Flask
- Requests

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/simple-app.git
    cd simple-app
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

La aplicación está dividida en dos servicios, un servicio de frontend y un servicio de backend. 


### Frontend 

El servidor de frontend responde 3 endpoints

* / html 
* /app/v1/local --> que devuelve el siguiente json {'answer': 'hello world from front'}
* /app/v1/remote --> que manda una petición a un servidor remoto en el endpoint /api/v1/remote

Por defecto el servidor escucha en http://127.0.0.1:5001, pero este comportamiento puede ser modificado mediante las variables APP_SERVER y APP_PORT
El servidor remoto al que se manda la petición por defecto es http://127.0.0.1:5002, este comportamiento puede ser modificado mediante las variables de entorno REMOTE_SERVER y REMOTE_PORT 

### Backend 

El servidor de backend responde a 2 endpoints 

* / html 
* /api/v1/remote --> Que devuelve el siguiente json {'answer': 'hello world from remote'} 
  
Por defecto el servidor escucha en http://127.0.0.1:5002, pero este comportamiento puede ser modificado mediante las variables APP_SERVER y APP_PORT


## Uso

Para iniciar los servidores se ejecuta:

### frontend

```shell
cd front 
python fron.py 
```

Si se quiere usar gunicorn para lanzar la app se puede ejecutar desde la raiz del proyecto

```shell
cd front
gunicorn -c gunicorn_config.py front:app
```

### backend

```shell
cd back 
python back.py 
```

Si se quiere usar gunicorn para lanzar la app se puede ejecutar desde la raiz del proyecto

```shell
cd front
gunicorn -c gunicorn_config.py back:app
```

Para comprobar si la app funciona por ejemplo:

```shell 
curl -X GET http://127.0.0.1:5001/api/v1/remote                  ✔  07:39:23 PM  
{
  "answer": "hello world from remote"
}

curl -X GET http://127.0.0.1:5001/api/v1/local                   ✔  07:39:28 PM  
{
  "answer": "hello world from front"
}
```
