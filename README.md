# Dominios

Script de obtención de datos de dominios 

## Dependencias

- python 2.7
- xlrd
- pip
- python-whois
- whois

## Ambiente 

- Instalar venv

```
pip install virtualenv
```

- Crear ambiente

```
virtualenv venv
```

- Activar ambiente

```
source venv/bin/activate
```

## Instalación dependencias

A través de pip3 instalar dependencia

``python3 -m pip install python-whois``


## Guardar dependencias

``pip3 freeze > requirements.txt``


## Instalar desde dependencias

``pip3 install -r requirements.txt``

## Ejecución

Para ejecutar el script, hay que pasar como parámetros de entrada el archivo xls que contienen los datos y el nombre del archivo de salida o resultado en CSV

```
python main.py datos.xls salida.csv
```


## Desinstalación

Usar pip para desintalar

``python3 -m pip uninstall python-whois``
