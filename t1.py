import random as r
from time import sleep
import os
import math


class Utils:
    """Clase de utilidad"""

    def cls():
        """Permite limpiar la consola con soporte multi-sistema"""
        os.system("cls" if os.name == "nt" else "clear")

    def blend_color(c1, c2, t):
        """Mezcla dos colores con una fuerza dada
        Args:
            c1: list. Debe tener la forma de una lista (R, G, B) con un valor de 0 a 1.
            c2: list. Debe tener la forma de una lista (R, G, B) con un valor de 0 a 1.
            t: float. Fuerza entre 0 y 1 de mezcla.
        Returns:
            El color mezclado en una lista de 3 elementos: R, G, B.
        """
        return [float(c1[i]) * (1.0 - t) + float(c2[i]) * t for i in [0, 1, 2]]


class Constantes:
    """Constantes utiles"""

    TIPO_TO_SISTEMA = {6: "BINARIO", 20: "OCTAL", 100: "HEXADECIMAL"}
    """Convierte la elección numérica del usuario a la cadena de texto de la base correspondiente"""
    TITULOS = [
        "Invitado",
        "Novato Binario",
        "Principiante Octal",
        "Adepto Hexadecimal",
        "Maestro Decimal",
        "Guerrero de la Base 2",
        "Campeón de la Base 8",
        "Leyenda de la Base 16",
        "Conquistador del Sistema Decimal",
        "Alquimista de Bits",
        "Mago de Bytes",
        "Señor de los Registros",
        "Dios de las Puertas Lógicas",
        "Arquimago de la Computación",
        "Ingeniero de la Realidad Virtual",
        "Creador de Universos Digitales",
        "Dominador del Ciberespacio",
        "Explorador de la Nube",
        "Maestro del Big Data",
        "Arquitecto de la Inteligencia Artificial",
        "Hackeador del Multiverso",
        "Semidiós de los Algoritmos",
        "Titán de la Programación",
        "Omnipotente del Código",
        "Demiurgo de los Sistemas Operativos",
        "Avatar de la Computación Cuántica",
        "Ascendido a la Singularidad",
        "Dios de los Bits y Bytes",
        "Emperador del Ciberespacio",
        "Creador del Metaverso",
    ]
    """Titulos de un nivel 0 a 30, solo para entretenimiento"""
    COLORES_TITULOS = [
        "#FF0000",  # Rojo
        "#FF4500",  # Naranja
        "#FFFF00",  # Amarillo
        "#00FF00",  # Verde
        "#00FFFF",  # Cian
        "#0000FF",  # Azul
        "#800080",  # Violeta
        "#FF00FF",  # Magenta
        "#FF8C00",  # Naranja oscuro
        "#FFFF80",  # Amarillo pálido
        "#80FF00",  # Verde claro
        "#00FFFF",  # Cian brillante
        "#0080FF",  # Azul marino
        "#8000FF",  # Violeta oscuro
        "#FF0080",  # Magenta oscuro
        "#FF69B4",  # Rosa
        "#FFD700",  # Dorado
        "#00FA9A",  # Verde turquesa
        "#00BFFF",  # Azul eléctrico
        "#4B0082",  # Índigo
        "#FF1493",  # Rosa chicle
        "#FFA500",  # Naranja claro
        "#FFFFE0",  # Amarillo cremoso
        "#32CD32",  # Verde lima
        "#00CED1",  # Azul cielo
        "#4169E1",  # Azul real
        "#9400D3",  # Violeta intenso
        "#DA70D6",  # Orquídea
        "#FFC0CB",  # Rosa claro
        "#FF8000",  # Naranja intenso
        "#FFFF00",  # Amarillo brillante
        "#00FF7F",  # Verde esmeralda
        "#00BFFF",  # Azul eléctrico
        "#8A2BE2",  # Violeta azul
        "#DB7093",  # Rosa pálido
        "#FF7F50",  # Coral
        "#FFFF00",  # Amarillo dorado
        "#228B22",  # Verde bosque
        "#00FFFF",  # Cian brillante
        "#4682B4",  # Azul acero
        "#9932CC",  # Púrpura
        "#E066FF",  # Lavanda
        "#FFB6C1",  # Rosa pálido
        "#FF4500",  # Naranja intenso
        "#FFFF00",  # Amarillo brillante
        "#008000",  # Verde oscuro
        "#00FFFF",  # Cian brillante
        "#191970",  # Azul medianoche
        "#8B008B",  # Violeta oscuro
        "#BA55D3",  # Púrpura claro
        "#FF69B4",  # Rosa
        "#FF8C00",  # Naranja oscuro
        "#FFFF80",  # Amarillo pálido
        "#3CB371",  # Verde agua
        "#00FFFF",  # Cian brillante
        "#483D8B",  # Azul oscuro
        "#800080",  # Violeta
        "#EE82EE",  # Violeta claro
        "#FFC0CB",  # Rosa claro
        "#FF0000",  # Rojo intenso
        "#FFFF00",  # Amarillo brillante
        "#008000",  # Verde oscuro
        "#0000FF",  # Azul
        "#8B0000",  # Marrón
        "#800080",  # Violeta
        "#4B0082",  # Índigo
        "#D8BFD8",  # Lavanda
        "#FF00FF",  # Magenta
        "#FF8C00",  # Naranja oscuro
        "#FFFF80",  # Amarillo pálido
        "#008B8B",  # Verde oscuro azulado
        "#0000FF",  # Azul
        "#2F4F4F",  # Verde oscuro
        "#800080",  # Violeta
        "#800000",  # Marrón
        "#FF00FF",  # Magenta
        "#FF4500",  # Naranja
        "#FFFF00",  # Amarillo
        "#008080",  # Verde azulado
        "#000080",  # Azul marino
        "#800000",  # Marrón
        "#800080",  # Violeta
        "#4B0082",  # Índigo
        "#D8BFD8",  # Lavanda
        "#FF00FF",  # Magenta
        "#FF8C00",  # Naranja oscuro
        "#FFFF80",  # Amarillo pálido
        "#008B8B",  # Verde oscuro azulado
        "#0000FF",  # Azul
        "#2F4F4F",  # Verde oscuro
        "#800080",  # Violeta
        "#800000",  # Marrón
        "#FF00FF",  # Magenta
        "#FF4500",  # Naranja
        "#FFFF00",  # Amarillo
        "#008080",  # Verde azulado
        "#000080",  # Azul marino
        "#800000",  # Marrón
        "#800080",  # Violeta
        "#4B0082",  # Índigo
        "#D8BFD8",  # Lavanda
        "#FF00FF",  # Magenta
        "#FF8C00",  # Naranja oscuro
        "#FFFF80",  # Amarillo pálido
    ]
    """Colores generados para cada titulo"""
    MENSAJES_CARGA = [
        "JUGANDO CON EL DESTINO",
        "PREDICIENDO EL FUTURO",
        "GENERANDO ALEATORIEDAD",
        "INVOCANDO MAGOS",
        "INGRESE TEXTO DE ESPERA",
        "PROCESANDO",
        "VIENDO EL PASADO",
        "CALCULANDO",
        "ESPERA",
        "ESPERANDO A QUE SE DETENGAN",
        "PREPARATE PARA EL FUTURO",
        "RECOGIENDO DADOS",
        "LEYENDO CARTAS DEL TAROT",
    ]
    """Lista con diferentes mensajes a imprimir aleatoriamente al tirar los dados"""
    CARÁCTERES_NUMÉRICOS = [
        *[str(x) for x in range(10)],
        *["A", "B", "C", "D", "E", "F"],
    ]
    """Lista con todos las unidades de todas las bases en sus índices correspondientes"""


