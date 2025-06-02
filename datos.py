
datos_usuarios = ["carlitos"]

datos_passwords = ["1234"]
 
datos_profesionales = [
    "neiner, maximiliano" ,
    "villegas, octavio" ,
    "cardozo, marina" ,
    "baus, christian" ,
    "luccheta, giovanni" ,
    "fernández, david" ,
    "ochoa, gonzalo" ,
    "gatto, catriel" ,
    "fernández, mariano" ,
    "bustos gil, felipe"
]
    
datos_servicios = [
    "consulta general", 
    "vacunación", 
    "control post-quirúrgico"
]

datos_precios = [
    15000,
    20000,
    30000
]

datos_turnos = [
    [1, 2, 6],  # t_totales = 9 / recaudado_serv = 15_000, 40_000, 180_000 / r_total = 235_000
    [2, 4, 3],  # t_totales = 9 / recaudado_serv = 30_000, 80_000, 90_000 / r_total = 200_000
    [6, 2, 2],  # t_totales = 10 / recaudado_serv = 90_000, 40_000, 60_000 / r_total = 190_000
    [1, 5, 3],  # t_totales = 9 / recaudado_serv = 15_000, 100_000, 90_000 / r_total = 205_000
    [8, 2, 3],  # t_totales = 13 / recaudado_serv = 120_000, 40_000, 90_000 / r_total = 250_000
    [2, 2, 2],  # t_totales = 6 / recaudado_serv = 30_000, 40_000, 60_000 / r_total = 130_000
    [5, 4, 1],  # t_totales = 10 / recaudado_serv = 75_000, 80_000, 30_000 / r_total = 185_000
    [4, 1, 7],  # t_totales = 12 / recaudado_serv = 60_000, 20_000, 210_000 / r_total = 290_000
    [6, 3, 8],  # t_totales = 17 / recaudado_serv = 90_000, 60_000, 240_000 / r_total = 390_000
    [9, 2, 3],  # t_totales = 14 / recaudado_serv = 135_000, 40_000, 90_000 / r_total = 265_000
]

# Comentarios resumen:
# Turnos totales: 109
#  Recaudado por servicio:
#     Consulta general (15000): 660_000
#     Vacunación (20000):       540_000
#     Control post (30000):     1_150_000
# Recaudación total: 2_350_000