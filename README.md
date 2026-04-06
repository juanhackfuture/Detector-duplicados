# 📂 Detector de Archivos Duplicados en Python

Este script automatiza la detección de archivos duplicados en cualquier carpeta de tu sistema. A diferencia de otros organizadores, este utiliza **hashing MD5**, lo que significa que identifica archivos idénticos aunque tengan nombres diferentes.

## 🚀 Funcionalidades

- **Identificación por Contenido**: Genera una "huella digital" única para cada archivo.
- **Detección Precisa**: Encuentra duplicados exactos comparando hashes MD5.
- **Reporte en Consola**: Lista todos los archivos repetidos y muestra el conteo total.
- **Seguridad**: Solo analiza archivos de primer nivel, evitando modificar o entrar en subcarpetas.

## 📄 Código fuente

👉 [Ver detector-duplicados.py](./detector-duplicados.py)

## ⚙️ Cómo usar

1. **Ejecuta el script** desde tu terminal o VS Code:
```bash
    python detector-duplicados.py
```
2. **Ingresa la ruta de la carpeta que quieres escanear** (ej: C:/Users/Usuario/Downloads).

3. El programa mostrará la lista de archivos que están de más.

## 🧠 Tecnologías
**Python 3**

**Lib hashlib**: Para la generación de firmas digitales de archivos.

**Lib os**: Para la navegación en el sistema de archivos.