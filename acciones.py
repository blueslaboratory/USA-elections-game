# Date: 24/12/2024

from config import modelo_democrata, modelo_republicano
from config import estados_democratas, estados_republicanos, estados_bisagra


# TODO
# [] Incluir una accion de tipo shoot my own foot, lo que vendria a ser un false friend que beneficie al enemigo pero que se camufle bien

#############################
###### ACCION: ANALISIS #####
#############################

accion_analisis = {
    "nombre": "Análisis de datos",
    "descripcion": "Obtén información clave sobre los votantes para ajustar tu estrategia.",
    "impacto": "analisis",
    "coste": 100*1000
}




# Casar los nombres de las claves con los nombres de las claves de modelos de config.py

#############################
#### ACCIONES DEMOCRATAS ####
#############################

acciones_democratas = [
    # 0
    {
        "nombre": "Discurso Kamaleonico",
        "descripcion": "Kamala sube al escenario y suelta un discurso que hasta hace llorar a las piedras. \nImpacta especialmente a mujeres y jóvenes idealistas.",
        "impacto": {
            "sexo": ["femenino"],
            "edad": range(18, 45),
        },
        "coste": 200*1000
    },
    # 1
    {
        "nombre": "Aumento de presupuesto",
        "descripcion": "¡Un misterioso donante con una billetera bien gorda llega al rescate! \nIncrementa el presupuesto de tu campaña en 350k$.",
        "impacto": "money",
        "coste": -350*1000  # Ingreso
    },
    # 2
    {
        "nombre": "Sanidad gratuita para todes",
        "descripcion": "Organizas un rally de salud gratuita para inmigrantes, todos se abrazan. \n(Los abrazos son opcionales, pero el impacto emocional está garantizado.)",
        "impacto": {
            "etnia": ["hispanic", "illegal", "asian"],
            "edad": range(20, 50),
        },
        "coste": 200*1000
    },
    # 3
    {
        "nombre": "Celebrities, ¡respaldadme!",
        "descripcion": "Lady Gaga, Brad Pitt y Beyoncé te dan su bendición en Instagram. \n¿Quién necesita más?",
        "impacto": {
            "edad": range(18, 40),
            # "estado": ["California", "New York", "Illinois"],
            "estado": estados_democratas + estados_bisagra,
        },
        "coste": 250*1000
    },
    # 4
    {
        "nombre": "¡Abrid las fronteras!",
        "descripcion": "Abres las fronteras con estilo. \nLos inmigrantes ilegales ya están buscando la forma de recompensarte en tu campaña.",
        "impacto": {
            "etnia": ["illegal", "hispanic"],
        },
        "coste": 210*1000
    },
    # 5
    {
        "nombre": "Ataque terrorista a Trump",
        "descripcion": "Un plan descabellado: organizas un ataque terrorista con el objetivo de eliminar a Trump.",
        "impacto": {
            # Representa un caso especial 
            "especial": "trump_assasination_attempt",  
            # Parámetros del modelo democrata
            "estado": modelo_democrata["estado"],
            "edad": modelo_democrata["edad"],
            "sexo": modelo_democrata["sexo"],
            "religion": modelo_democrata["religion"],
            "etnia": modelo_democrata["etnia"],
            "salario": modelo_democrata["salario"],
            "estudios": modelo_democrata["estudios"],
        },
        "coste": 450*1000  # Alto costo por el riesgo
    },
    # 6
    {
        "nombre": "Concierto de Taylor Swift",
        "descripcion": "Taylor Swift canta para Kamala. Los jóvenes corren a registrarse como votantes (y a hacerse selfies).",
        "impacto": {
            "edad": range(18, 35),
            "sexo": ["femenino"],
        },
        "coste": 280*1000
    },
    # 7
    {
        "nombre": "Discurso sobre los derechos de las mujeres",
        "descripcion": "Un discurso apasionado sobre los derechos de las mujeres. \nLos machistas empiezan a cuestionarse su estilo de vida.",
        "impacto": {
            "sexo": ["femenino"],
        },
        "coste": 170*1000
    },
    # 8
    {
        "nombre": "¡No somos fascistas!",
        "descripcion": "Lanzas una campaña para dejar claro que el fascismo no va contigo. \n¡Todos a la izquierda, camaradas, maaaarchen!",
        "impacto": {
            # "estado": ["California", "New York", "Massachusetts"],
            "estado": estados_democratas + estados_bisagra,
            
        },
        "coste": 250*1000
    },
    # 9
    {
        "nombre": "Campaña Woke",
        "descripcion": "Una campaña que grita: ¡Diversidad para todos!. \nEl lado inclusivo de la fuerza nunca había lucido tan bien.",
        "impacto": {
            "etnia": ["black", "hispanic", "asian"],
            "estudios": ["graduate", "masters", "doctor"],
        },
        "coste": 220*1000
    },
    # 10
    {
        "nombre": "DEI propaganda",
        "descripcion": "Propaganda enfocada en Diversidad, Equidad e Inclusión. \n¿Quién necesita enemigos con esta estrategia?",
        "impacto": {
            "estudios": ["graduate", "masters", "doctor"],
        },
        "coste": 170*1000
    },
    # 11
    {
        "nombre": "Impulso en RRSS: META",
        "descripcion": "Inundas las redes sociales con anuncios de Kamala. Hasta los gatos maúllan tu mensaje.",
        "impacto": {
            "edad": range(18, 50),
        },
        "coste": 200*1000
    },
]




