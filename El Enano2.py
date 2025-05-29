import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar(texto):
    limpiar_pantalla()
    input(texto)

def elegir_opcion(pregunta, opciones):
    limpiar_pantalla()
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}) {opcion}")
    while True:
        try:
            eleccion = int(input("Elige una opción: "))
            if 1 <= eleccion <= len(opciones):
                return eleccion
        except ValueError:
            pass
        print("Opción inválida. Intenta de nuevo.")

def contar_regresiva(segundos):
    for i in range(segundos, 0, -1):
        mostrar(f"Iniciando en {i}")

def historia_principal():
    mostrar("Bienvenido a la historia.")
    contar_regresiva(5)

    escenas = [
        "Estás en una cabaña en medio de un bosque.",
        "Se te acerca un enano tocando a la puerta vendiendo minerales.",
        "Lo miras muy asustado."
    ]
    for linea in escenas:
        mostrar(linea)

    decision = elegir_opcion("¿Qué haces?", [
        "Robarle todo",
        "Comprarle minerales"
    ])

    if decision == 1:
        historia_robo()
    else:
        historia_compra()

    mostrar("HAZ MUERTO")
    mostrar("FIN DE LA HISTORIA")

def historia_robo():
    mostrar("Has decidido robarle todo y ahora te metieron a la cárcel.")
    decision = elegir_opcion("¿Qué haces?", [
        "Escapar",
        "Esperar tu condena"
    ])

    if decision == 1:
        historia_escape()
    else:
        historia_espera()

def historia_escape():
    mostrar("Escapaste de la cárcel.")
    decision = elegir_opcion("¿Qué haces?", [
        "Buscar un nuevo hogar",
        "Ir a vengarte del enano"
    ])

    if decision == 1:
        historia_antartida()
    else:
        historia_venganza()

def historia_antartida():
    mostrar("Te perdiste y ahora estás en la Antártida.")
    decision = elegir_opcion("¿Qué haces?", [
        "Convertirte en pingüino",
        "Hacer una fogata"
    ])
    if decision == 1:
        mostrar("Ya eres un pingüino pero un oso te quiere comer.")
        elegir_opcion("¿Qué haces?", [
            "Dejarte comer",
            "Duelo épico a muerte oso-pingüino"
        ])
    else:
        mostrar("Creas una fogata e incendias la Antártida.")
        elegir_opcion("¿Qué haces?", [
            "Apagar el fuego",
            "Hacerte bolita"
        ])

def historia_venganza():
    mostrar("Te enfrentaste al enano y ahora eres nivel 100.")
    decision = elegir_opcion("¿Qué haces?", [
        "Conquistar el mundo",
        "Subir al nivel 1000"
    ])
    if decision == 1:
        mostrar("El mundo es tuyo, ya no tienes nada más que hacer.")
        elegir_opcion("¿Qué haces?", [
            "Te suicidas",
            "Enfrentar a Dios"
        ])
    else:
        mostrar("Eres más poderoso que Dios.")
        elegir_opcion("¿Qué haces?", [
            "Reiniciar el universo",
            "Enfrentar al Diablo"
        ])

def historia_espera():
    mostrar("Esperas tu condena y te dan 2 días de cárcel.")
    decision = elegir_opcion("¿Qué haces?", [
        "Convertirte en burro",
        "Escapar sin esperar"
    ])
    if decision == 1:
        historia_burro()
    else:
        historia_desnudo()

def historia_burro():
    mostrar("Te convertiste en burro y estudias TI en la UTC.")
    decision = elegir_opcion("¿Qué haces?", [
        "Hackear la NASA",
        "Hackear la vida"
    ])
    if decision == 1:
        mostrar("Hackeaste la NASA y descubres viajes en el tiempo.")
        elegir_opcion("¿Qué haces?", [
            "Viajar al inicio del universo",
            "Viajar al fin del universo"
        ])
    else:
        mostrar("Hackeaste la vida y ahora eres inmortal.")
        elegir_opcion("¿Qué haces?", [
            "Reiniciar la vida",
            "Eliminar la inmortalidad"
        ])

def historia_desnudo():
    mostrar("Escapas desnudo de la cárcel.")
    decision = elegir_opcion("¿Qué haces?", [
        "Ir a una playa nudista",
        "Pasarte Dark Souls en la vida real"
    ])
    if decision == 1:
        mostrar("Te bañas y te encuentras un tiburón.")
        elegir_opcion("¿Qué haces?", [
            "Comerte al tiburón",
            "Pedir ayuda al salvavidas nudista"
        ])
    else:
        mostrar("Juegas Dark Souls pero sigues desnudo.")
        elegir_opcion("¿Qué haces?", [
            "Enfrentar esqueleto",
            "Hacer speedrun nivel 1"
        ])

def historia_compra():
    mostrar("Compras todos los minerales y quedas en la pobreza.")
    decision = elegir_opcion("¿Qué haces?", [
        "Echarle ganas",
        "Irte a vivir a Tijuana"
    ])
    if decision == 1:
        historia_trabajo()
    else:
        historia_tijuana()

def historia_trabajo():
    mostrar("Le echas ganas pero quedas más pobre.")
    decision = elegir_opcion("¿Qué haces?", [
        "Jugar a la lotería",
        "Trabajar en Soriana"
    ])
    if decision == 1:
        mostrar("Ganas $10,000 en la lotería.")
        elegir_opcion("¿Qué haces?", [
            "Invertir en cripto",
            "Gastarlos en el table dance"
        ])
    else:
        mostrar("Trabajas en Soriana.")
        elegir_opcion("¿Qué haces?", [
            "Volverte jefe",
            "Volverte esclavo"
        ])

def historia_tijuana():
    mostrar("Te vas a vivir a Tijuana.")
    decision = elegir_opcion("¿Qué haces?", [
        "Viajar a EE.UU.",
        "Quedarte para siempre"
    ])
    if decision == 1:
        mostrar("Ahora eres gringo.")
        elegir_opcion("¿Qué haces?", [
            "Shut up motherfucker",
            "I don't speak inglés"
        ])
    else:
        mostrar("Entras al cartel de la tía Juana.")
        elegir_opcion("¿Qué haces?", [
            "Volverte jefe de narcos",
            "Ser puntero"
        ])

# Bucle principal
while True:
    historia_principal()
    reiniciar = input("¿Deseas reiniciar la historia? (si / no): ").strip().lower()
    if reiniciar not in ["si", "yes", "1"]:
        break
