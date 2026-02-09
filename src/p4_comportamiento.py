# p4_behavioral_patterns.py
from abc import ABC, abstractmethod

# --- PATRÓN OBSERVER: INFRAESTRUCTURA DE NOTIFICACIÓN ---

class Observer(ABC):
    @abstractmethod
    def update(self, event_data):
        pass

class InventoryDepartment(Observer):
    def update(self, event_data):
        print(f"[Observer] Almacén: Ajustando stock para venta de ${event_data:.2f}")

class AnalyticsDepartment(Observer):
    def update(self, event_data):
        print(f"[Observer] Analytics: Registrando métricas de tendencia.")

# --- PATRÓN STRATEGY: INFRAESTRUCTURA DE NEGOCIO ---

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class BlackFridayStrategy(DiscountStrategy):
    def calculate(self, price):
        return price * 0.50 if price > 500 else price * 0.80

# --- SISTEMA DE COMPORTAMIENTO (EL SUJETO) ---

class BehavioralSystem:
    def __init__(self):
        self.version = "4.0 - Behavioral"
        self._observers = []
        self._strategy = None

    # Métodos del Observer
    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, total):
        for observer in self._observers:
            observer.update(total)

    # Métodos del Strategy
    def set_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def process_sale(self, raw_price):
        print(f"--- P4: Procesando Venta con Estrategia y Observadores ---")
        
        # Ejecución del algoritmo (Strategy)
        final_price = self._strategy.calculate(raw_price) if self._strategy else raw_price
        print(f"Venta procesada. Precio Final: ${final_price:.2f}")
        
        # Notificación (Observer)
        self.notify(final_price)
        return final_price

# --- SIMULACIÓN EXPERIMENTAL ---
if __name__ == "__main__":
    system = BehavioralSystem()
    
    # Configuración dinámica
    system.attach(InventoryDepartment())
    system.attach(AnalyticsDepartment())
    system.set_strategy(BlackFridayStrategy())
    
    # Ejecución
    system.process_sale(1000)