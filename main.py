from sys import argv
import xlrd
import requests
from urllib import parse
import whois

def main(argv):  
  print("Main")
  print("Obtener fechas de creación de un listado de dominios provenientes de un xlsx")
  #print(argv)
  script,archivoXLXS,salidaCSV = argv
  print(archivoXLXS)
  print(salidaCSV)
  limpiarSalida(salidaCSV)  
  lineaInicial = "dominio;creacion;vencimiento";
  guardarLineaEnCSV(salidaCSV, lineaInicial)
  leerExcel(archivoXLXS, salidaCSV)

def leerExcel(archivoXLXS, salidaCSV):
  print("Leyendo excel" + archivoXLXS)
  workbook = xlrd.open_workbook(archivoXLXS)
  for hoja in workbook.sheets():
    print ('Hoja:',hoja.name)
    print ('Rows:',hoja.nrows)
    print ('Cols:',hoja.ncols)

    dominios = []
    for row in range(hoja.nrows):
      if(row>0):        
        dominios.append(hoja.cell(row,1).value)

    #print ('dominios: ', dominios)

  for dominio in dominios:
    consultar("http://"+dominio,salidaCSV);

def consultar(url, salidaCSV):
  print ("Consultar datos de dominio", url)

  try:
    requests.head(url).headers['server']
    hostname = parse.urlparse(url).netloc

    domain = whois.query(hostname)
    #print(domain.__dict__)
    print("Name:" + domain.name)
    print("Creation: " + domain.creation_date.strftime("%d/%m/%Y"))
    print("Expiration:" + domain.expiration_date.strftime("%d/%m/%Y"))
    lineaCSV = url+";"+domain.creation_date.strftime("%d/%m/%Y")+";"+domain.expiration_date.strftime("%d/%m/%Y")
    guardarLineaEnCSV(salidaCSV, lineaCSV)
  except requests.exceptions.RequestException as e:  # This is the correct syntax
    print("Error requests", e)
    lineaCSV = url+";N/A;N/A"
    guardarLineaEnCSV(salidaCSV, lineaCSV)
  except whois.exceptions.WhoisCommandFailed as e:
    print("Error whois", e)
    lineaCSV = url+";N/A;N/A"
    guardarLineaEnCSV(salidaCSV, lineaCSV)

def guardarLineaEnCSV(archivoCSV,lineaString):
  print("Guardando línea en csv",archivoCSV)
  with open(archivoCSV, 'a') as archivoCSV:
    archivoCSV.write(lineaString+"\n")

def limpiarSalida(archivoCSV):
  print("Borrando archivo "+archivoCSV)
  try:
    raw = open(archivoCSV, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)                        # <- This is the missing piece
    raw.truncate()
  except IOError:
    print ("Error: Archivo "+archivoCSV+ " no existe.")

if __name__ == '__main__':
  if len(argv) < 2:
    print(argv);
    #argv por defecto
    #argv = ['script', '1', '2', '3']
    print("Falta especificar ruta de archivo.xlsx y el archivo de salida .csv");
  else:
    main(argv)
