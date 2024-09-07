class Fresadora:
    def __init__(self,marca,peso,largo,ancho,alto,cantidad_ejes):

        self.marca=marca
        self.peso=peso
        self.largo=largo
        self.ancho=ancho
        self.alto=alto
        self.cantidad_ejes=cantidad_ejes

    def print_details(self):
        return (f"La fresadora {self.marca}-400 es una herramienta de precisión diseñada "
                f"para ofrecer un rendimiento excepcional en el mecanizado de piezas. "
                f"Esta máquina cuenta con las siguientes especificaciones:\n"
                f"- Marca: {self.marca}\n"
                f"- Peso: {self.peso} kg\n"
                f"- Largo: {self.largo} mm\n"
                f"- Ancho: {self.ancho} mm\n"
                f"- Alto: {self.alto} mm\n"
                f"- Cantidad de ejes: {self.cantidad_ejes}\n")



fresadora1= Fresadora("h1",3000,1000,2000,3000,3)

print(fresadora1.print_details())