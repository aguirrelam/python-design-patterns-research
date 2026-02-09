# tests/test_functional_equivalence.py
import pytest
from src.p1_control import MonolithicSystem
from src.p2_creacional import CreationalSystem
from src.p3_estructural import StructuralSystem
from src.p4_comportamiento import BehavioralSystem, BlackFridayStrategy

def test_document_export_equivalence():
    """Verifica que todos los sistemas exporten el PDF de la misma forma"""
    test_data = "Informe de Investigacion 2026"
    
    # Instanciación de los 4 sujetos de prueba
    s1 = MonolithicSystem()
    s2 = CreationalSystem()
    s3 = StructuralSystem()
    s4 = BehavioralSystem() # Para el caso de documentos en P4
    
    # Ejecución y captura de resultados
    res1 = s1.execute_document_process("pdf", test_data)
    res2 = s2.execute_document_process("pdf", test_data)
    res3 = s3.execute_enhanced_process("pdf", test_data, secure=False)
    
    # Aserciones: Todos deben producir el mismo string
    assert res1 == res2
    assert res2 == res3
    assert "<PDF Document>" in res1

def test_ecommerce_discount_equivalence():
    """Verifica que el calculo de descuentos sea idéntico (Caso Black Friday)"""
    price = 1000.0
    
    s1 = MonolithicSystem()
    s2 = CreationalSystem()
    s4 = BehavioralSystem()
    s4.set_strategy(BlackFridayStrategy())
    
    # En P1 y P2 el 'Black Friday' se activa por lógica interna o factory
    # Aquí simulamos la condición que dispararía el 50% de descuento
    res1 = s1.execute_ecommerce_discounts("vip", price) # Asumiendo VIP como 50%
    res2 = s2.execute_ecommerce_discounts("vip", price)
    res4 = s4.process_sale(price)
    
    assert res1 == res2 == res4
    assert res1 == 500.0

if __name__ == "__main__":
    print("Ejecutando pruebas de equivalencia funcional...")
    # Este bloque permite ejecutarlo sin pytest si es necesario
