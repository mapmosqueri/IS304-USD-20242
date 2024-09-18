# Herencia: desde aquí
class Figura:
    def __init__(self):
        pass

    def clasificar(self):
        pass

class Triangulo(Figura):  # hasta aquí
    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3  # Encapsulamiento: desde aquí

    def es_triangulo(self):
        # Verifica la desigualdad triangular
        return (self.__lado1 + self.__lado2 > self.__lado3 and
                self.__lado1 + self.__lado3 > self.__lado2 and
                self.__lado2 + self.__lado3 > self.__lado1)

    def clasificar(self):
        if not self.es_triangulo():
            return "No es un triángulo"

        # Clasificación por lados
        if self.__lado1 == self.__lado2 == self.__lado3:
            tipo = "Equilátero"
        elif self.__lado1 == self.__lado2 or self.__lado1 == self.__lado3 or self.__lado2 == self.__lado3:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"

        # Clasificación por ángulos (solo si es un triángulo válido)
        if (self.__lado1 ** 2 + self.__lado2 ** 2 == self.__lado3 ** 2 or
                self.__lado1 ** 2 + self.__lado3 ** 2 == self.__lado2 ** 2 or
                self.__lado2 ** 2 + self.__lado3 ** 2 == self.__lado1 ** 2):
            return f"{tipo} y Rectángulo"
        
        return tipo  # hasta aquí

def main():
    while True:
        try:
            lado1 = float(input("Ingrese el lado 1: "))
            lado2 = float(input("Ingrese el lado 2: "))
            lado3 = float(input("Ingrese el lado 3: "))

            tri = Triangulo(lado1, lado2, lado3)
            resultado = tri.clasificar()
            print(f"Clasificación: {resultado}")

            if resultado == "No es un triángulo":
                print("Fin del programa.")
                break
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
#Herencia: Comentarios desde la definición de la clase Figura hasta la definición de la clase Triangulo.
#Encapsulamiento: Comentarios alrededor de los atributos encapsulados (__lado1, __lado2, __lado3) en la clase Triangulo.
