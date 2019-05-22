# Lab2-Distribuidos

## Caso y contexto:
El dataset usado para la construcción del modelo pertenecen a un banco que desea iniciar una campaña de markenting
para ofrecer depósitos a plazo fijo. Con este modelo se busca realizar una clasificación para predecir si los clientes
aceptarían realizar el deposito.

Para la construcción del clasificador se entrena un modelo de regresión logística, con un dataset balanceado
de 11000 clientes aproximadamente.

La construcciión del modelo se lleva a cabo siguiendo las instrucciones de Susan Li en 
https://towardsdatascience.com/machine-learning-with-pyspark-and-mllib-solving-a-binary-classification-problem-96396065d2aa

## Estructura Dataset

 - age (Int): Edad del cliente
 - job (String): Oficio del cliente, puede tomar los siguientes valores: 
    'admin.','blue-collar','entrepreneur','housemaid',
    'management','retired','self-employed','services',
    'student','technician','unemployed','unknown'
    
 - marital (String): Estado civil, puede tomar los siguientes valores:
     'divorced','married','single','unknown'
 - education (String): Nivel educacional, puede tomar los siguientes valores:
      'primary','secondary','tertiary'
 - default (String): Indica si el cliente tiene créditos actualmente:
      'yes','no'
 - balance (Int): Cantidad promedio de dinero que posee el cliente, de forma anual:
 - housing (String): Indica si el cliente posee crédito para la compra de una vivienda (Housing loan):
      'yes','no'
 - loan (String): Indica si la persona posee algún préstamo:
      'yes','no'
 - contact (String): Tipo de comunicación que se tiene con el cliente:
      'unknown','cellular','telephone'
 - duration (Int): Indica cuanto tiempo duró el último contacto que se tuvo con el cliente
 - campaign (Int): Numero de contactos realizados con este cliente durante la campaña publicitaria
 - pdays (Int): Numero de días que pasaron desde el último contacto realizado, para una campaña previa
 - previous (Int): Numero de contactos realizados con este cliente antes de esta campaña
 - poutcome (String): Resultados de la campaña de marketing anterior para este cliente:
      'success','failure','unknown'
 - deposit (String): Indica si el cliente aceptó hacer el depósito. (SOLO PARA ENTRENAMIENTO):
      'yes','no'
 - id (Int): Este campo sirve para diferenciar a los clientes y se agrega solo en caso de consultas.
   
El dataset usado para este caso se obtiene de https://www.kaggle.com/rouseguy/bankbalanced, el cual corresponde
a una adaptación del dataset presente en UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

## Creación y uso del modelo

Actualmente se cuenta con dos funciones en el archivo classifier.py, las cuales corresponden a:

  - makeModel (nombre pipeline_model (String), nombre_model(String)) : Esta funcion permite construir y entrenar un 
clasificador a través de un modelo de regresión logística. Para dar persistencia al modelo construido se deben ingresar 2 argumentos. El primero se corresponde el flujo de procesamiento por el que deben pasar los datos antes de ser evaluado, mientras que el segundo se refiere al nombre con el que se guarda el modelo clasificador.
 
  - makePrediction (data (Json),nombre pipeline_model(String), nombre_model(String)): Esta función permite realizar
la clasificación de un cliente determinado usando un modelo ya creado. Los argumentos que recibe corresponden a una           lista de clientes, en formato JSON (Con la estructura previamente señalada), nombre del pipeline y modelo creado anteriormente. Como resultado devuelve una lista de diccionarios, donde cada elemento contiene un campo 'prediction' que toma el valor 1.0(si) o 0.0 (no).
  
  

Para poder ejecutar el código se debe instalar la versión 2.4.3 de pyspark. Con el comando
pip3 install -r requirements.txt (Instalar pip3) se instalarán pyspark automaticamente.

## Aclaración
Para la creación de modelos lo ideal es obtener los datos desde alguna base de datos. Actualmente estos se obtienen
directamente desde el archivo csvjson.json o bank.csv