#############################
### ACCIONES REPUBLICANAS ###
#############################

acciones_republicanas = [
    # 0
    {
        "nombre": "Trump Speech",
        "descripcion": "Trump toma el micrófono y entrega un discurso que hace que los patriotas lloren lágrimas de águila. \n¡Viva América!",
        "impacto": {
            "sexo": ["masculino"],
            "edad": range(30, 99),
        },
        "coste": 200*1000
    },
    # 1
    {
        "nombre": "Aumento de presupuesto",
        "descripcion": "Una llamada rápida a los amigos ricos: ¡se cuadran donaciones y el dinero fluye como el Mississippi! \nTu campaña respira aliviada con 350k$ adicionales.",
        "impacto": "money",
        "coste": -350*1000  # Ingreso
    },
    # 2
    {
        "nombre": "Patriotismo M.A.G.A.",
        "descripcion": "Lanzas una campaña para devolver a América a su antigua gloria. \nRonald Reagan está orgulloso de ti.",
        "impacto": {
            "etnia": ["white", "hispanic", "asian"],
            "edad": range(30, 60),
        },
        "coste": 200*1000
    },
    # 3
    {
        "nombre": "Rally de fe",
        "descripcion": "Padre he abierto los ojos. Un mitin lleno de fervor religioso y mensajes de esperanza. \n¿Es Trump un enviado celestial?",
        "impacto": {
            "etnia": ["white", "hispanic"],
            "religion": ["christianism", "other"],
        },
        "coste": 190*1000
    },
    # 4
    {
        "nombre": "Ocupar el Capitolio",
        "descripcion": "Movilizas una protesta 'pacífica' en el Capitolio. \nLos patriotas están preparados para dar guerra.",
        "impacto": {
            # "estado": ["Texas", "Florida", "Alabama", "Wyoming"],
            "estado": estados_republicanos + estados_bisagra,
        },
        "coste": 250*1000
    },
    # 5
    {
        "nombre": "¡Construyan el muro!",
        "descripcion": "Lanzas una campaña para construir un muro más grande y mejor. \nEl mejor y más grande muro jamás visto. \nLos votantes conservadores aplauden hasta quedarse sin manos.",
        "impacto": {
            "etnia": ["white", "hispanic"],
        },
        "coste": 210*1000
    },
    # 6
    {
        "nombre": "Intervención rusa",
        "descripcion": "¿Teléfono rojo? Volamos hacia Moscú. \nLlamas al Kremlin y consigues un escuadrón de hackers de élite. \n¡La elección podría ser tuya!",
        "impacto": {
            # Representa un caso especial
            "especial": "russian_hacking_attempt",
            # Parámetros del modelo republicano
            "estado": modelo_republicano["estado"],
            "edad": modelo_republicano["edad"],
            "sexo": modelo_republicano["sexo"],
            "religion": modelo_republicano["religion"],
            "etnia": modelo_republicano["etnia"],
            "salario": modelo_republicano["salario"],
            "estudios": modelo_republicano["estudios"],
        },
        "coste": 450*1000  # Alto costo por el riesgo
    },
    # 7
    {
        "nombre": "Discurso sobre el derecho a las armas",
        "descripcion": "Trump sube al escenario con un rifle y dispara al aire prometiendo proteger la 2ª Enmienda. \nLos votantes aplauden con entusiasmo (y algo de miedo).",
        "impacto": {
            "edad": range(35, 99),
            "sexo": ["masculino"],
        },
        "coste": 250*1000
    },
    # 8
    {
        "nombre": "¡No somos comunistas!",
        "descripcion": "Lanzas una campaña para dejar claro que la derecha no tiene nada que ver con el comunismo. \nLos votantes respiran aliviados.",
        "impacto": {
            # "estado": ["Alabama", "Arkansas", "Mississippi"],
            "estado": estados_republicanos + estados_bisagra,
        },
        "coste": 250*1000
    },
    # 9
    {
        "nombre": "Campaña Anti-Woke",
        "descripcion": "Una cruzada épica contra contra el wokeismo. \nPrometes proteger los valores tradicionales. \n¡Todos lanzan sus sombreros M.A.G.A. al aire celebrando el sentido común!",
        "impacto": {
            "etnia": ["white", "hispanic"],
            "estudios": ["high school", "undergrad"],
        },
        "coste": 220*1000
    },
    # 10
    {
        "nombre": "Han matado a Peanut, ¡Bastardos!",
        "descripcion": "Trump se solidariza con un hombre cuya ardilla, Peanut, fue cruelmente asesinada. \nEl país entero se conmueve ante la injusticia, habrá memes en su honor.",
        "impacto": {
            "edad": range(30, 50),
            "sexo": ["masculino"],
        },
        "coste": 170*1000
    },
    # 11
    {
        "nombre": "Tormenta en X",
        "descripcion": "Elon Musk se desata en X con una campaña masiva a favor de Trump. Las redes explotan (literalmente).",
        "impacto": {
            "edad": range(18, 55),
            "sexo": ["masculino"],
        },
        "coste": 200*1000
    },
]