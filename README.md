# Proyecto Capstone

Se desea desarrollar modelos multimodales para modelar fake news visuales en redes sociales en el contexto de los dos
procesos constitucionales de Chile. Esta necesidad surge dentro del desarrollo de un proyecto de modelamiento de
narrativas multimodales de noticias falsas, lo cual es una primera parte de un proyecto más grande, donde se pretende
desarrollador un marco computaciones basado en técnicas multimodales de extracción de narrativas y modelos de
lenguaje avanzado, enfocado también en fake news.

El primer paso para poder extraer las narrativas desde los datos requiere de un modelo adecuado de embeddings que
permita capturar la información contenida en las fake news visuales y calcular la similitud entre dichas publicaciones, lo
cual permitirá reconocer verosimilitud de cada noticia basándonos solamente en las características de la misma.

## Iniciar Proyecto

Es necesario contar con una versión de **python** igual o mayor a **3.11.9** ([descargar python](https://www.python.org/downloads/)). Se recomienda utilizar **visual studio code**.

1. Clonar Proyecto

   ```bash
   git clone https://github.com/MolodyGs/CapstoneProject.git
   ```

2. Crear un Entorno Virtual (si es necesario)

   ```bash
   python -m venv .venv
   .venv/Scripts/activate
   ```

3. Instalación de Dependencias

   Este procedimiento puede tomar entre 10 a 20 minutos despendiendo de la conectividad.

   ```bash
   pip install -r requirements.txt
   ```

## Utilización

1. Obtener Paginas - `get_pages.ipynb`
2. Modelo de Texto - `text_model.ipynb`
3. Extracción de Texto en Imagenes - `text_extract_in_images.ipynb`
4. Modelo Hibrido - `hybrid_model.ipynb`
5. Modelo Multimodal - `multimodal_model.ipynb`

## Mapa Conceptual de Modelos

![Mapa Conceptual](models_conceptual_map.png)