class ANSI:
    """Extraído del internet, solo para colorear y formatear el terminal :P"""

    BACKGROUND_WHITE = "\033[0;47m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    RESET = "\033[0m"

    def RGB(r: float, g: float, b: float):
        """Ejecuta un comando ANSI con unos valores de R,G y B personalizados (que van de 0 a 1)"""
        [r, g, b] = [str(round(x * 255)) for x in [r, g, b]]
        return f"\033[38;2;{r};{g};{b}m"


class ASCII:
    """Una clase de utilidad con iconos y textos bonitos :)"""

    LOGO = r"""    ____  ___     ____                
   / __ \( _ )   / __ \               
  / / / / __ \/|/ / / /   POR NICOLÁS CHEHADE Y LUCAS ENRÍQUEZ            
 / /_/ / /_/  </ /_/ /  D&D INF245               
/_____/\____/\/_____/__  __ __  ______
   /  _/ | / / ____/__ \/ // / / ____/
   / //  |/ / /_   __/ / // /_/___ \  
 _/ // /|  / __/  / __/__  __/___/ /  
/___/_/ |_/_/    /____/ /_/ /_____/"""
    SUCCESS = r"""
   __________  ____  ____  ______________________ 
  / ____/ __ \/ __ \/ __ \/ ____/ ____/_  __/ __ \
 / /   / / / / /_/ / /_/ / __/ / /     / / / / / /
/ /___/ /_/ / _, _/ _, _/ /___/ /___  / / / /_/ / 
\____/\____/_/ |_/_/ |_/_____/\____/ /_/  \____/"""
    FAIL = r"""
    _____   ____________  ____  ____  ______________________ 
   /  _/ | / / ____/ __ \/ __ \/ __ \/ ____/ ____/_  __/ __ \
   / //  |/ / /   / / / / /_/ / /_/ / __/ / /     / / / / / /
 _/ // /|  / /___/ /_/ / _, _/ _, _/ /___/ /___  / / / /_/ / 
/___/_/ |_/\____/\____/_/ |_/_/ |_/_____/\____/ /_/  \____/"""
    DICES = {
        6: ["      ", " .---.", " | %s |", " '---'"],
        20: ["   __  ", "  /__\ ", " /\\%s/\\", " \_\/_/"],
        100: ["   .  ", " .´ `.", " \\%s/", "  `-´ "],
    }


class Lanzamiento:
    """Clase principal de la tarea, en la clual se hacen los checks y se ejecuta la conversión entre lanzamientos"""

    __valor: str = ""
    """Representación en la base del valor, por eso es un str"""
    __tipo: int = -1
    """Tipo de dado"""
    __veces: int = 0
    """Variable de utilidad para almacenar la cantidad de veces que fue tirado"""

    def __init__(self, veces: int, tipo: int) -> None:
        """Constructor de lanzamiento. No se calcula de inmediato la conversión, pero sí se verifica de que los datos ingresados son válidos"""
        if veces <= 0:
            raise Exception("Se debe lanzar mínimo 1 vez")
        if veces > 1000000:
            raise Exception("No se permiten más de 1 millón de lanzamientos")
        if not (tipo in Constantes.TIPO_TO_SISTEMA):
            raise Exception(f"El dado D{tipo} no está admitido")
        self.__tipo = tipo
        self.__veces = veces

    def __binario(self, decimal: int) -> str:
        """A partir de un decimal entero, se transforma a base binaria (en representación str).
        Lease el README para entender funcionamiento"""
        numero = []
        binario = ""

        while decimal > 0:
            sobra = decimal % 2
            decimal //= 2
            numero.append(str(sobra))
        i = 1
        while i <= len(numero):
            binario += numero[-i]
            i += 1

        return binario

    def __hexa(self, decimal: int) -> str:
        """A partir de un decimal entero, se transforma a base hexadecimal (en representación str).
        Lease el README para entender funcionamiento"""
        numero = []
        hexa = ""
        while decimal > 0:
            sobra = decimal % 16
            decimal //= 16
            numero.append(str(sobra))
        i = 1

        while i <= len(numero):
            if numero[-i] == "15":
                numero[-i] = "F"
            elif numero[-i] == "14":
                numero[-i] = "E"
            elif numero[-i] == "13":
                numero[-i] = "D"
            elif numero[-i] == "12":
                numero[-i] = "C"
            elif numero[-i] == "11":
                numero[-i] = "B"
            elif numero[-i] == "10":
                numero[-i] = "A"
            hexa += numero[-i]
            i += 1

        return hexa

    def __octal(self, decimal: int) -> str:
        """A partir de un decimal entero, se transforma a base octal (en representación str).
        Lease el README para entender funcionamiento"""
        numero = []
        octal = ""
        while decimal > 0:
            sobra = decimal % 8
            decimal //= 8
            numero.append(str(sobra))
        i = 1
        while i <= len(numero):
            octal += numero[-i]
            i += 1

        return octal

    def __decimal(self, input: str) -> int:
        """A partir de un str con cualquier base, se transforma a decimal conociendo el tipo de base actual (gracias a variable '__tipo'.
        Lease el README para entender funcionamiento"""
        chars = {6: 2, 20: 8, 100: 16}[self.__tipo]
        return sum(
            [
                Constantes.CARÁCTERES_NUMÉRICOS.index(char)
                * (chars ** (len(input) - i - 1))
                for i, char in enumerate(input)
            ]
        )

    def lanzar(self):
        """Con esta función 'pública', se ejecuta el lanzamiento y se calcula la representación, actualizando el valor respectivo en la clase"""
        suma = sum(r.randint(1, self.__tipo) for _ in range(self.__veces))
        match tipo_dado:
            case 6:
                self.__valor = self.__binario(suma)
            case 20:
                self.__valor = self.__octal(suma)
            case 100:
                self.__valor = self.__hexa(suma)

    def resultado(self) -> str:
        """Devuelve el valor con su base. Es solo para que se vea bonito el llamado"""
        return self.__valor

    def decimal(self):
        """Devuelve el valor actual, pero en sistema decimal"""
        return self.__decimal(self.__valor)


class Game:
    """Clase de utilidad para el 'juego' de D&D de la aplicación"""

    streak = 0
    """Racha"""
    xp = 0
    """Float de experiencia"""
    error = ""
    """Variable que guarda un mensaje a través de ciclos para imprimir en el menú"""

    def xp_real():
        """Entrega un valor de experiencia más grande de lo que es realmente"""
        return round(1000 * (Game.xp * 10) ** 2, 1)

    def nivel():
        """Devuelve la cadena formateada correspondiente al titulo del usuario respectivo a su nivel"""
        i = math.floor(Game.xp * len(Constantes.TITULOS))

        color_nivel = (
            Constantes.COLORES_TITULOS[i]
            if i < len(Constantes.COLORES_TITULOS)
            else "#ffffff"
        )[1:]
        color_nivel = [
            sum(
                Constantes.CARÁCTERES_NUMÉRICOS.index(char.upper())
                * (16 ** (len(x) - j - 1))
                for j, char in enumerate(x)
            )  # <-- TRANSFORMAMOS DE HEXADECIMAL A NUMERO DE 0 A 255
            / 255
            for x in [color_nivel[i : i + 2] for i in range(0, len(color_nivel), 2)]
        ]

        nivel = (
            Constantes.TITULOS[i]
            if i < len(Constantes.TITULOS)
            else "Dios de los Sistemas Numéricos"
        )

        return ANSI.RGB(*color_nivel) + f"« {nivel} »".center(32) + ANSI.RESET

    def print_menu():
        """Imprime la pantalla principal del programa"""
        print(
            "\n".join(
                [
                    f"{ANSI.RGB(*Utils.blend_color([38.0 / 255, 183.0 / 255, 1], [96.0 / 255, 9.0 / 255,219.0 / 255], i/len(ASCII.LOGO.splitlines())))}{x}{ANSI.RESET}"
                    for i, x in enumerate(ASCII.LOGO.splitlines())
                ]
            )
        )
        print(
            ANSI.LIGHT_GREEN,
            (f"⟨ RACHA DE {Game.streak} ⟩" if Game.streak else "").center(32),
            ANSI.LIGHT_CYAN,
            ANSI.BOLD,
            "\n",
            Game.nivel(),
            "\n",
            ANSI.RESET,
            ANSI.FAINT,
            ANSI.ITALIC,
            f"({Game.xp_real()} XP)".center(25),
            "\n",
            ANSI.RESET,
        )


while True:  # Para que se ejecute permanentemente
    try:
        Utils.cls()
        Game.print_menu()

        """Solicitud de entrada"""
        print(
            f"INGRESA LOS DADOS A TIRAR {ANSI.FAINT}(FORMATO:{ANSI.RESET} {ANSI.RED}X{ANSI.RESET}d{ANSI.LIGHT_BLUE}Y{ANSI.RESET}):"
        )
        print(
            f"{ANSI.RED}    X: {ANSI.RESET}{ANSI.RED}{ANSI.FAINT}0 < N° Lanzamientos < 1.000.000{ANSI.RESET}"
        )
        print(
            f"{ANSI.LIGHT_BLUE}    Y: {ANSI.RESET}{ANSI.LIGHT_BLUE}{ANSI.FAINT}Tipo de Dado (6 | 20 | 100){ANSI.RESET}"
        )
        if Game.error:
            print(ANSI.RED, ANSI.BOLD, f"⚠️ {Game.error}", ANSI.RESET)
            Game.error = ""

        """Procesamiento de entrada"""
        dado = input("> ")
        if not dado:
            raise Exception("No puede ser vacío")
        try:
            [veces_lanzado, tipo_dado, *_] = [
                int(x) if x else None
                for x in [
                    *dado.split("d"),
                    "",
                    "",
                ]  # <-- Esto es por si se omiten los valores, para posteriormente manejar sus errores
            ]
        except Exception as e:
            raise Exception("Formato de entrada no reconocido")
        if veces_lanzado == None:
            raise Exception("No se introdujo el número de veces lanzado")
        if tipo_dado == None:
            raise Exception("No se introdujo el tipo de dado")

        lanzamiento = Lanzamiento(veces_lanzado, tipo_dado)
        dado_ascii = ASCII.DICES[tipo_dado]
        mensaje_carga = r.choice(Constantes.MENSAJES_CARGA)

        """Bonita animación de caída (?"""
        for frame in range(10):
            Utils.cls()
            print(ANSI.RESET, f"TIRANDO DADO D{tipo_dado}...\n{mensaje_carga}...")

            print("\n" * ((frame + 1) // 2))
            for i in range(len(dado_ascii)):
                print(
                    dado_ascii[i] if i != 2 else dado_ascii[i] % "?", end="", flush=True
                )
                if i != len(dado_ascii) - 1:
                    print()
                else:
                    print(ANSI.FAINT, f"x{veces_lanzado}")
            sleep(0.1)
        lanzamiento.lanzar()
        sleep(0.5)
        sleep((0.4 + 1.6 * r.random()) * (0.7 + 0.5 * r.random()))

        """Pantalla de desafío"""
        respuesta = 0
        while not respuesta:
            Utils.cls()
            print(ANSI.RESET, f"---- HORA DE TU DESAFÍO ----".center(35))
            print(
                ANSI.FAINT,
                f"INGRESA LA REPRESENTACIÓN DECIMAL".center(35),
                "\n",
                f"DEL NUMERO #{Constantes.TIPO_TO_SISTEMA[tipo_dado]}:".center(
                    36
                ).replace("#", ANSI.LIGHT_CYAN),
                ANSI.RESET,
            )

            sleep(1)
            print()
            print(ANSI.BOLD)
            print(f"{lanzamiento.resultado()}".center(35))
            print(ANSI.RESET)
            sleep(1)

            try:
                respuesta = int(input("RESPUESTA\n > "))
            except Exception as e:
                pass
        Utils.cls()

        """Verificación de respuesta"""
        if (decimal := lanzamiento.decimal()) == respuesta:
            Game.streak += 1
            last_xp = Game.xp_real()
            xp_win = 1 / len(Constantes.TITULOS) * (0.7 + r.random() * 3)
            Game.xp += xp_win

            for i in range(10):
                Utils.cls()
                print(
                    f"GANASTE {ANSI.YELLOW}{round(Game.xp_real() - last_xp, 1)}{ANSI.RESET} XP"
                )
                print(
                    f"ACERTASTE, LA RESPUESTA ERA {ANSI.LIGHT_PURPLE}{decimal}{ANSI.RESET}!",
                    end="",
                    flush=True,
                )
                if (i + 2) % 2 == 0:
                    print(ANSI.GREEN, ASCII.SUCCESS)
                sleep(0.3)
                print(ANSI.RESET)
        else:
            Game.streak = 0
            print(ANSI.RED, ASCII.FAIL, ANSI.RESET)
            sleep(1)
            print("LA RESPUESTA ERA", end="", flush=True)
            sleep(0.5)
            print(ANSI.LIGHT_PURPLE, f"{decimal}", ANSI.RESET)
            sleep(1)
        sleep(1)
    except Exception as e:
        """Manejo de errores inesperados"""
        Game.error = str(e)
