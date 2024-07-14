class App:
  def __init__(self,nombre,peso):
    self.nombre = nombre
    self.peso = peso
    
    self.Mostrar_app()


  def Mostrar_app(self):
    print(f'La app se llama {self.nombre} y pesa {self.peso}')


app = App('Subway surf','123Mb')


