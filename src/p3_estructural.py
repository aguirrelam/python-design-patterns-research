# p3_structural_decorator.py
import functools
import time
from abc import ABC, abstractmethod

# Reutilizamos las interfaces y clases base de P2 (Conceptualmente)
class Document(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFDocument(Document):
    def export(self, data):
        return f"<PDF Document>{data}</PDF Document>"

# --- DECORADORES ESTRUCTURALES ---

class DocumentDecorator(Document):
    """Clase base para decoradores"""
    def __init__(self, wrapped: Document):
        self._wrapped = wrapped

    def export(self, data):
        return self._wrapped.export(data)

class LoggingDecorator(DocumentDecorator):
    """Añade registro de tiempo de ejecución"""
    def export(self, data):
        start_time = time.time()
        print(f"[LOG] Iniciando exportación a las {time.ctime(start_time)}")
        result = self._wrapped.export(data)
        end_time = time.time()
        print(f"[LOG] Exportación finalizada. Duración: {end_time - start_time:.4f}s")
        return result

class EncryptionDecorator(DocumentDecorator):
    """Añade una capa de 'cifrado' (simulado para el experimento)"""
    def export(self, data):
        result = self._wrapped.export(data)
        encrypted_result = f"ENCRYPTED({result})"
        print(f"[SEC] Datos cifrados correctamente.")
        return encrypted_result

# --- SISTEMA ESTRUCTURAL ---

class StructuralSystem:
    def __init__(self):
        self.version = "3.0 - Structural"

    def execute_enhanced_process(self, format_type, data, secure=False):
        print(f"--- P3: Procesando con Decoradores ---")
        
        # 1. Obtenemos el objeto base (podría venir de la Factory de P2)
        if format_type == "pdf":
            doc = PDFDocument()
        
        # 2. Aplicamos capas estructurales dinámicamente
        doc = LoggingDecorator(doc)
        
        if secure:
            doc = EncryptionDecorator(doc)
            
        # 3. El cliente usa el objeto sin saber cuántas capas tiene
        result = doc.export(data)
        print(f"Resultado Final: {result}")
        return result