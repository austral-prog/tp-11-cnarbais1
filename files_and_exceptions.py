def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """ 
    try:
        with open(filename, "r") as file:
            contenido = file.read()

        ventas = contenido.split(";")
        data_dict = {}

        for venta in ventas:
            if ":" in venta:
                producto, valor = venta.split(":")
                valor = round(float(valor), 1)  # Convertir a float redondeado a 1 decimal

                if producto not in data_dict:
                    data_dict[producto] = [valor]
                else:
                    data_dict[producto].append(valor)

        return data_dict

    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")



def process_dict(data):
    """
    Para cada producto, imprime el total de ventas y el promedio.
    
    :param data: dict - diccionario a procesar
    :return: None
    """
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")


