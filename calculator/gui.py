"""
Interfaz gráfica de calculadora básica
Módulo de Puesta en Producción Segura - Unidad 0
"""

class CalculatorGUI:
    """Clase para la interfaz de calculadora"""

    def __init__(self):
        """Inicializa la calculadora"""
        self.result = 0

    def add(self, a, b):
        """Suma dos números"""
        return a + b

    def subtract(self, a, b):
        """Resta dos números"""
        return a - b

    def multiply(self, a, b):
        """Multiplica dos números"""
        return a * b

    def divide(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b


if __name__ == "__main__":
    # Ejemplo de uso
    calc = CalculatorGUI()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
