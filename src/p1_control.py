# p1_monolithic_baseline.py
import math

class MonolithicSystem:
    def __init__(self):
        self.version = "1.0 - Baseline"

    def execute_document_process(self, format_type, data):
        """Caso 1: Procesamiento de Documentos con lógica anidada."""
        print(f"--- Iniciando Procesamiento de Documento ({format_type}) ---")
        
        # Validación y Transformación (Lógica mezclada)
        if not data:
            return "Error: Sin datos"
        
        # Simulación de exportación mediante estructuras condicionales masivas
        if format_type.lower() == "pdf":
            result = f"<PDF Document>{data}</PDF Document>"
        elif format_type.lower() == "json":
            result = f"{{\"data\": \"{data}\"}}"
        elif format_type.lower() == "xml":
            result = f"<xml><data>{data}</data></xml>"
        elif format_type.lower() == "csv":
            result = f"header,data\n1,{data}"
        else:
            raise ValueError("Formato no soportado")
            
        print(f"Resultado: {result}")
        return result

    def execute_ecommerce_discounts(self, customer_type, price, items_count):
        """Caso 2: Motor de Descuentos con múltiples ramas de decisión."""
        print(f"\n--- Calculando Descuento para: {customer_type} ---")
        
        final_price = price
        
        # Lógica de negocio hard-coded
        if customer_type == "REGULAR":
            if items_count > 10:
                final_price = price * 0.95  # 5% Descuento por volumen
            else:
                final_price = price
        elif customer_type == "VIP":
            if price > 1000:
                final_price = price * 0.85  # 15% Descuento VIP Premium
            else:
                final_price = price * 0.90  # 10% Descuento VIP Estándar
        elif customer_type == "ESTUDIANTE":
            final_price = price * 0.80      # 20% Fijo
        else:
            final_price = price
            
        print(f"Precio final: ${final_price:.2f}")
        return final_price

# Simulación de ejecución
if __name__ == "__main__":
    system = MonolithicSystem()
    system.execute_document_process("pdf", "Reporte de Investigación")
    system.execute_ecommerce_discounts("VIP", 1200, 5)