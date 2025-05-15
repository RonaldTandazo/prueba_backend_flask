1. Crear el entorno virtual, aplicar este comando: 
    - Linux o Mac: python3 -m venv venv
    - Windows: python -m venv venv

2. Activar el entorno virtual, aplicar este comando:
    - Linux o Mac: source venv/bin/activate
    - Windows: venv\Scripts\activate

3. Por último instalar las dependencias, aplicar el comando:
    - pip install -r requirements.txt

4. Levantar el proyecto con el comando: python main.py

NOTA: Las credenciales utilizadas en el .env para la conexión a la DB corresponden a la plataforma Supabase, la cual proporciona servicios de DB PGSQL Online