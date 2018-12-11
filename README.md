# project-codewars-linkedin-IH
Proyecto final del bootcamp de ironhack en Data Analytics

Sistema de recomendación para recruiters obteniendo datos de webs como codewars y github. 

## Fase 1: Obtención de usuarios de forma iterativa

1. Haciendo web scrapping de la página de los top 500 en Codewars obtenemos sus usuarios y los incluimos en la lista de usuarios de codewars. 
2. Haciendo web scrapping de cada usuario de la lista obtenemos sus contactos sociales (following, followers, allies)
3. Añadimos estos nuevos contactos a muestra lista de usuarios de codewars. 
4. Repetimos paso 2 y 3 hasta obtener un número de registros de +5000. 

## Fase 2: Obtención de datos de usuario

### 2.1 API codewars
Sobre cada uno de los usuarios de la lista hacemos una petición a la API (https://dev.codewars.com/):  
```$curl "https://www.codewars.com/api/v1/users/some_user"```
Y obtenemos un json de la forma: 
```
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





