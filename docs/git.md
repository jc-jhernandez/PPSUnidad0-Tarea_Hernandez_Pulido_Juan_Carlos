# Inicializamos variables 
```bash
Tu_nombre=
Tu_mail_github=Aqui_Pones_Tu_mail_github
Tu_usuario_github=Aquí_Pones_Tu_usuario_github
```



**Diapositiva 33**
---
1. Crar cuenta en Github.com

    <https://github.com>

    **Diapositiva 34**
    ---

1. Instalamos git y gh

    ```bash
    sudo apt install git gh
    ```   
    Después hay que configurar la variables de login, user, etc. con git config, lo haremos en la actividad.

    **Diapositiva 36**
    ---


1. Configuramos nuestro nombre, el email con el que has abierto tu cuenta de git y el editor preferido.
    ```bash
    git config --global user.name $Tu_usuario_github
    git config --global user.email $Tu_mail_github
    git config --global init.defaultBranch main
    git config --global core.editor nano
    ```

1. Vamos también a configurar para que cuando utilicemos  `git diff` o ``git log`se nos muestre todo el mensaje sin entrar en editor. Para ello ` ``.
    ```bash
    git config --global core.pager ""
    ```

1. Para acceder a la ayuda de git tenemos tres formas: 
    ``` bash 
    git help <verb>
    git <verb> --help
    man git<verb>
    ```

    **Diapositiva 37**
    ---


