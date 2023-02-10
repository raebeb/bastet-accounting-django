![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
# Bastet Accounting Backend 💲📊💸

![a_minimalist_logo_for_a_software_development_company_cal_24c7dd5b-1999-43ce-b65a-52e872362794](https://user-images.githubusercontent.com/27713965/218191766-5f1b570c-dad7-4fba-8b7d-ad96fdde6c8c.png)

Aplicacion web con el objetivo de facilitar las labores realizadas por contadores auditores


## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

-   Docker 19.03^
-   Docker Compose 1.25^
***
---

## Instalación 🔧

### 1. Clonar el repositorio
```
https://github.com/raebeb/bastet-accounting-django.git
```
ó
```
git@github.com:raebeb/bastet-accounting-django.git
```
---

### 2. Levantar el contenedor
```
docker-compose up
```
> Si es primera vez que se levanta el proyecto, este se _buildeara_ e instalara todas las dependencias necesarias

Si en la terminal aparece un mensaje como el siguiente, el proyecto se ha levantado con éxito
```
Container bastet-accounting-django-db-1  Running
Container bastet-accounting-django-web-1  Created
Attaching to bastet-accounting-django-web-1
bastet-accounting-django-web-1  | Watching for file changes with StatReloader
bastet-accounting-django-web-1  | Performing system checks...
bastet-accounting-django-web-1  | 
bastet-accounting-django-web-1  | System check identified no issues (0 silenced).
bastet-accounting-django-web-1  | February 10, 2023 - 19:05:29
bastet-accounting-django-web-1  | Django version 4.1.4, using settings 'bastet.settings'
bastet-accounting-django-web-1  | Starting development server at http://0.0.0.0:8000/
bastet-accounting-django-web-1  | Quit the server with CONTROL-C.

```
> La primera vez que se levanta el proyecto es posible que falle, ya que se levanta web antes que db, si esto ocurre es necesario detener el contenedor con ```Ctrl + C``` y volver a levantarlo con ```docker-compose up```

---

***
## Ejecutando las pruebas ⚙
_El proyecto cuenta con una serie de tests, para ejecutarlos el primer paso es tener contenedor levantado, luego seguir con los siguientes pasos_

1.  Ejecutar el siguiente comando en una terminal diferente:
	```
	docker-compose exec web sh -c "python manage.py test"
	```
   > En este paso se llevara a cabo la ejecución de los test unitarios desarrollados, al finalizar se visualizara un mensaje como el siguiente, indicando que todas las pruebas se ejecutaron con éxito
 ```
Ran 14 tests in 518.023s

OK
Destroying test database for alias 'default'...
 ```
2. Para verificar la covertura de codigo testeado es necesario seguir los siguientes pasos

2.1 Ejecutar el siguiente comando
  	```
    docker-compose exec web sh -c "coverage run manage.py test"
    ```
> Este comando ejecutara los test y actualizara el conocimiento de ellos a la libreria coverage

2.2 Luego, ejecutar el siguiente comando
  ```
  docker-compose exec web sh -c "coverage report -m"
  ```
Este comando mostrara un mensaje como el siguiente (siempre y cuando no existan problemas con los tests)
```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
my_program.py                20      4    80%   33-35, 39
my_other_module.py           56      6    89%   17-23
-------------------------------------------------------
TOTAL                        76     10    87%
```


Tambien es posible ver la covertura de los test en una pagina web estatica, para esto debemos ejecutar el punto 2.1 y luego el siguiente comando
  ```
  docker-compose exec web sh -c "coverage html"
  ```
Este comando creara en nuestro proyecto un directorio llamado ```coverage_html_reports```

  ![image](https://user-images.githubusercontent.com/27713965/218193093-8caff1c2-c4cc-4190-a615-1e6ef369486a.png)
  
_dentro de esta estara el archivo index.html el cual podremos ver en cualquier navegador_
![image](https://user-images.githubusercontent.com/27713965/218193349-92047cd9-5eb4-45c0-99d4-c89afaa528f1.png)

  
***
## Construido con 🛠️
* [Python 3.11](https://www.python.org) - Lenguaje de programación
* [Django 4.1](https://www.djangoproject.com) - Framework web utilizado
* [PostgreSQL 14.4](https://www.postgresql.org) - Gestor de base de datos
* [Docker](https://www.docker.com) - Gestor de contenedores

***


## Autores ✒️
* [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) - Trabajo inicial
* [Larva](https://github.com/javix70)


***
## ⌨️ con ❤️ por [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) & [Larva](https://github.com/javix70)👩‍💻

```
          ／＞　 フ
         | 　_　_| 
       ／` ミ＿xノ 
      /　　　　 |
     /　 ヽ　　 ﾉ
    │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_  ヽ_)__)
＼二)
```

