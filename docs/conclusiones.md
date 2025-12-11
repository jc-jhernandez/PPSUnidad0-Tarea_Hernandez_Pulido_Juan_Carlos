# Conclusiones

## Resumen

He terminado todos los apartados de la tarea RA5. He trabajado con Git, GitHub Actions, Docker y MkDocs para montar una web de documentación.

## Preparación del entorno

He adaptado una imagen de Kali para arquitectura arm64, ya que no hay imágenes oficiales disponibles para esta arquitectura en la web.

He configurado Visual Studio Code en mi instancia de Kali, lo que me ha permitido trabajar con todas las herramientas integradas en el mismo entorno.

He aplicado buenas prácticas con Pull Requests para mantener el código organizado antes de fusionar cambios entre ramas.

## Lo que he hecho

He creado un repositorio en GitHub con dos ramas (main y develop), he configurado GitHub Actions para que publique automáticamente la documentación cada vez que subo cambios, y he montado un contenedor Docker con NGINX para servir la web localmente.

La documentación está publicada en: [https://jc-jhernandez.github.io/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/](https://jc-jhernandez.github.io/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/)

## Problemas que me encontré

Al crear el archivo mkdocs.yml me daba error de encoding. Lo resolví copiándolo desde un ejemplo que funcionaba.

Las imágenes no se veían porque las rutas apuntaban a la carpeta incorrecta. Las moví a docs/images/ y actualicé las referencias.

El workflow de GitHub Actions no podía publicar en gh-pages por falta de permisos. Lo arreglé activando los permisos de escritura en la configuración del repositorio.

## Conclusión

Espero haber alcanzado todos los objetivos que se solicitaban en la tarea.

**Repositorio**: [https://github.com/jc-jhernandez/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos](https://github.com/jc-jhernandez/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos)

**Web**: [https://jc-jhernandez.github.io/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/](https://jc-jhernandez.github.io/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/)
