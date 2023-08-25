import requests
import random
import time

# Configuración de la URL de Prometheus
prometheus_url = "http://prometheus-service.monitoring.svc:9090/api/v1/write"

# Nombres de las métricas simuladas
metric_names = ["app_memory_usage_bytes", "app_cpu_usage_seconds"]

# Función para enviar métricas a Prometheus
def send_metrics(metric_name, value):
    payload = f"{metric_name} {value}\n"
    try:
        response = requests.post(prometheus_url, data=payload, timeout=10)
        response.raise_for_status()  # Levanta una excepción si la respuesta es un error HTTP
        print(f"Metric {metric_name}: {value} sent successfully")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send metric {metric_name}: {e}")

# Simulación de generación de métricas
while True:
    metric_name = random.choice(metric_names)
    value = random.uniform(0, 100)
    send_metrics(metric_name, value)
    time.sleep(10 + random.uniform(-1, 1))  # Espera aleatoria entre 9 y 11 segundos

