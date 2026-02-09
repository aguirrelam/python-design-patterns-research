# p2_creational_factory.py
from abc import ABC, abstractmethod

# --- CASO 1: INFRAESTRUCTURA DE DOCUMENTOS ---

class Document(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFDocument(Document):
    def export(self, data):
        return f"<PDF Document>{data}</PDF Document>"

class JSONDocument(Document):
    def export(self, data):
        return f"{{\"data\": \"{data}\"}}"

class DocumentFactory:
    """Factory Method para Documentos"""
    _formats = {
        "pdf": PDFDocument,
        "json": JSONDocument
    }
    
    @staticmethod
    def get_document(format_type):
        target_class = DocumentFactory._formats.get(format_type.lower())
        if not target_class:
            raise ValueError("Formato no soportado")
        return target_class()

# --- CASO 2: INFRAESTRUCTURA DE E-COMMERCE ---

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price, items_count):
        pass

class VIPDiscount(DiscountStrategy):
    def calculate(self, price, items_count):
        return price * 0.85 if price > 1000 else price * 0.90

class RegularDiscount(DiscountStrategy):
    def calculate(self, price, items_count):
        return price * 0.95 if items_count > 10 else price

class DiscountFactory:
    """Factory Method para Descuentos"""
    _types = {
        "VIP": VIPDiscount,
        "REGULAR": RegularDiscount
    }

    @staticmethod
    def get_discount(customer_type):
        target_class = DiscountFactory._types.get(customer_type)
        return target_class() if target_class else None

# --- SISTEMA REFACTORIZADO (EL CLIENTE) ---

class CreationalSystem:
    def __init__(self):
        self.version = "2.0 - Creational"

    def execute_document_process(self, format_type, data):
        print(f"--- P2: Procesando Documento ({format_type}) ---")
        doc = DocumentFactory.get_document(format_type)
        result = doc.export(data)
        print(f"Resultado: {result}")
        return result

    def execute_ecommerce_discounts(self, customer_type, price, items_count):
        print(f"\n--- P2: Calculando Descuento para: {customer_type} ---")
        strategy = DiscountFactory.get_discount(customer_type)
        final_price = strategy.calculate(price, items_count) if strategy else price
        print(f"Precio final: ${final_price:.2f}")
        return final_price