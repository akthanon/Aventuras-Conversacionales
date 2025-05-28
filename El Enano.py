import os
def choripan(texto):
    os.system("cls")
    input(texto)
def opciones(texto):
    os.system("cls")
    salida=input(texto)
    return salida

while True:
    choripan("Bienvenido a la historia. ")

    for i in range(5):
        choripan(f"Iniciando en {5-i}")

    bloque_texto="""Estas en una cabaña en medio de un bosque. 
Se te acerca un enano tocando a la puerta vendiendo minerales. 
Lo miras muy asustado. """
    bloque_texto=bloque_texto.split("\n")
    for linea in bloque_texto:
        choripan(linea)
    opcion=0

    print("¿Qué haces?")
    print("1) Robarle todo")
    print("2) Comprarle minerales")
    opcion=int(input("Introduce la Opción: "))

    if opcion==1:
        choripan("Haz decidido robarle todo y ahora te metieron a la carcel. ")
        print("¿Qué haces?")
        print("1) Escapar")
        print("2) Esperar tu condena")
        opcion=int(input("Introduce la Opción: "))
        if opcion==1:
            choripan("Escapaste de la carcel. ")
            print("¿Qué haces?")
            print("1) Buscar un nuevo hogar")
            print("2) Ir a vengarte del enano")
            opcion=int(input("Introduce la Opción: "))
            if opcion==1:
                choripan("Te perdiste y ahora estás en la antartida. ")
                print("¿Qué haces?")
                print("1) Convertirte en pinguino.")
                print("2) Hacer una fogata para calentarte. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Ya eres un pinguino pero un oso te quiere comer. ")
                    print("¿Qué haces?")
                    print("1) Dejarte comer")
                    print("2) Enfrentar al oso en un duelo epico a muerte oso pinguino. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Creas una fogate e incendias la antartida. ")
                    print("¿Qué haces?")
                    print("1) Apagar el fuego")
                    print("2) Hacerte bolita. ")
                    opcion=int(input("Introduce la Opción: "))
            if opcion==2:
                choripan("Te enfrentaste a un duelo a muerte con el enano y ahora eres nivel 100. ")
                print("¿Qué haces?")
                print("1) Conquistar el mundo con tus nuevos super poderes.")
                print("2) Subir al nivel 1000. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("El mundo es tuyo y ya no tienes nada mas que hacer. ")
                    print("¿Qué haces?")
                    print("1) Te suicidas")
                    print("2) Te enfrentas a dios para conquistar el universo. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Eres mas poderoso que dios. ")
                    print("¿Qué haces?")
                    print("1) Reiniciar el ciclo del universo")
                    print("2) Enfrentar al diablo. ")
                    opcion=int(input("Introduce la Opción: "))
        if opcion==2:
            choripan("Esperas tu condena y te dan 2 dias de carcel. ")
            print("¿Qué haces?")
            print("1) Te conviertes en burro")
            print("2) Escapas sin esperar tu condena")
            opcion=int(input("Introduce la Opción: "))
            if opcion==1:
                choripan("Te convertiste en burro y ahora estudias TI en la UTC. ")
                print("¿Qué haces?")
                print("1) Hackear la nasa.")
                print("2) Hackear la vida. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Hackeaste la nasa y descubres viajes en el tiempo. ")
                    print("¿Qué haces?")
                    print("1) Viajo al inicio del universo")
                    print("2) Viajo al fin del universo. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Hackeaste la vida y ahora eres inmortal. ")
                    print("¿Qué haces?")
                    print("1) Reinicio la vida")
                    print("2) Elimino la inmortalidad. ")
                    opcion=int(input("Introduce la Opción: "))
            if opcion==2:
                choripan("Escapas desnudo de la carcel. ")
                print("¿Qué haces?")
                print("1) Ir a una playa nudista.")
                print("2) Pasarte Dark Souls en la vida real. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Te bañas en la playa y te encuentras un tiburón. ")
                    print("¿Qué haces?")
                    print("1) Te comerme al tiburon")
                    print("2) Pedir ayuda al salvavidas nudista. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Juegas dark souls en la vida real pero sigues desnudo. ")
                    print("¿Qué haces?")
                    print("1) Te enfrentas a un enemigo esqueleto")
                    print("2) Haces speedrun al lvl 1. ")
                    opcion=int(input("Introduce la Opción: "))
    if opcion==2:
        choripan("Compras todos los minerales y quedas en la pobreza. ")
        print("¿Qué haces?")
        print("1) Echarle ganas")
        print("2) Irte a vivir a tijuana")
        opcion=int(input("Introduce la Opción: "))
        if opcion==1:
            choripan("Le echas ganas pero quedas mas pobre. ")
            print("¿Qué haces?")
            print("1) Jugar a la loteria")
            print("2) Chambear en el soriana")
            opcion=int(input("Introduce la Opción: "))
            if opcion==1:
                choripan("Juegas la loteria y ganas 10,000 pesos. ")
                print("¿Qué haces?")
                print("1) Los inviertes en criptomonedas.")
                print("2) Te los gastas en el teibol. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Te convertiste en criptobro y te mandan a matar. ")
                    print("¿Qué haces?")
                    print("1) Escapas hacia pluton")
                    print("2) Peleas hasta la muerte. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("En el teibol conoces al amor de tu vida. ")
                    print("¿Qué haces?")
                    print("1) Me caso con la teibolera")
                    print("2) Ignoro a la teibolera. ")
                    opcion=int(input("Introduce la Opción: "))
            if opcion==2:
                choripan("Chambeas en el soriana. ")
                print("¿Qué haces?")
                print("1) Volverme jefe.")
                print("2) Volverme esclavo. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Te vuelves jefe pero te buscan por evadir impuestos. ")
                    print("¿Qué haces?")
                    print("1) Te enfrentas al SAT")
                    print("2) Entras al narco. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Vives feliz hasta los 100 años pero con sueldo de esclavo. ")
                    print("¿Qué haces?")
                    print("1) Espero mi muerte de viejo")
                    print("2) Me enfrento al diablo. ")
                    opcion=int(input("Introduce la Opción: "))
        if opcion==2:
            choripan("Te vas a vivir a tijuana. ")
            print("¿Qué haces?")
            print("1) Viajas a estados unidos")
            print("2) Te quedas a vivir para siempre")
            opcion=int(input("Introduce la Opción: "))
            if opcion==1:
                choripan("Ahora eres gringo. ")
                print("¿Qué haces?")
                print("1) Shut up moderfucker.")
                print("2) I dont spik ingliz. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Do you want to die?. ")
                    print("¿Qué haces?")
                    print("1) Yes")
                    print("2) No but yes. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Te regresan a México. ")
                    print("¿Qué haces?")
                    print("1) Te enfrentas a donald trump")
                    print("2) Te enfrentas a sheinbaum. ")
                    opcion=int(input("Introduce la Opción: "))
            if opcion==2:
                choripan("Entras al cartel de la tia Juana. ")
                print("¿Qué haces?")
                print("1) Volverme jefe de narcos.")
                print("2) Ser puntero. ")
                opcion=int(input("Introduce la Opción: "))
                if opcion==1:
                    choripan("Eres jefe de los narcos. ")
                    print("¿Qué haces?")
                    print("1) Le declaro la guerra a estados unidos")
                    print("2) Le declaro el amor al amor de mi vida. ")
                    opcion=int(input("Introduce la Opción: "))
                if opcion==2:
                    choripan("Te atrapa el cartel rival. ")
                    print("¿Qué haces?")
                    print("1) Ya valiste vrg morro")
                    print("2) Ya valiste vrg morro. ")
                    opcion=int(input("Introduce la Opción: "))

    choripan("HAZ MUERTO")
    choripan("FIN DE LA HISTORIA")
    final=input("¿Deseas Reiniciar la Historia? (si) (no): ")
    if final=="si" or final=="yes" or final == 1:
        break
