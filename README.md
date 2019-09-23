# project-codewars-linkedin-IH
Proyecto final del bootcamp de ironhack en Data Analytics

Sistema de recomendación para recruiters obteniendo datos de webs como codewars y github. 

## Fase 1-2-3: Obtención de datos de usuarios de Codewers

1. A partir de una primera semilla que son el top 500 (leaderboard) en Codewars obtenemos sus sus contactos sociales (following, followers, allies)
2. Añadimos estos nuevos contactos a muestro conjunto de usuarios de codewars. 
3. Repetimos este procedimiento hasta alcanzar los 20000 usuarios. 

Ejecutamos la siguiente linea de comandos: 
```console
$ python3 sourcepy/data-adquisition.py
```
Cada 100 usuarios se persisten los datos. 

## Fase 4: Limpieza de los datos

Un pipeline para limpiar los datos. 

Ejecutamos la siguiente linea de comandos: 
```console
$ python3 sourcepy/data-cleaning.py
```

## Fase 5: Análisis de datos. ML - > TO DO

Un pipeline para analizar los datos y reportar resultados

Ejecutamos la siguiente linea de comandos: 
```console
$ python3 sourcepy/data-analysis.py
```

## Fase 6: Representación de datos. BI -> TO DO

Un pipeline para representar los datos y persistirlos en imágenes o similar. 

Ejecutamos la siguiente linea de comandos: 
```console
$ python3 sourcepy/data-representation.py
```

## Fase 7: Sistema de Recomendación -> TO DO

Un pipeline para representar los datos y persistirlos en imágenes o similar. 

Ejecutamos la siguiente linea de comandos: 
```console
$ python3 sourcepy/recomender-system.py -l "python, java, c"
```


### 2.1 API codewars
Sobre cada uno de los usuarios de la lista hacemos una petición a la API (https://dev.codewars.com/):
```$curl "https://www.codewars.com/api/v1/users/some_user"```
Y obtenemos un json de la forma: 
```python
{
    "username": "some_user",
    "name": "Some Person",
    "honor": 544,
    "clan": "some clan",
    "leaderboardPosition": 134,
    "skills": [
        "ruby",
        "c#",
        ".net",
        "javascript",
        "coffeescript",
        "nodejs",
        "rails"
    ],
    "ranks": {
        "overall": {
            "rank": -3,
            "name": "3 kyu",
            "color": "blue",
            "score": 2116
        },
        "languages": {
            "javascript": {
                "rank": -3,
                "name": "3 kyu",
                "color": "blue",
                "score": 1819
            },
            "ruby": {
                "rank": -4,
                "name": "4 kyu",
                "color": "blue",
                "score": 1005
            },
            "coffeescript": {
                "rank": -4,
                "name": "4 kyu",
                "color": "blue",
                "score": 870
            }
        }
    },
    "codeChallenges": {
        "totalAuthored": 3,
        "totalCompleted": 230
    }
}
```
De estos datos obtenemos sus skills y sus niveles en cada lenguaje. 
### 2.2 Web Scrapping codewars
Sobre cada uno de los usuarios de la lista hacemos un web scrapping y obtenemos: 
1. Member Since:Oct 2018
2. Enlace de Github (si lo tiene)
3. Enlace de LinkedIn (si lo tiene)

NOTA: Se puede obtener para: 
* GitHub
* Facebook
* Tweeter
* LinkedIn
* StackOverflow


### 2.3 Creación de DataFrame
Hemos creado una función **get_row** cuya función es generar un diccionario a partir de un nombre de usuario haciendo uso de las funciones de las fases 2.1 y 2.2. 
```
def get_row(user): 
    ''' 
    Crea un diccionario con los datos recopilados que se puede
    añadir como fila en nuestro dataframe de pandas
    '''
    user_json = get_user_api(user)
    res = get_all_stats(user)
    res.update(get_scores(user_json))
    return res
```
Luego iteraremos por todo nuestro poll de usuarios obtenidos en la Fase 1 y crearemos un dataframe que guardaremos en un fichero CSV.

Tiempos: 

### Tiempos: 

Iter	users	timeit(ms) social	timeit(ms) rows	
1	500	3847.40
2	3939	7642800.01		9796075.92
3	11520	11027477.05		28818747.81


## Fase 3: Persistencia de datos

Guardamos nuestro DataFrame en un archivo en la carpeta **output**: 
```
df_users.to_csv('../output/df-codewars-2929x221.csv')
df = pd.read_csv('../output/df-codewars-2929x221.csv')
```

## Fase 4: Limpieza de datos

En esta fase limpiamos columnas innecesarias. Nos encontramos con más de 200 de las que queremos guardar los scores en cada lenguaje y unos pocos datos de identificación de usuarios. Columnas finales: 
* Las correspondientes a los lenguajes
* allies, clan, comments, followers, following, highest trained, honor, kumite, last seen, leaderboard position, member since, total completed kata, total languages trained, username, github, skills, linkedin, 

### 4.X Columna a columna

Vamos limpiando columna a columna

### 4.12 Guardamos los datos
```
df.to_csv('../output/dataframe-limpio3939x56.csv')
``` 

## Fase 5: Análisis de datos

En esta fase analizaremos los datos con las herramientas conocidas y provaremos diferentes sistemas de ML para clasificar. 

### 5.1 Correlación | Heatmap

### 5.2 D3

### 5.3 Unsupervised Learning

### Mejoras y seguiento

https://github.com/Mihlos/api-heroku
poner __init__.py en todas las carpetas con código para que se puedan comunicar las partes

