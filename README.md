# Proyecto Final - Nelson Gabriel Quispe

Proyecto final para el curso de Python en Coderhouse. Es una aplicación web Django que permite a los usuarios realizar ordenes de produtos y a los usuarios con permisos gestionar los mismos. Se aplico los conceptos de herencia de plantillas, formularios, vistas basadas en unciones y clases, autenticación y autorización.

---
## Instalación y ejecución

Sigue estos pasos para instalar el proyecto en tu máquina local:

- Clone este repositorio en su máquina local usando el comando `git clone https://github.com/NeQuispe/proyecto-final.git`.

- Si usa Visual Studio Code, abra el archivo `requirements.txt` y haga clic en Crear ambiente, luego elegir Venv y el intérprete Python, y finalmente pregunta por las dependencias: elegimos `requirements.txt`. Esto creara el entorno virtual e instalará todas las librerías necesarias para ejecutar el proyecto.

- Si prefiere instalarlo de manera manual, use el comando `python -m venv .venv`. Esto creará una carpeta llamada `.venv` dentro del directorio del proyecto.
Active el entorno virtual usando el comando `source .venv/bin/activate` en Linux o Mac, o `.venv\Scripts\activate` en Windows.
Instale las dependencias del proyecto usando el comando `pip install -r requirements.txt`. 

- Ejecute las migraciones de la base de datos usando los comandos `python manage.py makemigrations` y `python manage.py migrate`. Esto creará las tablas necesarias en la base de datos.

- Para ejecutar el servidor de desarrollo, muévase hasta el directorio del proyecto usando el comando `cd project` y use el comando `python manage.py runserver`. Esto iniciará el servidor en el puerto 8000 de su máquina local. Abre tu navegador y navega a `http://localhost:8000` para ver la aplicación en acción.

- Si quiere detener el servidor, simplemente presione `CTRL + C` en la consola donde está ejecutándose.

---
## Funcionalidades
- Registro y inicio de sesión de usuario
- Personalización del modelo de usuario de Django usando relación uno a uno
- Operaciones CRUD de Productos y Ordenes
- Permisos para controlar el acceso a las vistas
- Validaciones en el modelo Order

---
## Uso

Para utilizar la aplicación, primero crea una cuenta haciendo clic en el enlace "Registrarse" en la página de inicio. Una vez que tengas una cuenta, puedes iniciar sesión y comenzar a realizar Ordenes de productos.

Para poder crear, modificar y eliminar productos, es necesario contar con un superusuario o con un usuario con permiso para hacerlo.
Para crear un superusuario, utiliza el comando `python manage.py createsuperuser`. Una vez creado el superusuario, puedes iniciar sesión con estas credenciales y acceder al panel de administración de Django para gestionar los modelos y los permisos de los usuarios

---
## Video demostracion

https://youtu.be/19HHJd_iX9Y/
---
