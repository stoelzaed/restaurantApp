
from fastapi import APIRouter
from app.db import get_connection

router = APIRouter()

@router.get("/productes")
def get_productes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom_estandard, preu_unitari_sense_iva FROM productes")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1], "preu_sense_iva": float(r[2])} for r in result]
