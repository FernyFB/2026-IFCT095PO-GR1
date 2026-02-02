def mostrar(lista):
    ancho = maxima_cadena(lista)

    print("\033[31;42m")

    print("┌" + (ancho + 2) * "-" + "┐")
    for elemento in lista:
        print("│ " + elemento.ljust(ancho) + " │")

    print("\033[921;107m")

    print("└" + (ancho + 2) * "-" + "┘")
    print(f"En total hay [{len(lista)}] elementos")


def maxima_cadena(lista):
    upper = 0

    for elemento in lista:
        if len(elemento) > upper:
            upper = len(elemento)

    return upper


lista = [
    "patata",
    "melón",
    "sandia",
    "Oliva",
    "Aguacate"
]

lista_grande = [
    "Manzana",
    "Pera",
    "Plátano",
    "Uva",
    "Melocotón",
    "Albaricoque",
    "Ciruela",
    "Cereza",
    "Nectarina",
    "Paraguaya",
    "Platerina",
    "Membrillo",
    "Níspero",
    "Dátil",
    "Higo",
    "Sandía",
    "Melón Piel de Sapo",
    "Melón Galia",
    "Melón Cantalupo",
    "Aguacate",
    "Naranja",
    "Mandarina",
    "Limón",
    "Lima",
    "Pomelo",
    "Clementina",
    "Tangelo",
    "Lima Kaffir",
    "Kumquat",
    "Yuzu",
    "Cidra",
    "Mano de Buda",
    "Calamansi",
    "Naranja sanguina",
    "Lima dedo",
    "Bergamota",
    "Chinotto",
    "Lima dulce",
    "Mapo",
    "Ugli",
    "Fresa",
    "Frambuesa",
    "Arándano azul",
    "Arándano rojo",
    "Mora",
    "Zarzamora",
    "Grosella negra",
    "Grosella roja",
    "Grosella blanca",
    "Uva espina",
    "Saúco",
    "Maqui",
    "Calafate",
    "Moral",
    "Endrina",
    "Cornejo",
    "Goji",
    "Escaramujo",
    "Madroño",
    "Camarina",
    "Piña",
    "Mango",
    "Papaya",
    "Kiwi",
    "Coco",
    "Maracuyá",
    "Granadilla",
    "Guayaba",
    "Chirimoya",
    "Guanábana",
    "Lichi",
    "Rambután",
    "Longan",
    "Mangostino",
    "Carambola",
    "Pitahaya",
    "Durian",
    "Yaca",
    "Tamarindo",
    "Fruta del pan",
    "Zapote negro",
    "Zapote blanco",
    "Mamey",
    "Lúcuma",
    "Feijoa",
    "Kiwano",
    "Tomate de árbol",
    "Uchuva",
    "Pepino dulce",
    "Lulo",
    "Borojó",
    "Curuba",
    "Badea",
    "Higo chumbo",
    "Salak",
    "Jabuticaba",
    "Ackee",
    "Cupuaçu",
    "Açaí",
    "Camu camu",
    "Acerola",
    "Noni",
    "Mamoncillo",
    "Jocote",
    "Nance",
    "Capulín",
    "Pacay",
    "Sapotilla",
    "Santol",
    "Fruta milagrosa",
]

mostrar(lista_grande)
