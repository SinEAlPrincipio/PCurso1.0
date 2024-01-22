class vehiculo():
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca  = marca
        self.color = color
        self.avanza= False
        self.frena = False
        self.gira = False
        
    def avanzar(self):
        self.avanza = True
    
    def frenar(self):
        self.frena = True
        
    def girar(self):
        self.gira = True
        
    def imprimir(self):
        print(f'matricula: {self.matricula} \n modelo: {self.modelo} \n marca: {self.marca} \n color: {self.color} \n'
              f'avanzar : {self.avanza} \n frenar : {self.frena} \n girar : {self.gira} \n')
        
class Moto(vehiculo):
    def __init__(self, matricula, modelo, marca, color, cilindraje):
        super().__init__(matricula, modelo, marca, color,)
        self.cilindraje = cilindraje
        

moto1= Moto("HYC88F", 2021, "YAMAHA", "NEGRO", "150CC")
print("Cilindraje :" + str(moto1.cilindraje))
moto1.avanzar()
moto1.girar()
moto1.frenar()
moto1.imprimir()