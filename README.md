# Veterinary-Api-Ui
#Instrucciones
Una vez descargado el zip del repositorio, procederemos a configurar y abrir la APi en nuestro computador:

Instrucciones para correr la API:

1- Verificar que se tiene instalado docker. En caso de no tenerlo favor de descargarlo siguiendo el enlace: https://www.docker.com y añadir el volumen de Mariadb.

2- Prender el docker.

3- Accederemos al dashboard de docker y nos dirigiremos a la sección de ajustes > resources > file sharing. En donde agregaremos los permisos para que nuestro docker pueda utilizar la carpeta que acabamos de descargar. PAra esto simplemente se hará clic en el "+" y se buscará la ruta donde se encuentra nuestra carpeta y le damos en listo.

4- Abrir la terminal y acceder a la dirección donde se encuentra la carpeta descargada o también llamada "HTMLClase". En esa misma carpeta nos moveremos a la sección de  "Veterinary_Api", que es donde se encuentra nuestra API.

5- Una vez estando en esa ruta, procederemos a escribir en la terminal el comando "docker-compose up -d". Esto con el fin de que se cree nuetsro contenedor en nuetsro docker local.

6- Realizaremos los pasos 3 -5 para la carpeta de "db" la cual contiene los datos de nuetsra base de datos en un contenedor en docker.

7- Abrimos los archivos en nuestro IDE favorito para poder visualizar el código.

8- Seguido de esto, procederemos a escribir  el comando "docker-compose up " en ambos archivos (db y Veterinary_API)

9- Una vez creados nuestros contenedores, procederemos a configurar nuestro gestor de base de datos. Para esto, procederemos a abrir nuestro gestor favorito e introduciremos los datos que se encuentran en el archivo "docker-file" que se encuentra en la carpeta de "db" que es la que contiene los datos para poder vindularnos. Una vez agregados los datos, probaremos al conexión y se debe visualizar las tablas de la base de datos ( pet, servicios, owner, etc.)

10- Seguido de esto, procederemos a escribir  el comando "docker-compose up " para poder correr el programa.

11- Una vez lista la configuración solo es necesario acceder a tu navegador favorito e ir a "localhost:8000" . Para poder visualizar las rutas de la api favor de leer el Rest full Api reference.

12- Para poder acceder a nuestra interfaz de la api, primero se levantará el contenedor como se hizo anteriormente, siguiendo los pasos del 3- 5.

13- Una vez instalado el contenedor, procederemos a ir a nuestro navegador y escribir la dirección de localhost:8001. La cual nos va a dirigir a la página principal de la interfaz.

14- Dentro de la interfaz el usuario podrá editar, eliminar y agregar una mascota nueva.
