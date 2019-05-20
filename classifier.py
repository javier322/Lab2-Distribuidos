
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel

from pyspark.sql.types import StructType,StructField
from pyspark.sql.types import IntegerType, StringType
from sparkSession import SPARK_SESSION
import json


SCHEMA = StructType([
    StructField("age", IntegerType(), True),
    StructField("job", StringType(), True),
    StructField("marital", StringType(), True),
    StructField("education", StringType(), True),
    StructField("default", StringType(), True),
    StructField("balance", IntegerType(), True),
    StructField("housing", StringType(), True),
    StructField("loan", StringType(), True),
    StructField("contact", StringType(), True),
    StructField("day", IntegerType(), True),
    StructField("month", StringType(), True),
    StructField("duration", IntegerType(), True),
    StructField("campaign", IntegerType(), True),
    StructField("pdays", IntegerType(), True),
    StructField("previous", IntegerType(), True),
    StructField("poutcome", StringType(), True),
    StructField("deposit", StringType(), True)])


def makePrediction(data,name_pipelineModel,name_model):

    #stringJson=json.dumps(data)
    jsonStringRdd=SPARK_SESSION.sparkContext.parallelize(data)
    df=SPARK_SESSION.read.option('multiline', "true").json(jsonStringRdd,SCHEMA)

    df.show()

    pipelineModel=PipelineModel.load(name_pipelineModel)
    df = pipelineModel.transform(df)

    selectedCols = ['features'] + df.columns
    df = df.select(selectedCols)
    
    model=LogisticRegressionModel.load(name_model)
    result=model.transform(df)

    value=result.select('prediction').collect()
    predictions=[]
    for p  in value:
        e=p.asDict()['prediction']
        print(e)
        predictions.append({"prediction":e})

    return predictions



def makeModel(name_pipelineModel,name_model):
    
    df=SPARK_SESSION.read.option("multiline", "true").json("csvjson.json",SCHEMA)

    df = df.select('age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'deposit')
    cols = df.columns

    pipeline=Pipeline.load("Mypipeline")
    pipelineModel=pipeline.fit(df)
    pipelineModel.save(name_pipelineModel)
    df = pipelineModel.transform(df)
    selectedCols = ['label', 'features'] + cols
    df = df.select(selectedCols)

    lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
    lrModel = lr.fit(df)
    lrModel.save(name_model)



makeModel("pipeline2","model2")
element=[
   {
    "age": 50,
    "job": "retired",
    "marital": "single",
    "education": "tertiary",
    "default": "yes",
    "balance": 2000,
    "housing": "yes",
    "loan": "yes",
    "contact": "cellular",
    "duration": 120,
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown"
  },
  {
    "age": 23,
    "job": "student",
    "marital": "single",
    "education": "tertiary",
    "default": "no",
    "balance": 0,
    "housing": "no",
    "loan": "no",
    "contact": "cellular",
    "duration": 120,
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "success"
  }]
result=makePrediction(element,"pipeline2","model2")
print("aqui llego")
print(result)
for r in result:
    print(r)
    print(type(r))


