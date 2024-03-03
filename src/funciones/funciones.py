from config.db import db
from gridfs import GridFS

fs = GridFS(db) # Crear un sistema de archivos en la base de datos

def guardar_archivo(file):
    fs.put(file, filename=file.filename)

def obtener_archivos(extension):
    files = fs.find({'filename': {'$regex': f'\.{extension}$'}})
    return files
    
