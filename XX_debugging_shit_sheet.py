states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", 
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
    "Wisconsin", "Wyoming"
]

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




estados_bisagra = []

for state in states:
    if state not in estados_democratas and state not in estados_republicanos:
        estados_bisagra.append(state)

print(estados_bisagra)




print("==== Statistics ====")
print(f"Estados totales: {len(states)}")
print(f"Estados democratas: {len(estados_democratas)}")
print(f"Estados republicanos: {len(estados_republicanos)}")
print(f"Estados bisagra: {len(estados_bisagra)}")
print("====================")


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