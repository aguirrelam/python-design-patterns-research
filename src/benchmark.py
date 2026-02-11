import timeit
import tracemalloc
import statistics
import csv
import sys

# Importación de tus módulos (asegúrate de que estén en la misma carpeta)
import p1_control
import p2_creacional
import p3_estructural
import p4_comportamiento

def benchmark_function(name, func, iterations=5000):
    # 1. Medición de Memoria
    tracemalloc.start()
    func() # Ejecución de calentamiento
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    memory_peak_mb = peak / 10**6

    # 2. Medición de Tiempo
    timer = timeit.Timer(func)
    try:
        times = timer.repeat(repeat=5, number=iterations)
        avg_time_per_call = statistics.mean([t / iterations for t in times])
    except Exception as e:
        print(f"Error en {name}: {e}")
        avg_time_per_call = 0

    return {
        "Variant": name,
        "Time_avg_sec": avg_time_per_call,
        "Memory_peak_MB": memory_peak_mb
    }

def run_suite():
    results = []
    ITERATIONS = 20000 

    # --- ESCENARIO 1: PROCESAMIENTO DE DOCUMENTOS ---
    data_payload = "Data" * 100 
    p1_sys = p1_control.MonolithicSystem()
    p2_sys = p2_creacional.CreationalSystem()
    p3_sys = p3_estructural.StructuralSystem()

    # P1
    results.append(benchmark_function("P1_Monolith_Docs", 
                   lambda: p1_sys.execute_document_process("pdf", data_payload), ITERATIONS))
    # P2
    results.append(benchmark_function("P2_Factory_Docs", 
                   lambda: p2_sys.execute_document_process("pdf", data_payload), ITERATIONS))
    # P3
    results.append(benchmark_function("P3_Decorator_Docs", 
                   lambda: p3_sys.execute_enhanced_process("pdf", data_payload, False), ITERATIONS))

    # --- ESCENARIO 2: VENTAS E-COMMERCE ---
    price_val = 1000
    p4_sys = p4_comportamiento.BehavioralSystem()
    p4_sys.attach(p4_comportamiento.InventoryDepartment())
    p4_sys.attach(p4_comportamiento.AnalyticsDepartment())
    p4_sys.set_strategy(p4_comportamiento.BlackFridayStrategy())

    # P1
    results.append(benchmark_function("P1_Monolith_Sales", 
                   lambda: p1_sys.execute_ecommerce_discounts("VIP", price_val, 1), ITERATIONS))
    # P4
    results.append(benchmark_function("P4_StrategyObserver_Sales", 
                   lambda: p4_sys.process_sale(price_val), ITERATIONS))

    # Guardar a CSV
    filename = "benchmark_results.csv"
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, results[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(results)
    
    return filename

# Ejecutar
if __name__ == "__main__":
    archivo = run_suite()
    print(f"Resultados guardados en {archivo}")