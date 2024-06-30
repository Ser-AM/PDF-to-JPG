# PDF-to-JPG

## Convierte las portadas de archivos PDF a imágenes JPG de manera sencilla.

Este repositorio contiene un script en Python que convierte la primera página de archivos PDF en imágenes JPG con una resolución específica. Puedes modificar la resolucion en la linea 5 del script.  Ideal para crear miniaturas o imágenes de portada a partir de catálogos en PDF. Simplemente coloca tus archivos PDF en la carpeta de entrada, ejecuta el script y encontrarás tus imágenes convertidas en la carpeta de salida.


### Características:

- Convierte la primera página de archivos PDF a JPG.
- Redimensiona las imágenes a una resolución objetivo de 200x283 píxeles.
- Fácil de usar: solo tienes que colocar los PDFs en la carpeta de entrada y ejecutar el script.


### Requisitos

Este script requiere tener instalado python y las siguientes librerías:
- PyMuPDF (`pip install pymupdf`)
- Pillow (`pip install pillow`)


### Estructura de carpetas necesaria:

PDFtoJPG/
├── script/
│ └── convert.pyw
├── entrada/
│ └── (coloca aquí tus archivos PDF)
└── salida/
└── (aquí aparecerán las imágenes JPG convertidas)

## Uso

Para ejecutar el script, simplemente haz doble clic en el archivo `script.pyw` o ejecútalo desde la línea de comandos:

python convert.pyw