from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result

class cloudantManager:
    # Autentificacion
    client = Cloudant.iam("d6179485-8359-47c6-9067-337120997531-bluemix", "2_9ItqbvPPIMPM7meDDr4nbB1ND-vvZ4dXMT8z8oGH1_")

    # Conexion al servicio
    def connect_service(self):
        try:
            cloudantManager.client.connect()
            return "ok"
        except:
            return "error"

    # Crear base de datos Cloudant
    def create_db(self, db_name):
        try:
            my_db = Cloudant.client.create_database(db_name, throw_on_exit= True)
            return my_db
        except: CloudantException as ex:
            return ex
    
    # Crear la conexion con el servicio
    def disconnect_db(self, db_name):
        try:
            cloudantManager.client.disconnect()
            return "ok"
        except:
            return "error"
    
    #Eliminar una base de datos Cloudant
    def delete_db(self, db_name):
        try:
            cloudantManager.client.delete_database(db_name)
            return "ok"
        except:
            return "error"
    
    # Crear documentos
    def add_doc(self, db, *args):
        try:
            for doc in args:
                document = db.create_document(doc)
            return "ok"
        except:
            return "error"

    # Actualizar documentos 
    def update_db(self, db, id_doc, **kwargs):
        try:
            doc_temp = db[id_doc]
            for key, value in kwargs.items():
                doc_temp[key]= value
            doc_temp.save()
            return "ok"
        except:
            return "error"
        
    # Eliminar documentos
    def delete_doc(self, db , id_doc):
        try:
            doc_temp = db[id_doc]
            doc_temp.delete()
            return "ok"
        except:
            return "error"

    # Consulta general
    @staticmethod
    def get_all_docs(db):
        try:
            docs = Result(db.all_docs, include_docs= True)
            return docs
        except:
            return "error"

    def get_query_by(self, db, id_doc):
        try:
            docs = cloudantManager.get_all_docs(db)
            for doc in docs:
                if id_doc == doc['id']:
                    return "ok"
        except:
            return "error"