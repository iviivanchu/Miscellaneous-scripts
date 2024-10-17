import sqlite3
import os
from datetime import datetime, timedelta
import sys

def getHistoryResults(dia, hora, user_profile):
    """
    """
    history_path = os.path.join(user_profile, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")
    
    if not os.path.exists(history_path):
        return "History not found"

    conn = sqlite3.connect(history_path)
    cursor = conn.cursor()
    
    fecha_hora = datetime.strptime(f"{dia} {hora}", "%Y-%m-%d %H:%M:%S")

    base_time = datetime(1601, 1, 1)
    timestamp_inicial = int((fecha_hora - base_time).total_seconds() * 1000000)
    timestamp_final = int(((fecha_hora + timedelta(minutes=15)) - base_time).total_seconds() * 1000000)

    query = f"""
    SELECT urls.url, urls.title, visits.visit_time
    FROM urls, visits
    WHERE urls.id = visits.url
    AND visits.visit_time BETWEEN {timestamp_inicial} AND {timestamp_final}
    ORDER BY visits.visit_time DESC
    """
    
    cursor.execute(query)
    
    registros = cursor.fetchall()
    if registros:
        for registro in registros:
            url = registro[0]
            titulo = registro[1]
            visit_time = base_time + timedelta(microseconds=registro[2])
            sys.stdout.write(f"Time: {visit_time}, Page: {titulo}, URL: {url}")
    else:
        sys.stdout.write("No history found on that time")
    
    conn.close()

user_profile = ""
dia = "2024-10-13"  # Día en formato YYYY-MM-DD
hora = "14:00:00"   # Hora en formato HH:MM:SS
getHistoryResults(dia, hora)
