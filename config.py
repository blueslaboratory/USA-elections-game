# Date: 23/12/2024

from datetime import datetime

#############################
####### OUTPUT FOLDER #######
#############################
output_folder = "datos_votantes"




#############################
##### PARAMETROS JUEGO ######
#############################
# Recomendado: Turnos (16), Minutos (10)
TURNOS_TOTALES = 8
MINUTOS_ANALISIS = 10
DINERO_INICIAL = 125000*TURNOS_TOTALES




#############################
##### FECHAS DEL JUEGO ######
#############################

# 8 turnos, 4 por jugador
# Fecha inicial: Antes del 5 de noviembre de 2024: (Celebracion de las elecciones)
# 1 de Enero de 2024:
fecha_inicial = datetime(2024, 1, 1)
# 5 de Noviembre de 2024: 
fecha_final = datetime(2024, 11, 5)

# Diccionario para mapear los meses en español
MESES = {
    1: "Enero", 
    2: "Febrero", 
    3: "Marzo", 
    4: "Abril", 
    5: "Mayo", 
    6: "Junio",
    7: "Julio", 
    8: "Agosto", 
    9: "Septiembre", 
    10: "Octubre", 
    11: "Noviembre", 
    12: "Diciembre"
}



#############################
#### GENERADOR ALEATORIO ####
#############################

# 50 Estados Estadounidenses:
estados = [
    "Alabama", 
    "Alaska", 
    "Arizona", 
    "Arkansas", 
    "California", 
    "Colorado", 
    "Connecticut", 
    "Delaware", 
    "Florida", 
    "Georgia", 
    "Hawaii", 
    "Idaho", 
    "Illinois", 
    "Indiana", 
    "Iowa", 
    "Kansas", 
    "Kentucky", 
    "Louisiana", 
    "Maine", 
    "Maryland", 
    "Massachusetts", 
    "Michigan", 
    "Minnesota", 
    "Mississippi", 
    "Missouri", 
    "Montana", 
    "Nebraska", 
    "Nevada", 
    "New Hampshire", 
    "New Jersey", 
    "New Mexico", 
    "New York", 
    "North Carolina", 
    "North Dakota", 
    "Ohio", 
    "Oklahoma", 
    "Oregon", 
    "Pennsylvania", 
    "Rhode Island", 
    "South Carolina", 
    "South Dakota", 
    "Tennessee", 
    "Texas", 
    "Utah", 
    "Vermont", 
    "Virginia", 
    "Washington", 
    "West Virginia", 
    "Wisconsin", 
    "Wyoming"
]

sexo = [
    "masculino", 
    "femenino"
]

religiones = [
    "judaism", 
    "islam", 
    "christianism", 
    "hinduism", 
    "atheism",
    "other"
]

etnias = [
    "white", 
    "black", 
    "hispanic", 
    "asian", 
    "indian",
    "illegal"
]

estudios = [
    "high school", 
    "undergraduate", 
    "graduate", 
    "masters", 
    "doctor"
]



#############################
#### PESOS FORMULA VOTOS ####
#############################

pesos_votos = {
    "estado": 0.24,
    "estudios": 0.20,
    "etnia": 0.14,
    "edad": 0.14,
    "sexo": 0.14,
    "salario": 0.10,
    "religion": 0.04
}



########################
######## STATES ########
########################

# 12
estados_democratas = [
    "California",
    "Connecticut",
    "Delaware",
    "Hawaii",
    "Illinois",
    "Maryland",
    "Massachusetts",
    "New Jersey",
    "New York",
    "Oregon",
    "Vermont",
    "Washington"
]

# 12
estados_republicanos = [
    "Alabama", 
    "Arkansas",
    "Florida", 
    "Idaho", 
    "Louisiana", 
    "Mississippi", 
    "North Dakota", 
    "Oklahoma", 
    "South Carolina", 
    "Tennessee", 
    "Texas", 
    "Wyoming", 
]

# 26
estados_bisagra = [
    'Alaska', 
    'Arizona', 
    'Colorado', 
    'Georgia', 
    'Indiana', 
    'Iowa', 
    'Kansas', 
    'Kentucky', 
    'Maine', 
    'Michigan', 
    'Minnesota', 
    'Missouri', 
    'Montana', 
    'Nebraska', 
    'Nevada', 
    'New Hampshire', 
    'New Mexico', 
    'North Carolina', 
    'Ohio', 
    'Pennsylvania', 
    'Rhode Island', 
    'South Dakota', 
    'Utah', 
    'Virginia', 
    'West Virginia', 
    'Wisconsin'
]



#############################
########## MODELOS ##########
#############################

# Tipo: Jovenes, urbanos, progresistas, academicos, diversos
modelo_democrata = {
    # Estados progresistas y urbanos típicos de votantes demócratas
    "estado": [
        "California",
        "Connecticut",
        "Delaware",
        "Hawaii",
        "Illinois",
        "Maryland",
        "Massachusetts",
        "New Jersey",
        "New York",
        "Oregon",
        "Vermont",
        "Washington"
    ],
    # Jóvenes y adultos jóvenes, enfocados en cambios sociales y políticas progresistas
    "edad": range(18,35),
    # Estereotipo: femenino
    "sexo": ["femenino"],
    # Religiones asociadas a la pluralidad y el progresismo
    "religion": ["atheism", "hinduism", "judaism"],
    # Diversidad étnica
    "etnia": ["black", "hispanic", "asian", "indian", "illegal"],
    # Ingresos medio-bajo, clase media
    "salario": range(30*1000, 85*1000), 
    # Nivel educativo elevado, votantes progresistas
    "estudios": ["graduate", "masters", "doctor"]
}


# tradicionalistas, rurales/suburbanos, religiosos, economicos, patrioticos
modelo_republicano = {
    # Estados rurales y conservadores típicos de votantes republicanos
    "estado": [
        "Alabama", 
        "Arkansas",
        "Florida", 
        "Idaho", 
        "Louisiana", 
        "Mississippi", 
        "North Dakota", 
        "Oklahoma", 
        "South Carolina", 
        "Tennessee", 
        "Texas", 
        "Wyoming", 
    ],
    # Adultos mayores y generaciones tradicionales
    "edad": range(35, 99),
    # Estereotipo: masculino
    "sexo": ["masculino"],
    # Religion cristiana dominante
    "religion": ["christianism", "other"],
    # Predominio blanco y minorias conservadoras
    "etnia": ["white", "hispanic", "asian"],
    # Ingresos medio-alto, clase media alta y ricos
    "salario": range(50*1000, 250*1000),
    # Nivel educativo basico
    "estudios": ["high school", "undergrad", "graduate"] 
}
