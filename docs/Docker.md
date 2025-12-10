 índice 
 - [Ejecución de contenedores Docker](#ejecución-de-contenedores-docker)
 - [Imágenes en Docker](#imágenes-en-docker)
 - [Almacenamiento en Docker](#almacenamiento-en-docker)

# Inicializamos variables 
```bash
Hernandez_Pulido_Juan_Carlos=Aquí_Pones_Hernandez_Pulido_Juan_Carlos
Tu_mail_docker=Aqui_Pones_Tu_mail_github
Tu_usuario_docker=Aquí_Pones_Tu_usuario_github
```

# Añadir Registry local (Solo en modalidad presencial) 

Añadimos un registro local docker para mejorar tiempo de descarga de imágenes.

1. Creamos un archivo en nuestro equipo:
`/etc/docker/daemon.json`
```json
{
    "insecure-registries":[
        "10.0.21.6:5000"
    ]
}
```

2. Reiniciamos demonio y docker:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

Para usar la imagen local en vez de nombre de la imagen, utilizaremos 10.0.21.6:5000/nombreImagen...

P.e: para ubuntu/apache2 ponemos: 10.0.21.6:5000/ubuntu/apache2.


 # Ejecución de contenedores Docker
**Diapositiva 20**
---

1. Instalamos docker
    ```bash
    sudo apt update
    sudo apt install -y docker.io
    # instalamos también docker-cli 
    sudo apt install docker-cli
    docker
    # Nos debe de mostrar la versión de docker instalada
    sudo usermod -aG docker $USER
    systemctl restart docker.socket
    systemctl restart docker.service
    ```
    Verificar instalación

    ```bash
    docker version
    # comprobamos si está instalado docker compose V2
    docker compose version
    ```
    ```bash
    docker info
    ```

    **Diapositiva 23**
    ---

1. Ver ayuda de docker
    ```bash
    man docker run
    ```
    
    ```bash
    docker image --help
    ```

    **Diapositiva 24**
    ---

1. Docker run
    ```bash
    docker run ubuntu echo 'Hello world' 
    ```

    **Diapositiva 25**
    ---

1. Contenedor hello World

    ```bash
    docker run hello-world
    ```

    **Diapositiva 27**
    ---

1.  Docker ps

    ```bash
    docker ps
    ```
    Vemos toda la información que nos muestra de los contenedores

    ```bash
    docker ps -a
    ```

    **Diapositiva 28**
    ---

1. Docker images

    ```bash
    docker images
    ```

    ```bash
    docker image ls
    ```

    **Diapositiva 29**
    ---

1. Opciones ejecución 

    ```bash
    docker run --name miHello --rm hello-world
    ```

    ```bash
    # vemos que no aparece por que se ha borrado
    docker ps -a 

    ```


    **Diapositiva 30**
    ---

1. Contenedor interactivo

    ```bash
    docker run -it --name contenedor2 -h cont1 ubuntu bash 
    ```
    Abrimos otro terminal

    ```bash
    # Vemos como está corriendo el contenedor
    docker ps 
    ```

    **Diapositiva 31**
    ---

1. Docker attach, seguimos en el otro terminal
    ```bash
    docker attach contenedor2
    ```

    vemos el hostname del contenedor

    ```bash
    hostname
    # Realizamos las operaciones que queramos
    ls -l
    ```
    
    Salimos del contenedor
    ```bash
    exit
    ```
    
    Vemos como al salir del contenedor se ha detenido y también hemos salido del contenedor en la pestaña que dejamos abierta.

    ```bash
    docker ps
    ```

    Volvemos a lanzar el contenedor

    ```bash
    docker run -it --name contenedor2 -h cont1 ubuntu bash 
    ```
    Nos va a dar un error indicándonos que el contenedor ya existe, y no podemos crear otro con el mismo nombre

    **Diapositiva 32**
    ---

1. Lanzamos un nuevo contenedor ubuntu
    ```bash
    docker run -it --name contenedor3 -h cont3 ubuntu bash 
    ```

    Abrimos de nuevo otra pestaña para poder ejecutar comandos en el  contenedor

    
1. Realizamos cualquier comando que queramos
    ```bash
    docker exec contenedor3 ls 
    ```
    Podemos realizar también cualquier operación sobre bash, por ejemplo creando un bucle. Finalizamos ejecuación con ctrl + c

    ```bash
    docker exec contenedor3 /bin/bash -c "while true; do echo 'hello world'; sleep 1; done" 
    ```
    Vemos que entra en un bucle... para parar con ctrl + c

    ```bash
    docker ps
    ```

    Vemos que ahora cuando hemos salido el contenedor no se ha parado, ya que lo hemos ejecutado con docker exec.
    
    **Diapositiva 33**
    ---

1. Eliminamos 
    ```bash
    # vemos contenedores en ejecución
    docker ps
    # y contenedores incluso parados
    docker ps -a
    ```
    Desde la consola que tenemos con nuestro usuario (no la del contenedor)

    ```bash
    docker rm contenedor2
    docker rm contenedor3
    #nos dará error ya que está en ejecución o sea que podemos forzar
    docker rm -f contenedor3
    ```

    **Diapositiva 34**
    ---

1. Contenedores demonio

    Creamos un contenedor nginx

    ```bash
    docker run -d --name  MiServidorWeb -p 8080:80 nginx
    ```
    Accedemos a nuestra página web <http://localhost:8080>

   


    **modificamos el contenido de nuestra página web**.   
    Tenemos diferentes formas de hacerlo
:
    1. Accediendo a la máquina
         ```bash
        docker exec -it MiServidorWeb /bin/bash
        ```
        Y dentro de MiServidorWeb

        ```bash
        cd /usr/share/nginx/html
        # y modificamos en archivo index.html 
        apt update
        apt install nano
        nano /usr/share/nginx/html/index.html
        ```
        Cuando terminamos, salimos del contenedor. con exit
        Refrescamos el navegador y comprobamos que ha cambiado la página web.

    1. Machacando el index con uno nuestro
       ```bash
        docker exec MiServidorWeb /bin/bash -c "mv /usr/share/nginx/html/index.html /usr/share/nginx/html/index.html.save"
        docker exec MiServidorWeb /bin/bash -c "echo '<h1> Este es mi servidor web </h1>' > /usr/share/nginx/html/index.html"
        ```

   **Diapositiva 35**

   **Docker cp**
   ---

    1. Docker cp, Creo un index en mi directorio y lo copio con `docker cp`

        ```bash
        echo  "<h1> Este es mi servidor usando docker cp </h1>" > index.html

        docker cp index.html MiServidorWeb:/usr/share/nginx/html/index.html
        ```

    Vamos a copiar en el otro sentido, archivos de contenedora nuestro directorio:
    ```bash
    docker cp MiServidorWeb:/usr/share/nginx/html/50x.html
    ls 
    cat 50x.html   
    ```

   **Diapositiva 36**
    ---
1. Docker logs
    ```bash
    docker logs MiServidorWeb
    ```
    si queremos quedarnos escuchando los logs
    ```bash
    docker logs -f MiServidorWeb

    ```

    **Diapositiva 37**
    ---

1. Borramos la máquina de nginx y la volvemos a crear de nuevo !!!! **Explicar persistencia de datos**!!!!
    ```bash
    docker rm -f MiServidorWeb
    docker run -d --name  MiServidorWeb -h nginxdocker  -e USUARIO=PPS -p 8080:80 --hostname ServidorNginx nginx

    ```
    Comprobamos el nombre de las variables y hostname
    ```bash
    docker exec MiServidorWeb /bin/bash -c "hostname; echo \$USUARIO"
    ```

    **Diapositiva 38**
    ---

1. paramos nuestro servidor web

    ```bash
    docker stop MiServidorWeb
    # vemos su estado
    docker ps
    ```

    **Diapositiva 39**
    ---
1. 
    ```bash
     docker start MiServidorWeb
    # vemos su estado
    docker ps
    ```

    **Diapositiva 40**
    ---

1. Docker pause
    ```bash
     docker pause MiServidorWeb
    # vemos su estado
    docker ps
    ```

    ```bash
    # vemos como no podemos conectarnos a ella
    docker exec -it MiServidorWeb /bin/bash
    ```

1. Docker unpause
    ```bash
     docker unpause MiServidorWeb
    # vemos su estado
    docker ps
    # y ahora sí nos conectamos
    docker exec -it MiServidorWeb /bin/bash
    ```

    **Diapositiva 41**

1. Docker inspect
    ```bash
    docker inspect MiServidorWeb
    ``` 
    Salimos del contenedor con `exit`.

# Imágenes en Docker

**Diapositiva 46**
---

1. Etiquetas imágenes

    <https://hub.docker.com/_/nginx>

    **Diapositiva 50**
    ---

1. Docker pull

    ```bash
    docker pull nginx:1.28.0-alpine-otel
    # comprobamos las imágenes
    docker image ls
    # vemos detalles de la imagen
    docker inspect nginx:1.28.0-alpine-otel
    ```
    Para ver información de imagenes vamos a levantar máquina
    ```bash
    docker run -d -p 8080:80 --name miNginx nginx:1.28.0-alpine-otel
    ```
    Vemos que nos da error, ocupado el puerto 8080.

    ```bash
    docker rm -f MiServidorWeb
    docker rm -f miNginx
    #volvemos a lanzar ejecución
    docker run -d -p 8080:80 --name miNginx nginx:1.28.0-alpine-otel
    ```
    Podríamos también haber usado otro puerto si tuviéramos ocupado el 8080. Por ejemplo: -p 8081:80 
    Entramos en máquina para ver
    ```bash
    docker exec -it miNginx /bin/sh
    # hacemos un inspect para ver la imagen
    docker inspect nginx:1.28.0-alpine-otel

    ```

    y hacemos un ls y mostramos contendio de docker-entrypoint.sh
    ```bash
    ls
    cat docker-entrypoint.sh
    
    ls -l /usr/sbin/nginx
    ```

    No salimos del contenedor, desde otro terminal 

    **Diapositiva 51**
    ---

1. Docker search

    ```bash
    docker search fog
    ```

    **Diapositiva 52**
    ---
1. docker rmi

    ```bash
    # vemos las imágenes que tenemos en registry local
    docker images
    ``` 
    y ahora borramos la imagen de 
    ```bash
    docker rmi nginx:1.28.0-alpine-otel
    docker image ls
    ```
    No nos deja porque la estamos usando para nginx

    ```bash
    # forzamos el borrado
    docker rmi -f nginx:1.28.0-alpine-otel
    docker images
    ```

# Almacenamiento en Docker
1. Operaciones con volumenes

    **Diapositiva 59**  
    ---
    
    ```bash
    docker volume create miVolumen
    docker volume ls 
    docker volume inspect miVolumen
    ```

    ```bash
    docker volume rm miVolumen
    docker volume rm -f miVolumen
    ```

1. vamos a volver a crear nuestro servidor web, pero antes eliminamos los contenedores que tenemos parados
    ```bash
    docker ps -a
    docker rm -f MiServidorWeb
    docker rm -f miNginx
    docker run -d --name  MiServidorWeb -e USUARIO=PPS -p 8080:80 --hostname ServidorNginx nginx
    # si nos da error, ya sabemos que tenemos que eliminarla.
    
    ```

    ir a <http://localhost:8080> y vemos como volvemos a tener la página por defecto. Aquí vemos el problema que los contenedores son efímeros y el problema de la persistencia de datos.

   
    **Diapositiva 60 y 61**
    ---
1. Operaciones con volúmenes
     Creamos de nuevo mi contenedor pero con volúmen docker
    ```bash
     echo "<h1> Bienvenidos a mi pagina web de PPS </h1>" > index.html
     docker rm -f MiServidorWeb
     docker run -d --name  MiServidorWeb  -e USUARIO=PPS -p 8080:80 --hostname ServidorNginx  -v MiVolumen:/usr/share/nginx/html nginx
     # copiamos el index.html
     docker cp index.html MiServidorWeb:/usr/share/nginx/html/index.html
    ```

     Comprobamos que está en la máquina
     ir a <http://localhost:8080>, debe de mostrarse nuestro index personalizado.

    ```bash
    docker exec MiServidorWeb cat /usr/share/nginx/html/index.html
    ```
    Por otra parte en mi máquina anfitriona
    ```bash
    # vemos la información de los volúmenes
    docker volume ls 
    docker volume inspect MiVolumen
    sudo ls /var/lib/docker/volumes/MiVolumen/_data
    sudo nano /var/lib/docker/volumes/MiVolumen/_data/index.html
    #hacemos alguna modificación en el index.html y comprobamos que se ha modificado
    ```
    Para comprobar la persistencia, eliminamos el contenedor y volvemos a crear con el mismo vólumen:

    ```bash
    docker rm -f MiServidorWeb
     docker run -d --name  MiServidorWeb -h nginxdocker  -e USUARIO=PPS -p 8080:80 --hostname ServidorNginx  -v MiVolumen:/usr/share/nginx/html nginx
    ```

    Refrescamos y vemos como en esta ocasión se han mantenido los datos entre dos ejecuciones.

    ```bash
    # eliminamods máquina y volumen
    docker rm -f MiServidorWeb
    docker volume rm MiVolumen
    ```
   **diapositiva 62**
    ---

1. Volumenes Bind-Mount 
   
    ```bash
    #copiamos archivos y cambiamos de directorio para ver bind-mount
    mkdir MiServidorWeb
    cp index.html MiServidorWeb/
    cp 50x.html MiServidorWeb/

    ```

 
    ```bash
    docker rm -f MiServidorWeb
    docker run -d --name  MiServidorWeb -h nginxdocker  -e USUARIO=PPS -p 8080:80 --hostname ServidorNginx  -v ./MiServidorWeb:/usr/share/nginx/html nginx
    ```
    Comprobamos que está en la máquina
    ir a <http://localhost:8080>, debe de mostrarse nuestro index personalizado.
1. Comprobamos y eliminamos los contenedores y volúmenes que tengamos creados:

    ```bash
    docker ps -a
    docker volume ls
    ```

# Redes en docker  


   **Diapositiva 64**
   ---

1. Tipos de redes 
    ```bash
    docker network ls
    ```

    **Diapositiva 67**
    ----

1. Creamos una red brige personalizada y creamos dos contenedores que la utilizan.
    ```bash
    docker network create --subnet 192.168.0.0/24 --gateway 192.168.0.100 red2
    docker run -it  --name contenedor1 --network red2  --ip 192.168.0.10    --hostname servidor1  ubuntu
    ```
    en otro terminal
    ```bash
    docker run -it --name contenedor2 --network red2  --ip 192.168.0.20 --hostname servidor2  ubuntu
    ```
    En otra pestaña vemos máquinas creadas y los detalles de la red

    ```bash
    docker ps 
    docker inspect red2
    ```
    En las dos máquinas

    ```bash
    apt update
    apt install iproute2 dnsutils iputils-ping

    ```
1. Vamos a crear otro contenedor pero no lo vamos a colocar en la RED2, sino esté estará en la red de docker por defecto.
    
    ```bash
    docker run -it --name contenedor3 --hostname servidor3  ubuntu
    ```
    
    Entrando en cada una de las máquinas vemos como resuelve tanto por el nombre de la máquina como por el hostname
    ```bash
    dig contenedor1 
    dig contenedor2 
    dig servidor1 
    dig servidor2
    # pero contenedor3 no resuelve.
    dig contenedor3
    ```
1. Eliminamos lo creado

    ```bash
    docker network rm -f red2
    docker rm -f contenedor1
    docker rm -f contenedor2
    docker rm -f contenedor3

    ```
# Escenarios multicontenedor

1. Vamos descargando las imagenes:
    ```bash
    docker pull  postgres:11.6-alpine
    docker pull nabo.codimd.dev/hackmdio/hackmd:2.6.0
    ```

1. Creamos una carpeta con nombre CodiMD y entramos en ella

    ```bash
    mkdir CodiMD
    cd CodiMD
    ```

    **Diapositiva 75**  
    ---

1. Analizando docker-compose.yml

    `dockercompose.yml`
    ```bash
    services:
        database:
            image: postgres:11.6-alpine
            environment:
            - POSTGRES_USER=codimd
            - POSTGRES_PASSWORD=change_password
            - POSTGRES_DB=codimd
            volumes:
            - "database-data:/var/lib/postgresql/data"
            restart: always

        codimd:
            image: nabo.codimd.dev/hackmdio/hackmd:2.6.0
            environment:
            - CMD_DB_URL=postgres://codimd:change_password@database/codimd
            - CMD_USECDN=false
            depends_on:
            - database
            ports:
            - "3000:3000"
            volumes:
            - upload-data:/home/hackmd/app/public/uploads
            restart: always
    volumes:
        database-data: {}
        upload-data: {}

    ```
**Diapositiva 76**
---

1. Levantar escenario
    ```bash
    docker compose up 
    ```
    Accedemos al servicio CodiMD <http://localhost:3000>

    Nos registramos, creamos un usuario y vemos como vemos información en los logs.
    Con Ctrl + X finalizamos el contenedor.

    ```bash
    Eliminamos el escenario y volvemos a crear en modo demonio
    docker compose -v 
    docker compose up -d
    ```
    **Diapositiva 77**

1. vemos información de escenario y de servicios.
    ```bash
    docker compose ls
    ```
    ```bash
    docker compose ps 
    ```
    Podemos tambien ver información de los contenedores con comandos docker
    ```bash
    docker inspect codimd-codimd-1 
    ```

    **Diapositiva 78**
    ---

1. Parando y arrancando
    ```bash
    docker compose stop
    docker ls
    docker ls -a
    ```
    Comprobamos si tenemos acceso a máquina refrescando navegador

    ```bash
    docker compose up -d
    docker compose ls
    ```
    **Diapositiva 79**
    ---
    

1. Pausando y despausando
    ```bash
    docker compose pause
    docker compose ls
    docker ps -a
    ```
    Comprobamos si tenemos acceso a máquina refrescando navegador

    ```bash
    docker compose unpause
    docker compose ls
    ```
    **Diapositiva 80**
    ---
1. Viendo los logs
    ```bash
    docker compose logs

    ```
    También podemos ver los de las máquinas
    ```bash
    docker compose logs codimd 
    ```
     ```bash
    docker compose logs database 
    ```
    **Diapositiva 81**
    ---   
1. docker compose top

    ```bash
    docker compose top
    ```
    **Diapositiva 81**
    ---   
1.    Más comandos de docker compose

    ```bash
    docker compose --help
    man docker compose <comando>
    ```
    **Diapositiva 81**
    ---   
1. Docker compose rm y down
    ```bash
    docker compose rm

    ```
    Nos da error ya que están arrancados


    ```bash
    docker compose down
    # vemos como todavía está el volumen
    docker volume ls 
    ```  
    ```bash
    docker compose down -v
    # nos elimina los volúmenes y las redes
    docker volume ls 
    ```
# Creación de imágenes con Docker
    **Diapositiva 86**
1. Entramos en <hub.docker.com>
    
    - Nos logeamos con nuestra cuenta de `educarex` o `iesvalledeljerte`.
    - Nos pedirá que cómo queremos que se llame nuestro usuario `$Tu_usuario_docker`

1. Creamos un token para poder hacer operaciones desde terminal en la cuenta de `hub.docker.com`
    - Seleccionamos nuestro usuario -> Account settings -> Personal access tokens
    - Creamos un nuevo token con permisos de lectura, escritura y borrado.
    - Lo guardamos por que no podremos volver a recuperar.

1. En terminal

    ```bash
    docker login -u $Tu_usuario_docker 
    ```
    Nos pide contraseña, le pegamos el `token` y nos muestra `Login Succeeded`.

   **Diapositiva 88**
    ---   
1.  Creamos imagen personalizada
    ```bash
    docker run --name miUbuntu -it ubuntu

    ```
    Instalamos dnsutils, nano e iproute2 dentro del contenedor

    ```bash
    apt update
    apt install dnsutils iproute2 nano
    ```
    Guardamos la imagen personalizada
    ```bash
    docker commit miUbuntu $Tu_usuario_docker/miubuntu:V1
    docker images
    docker rm -f miUbuntu
    ```

1. Utilizamos nuestra imagen personalizada:
    ```bash
    docker run -it --name ubuntuPersonalizado $Tu_usuario_docker/miubuntu:V1
    ```
    Dentro comprobamos que tiene instalado los paquetes que instalamos en nuestra imagen

    ```bash
    dpkg -l dnsutils iproute2
    ```

    **Diapositiva 93**
    ---   

1. Vamos a crear un servidor web desde un debian 
    ```bash
    mkdir miServidorWWW
    cd miServidorWWW
    nano Dockerfile
    ```
2. Creamos un index personalizado.
    ```bash
    echo "<h1>Este es mi apache construido desde un debian</h1>"
    ```
3. Creamos nuestro fichero Dockerfile

    `miServidorWWW/Dockerfile`
    ```Dockerfile
    FROM debian:stable-slim
    RUN apt-get update  && apt-get install -y  apache2 
    WORKDIR /var/www/html
    COPY index.html .
    CMD apache2ctl -D FOREGROUND

    ```  
    Y construimos la imagen desde `docker build`

    ```bash
    docker build -t $Tu_usuario_docker/miservidorwww:V1 .
    # y comprobamos que se ha generado
    docker image ls
    ```
4. Podemos crear ya contenedores a partir de ella:

    ```bash
    docker run -d --name midebianweb -p 8080:80 $Tu_usuario_docker/miservidorwww:V1
    ```
5. Vamos al navegador a comprobar <http://localhost:8080>

    **Diapositiva 95**
    ---   
1. Generamos un archivo .tar con la imagen    
    ```bash
    docker save $Tu_usuario_docker/miservidorwww:V1 > miservidorwww.tar
    ```
1. Comprobamos añadiendo la imagen al respositorio después de borrarla
    ```bash
    docker rmi -f $Tu_usuario_docker/miservidorwww:V1 
    docker image ls
    docker load -i miservidorwww.tar
    docker image ls

    ```  
    **Diapositiva 96**
    ---   
1.    Subimos la imagen a nuestro servidor

    ```bash
    docker push $Tu_usuario_docker/miservidorwww:V1 
    ```
2. Comprobamos en <http://hub.docker.com> que se ha subido correctamente.

[![Licencia: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
