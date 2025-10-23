# App Calorías

Aplicación simple en Python para registrar sesiones de ejercicio, calcular calorías quemadas a partir de MET, visualizar progreso en gráficos, y desbloquear logros. Cuenta con una interfaz GUI basada en Tkinter y persiste datos en SQLite.

## Características
- Registrar sesión: fecha, peso, tiempo y MET; calcula calorías automáticamente.
- Logros automáticos: se marcan cuando alcanzas metas de calorías acumuladas.
- Notificaciones en la app: ventanas de aviso al desbloquear logros.
- Gráfico de progreso: visualiza calorías por fecha usando `matplotlib`.
- Base de datos local: usa `SQLite` (`calorias.db`) y crea tablas al iniciar.

## Requisitos
- Python 3.9+ (recomendado 3.10 o superior).
- Dependencias (instaladas vía `pip`):
  - `matplotlib`
  - `win10toast` (Windows 10/11; muestra notificaciones del sistema)
- Tkinter viene incluido con la instalación estándar de Python en Windows.

## Instalación
1. Clona el repo:
   ```bash
   git clone https://github.com/robinjm21/app_calorias.git
   cd app_calorias
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
- Ejecuta la aplicación:
  ```bash
  python main.py
  ```
- En la ventana principal:
  - Ingresa `Peso (kg)`, `Tiempo (min)` y `Nivel MET`.
  - Clic en `Guardar Sesion` para registrar y evaluar logros.
  - `Ver Progreso` muestra el gráfico de calorías por fecha.
  - `Reto Semanal` sugiere metas aleatorias.
  - `Ver Logros` lista todos los logros y su estado.

## Persistencia y datos
- La BD `calorias.db` se crea automáticamente en la primera ejecución.
- Las tablas se crean si no existen y se insertan logros iniciales una sola vez.
- El archivo `historial.csv` no se usa por defecto en la app GUI y está ignorado por `.gitignore`.

## Estructura del proyecto
```
app_calorias/
├── base_datos.py       # Conexión SQLite, tablas, inserciones y verificación de logros
├── calculadora.py      # Cálculo de calorías por MET
├── graficos.py         # Gráfico del historial (matplotlib)
├── main.py             # GUI Tkinter y flujo principal
├── calorias.py         # (Reservado / vacío)
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este documento
```

## Notas
- `.gitignore` excluye archivos temporales y bases de datos (`*.db`, `*.sqlite*`) y CSV (`*.csv`, `historial.csv`).
- Si deseas versionar la BD (no recomendado), elimina las reglas correspondientes en `.gitignore` y ten en cuenta que puede contener datos locales sensibles.

## Problemas conocidos
- En algunas instalaciones, `Tkinter` puede faltar; reinstala Python incluyendo `tcl/tk`.
- Las notificaciones del sistema (`win10toast`) requieren Windows 10/11.

## Licencia
- Uso personal/educativo. Ajusta la licencia según tus necesidades.