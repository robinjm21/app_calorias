import sqlite3

DB_NAME = "calorias.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sesiones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        peso REAL,
        tiempo REAL,
        met REAL,
        calorias REAL
        )
    """)
    conn.commit()
    conn.close()

def registrar_sesion(fecha, peso, tiempo, met, calorias):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sesiones (fecha, peso, tiempo, met, calorias) VALUES (?, ?, ?, ?, ?)",
        (fecha, peso, tiempo, met, calorias))

    conn.commit()
    conn.close()

def obtener_historial():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, calorias FROM sesiones ORDER BY fecha")
    data = cursor.fetchall()
    conn.close()
    return data

# Ejecutar la creacion de la tabla la primera vez 
crear_tabla()

def calcular_calorias(peso, tiempo, met):
    # tiempo en minutos -> converti a horas
    return met * peso * (tiempo / 60)

def crear_tabla_logros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            calorias_meta REAL,
            logrado INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def insetar_logros_iniciales():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM logros")
    count = cursor.fetchone()[0] or 0
    if count > 0:
        conn.close()
        return
    logros = [
        ("Nivel 1", "Quema 500 calorias", 500),
        ("Nivel 2", "Quema 1000 calorias", 1000),
        ("Nivel 3", "Quema 2000 calorias", 2000)
    ]
    for nombre, desc, meta in logros:
        cursor.execute(
            "INSERT OR IGNORE INTO logros (nombre, descripcion, calorias_meta) VALUES (?, ?, ?)",
            (nombre, desc, meta),
        )
    conn.commit()
    conn.close()

crear_tabla_logros()
insetar_logros_iniciales()

def total_calorias():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(calorias) FROM sesiones")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0

def verificar_logros():
    total = total_calorias()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, calorias_meta, logrado FROM logros")
    logros = cursor.fetchall()
    nuevos = []
    for l in logros:
        if total >= l[2] and l[3] == 0:
            cursor.execute("UPDATE logros SET logrado = 1 WHERE id = ?", (l[0],))
            nuevos.append(l[1])
    conn.commit()
    conn.close()
    return nuevos

def crear_tabla_logros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            calorias_meta REAL,
            logrado INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def cargar_logros_iniciales():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM logros")
    count = cursor.fetchone()[0] or 0
    if count > 0:
        conn.close()
        return
    logros = [
        ("Calentando motores", "Quema tur primeras 300 calorias.", 300),
        ("Sudor y esfuerzo", "Alcanza las 1000 calorias totales.", 1000),
        ("Atleta", "Supera las 2000 calorias totales.", 2000),
    ]
    for nombre, desc, meta in logros:
        cursor.execute(
            """
            INSERT OR IGNORE INTO logros (nombre, descripcion, calorias_meta) VALUES (?, ?, ?)
            """,
            (nombre, desc, meta),
        )
    conn.commit()
    conn.close()

crear_tabla_logros()
cargar_logros_iniciales()

def verificar_logros():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT nombre, calorias_meta, logrado FROM logros")
    logros = c.fetchall()

    c.execute("SELECT SUM(calorias) FROM sesiones")
    total = c.fetchone()[0] or 0

    nuevos = []
    for nombre, meta, logrado in logros:
        if total >= meta and not logrado:
            nuevos.append(nombre)
            c.execute("UPDATE logros SET logrado = 1 WHERE nombre = ?", (nombre,))
    conn.commit()
    conn.close()
    return nuevos


