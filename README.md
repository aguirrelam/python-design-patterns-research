# Evaluación del Impacto de los Patrones de Diseño en la Mantenibilidad del Software

Este repositorio contiene el material suplementario y el código fuente utilizado para el artículo científico enviado a la **Revista Cubana de Ciencias Informáticas (RCCI)** bajo el título: *"Impacto de los patrones de diseño en la mantenibilidad y complejidad del software: un estudio comparativo en Python 3.12"*.

## Estructura del Proyecto

El experimento se divide en cuatro variantes de implementación sobre dos casos de estudio:
- `p1_control.py`: Implementación monolítica (Línea base).
- `p2_creacional.py`: Aplicación del patrón Factory Method.
- `p3_estructural.py`: Aplicación del patrón Decorator.
- `p4_comportamiento.py`: Aplicación de los patrones Strategy y Observer.

## Requisitos y Configuración

Para replicar las métricas obtenidas en la investigación, se requiere Python 3.12+ y la herramienta de análisis estático `radon`.

1. Instalar dependencias:
   
   pip install radon
   
2. Ejecutar análisis de Complejidad Ciclomática (CC):
   
   radon cc . -s
