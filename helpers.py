from datos import *
from colorama import Fore,Style

def crear_vector(contenido: any, dimension: int) -> list:
    """Crea un vector repitiendo el "contenido" en cada uno de los espacios defiinidos por "dimension"
    Args:
        contenido (any): Contenido que llenara los indices del array (Ej: None)
        dimension (int): Cantidad de indices o posiciones que tendra el array

    Returns:
        list: Devuelve una lista "cruda"
    """
    vector = [contenido] * dimension
    return vector

def agregar_valor_lista(lista: list, nuevo_valor):
    """Toma una lista, y crea una nueva con el tamaño de la ingresada + 1 y luego agrega todos los valores
    de la anterior, mas el nuevo valor


    Args:
        lista (list): Lista a "actualizar"
        nuevo_valor (_type_): Valor nuevo a insertar en la nueva lista

    Returns:
        _type_: Devuelve una nueva lista actualizada
    """
    nueva_lista = crear_vector(None, len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = nuevo_valor
    return nueva_lista

def palabra_normalizada(palabra: str) -> str:
    """Sustituye las primeras letras y las que vienen luego de un espacio por sus respectivas mayusculas

    Args:
        palabra (str): palabra a modificar

    Returns:
        str: palabla con mayusculas en el index 0 y luego de un espacio
    """
    palabra_modificada = ""
    espacio_encontrado = False
    for i in range(len(palabra)):
        if i == 0:
            palabra_modificada += chr(ord(palabra[i]) - 32)
        elif ord(palabra[i]) == 32:
            palabra_modificada += " " + chr(ord(palabra[i+1]) - 32)
            espacio_encontrado = True
        elif espacio_encontrado:
            espacio_encontrado = False
            continue
        else:
            palabra_modificada += palabra[i]
    return palabra_modificada

def normalizar_lista_str(datos: list) -> list:
    """Toma una lista de str (ej: nombres y apellidos) y los devuelve normalizados, 
    con sus mayusculas al comenzar el nombre/apellido

    Args:
        datos (list): lista de strs

    Returns:
        list: lista de strs normalizadas
    """
    lista_modificada = []
    for i in range(len(datos)):
            palabra_modificada = palabra_normalizada(datos[i])
            lista_modificada = agregar_valor_lista(lista_modificada, palabra_modificada)
    return lista_modificada

def imprimir_titulos(subtitulo1: str, subtitulo2: str, titulo: str = None):
    if titulo != None:
        print(Fore.GREEN + titulo)
    print(f"{f"\n{subtitulo1}":<30}", end="")
    print(f"{subtitulo2}\n"+ Style.RESET_ALL)

def ordenar_alfabeticamente(lista: list, extra: list = None) -> list:
    """Ordena alfabeticamente una lista, si hay un extra, lo ordena acorde a la primer lista

    Args:
        lista (list): lista a ordenar
        extra (list, optional): lista extra a ordenar. Defaults to None.

    Returns:
        list: una lista con 2 listas dentro: lista ordenada y lista extra/None
    """
    lista_ordenada = lista
    extra_ordenado = extra
    todo_odenado = None
    for i in range(len(lista_ordenada)-1):
        for j in range(i+1,len(lista_ordenada)):
            if lista_ordenada[i] > lista_ordenada[j]:
                auxiliar = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[i]
                lista_ordenada[i] = auxiliar
    
                if extra != None:
                    auxiliar = extra_ordenado[j]
                    extra_ordenado[j] = extra_ordenado[i]
                    extra_ordenado[i] = auxiliar
    todo_odenado = lista_ordenada
    if extra != None:
        todo_odenado = [lista_ordenada, extra_ordenado]
    return todo_odenado

def añadir_turno(turnos: list, profesionales: list, servicios: list, pro_seleccionado: str, serv_seleccionado: str) -> list:
    """Añade un turno a consulta, vacunacion o quirurgico, dependiendo el servicio.
    Lo acomoda en la matriz segun el indice del profesional y el servicio

    Returns:
        _type_: matriz de turnos actualizada
    """
    for i in range(len(turnos)):
        for j in range(len(turnos[0])):
            if pro_seleccionado == palabra_normalizada(profesionales[i]) and serv_seleccionado == palabra_normalizada(servicios[j]):
                    turnos[i][j] += 1
                    break
    return turnos

def total_turnos(turnos: list) -> list:
    total_turnos = 0
    for i in range(len(turnos)):
        for j in range(len(turnos[0])):
            total_turnos += turnos[i][j]
    return total_turnos

def total_turnos_profesional(profesional_index: int, turnos: list) -> list:
    total_turnos = 0
    for i in range(len(turnos[0])):
        total_turnos += turnos[profesional_index][i]
    return total_turnos

def turnos_totales_por_veterinario(profesionales: list, turnos: list) -> None:
    """Calcula la cantidad de turnos totales por profesional

    Args:
        profesionales (list): profesionales
        turnos (list): matriz de turnos
    """
    imprimir_titulos("Profesional","Turnos","TURNOS TOTALES POR PROFESIONAL")
    for i in range(len(profesionales)):
        nombre = profesionales[i]
        nombre_normalizado = palabra_normalizada(nombre)
        print(Fore.YELLOW +f"{nombre_normalizado:<30}", end="")
        print(f"{total_turnos_profesional(i,turnos)}")

def lista_turnos_veterinarios(profesionales: list, turnos: list) -> None:
    """Calcula el promedio de turnos por tipo de servicio entre todos los veterinarios

    Args:
        profesionales (list): lista de profesionales
        turnos (list): matriz de turnos
    """
    print(Fore.GREEN +"LISTADO DE TURNOS")
    print(f"{"\nProfesional":<30}", end="")
    print(f"{"Consulta general":<20}", end="")
    print(f"{"Vacunacion":<14}", end="")
    print(f"{"Post-quirurgico"}"+ Style.RESET_ALL)
    for i in range(len(profesionales)):
        nombre = profesionales[i]
        nombre_normalizado = palabra_normalizada(nombre)
        print(Fore.YELLOW +f"{nombre_normalizado:<29}", end="")
        for j in range(len(turnos[0])):
            if j == 0:
                print(f"{turnos[i][j]:<20}", end="")
            elif j == 1:
                print(f"{turnos[i][j]:<14}", end="")
            else:
                print(f"{turnos[i][j]}")

def promedio_turnos_por_servicio(servicios: list, turnos: list) -> None:
    """Calcula el promedio del total de cada servicio entre todos los veterinarios

    Args:
        turnos (list): lista de turnos
    """
    imprimir_titulos("Servicio", "Promedio", "PROMEDIO DE TURNOS POR TIPO DE SERVICIO")
    total_turnos = [0 for _ in range(len(servicios))]
    for i in range(len(turnos)):
        for j in range(len(servicios)):
            total_turnos[j] += turnos[i][j]

    for i in range(len(servicios)):
        promedio = total_turnos[i] / len(turnos)
        print(Fore.YELLOW + f"{palabra_normalizada(servicios[i]):<29}", end="")
        print(f"{promedio}")


def recaudacion_total(precios: list, turnos: list) -> None:
    """Calcula la recaudacion total de la veterinaria

    Args:
        precios (list): lista de precios
        turnos (list): matriz de turnos
    """
    total = 0
    for i in range(len(turnos)):
        for j in range(len(turnos[0])):
            total += turnos[i][j] * precios[j]
    print(Fore.GREEN +"TOTAL RECAUDADO\nClinica Veterinaria 'El Rope'"+ Style.RESET_ALL)
    print(Fore.YELLOW +f"$ {total}")
            
def ordenar_turnos(ordenamiento: list, lista_a_ordenar: list) -> list:
    """Ordena los turnos en base un array de numeros

    Args:
        ordenamiento (list): array con numeros dentro, cada uno equivale al indice a utilizar
        lista_a_ordenar (list): lista a ordenar

    Returns:
        list: lista ordenada
    """
    lista_nueva = [None for _ in range(len(lista_a_ordenar))]
    for i in range(len(ordenamiento)):
        lista_nueva[i] = lista_a_ordenar[ordenamiento[i]]
    return lista_nueva

def recaudacion_por_servicio(profesionales: list, precios: list, turnos: list) -> None:
    """Muestra lo recaudado por cada profesional

    Args:
        profesionales (list): lista de profesionales
        precios (list): lista de precios
        turnos (list): matriz de turnos
    """
    profesionales_lista = normalizar_lista_str(profesionales)
    ordenamiento = [i for i in range(len(profesionales_lista))]
    ordenar_alfabeticamente(profesionales_lista, ordenamiento)
    turnos_ordenados = ordenar_turnos(ordenamiento, turnos)
    imprimir_titulos("Profesional", "Recaudado", "RECAUDACION POR PROFESIONAL")
    for i in range(len(profesionales_lista)):
        print(Fore.YELLOW +f"{profesionales_lista[i]:<29}", end="")
        total_servicios = 0
        for j in range(len(turnos_ordenados[0])):
            total_servicios += turnos_ordenados[i][j] * precios[j]
        print(f"$ {total_servicios}")

def porcentaje_por_servicio(servicios:list, turnos: list) -> None:
    """Muestra el porcentaje de cada tipo de servicio respecto al total general de turnos

    Args:
        servicios (list): lista de servicios
        turnos (list): matriz de turnos
    """
    total_servicios = 0
    total_por_servicio = [0 for _ in range(len(servicios))]
    for i in range(len(turnos)):
        for j in range(len(turnos[0])):
            total_servicios += turnos[i][j]
            total_por_servicio[j] += turnos[i][j]
    imprimir_titulos("Servicios", "Porcentaje de turnos", "PORCENTAJE POR SERVICIO")
    for i in range(len(servicios)):
        servicio_normalizado = servicios[i]
        print(Fore.YELLOW +f"{palabra_normalizada(servicio_normalizado):<29}", end="")
        if total_servicios != 0:
            porcentaje = (total_por_servicio[i]) * 100 / total_servicios
        else:
            porcentaje = 0.0
        print(f"% {porcentaje}")

def profesional_menos_turnos(profesionales: list, turnos: list) -> None:
    """Muestra el veterinario con menor cantidad total de turnos

    Args:
        profesionales (list): lista de profesionales
        turnos (list): matriz de turnos
    """
    profesional_sin_laburo = ""
    cantidad_menor_turnos = 0
    for i in range(len(turnos)):
        cantidad_turnos = 0
        for j in range(len(turnos[0])):
            cantidad_turnos += turnos[i][j]
        if cantidad_menor_turnos > cantidad_turnos or i == 0:
            cantidad_menor_turnos = cantidad_turnos
            profesional_sin_laburo = profesionales[i]
    imprimir_titulos("Profesional", "Cantidad de turnos", "PROFESIONAL CON MENOS TURNOS")
    print(Fore.YELLOW +f"{palabra_normalizada(profesional_sin_laburo):<29}", end="")
    print(f"{cantidad_menor_turnos}")

def porcentaje_turnos_por_profesional(profesionales: list, turnos: list):
    """Muestra el porcentaje de turnos por veterinario respecto al total general

    Args:
        profesionales (list): lista de profesionales
        turnos (list): matriz de turnos
    """
    turnos_total = total_turnos(turnos)
    imprimir_titulos("Profesional", "Porcentaje", "PORCENTAJE TURNOS POR PROFESIONAL")
    for i in range(len(turnos)):
        print(Fore.YELLOW +f"{palabra_normalizada(profesionales[i]):<29}", end="")
        if turnos_total != 0:
            porcentaje = (total_turnos_profesional(i,turnos)) * 100 / turnos_total
        else:
            porcentaje = 0.0
        print(f"% {porcentaje}")

def servicio_mas_solicitado(profesionales: list, servicios:list, turnos: list):
    """Muestra el servicio/s más solicitado/s por cada veterinario

    Args:
        profesionales (list): lista de profesionales
        servicios (list): lista de servicios
        turnos (list): matriz de turnos
    """
    imprimir_titulos("Profesional", "Servicio", "SERVICIO MAS SOLICITADO")
    for i in range(len(turnos)):
        servicio_mas_solicitado = "no hay"
        servicio_mas_solicitado_cantidad = 0
        for j in range(len(turnos[0])):
            if servicio_mas_solicitado_cantidad < turnos[i][j]:
                servicio_mas_solicitado = servicios[j]
                servicio_mas_solicitado_cantidad = turnos[i][j]
        print(Fore.YELLOW +f"{palabra_normalizada(profesionales[i]):<29}", end="")
        print(f"{palabra_normalizada(servicio_mas_solicitado)}")


def servicio_mas_recaudado(servicios: list, precios:list, turnos: list) -> None:
    """Muestra el servicio que mas recaudo

    Args:
        servicios (list): lista de servicios
        precios (list): lista de precios
        turnos (list): lista de turnos
    """
    servicio_top_cantidad = 0
    servicio_top = "no hay"
    for j in range(len(turnos[0])):
        total_servicios = 0
        for i in range(len(turnos)):
            total_servicios += turnos[i][j] * precios[j]
        if servicio_top_cantidad < total_servicios:
            servicio_top_cantidad = total_servicios
            servicio_top = servicios[j]
    imprimir_titulos("Servicio", "Recaudado", "SERVICIO CON MAS RECAUDACION")
    if servicio_top_cantidad != 0:
        print(Fore.YELLOW +f"{palabra_normalizada(servicio_top):<29}", end="")
        print(f"$ {servicio_top_cantidad}")
    else:
        print(Fore.RED +"No hay ningun servicio activo")

def porcentaje_turnos_alfabeticamente(profesionales: list, turnos: list) -> None:
    """Muestra el porcentaje de turnos de cada profesional ordenados alfabeticamente

    Args:
        profesionales (list): lista de profesionales
        turnos (list): lista de turnos
    """
    profesionales_lista = normalizar_lista_str(profesionales)
    ordenamiento = [i for i in range(len(profesionales_lista))]
    ordenar_alfabeticamente(profesionales_lista, ordenamiento)
    turnos_ordenados = ordenar_turnos(ordenamiento, turnos)
    imprimir_titulos("Profesional", "Porcentaje", "PORCENTAJE DE TURNOS")
    turnos_total = total_turnos(turnos_ordenados)
    for i in range(len(turnos_ordenados)):
        print(Fore.YELLOW +f"{profesionales_lista[i]:<29}", end="")
        if turnos_total != 0:
            porcentaje = (total_turnos_profesional(i,turnos_ordenados)) * 100 / turnos_total
        else:
            porcentaje = 0.0
        print(f"% {porcentaje}")
    
    
    
