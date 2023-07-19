print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=⠀⠀⠀⠀⠀⠀⠀

          __-------__
      / --------------_ \
     // \ \
     | | | |
     |_|___________|_|
 /-\| |/-\
| _ |\ 0 /| _ |
|(_)| \ ! / |(_)|
|___|__\_____!_____/__|___|
[_________|MEIN1|_________]
 |||| ~~~~~~~~ ||||
 `--' `--'
         Bienvenidos a diseñar tu auto de los sueños.
        
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""")


class carro:
  def __init__(self,marca,modelo,año,color,musica,destino,aire):
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.color = color
    self.aire = False
    self.musica = musica
    self.destino = destino
  
  def ACON(self):
    self.aireon = True
  def ACOFF(self):
    self.aireoff = True
  def describir(self):
    
    if self.aire == True:
      b = "aire dañado"
    else:
      b = "aire frío"
      
      return f"Perfecto!,recuerda que tu carro es un {self.marca} {self.modelo} del año {self.año} color {self.color} y tienes el {b}.Estas escuchando {self.musica} de camino a {self.destino} Buen Viaje👋"

MiCarro = carro("Ford","Mustang",1969,"Gris","Camilo","Carolina","aireON")
Carro2 = carro("Nissan.","Rogue.",2008.,"Gris claro.","Luis Fonsi","Corozal","aireOFF")

marca = input("Escribe cual es la marca del carro de tus sueños ")
print("")
print("")
modelo = input("Ahora que modelo es el carro? ")
print("")
print("")
año = input(" Y de que de que año es?" )
print("")
print("")
color = input("De que color sera el carro?")
print("")
print("")
musica = input( "Que musica escucharas? ")
print("")
print("")
destino = input(  "Cual sera tu destino?")
print("")
print("")
aire = input( "Y por último como está el aire frío o dañado?")

print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")

print("""
        __-------__
     / --------------_ \
   // \ \
  | | | |
 |_|___________|_|
 /-\| |/-\
| _ |\ 0 /| _ |
|(_)| \ ! / |(_)|
|___|__\_____!_____/__|___|
[_________|MEIN1|_________]
 |||| ~~~~~~~~ ||||
 `--' `--'    
""")

car = carro(marca,modelo,año,color,musica,destino,aire)
print(car.describir())
print("")
print("")

print("""                             

    __-------__
      / --------------_ \
     // \ \
     | | | |
     |_|___________|_|
 /-\| |/-\
| _ |\ 0 /| _ |
|(_)| \ ! / |(_)|
|___|__\_____!_____/__|___|
[_________|MEIN1|_________]
 |||| ~~~~~~~~ ||||
 `--' `--'



""") 