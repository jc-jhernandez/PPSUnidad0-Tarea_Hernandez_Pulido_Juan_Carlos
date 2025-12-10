# PPS - Unidad 0 - Tarea RA5

Repositorio de entrega de la tarea obligatoria RA5 del módulo de Puesta en Producción Segura.

**Autor**: Juan Carlos Hernández Pulido
**Curso**: Puesta en Producción Segura
**Fecha**: Diciembre 2024

## Descripción

Este repositorio contiene la documentación y configuración de las herramientas trabajadas en la Unidad 0:

- **Git y GitHub**: Control de versiones, workflow con ramas, pull requests
- **GitHub Actions**: Automatización de despliegue de documentación
- **GitHub Pages**: Publicación de documentación estática
- **MkDocs**: Generación de documentación a partir de archivos Markdown
- **Docker**: Contenedorización de la documentación con NGINX

## Estructura del proyecto

```
PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/
├── calculator/              # Paquete Python de ejemplo
├── docs/                    # Documentación en Markdown
│   ├── index.md            # Introducción
│   ├── git.md              # Git y GitHub
│   ├── gitActions.md       # GitHub Actions
│   ├── gitPages.md         # GitHub Pages
│   ├── docker.md           # Docker
│   └── conclusiones.md     # Conclusiones
├── images/                  # Capturas de pantalla
├── .github/workflows/       # GitHub Actions workflows
├── mkdocs.yml              # Configuración de MkDocs
├── requirements.txt        # Dependencias Python
├── docker-compose.yml      # Configuración Docker Compose
└── Dockerfile              # Imagen Docker personalizada
```

## Acceso a la documentación

La documentación completa está disponible en GitHub Pages:

**URL**: [https://jc-jhernandez.github.io/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/](https://jc-jhernandez.github.io/PPSUnidad0-Tarea_Hernandez_Pulido_Juan_Carlos/)

## Uso local

### Visualizar la documentación con MkDocs

```bash
# Instalar dependencias
pip install -r requirements.txt

# Servir la documentación en http://127.0.0.1:8000
mkdocs serve
```

### Ejecutar con Docker

```bash
# Generar la documentación estática
mkdocs build

# Levantar el contenedor NGINX
docker-compose up -d

# Acceder a http://localhost:8085
```

## Contenido de la tarea

La documentación incluye el proceso completo de:

1. **Configuración de Git**: Creación de claves SSH, repositorio, estructura de ramas
2. **GitHub Actions**: Workflow automático para generar y desplegar documentación
3. **GitHub Pages**: Configuración y publicación del sitio estático
4. **Docker**: Contenedorización con NGINX y Docker Compose
5. **Conclusiones**: Reflexiones sobre las herramientas y el proceso

Cada sección incluye capturas de pantalla, código de ejemplo y explicaciones detalladas.

## Tecnologías utilizadas

- Git 2.x
- GitHub (Actions, Pages)
- Python 3.x
- MkDocs + Material theme
- Docker + Docker Compose
- NGINX Alpine

---

*Repositorio preparado para la entrega de la tarea RA5 - Unidad 0*