1. Configuramos claves .ssh
    ```bash
    ssh-keygen -t ed25519 -C $Tu_mail_github
    # Iniciamos el agente en segundo plano
    eval "$(ssh-agent -s)"
    #Nos mostrará un mensaje como 
    #Agent pid 59566
    ssh-add ~/.ssh/id_ed25519
    ```

    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    Y añadimos la clave generado por el siguiente comando a nuestra cuenta de github.com en apartado **Settings**/**SSH and GPG keys** y **Agregar claves .ssh**.

    > En este punto yo reiniciaría la MV, para que nos coja las claves SSH.

1. Crear un nuevo repositorio.

    <https://github.com/new>

    - Nombre:Git-Prueba
    - Añadir README.
    - Crear repositorio.


1. Vamos a Github.com y copiamos el `enlace ssh` del repositorio

    ```bash
    git clone <enlace>
    ```

     Si nos sale el mensaje:
    `The authenticity of host 'github.com (140.82.121.4)' can't be established.`
    `ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.`
    `This key is not known by any other names.`
    `Are you sure you want to continue connecting (yes/no/[fingerprint])? `

    Contestamos `yes`

    ```bash
    cd Git-Prueba
    ```   

    **Diapositiva 38 y 39**
    ---

1. Vemos contenido directorio de trabajo y repositorio

    ```bash
    ls -la
    tree -a .git
    ```   
    **Diapositiva 40**
    ---

1. Estado git: confirmado

    ```bash
    git commit -am "repositorio inicializado"
    # aquí tenemos el repositorio confirmado.
    
    ```   
   
1. Estado git: modificado

    ```bash
    nano README.md
    # escribimos en README
    git status
    ```   
   
1. Estado git: preparado

    ```bash
    git add .
    git status
    ```   
   
1. Vuelta  a estado confirmado

    ```bash
    git commit -am "creado archivo README.md"
    git status
    ```   
   
    **Diapositiva 41**   
    ---

1. Subiendo a repositorio remoto

    ```bash
    git push origin main
    
    ```   
   
    **Diapositiva 47**
    ---

1. git init lo utilizamos para inicializar un repositorio desde la línea de comandos. En esta ocasión lo hemos clonado o sea que no es necesario.
    Si lo hubiermos querido hacer así:
    - Creamos carpeta.
    - Nos colocamos en esa carpeta.
    - Creamos y añadimos el README y ...
    - Desde `gh repo create project-name --public`

    **Diapositiva 48**
    ---
1. Git Clone
    Y hemos hecho el git clone  para clonar el repositorio

   **Diapositiva 49 y 50**
    ---

1. Git add . 
    Creamos una archivo por ejemplo con nombre license

    ```bash
    nano license 
    #escribimos dentro de él.
    git status
    ```
 
    ```bash
    git add license
    # git add *
    # git add -A
    # git add .
    git status
    ```
    **Diapositiva 51**
    ---

    ```bash 
    git commit -am "añadido license"
    ```   

   **Diapositiva 52**
    ---


1. git rm

    ```bash
    git rm license
    git status
    rm license
    ```   
    Si los cambios no estubieran en el área de confirmado sino en la de preparado o staged.

    ```bash
    nano license
    git add license
    git rm --cached license
    git status
    rm licencse
    ls -l
    git commit -am "punto 17"
    ```   

      **Diapositiva 53**
    ---

1. git diff

    ```bash
    #creamos un archivo
    nano pruebas
    git add pruebas
    git commit -am "guardando Pruebas"
    ```
    Modificamos fichero
    ```bash
    nano pruebas
    #modificamos pruebas
    git diff pruebas
    ```   

    **Diapositiva 54**
    ---

1. git restore

    ```bash
    git restore pruebas
   
    ```   
 
    **Diapositiva 55**
    ---

1. git log

    ```bash
    # Muestra los logs de los commits 
    git log

    ```    

    ```bash
    # Muestra los 2 últimos logs 
    git log -n 2
    # git log -2

    ```    

    ```bash
    Muestra los logs de los commits dónde se ha modificado el archivo pruebas
    git log --follow pruebas

    ```   

    ```bash
    # Muestra los logs con los cambios en cada commit 
    git  log -p

    ```    
    ```bash
    # Muestra los  logs en una única línea 
    git log --oneline

    ```    
    **Diapositiva 56**
    ---


1. git show 

    ```bash
    #Copiamos uno de los primeros  id de commit y lo pegamos 
    git show <id commit> 
    ```    

    **Diapositiva 57**
    ---

1. git reset

    ```bash
    nano eliminadoReset
    #modificamos eliminadoReset
    ```
    
    ```bash
    git add .
    git commit -am "vamos a hacer un git reset"
    # vemos los camibos que hemos hecho y el id de commit <id commit>
    git log -p -1
    ```
    Modificamos eliminadoReset y hacemos los cambios 

    ```bash
    nano eliminadoReset
    #modificamos eliminadoReset
    git add .
    git commit -am "hemos modificado eliminadoReset"
    git status
    cat eliminadoReset
    ```

   ```bash
    git add .
    git commit -am "vamos a hacer un reset hard"
    # hacemos el git reset --hard de  commit anterior.
    git reset --soft <id-commit>
    git status
    git log -p -1
    cat eliminadoReset

    ```   
    Vemos que nos lo ha sacado del area de modificado pero no ha cambiado el fichero

1. git reset --hard
    ```bash
    # hacemos el git reset --hard de  commit anterior.
    git reset --hard <id-commit>
    git status
    git log -p -1

    ```   
    Vemos que nos ha cambiado los archivos al estado del commit indicado. 

    **Diapositiva 58**
    ---

1. git branch

    ```bash
    # Nos muestra las ramas de nuestro proyecto
    git branch
    ```     
    
    Crea una rama con nombre `dev`
    
    ```bash
    git branch dev
    git branch testing
    git branch
    ```

    Elimina una rama

    ```bash
    git branch -d dev
    git branch
    ```

    **Diapositiva 59**
    ---

1. git checkout

    ```bash
    git checkout testing
    git branch
    ```     
    
    ```bash
    git checkout -b alpha
    git branch
    ```

    **Diapositiva 60**
    ---

1. git pull

    ```bash
    # me muevo a la rama main y hago un pull
    git checkout main
    git pull
    ```     
    
    Con --rebase forzamos a descargar los archivos existentes y eliminamos todo lo que tengamos en nuestro directorio de trabajo.

    ```bash
    git pull --rebase
    ```     

    Para descargarlo en una rama nueva 
    ```bash
    git pull origin alpha
    ```     
    
    **Diapositiva 61**
    ---

    
1. git push

    ```bash
   git push origin main
    ```     
    
    Sube todas las ramas

    ```bash
   git push --all origin
    ```     
    
    Sube nuestro repositorio a la rama indicada

    ```bash
    git push origin alpha
    ```     

    **Diapositiva 62**
    ---

1. git merge

    ```bash
   git merge main
    ```     
    

    
[![Licencia: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
