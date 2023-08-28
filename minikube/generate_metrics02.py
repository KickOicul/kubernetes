from prometheus_client import start_http_server, Gauge, Counter
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

counter_metric = Counter('my_count_metric', 'test')

def generate_counter_mtr():
#   value = 1.5
    while counter_metric < 30:
        counter_metric.inc(1.6)
        time.sleep(5)
        

if __name__ == '__main__':
    # Iniciar el servidor HTTP para exponer las métricas
    start_http_server(port=9091)

    # Generar y actualizar la métrica en segundo plano
    generate_metric()
    generate_counter_mtr() 

