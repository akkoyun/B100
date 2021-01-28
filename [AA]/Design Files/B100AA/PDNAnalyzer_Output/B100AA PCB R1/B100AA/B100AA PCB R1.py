designFile = "C:/Altium Projects/B100/[AA]/Design Files/B100AA/PDNAnalyzer_Output/B100AA PCB R1/odb.tgz"

powerNets = ["VCC", "3V8", "VIOT", "VIOT1", "VIOT2", "5V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J2", "60"), ("J2", "1") ],
"ground_pins": [ ("J2", "30"), ("J2", "58"), ("J2", "4"), ("J2", "31") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("J3", "60"), ("J3", "1") ],
"ground_pins": [ ("J3", "30"), ("J3", "58"), ("J3", "4"), ("J3", "31") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U4", "M02"), ("U4", "M01") ],
"ground_pins": [ ("U4", "B13"), ("U4", "E14"), ("U4", "A04"), ("U4", "A02"), ("U4", "E02"), ("U4", "F02"), ("U4", "E01"), ("U4", "G01"), ("U4", "M12"), ("U4", "P13"), ("U4", "P08"), ("U4", "P10"), ("U4", "P09"), ("U4", "R10"), ("U4", "H02"), ("U4", "M04"), ("U4", "M03"), ("U4", "G02"), ("U4", "J02"), ("U4", "H01"), ("U4", "K02"), ("U4", "J01"), ("U4", "L02"), ("U4", "L01"), ("U4", "N06"), ("U4", "N04"), ("U4", "P06"), ("U4", "N05"), ("U4", "R08"), ("U4", "P05"), ("U4", "R06"), ("U4", "R05"), ("U4", "N03"), ("U4", "P04"), ("U4", "P03"), ("U4", "R03"), ("U4", "R04"), ("U4", "R02") ],
"current": 0.15,
"Rpin": 2.53333333333333,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("U4", "N01"), ("U4", "N02"), ("U4", "P02"), ("U4", "P01") ],
"ground_pins": [ ("U4", "B13"), ("U4", "E14"), ("U4", "A04"), ("U4", "A02"), ("U4", "E02"), ("U4", "F02"), ("U4", "E01"), ("U4", "G01"), ("U4", "M12"), ("U4", "P13"), ("U4", "P08"), ("U4", "P10"), ("U4", "P09"), ("U4", "R10"), ("U4", "H02"), ("U4", "M04"), ("U4", "M03"), ("U4", "G02"), ("U4", "J02"), ("U4", "H01"), ("U4", "K02"), ("U4", "J01"), ("U4", "L02"), ("U4", "L01"), ("U4", "N06"), ("U4", "N04"), ("U4", "P06"), ("U4", "N05"), ("U4", "R08"), ("U4", "P05"), ("U4", "R06"), ("U4", "R05"), ("U4", "N03"), ("U4", "P04"), ("U4", "P03"), ("U4", "R03"), ("U4", "R04"), ("U4", "R02") ],
"current": 0.15,
"Rpin": 4.82539682539683,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U20", "3") ],
"ground_pins": [ ("U20", "6") ],
"current": 0.05,
"Rpin": 2,
}
,
{
"id": "5",
"type": "source",
"power_pins": [ ("U21", "6") ],
"ground_pins": [ ("U21", "3"), ("U21", "2"), ("U21", "8") ],
"voltage": 3.8,
"Rpin": 0,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("U21", "10") ],
"ground_pins": [ ("U21", "3"), ("U21", "2"), ("U21", "8") ],
"current": 0.853932584269663,
"Rpin": 0.175657894736842,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("R65", "2") ],
"ground_pins": [ ("R66", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "8",
"type": "source",
"power_pins": [ ("U22", "6") ],
"ground_pins": [ ("U22", "3"), ("U22", "2"), ("U22", "8") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("U22", "10") ],
"ground_pins": [ ("U22", "3"), ("U22", "2"), ("U22", "8") ],
"current": 0.0001,
"Rpin": 150000,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("R68", "2") ],
"ground_pins": [ ("R70", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
]


voltage_regulators = [
{
"id": "11",
"type": "linear",

"in": [ ("U1", "1") ],
"out": [ ("U1", "6") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "12",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "13",
"type": "linear",

"in": [ ("FB2", "1") ],
"out": [ ("FB2", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.3E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.05, 'Thickness': 0.0001},
        {'name': 'MID_LAYER_1', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.5, 'Thickness': 0.000565},
        {'name': 'MID_LAYER_2', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.25, 'Thickness': 0.000127},
        {'name': 'MID_LAYER_3', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-4', 'DielectricConstant': 4.5, 'Thickness': 0.000565},
        {'name': 'MID_LAYER_4', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-5', 'DielectricConstant': 4.05, 'Thickness': 0.0001},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.3E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
