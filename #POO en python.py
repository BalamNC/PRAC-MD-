
# Coche
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, cantidad):
        # Sumamos a la velocidad actual
        self.velocidad = self.velocidad + cantidad
        print("Acelerando... ahora vas a", self.velocidad, "km/h")

    def frenar(self, cantidad):
        # Restamos a la velocidad
        self.velocidad = self.velocidad - cantidad
        # Si la velocidad baja de cero, la dejamos en cero por seguridad
        if self.velocidad < 0:
            self.velocidad = 0
        print("Frenando... ahora vas a", self.velocidad, "km/h")

    def mostrar_info(self):
        print("Coche informacion")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad actual:", self.velocidad, "km/h")


#Cuenta Bancaria
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Se depositaron:", cantidad)
        print("Saldo nuevo:", self.saldo)

    def retirar(self, cantidad):
        # Primero revisamos si el dinero alcanza
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            print("Retiraste:", cantidad)
            print("Te queda:", self.saldo)
        else:
            print("No tienes dinero suficiente para ese retiro")

    def mostrar_saldo(self):
        print("Titular de la cuenta:", self.titular)
        print("Saldo actual:", self.saldo)


#Rectangulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        area = self.ancho * self.alto
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.ancho + self.alto)
        return perimetro

    def mostrar_info(self):
        # Guardamos los resultados en variables antes de imprimir para que sea claro
        resultado_area = self.calcular_area()
        resultado_perimetro = self.calcular_perimetro()
        
        print("Rectangulo")
        print("Ancho:", self.ancho)
        print("Alto:", self.alto)
        print("El área es:", resultado_area)
        print("El perímetro es:", resultado_perimetro)


#Acciones

print("Prueba del coche")
mi_carro = Coche("Mazda", "2 i Sport", "Rojo")
mi_carro.acelerar(50)
mi_carro.mostrar_info()

print("Prueba de la cuenta")
mi_cuenta = CuentaBancaria("Balam Alain")
mi_cuenta.depositar(1000)
mi_cuenta.retirar(400)
mi_cuenta.mostrar_saldo()

print("Prueba del rectanguloO")
mi_dibujo = Rectangulo(10, 5)
mi_dibujo.mostrar_info()