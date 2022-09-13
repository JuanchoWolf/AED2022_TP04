class Popularidad:
  def __init__(self, mes, estrellas, cant_proy):
    self.mes = mes
    self.estrellas = estrellas
    self.cant_proy = cant_proy

  def __str__(self):
    return "{:^6} | {:>10.2f}k | {:>10}".format(self.mes, self.estrellas, self.cant_proy)


def cabera_popularidad():
  return "{:^6} | {:>11} | {:>10}".format("Mes", "Estrellas", "Proyectos") + "\n" + "-" * 34


if __name__ == "__main__":
  popularidad = Popularidad(1, 100, 10)
  print(cabera_popularidad())
  print(popularidad)