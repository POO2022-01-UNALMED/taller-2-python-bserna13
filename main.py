class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if color=="rojo":
            self.color="rojo"
        elif color=="verde":
            self.color="verde"
        elif color=="amarillo":
            self.color="amarillo"
        elif color=="negro":
            self.color="negro"
        elif color=="blanco":
            self.color="blanco"
        
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        Asiento.asientos=asientos
        self.marca=marca

        self.motor=motor
        Motor.motor=motor

        self.regitro=registro
        #Auto.cantidadCreados=cantidadCreados

    #@classmethod
    def cantidadAsientos(self):
        contador=0
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None:
                contador+=1

        return contador

    
    def verificarIntegridad(self):
        lista=[]
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None:
                lista.append(i)
        
        for e in lista:
            if (self.asientos[lista[0]].registro!=self.asientos[e].registro):
                return "Las piezas no son originales"
        if((self.asientos)[lista[0]]).registro==self.regitro and self.regitro== (self.motor).registro and (self.motor).registro== ((self.asientos)[lista[0]]).registro :
            return "Auto original"
        
        return "Las piezas no son originales"

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,regis):
        self.registro=regis

    def asignarTipo(self,tip):
        if tip=="electrico":
            self.tipo="electrico"
        elif tip=="gasolina":
            self.tipo="gasolina"




        