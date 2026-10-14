# Examen de SBD sin conexión

Material para preparar un portátil con **Windows 11** o **Ubuntu 22.04 LTS Desktop** y realizar un examen de **Sistemas de Big Data (SBD)** del curso de especialización en **Inteligencia Artificial y Big Data (IABD)**.

Los instaladores crean un entorno virtual de Python con JupyterLab. Una vez preparado el equipo, puedes abrir cuadernos, ejecutar código, escribir explicaciones y guardar tu trabajo **sin conexión a Internet**.

**Descarga:** [descargar todos los archivos en ZIP](https://github.com/iesataulfoargentasor/sbd-examen-sin-internet/archive/refs/heads/main.zip). También puedes usar **Code → Download ZIP** en la parte superior del repositorio. No necesitas una cuenta de GitHub.

**Guía para conservar en el portátil:** [abrir la guía del alumnado en PDF](GUIA_ALUMNADO.pdf). El PDF y este README están incluidos en el ZIP.

> **La instalación inicial necesita Internet y debe hacerse antes del examen.** El enunciado que entregue el docente determina los ejercicios y los archivos que hay que entregar. Este repositorio no obliga a dibujar grafos, utilizar NetworkX ni exportar un CSV.

## Contenido

- [Qué necesitas](#qué-necesitas)
- [Descargar y preparar la carpeta](#1-descargar-y-preparar-la-carpeta)
- [Instalar en Windows 11](#2a-instalar-en-windows-11)
- [Instalar en Ubuntu 22.04](#2b-instalar-en-ubuntu-2204)
- [Comprobar el equipo sin conexión](#3-comprobar-el-equipo-sin-conexión)
- [Realizar el examen](#4-realizar-el-examen)
- [Guardar y entregar](#5-guardar-y-entregar)
- [Resolver problemas](#resolver-problemas)
- [Información para el docente](#información-para-el-docente)

## Qué necesitas

| Requisito | Qué debes tener preparado |
| --- | --- |
| Sistema operativo | Windows 11 o Ubuntu 22.04 LTS Desktop. |
| Python | CPython 3.10, 3.11, 3.12, 3.13 o 3.14 instalado. El instalador de este repositorio no instala Python. |
| Navegador | Una versión reciente de Firefox, Chrome o Edge instalada antes del examen. |
| Carpeta local | Una ubicación donde puedas escribir y guardar archivos. |
| Internet | Necesario para descargar el material e instalar los paquetes antes del examen. |

En **Windows** se recomienda Python **3.14**, descargado de [python.org](https://www.python.org/downloads/windows/). Instálalo para tu usuario e incluye el lanzador `py`. Si solo tienes Python 3.15, puedes conservarlo e instalar también Python 3.14: este paquete está preparado para las versiones 3.10 a 3.14.

En **Ubuntu 22.04**, el Python **3.10** que viene con el sistema es suficiente. No necesitas reemplazarlo por la versión más reciente.

JupyterLab se utiliza a través del navegador, pero el programa y el código se ejecutan en tu portátil. Una dirección como `http://127.0.0.1:8888` o `http://localhost:8888` es local y funciona sin Internet. No necesitas Colab ni una cuenta de Google.

## 1. Descargar y preparar la carpeta

1. Descarga el ZIP desde el enlace de este README o mediante **Code → Download ZIP**.
2. **Extrae todo su contenido**. No ejecutes los instaladores desde dentro del ZIP.
3. Coloca la carpeta extraída en una ubicación local definitiva; por ejemplo, dentro de Documentos. Puedes llamarla `SBD_EXAMEN` antes de instalar.
4. Abre esa carpeta. Debes ver `INSTALAR_WINDOWS.cmd`, `INSTALAR_UBUNTU.sh` y la carpeta `trabajo`, entre otros archivos.

**Después de instalar, no renombres ni muevas esta carpeta.** El entorno virtual conserva rutas a su ubicación original. Tampoco debes copiar una carpeta `.venv` ya instalada desde el portátil de otra persona.

## 2A. Instalar en Windows 11

Realiza estos pasos con conexión a Internet:

1. Haz doble clic en **`INSTALAR_WINDOWS.cmd`**.
2. Se abrirá una ventana de comandos. Déjala abierta mientras se descargan e instalan los paquetes.
3. Espera a que aparezca **`INSTALACION COMPLETADA`**. Si el entorno ya estaba preparado, el instalador lo comprobará y mostrará **`COMPROBACION CORRECTA`**.
4. Pulsa una tecla para cerrar la ventana cuando se indique.

No necesitas ejecutar este instalador como administrador ni activar manualmente el entorno virtual. El instalador busca una versión compatible de Python y utiliza su propio entorno `.venv`.

Si aparece un error, la instalación no está terminada. Revisa el apartado de problemas o comunica el mensaje al docente antes del examen.

## 2B. Instalar en Ubuntu 22.04

Realiza estos pasos con conexión a Internet:

1. Abre la carpeta extraída en el gestor de archivos.
2. Haz clic derecho en un espacio vacío de la carpeta y selecciona **Abrir en una terminal**.
3. Escribe esta orden y pulsa Intro:

```bash
bash INSTALAR_UBUNTU.sh
```

4. Espera al mensaje **`INSTALACION COMPLETADA`** o **`COMPROBACION CORRECTA`**.

No hace falta cambiar los permisos de los archivos `.sh` si los ejecutas con `bash` como se muestra aquí. **Ejecuta el instalador sin `sudo`.**

Si aparece el mensaje de que falta el soporte `venv`, prepara ese requisito con estas órdenes:

```bash
sudo apt update
sudo apt install python3-venv
```

Después vuelve a ejecutar:

```bash
bash INSTALAR_UBUNTU.sh
```

Este paso opcional instala el soporte de entornos virtuales del sistema y puede pedir una contraseña de administrador. Si no tienes esos permisos, avisa al docente. JupyterLab y los paquetes del examen se instalarán después dentro de `.venv`.

## 3. Comprobar el equipo sin conexión

Haz esta prueba **antes del día del examen**:

1. Cierra JupyterLab si estaba abierto.
2. Desconecta el Wi-Fi y las demás conexiones a Internet, incluido el cable de red o una conexión compartida desde el móvil.
3. Inicia JupyterLab con el acceso correspondiente:

| Sistema | Cómo iniciar |
| --- | --- |
| Windows 11 | Doble clic en **`INICIAR_EXAMEN_WINDOWS.cmd`**. |
| Ubuntu 22.04 | Abre una terminal en la carpeta y ejecuta **`bash INICIAR_EXAMEN_UBUNTU.sh`**. |

4. Se abrirá el navegador. **Mantén abierta la ventana de comandos** que ha iniciado JupyterLab.
5. En el panel de archivos de JupyterLab, abre **`00_Prueba_entorno.ipynb`**.
6. Si te pregunta qué kernel utilizar, elige **`Python (SBD sin Internet)`**. El kernel es el proceso que ejecuta tu código.
7. Selecciona cada celda de código y pulsa **Mayús + Intro**, de arriba abajo. Al terminar debe aparecer **`PRUEBA CORRECTA`**.
8. Pulsa **Ctrl + S** para guardar. Cierra la pestaña del cuaderno y ábrela otra vez: sus resultados deben seguir guardados.

El cuaderno de prueba utiliza únicamente Python básico. **No dibuja grafos, no utiliza NetworkX y no genera un CSV.** Su finalidad es comprobar que puedes ejecutar y guardar un cuaderno sin conexión.

También puedes ejecutar el comprobador automático: doble clic en `COMPROBAR_WINDOWS.cmd` o `bash COMPROBAR_UBUNTU.sh`. Comprueba las bibliotecas instaladas, arranca un kernel y realiza una pequeña prueba temporal de escritura. Esta comprobación tampoco necesita Internet y no constituye un ejercicio del examen.

## 4. Realizar el examen

### Abrir el cuaderno correcto

1. Lee el enunciado y sigue las indicaciones del docente sobre materiales permitidos y archivos de entrega.
2. Si recibes un cuaderno `.ipynb`, cópialo dentro de la carpeta **`trabajo`** del paquete.
3. Abre JupyterLab con **`INICIAR_EXAMEN`** de tu sistema y abre ese cuaderno desde el panel de archivos.
4. Si el docente pide empezar un cuaderno desde cero, crea un **Notebook** desde el panel inicial de JupyterLab y selecciona el kernel **`Python (SBD sin Internet)`**.
5. Guarda el archivo con el nombre indicado en el enunciado. Si el docente no fija uno, puedes usar un nombre identificable, como `SBD_Apellidos_Nombre.ipynb`.

El panel de archivos de JupyterLab muestra la carpeta `trabajo`. El cuaderno incluido `00_Prueba_entorno.ipynb` sirve para comprobar la instalación; **el examen se entrega o se crea aparte según las indicaciones del docente**.

### Escribir código y explicaciones

Los cuadernos permiten combinar dos tipos de celdas:

| Tipo de celda | Para qué sirve |
| --- | --- |
| **Code** | Escribir y ejecutar código Python. Los resultados aparecen debajo de la celda. |
| **Markdown** | Escribir explicaciones, títulos, justificaciones y conclusiones cuando las pida el enunciado. |

Puedes cambiar el tipo de la celda seleccionada desde el desplegable de la barra del cuaderno.

| Acción | Atajo |
| --- | --- |
| Ejecutar una celda y pasar a la siguiente | **Mayús + Intro** |
| Ejecutar la celda actual sin avanzar | **Ctrl + Intro** |
| Guardar el cuaderno | **Ctrl + S**, con el cuaderno seleccionado |

Ejecuta las celdas en el orden previsto. Una variable creada en una celda puede utilizarse en las siguientes. Si reinicias el kernel, las variables se borran de la memoria y debes volver a ejecutar las celdas que las crean.

Si una celda se queda ejecutándose, puedes usar **Kernel → Interrupt Kernel** para interrumpirla. Revisa el código y pregunta al docente si se trata de una incidencia técnica.

### Qué herramientas hay que utilizar

**El enunciado determina lo que debes resolver y entregar.**

- Si solo pide operaciones, estructuras de datos o funciones de Python, resuelve esos apartados con las herramientas que correspondan.
- **NetworkX está preinstalado como recurso adicional**, por si algún ejercicio lo requiere. Su instalación no implica que debas usarlo.
- **Solo debes construir o dibujar grafos si se pide expresamente.** Construir o analizar un grafo no obliga por sí mismo a dibujarlo.
- **Solo debes exportar un CSV si lo pide el enunciado.** Si no se pide, no añadas ese archivo como requisito de entrega.
- No necesitas descargar paquetes durante el examen. Las herramientas necesarias deben estar preparadas previamente.

## 5. Guardar y entregar

1. Guarda con frecuencia con **Ctrl + S**.
2. Antes de terminar, revisa que has contestado los apartados del enunciado y que las explicaciones están en el cuaderno cuando se soliciten.
3. Si el docente pide comprobar una ejecución completa, utiliza **Kernel → Restart Kernel and Run All Cells**. Esto reinicia la memoria y ejecuta el cuaderno desde el principio. Revisa las salidas y vuelve a guardar.
4. Comprueba que el archivo `.ipynb` está dentro de **`trabajo`**. El cuaderno guarda el código, las explicaciones y las salidas que hayas guardado.
5. Entrega **exactamente los archivos que indique el docente**, por el medio que establezca. Añade un CSV u otros archivos únicamente cuando se soliciten.

**No entregues `.venv`, `.estado` ni toda la carpeta de herramientas.** Tampoco necesitas subir tu examen a este repositorio de GitHub.

Para cerrar JupyterLab, guarda el cuaderno, vuelve a la ventana de comandos y pulsa **Ctrl + C**. Confirma el cierre si te lo pide. Cerrar solo la pestaña del navegador puede dejar el servidor funcionando.

## Resolver problemas

| Problema | Qué hacer |
| --- | --- |
| El instalador no encuentra Python en Windows. | Instala CPython 3.14 para tu usuario con el lanzador `py` y repite la instalación. Si el centro gestiona tu equipo, consulta al docente. |
| Solo tengo Python 3.15. | Prepara también Python 3.14 antes del examen. Este paquete admite versiones 3.10 a 3.14. |
| Ubuntu indica que falta `venv`. | Sigue el paso de instalación de `python3-venv` descrito arriba y repite el instalador sin `sudo`. |
| La instalación se interrumpe o falla una descarga. | Revisa la conexión y repite el instalador. Si persiste, conserva el mensaje y el archivo `.estado/instalacion.log` para el docente. |
| El navegador no se abre automáticamente. | Copia la dirección local completa que muestra la ventana de comandos, incluido el token, y pégala en el navegador. |
| No aparece el cuaderno del examen. | Comprueba que lo has copiado dentro de `trabajo`. Actualiza el panel de archivos de JupyterLab. |
| Se pregunta qué kernel utilizar. | Selecciona `Python (SBD sin Internet)`. |
| Aparece `ModuleNotFoundError`. | Comprueba el kernel y ejecuta `COMPROBAR` de tu sistema. Si el examen pide otra biblioteca, comunica la incidencia al docente. |
| He movido o renombrado la carpeta después de instalar. | Conserva `trabajo` y avisa al docente. Antes del examen y con Internet, puede renombrarse `.venv` y volver a ejecutar el instalador en la ubicación definitiva. |
| Ya he instalado y no tengo Internet. | Usa `INICIAR_EXAMEN`, que no descarga paquetes. No necesitas volver a instalar. |

## Qué se guarda en cada carpeta

| Carpeta o archivo | Contenido |
| --- | --- |
| `trabajo/` | Cuaderno de prueba, cuaderno del examen y resultados que generes. |
| `.venv/` | Entorno virtual con JupyterLab, NetworkX y sus dependencias. Se crea al instalar. |
| `.estado/` | Configuración, temporales y registro de instalación. Se crea al preparar el entorno. |
| `soporte/` | Programas utilizados por los instaladores y los accesos de inicio. |
| `GUIA_ALUMNADO.pdf` | Guía breve que puedes consultar sin Internet. |

Las carpetas que empiezan por un punto pueden estar ocultas en el gestor de archivos. No necesitas abrirlas para realizar el examen. **Conserva siempre `trabajo`**, porque contiene tus archivos.

## Información para el docente

La preparación mantiene las bibliotecas del examen dentro de un entorno virtual. No reemplaza el Python del sistema ni convierte el equipo en una máquina virtual. El requisito opcional `python3-venv` de Ubuntu sí se instala mediante el gestor de paquetes del sistema.

Las versiones principales están fijadas en [`requirements.txt`](requirements.txt): **JupyterLab 4.6.4** y **NetworkX 3.4.2**. Esta versión de NetworkX permite conservar la compatibilidad con Python 3.10 de Ubuntu 22.04. Las dependencias indirectas se resuelven al instalar y su lista queda en `.estado/versiones_instaladas.txt`.

Antes de la evaluación, prueba el material en los dos sistemas y pide al alumnado que haga la comprobación con la red desconectada. Este paquete permite trabajar sin Internet, pero **no bloquea la red ni otras aplicaciones**: las condiciones de la evaluación se organizan aparte.

El enunciado, las soluciones y las entregas del alumnado no forman parte de este repositorio. El archivo `.gitignore` evita añadir por defecto entornos, registros y archivos de trabajo distintos del cuaderno de prueba.

Consulta las [notas para el docente](NOTAS_DOCENTE.txt) y el [alcance de las comprobaciones realizadas](VALIDACION.txt). La instalación y el inicio se han probado en Windows; la ejecución completa en Ubuntu 22.04 sigue pendiente de comprobación en un equipo real.

## Documentación de referencia

Estos enlaces requieren Internet; consúltalos durante la preparación:

- [Entornos virtuales de Python](https://docs.python.org/3/library/venv.html).
- [Instalación de JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).
- [Inicio de JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html).
- [Versiones de Python disponibles en Ubuntu](https://ubuntu.com/developers/docs/reference/availability/python/).
