from prometheus_client import start_http_server, Gauge
import random
import time

# Definir una métrica de tipo "Gauge"
gauge_metric = Gauge('my_gauge_metric', 'Descripción de la métrica')

# Función para generar y actualizar la métrica
def generate_metric():
    while True:
        value = random.randint(0, 100)
        gauge_metric.set(value)
        time.sleep(5)  # Actualizar la métrica cada 5 segundos

if __name__ == '__main__':
    # Iniciar el servidor HTTP para exponer las métricas
    start_http_server(port=9091)

    # Generar y actualizar la métrica en segundo plano
    generate_metric()

