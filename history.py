import os
import sqlite3

def buscar_historial_chrome(dominio):
    # Ruta a la base de datos de historial de Chrome
    user_profile = os.getenv("USERPROFILE") or os.getenv("HOME")
    chrome_history_path = os.path.join(user_profile, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History")
    
    if not os.path.exists(chrome_history_path):
        print("No se encontró el historial de Chrome. Verifica que Chrome esté instalado y configurado correctamente.")
        return

    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(chrome_history_path)
        cursor = conn.cursor()

        # Consulta SQL para buscar URLs que contienen el dominio
        query = "SELECT url, title, visit_count, last_visit_time FROM urls WHERE url LIKE ?"
        cursor.execute(query, (f"%{dominio}%",))

        # Obtener resultados
        resultados = cursor.fetchall()
        
        if resultados:
            print(f"Se encontraron {len(resultados)} resultados para el dominio '{dominio}':\n")
            for url, title, visit_count, last_visit_time in resultados:
                print(f"URL: {url}\nTítulo: {title}\nVisitas: {visit_count}\n")
        else:
            print(f"No se encontraron resultados para el dominio '{dominio}'.")
    
    except sqlite3.OperationalError as e:
        print(f"Error al acceder al historial de Chrome. Asegúrate de que Chrome esté cerrado. Error: {e}")
    
    finally:
        if 'conn' in locals():
            conn.close()

# Ejemplo de uso
dominio = input("Introduce el dominio a buscar (e.g., example.com): ")
buscar_historial_chrome(dominio)
