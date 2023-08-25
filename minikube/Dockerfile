# Usar una imagen base de Python
FROM python

# Copiar el script de la aplicación al contenedor
COPY generate_metrics02.py /app/generate_metrics02.py

# Instalar las dependencias necesarias
RUN pip install prometheus_client

# Establecer el directorio de trabajo
WORKDIR /app

# Ejecutar el script de la aplicación
ENTRYPOINT ["python3", "generate_metrics02.py"]

