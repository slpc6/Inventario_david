"""Metodo que establece la conexion entre MongoDB y el API"""

#External libraries
import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


load_dotenv()
DBCONN = os.getenv('DBCONN')


def get_client() -> MongoClient:
    """Establece una conexcion con una base de datos mongo

    :returns:
        Una instancia con la conexcion a la coleccion espeficica de la base de datos

    """

    client = MongoClient(DBCONN, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client['api_db']
    collection = db['inventario_collection']

    return collection
