designFile = "C:/Altium Projects/B100/[AA]/Design Files/B100AA/PDNAnalyzer_Output/B100AA PCB R1/odb.tgz"

powerNets = ["VCC", "3V8", "VIOT", "VIOT1", "VIOT2", "5V", "3V3", "VMCU", "VFOTA"]

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
"power_pins": [ ("U4", "M01"), ("U4", "M02") ],
"ground_pins": [ ("U4", "R02"), ("U4", "R04"), ("U4", "R03"), ("U4", "P03"), ("U4", "P04"), ("U4", "N03"), ("U4", "R05"), ("U4", "R06"), ("U4", "P05"), ("U4", "R08"), ("U4", "N05"), ("U4", "P06"), ("U4", "N04"), ("U4", "N06"), ("U4", "L01"), ("U4", "L02"), ("U4", "J01"), ("U4", "K02"), ("U4", "H01"), ("U4", "J02"), ("U4", "G02"), ("U4", "M03"), ("U4", "M04"), ("U4", "H02"), ("U4", "R10"), ("U4", "P09"), ("U4", "P10"), ("U4", "P08"), ("U4", "P13"), ("U4", "M12"), ("U4", "G01"), ("U4", "E01"), ("U4", "F02"), ("U4", "E02"), ("U4", "A02"), ("U4", "A04"), ("U4", "E14"), ("U4", "B13") ],
"current": 0.125,
"Rpin": 3.04,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("U4", "P01"), ("U4", "P02"), ("U4", "N02"), ("U4", "N01") ],
"ground_pins": [ ("U4", "R02"), ("U4", "R04"), ("U4", "R03"), ("U4", "P03"), ("U4", "P04"), ("U4", "N03"), ("U4", "R05"), ("U4", "R06"), ("U4", "P05"), ("U4", "R08"), ("U4", "N05"), ("U4", "P06"), ("U4", "N04"), ("U4", "N06"), ("U4", "L01"), ("U4", "L02"), ("U4", "J01"), ("U4", "K02"), ("U4", "H01"), ("U4", "J02"), ("U4", "G02"), ("U4", "M03"), ("U4", "M04"), ("U4", "H02"), ("U4", "R10"), ("U4", "P09"), ("U4", "P10"), ("U4", "P08"), ("U4", "P13"), ("U4", "M12"), ("U4", "G01"), ("U4", "E01"), ("U4", "F02"), ("U4", "E02"), ("U4", "A02"), ("U4", "A04"), ("U4", "E14"), ("U4", "B13") ],
"current": 0.125,
"Rpin": 5.79047619047619,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U20", "3") ],
"ground_pins": [ ("U20", "6") ],
"current": 0.00018,
"Rpin": 555.555555555556,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("R62", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("R62", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("U17", "6") ],
"ground_pins": [ ("U17", "5") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("U6", "1") ],
"ground_pins": [ ("U6", "8"), ("U6", "9"), ("U6", "17") ],
"current": 0.0001,
"Rpin": 1500,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("U7", "1") ],
"ground_pins": [ ("U7", "8"), ("U7", "9"), ("U7", "17") ],
"current": 0.0001,
"Rpin": 1500,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("U8", "1") ],
"ground_pins": [ ("U8", "8"), ("U8", "9"), ("U8", "17") ],
"current": 0.0001,
"Rpin": 1500,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("R13", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 39166.6666666667,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("R12", "2") ],
"ground_pins": [ ("U6", "8"), ("U6", "9"), ("U6", "17") ],
"resistance": 1E-09,
"Rpin": 35250,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("R14", "2") ],
"ground_pins": [ ("U7", "8"), ("U7", "9"), ("U7", "17") ],
"resistance": 1E-09,
"Rpin": 35250,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("R16", "2") ],
"ground_pins": [ ("U8", "8"), ("U8", "9"), ("U8", "17") ],
"resistance": 1E-09,
"Rpin": 35250,
}
,
{
"id": "15",
"type": "load",
"power_pins": [ ("R15", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 39166.6666666667,
}
,
{
"id": "16",
"type": "load",
"power_pins": [ ("R17", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 39166.6666666667,
}
,
{
"id": "17",
"type": "load",
"power_pins": [ ("Q3", "2") ],
"ground_pins": [ ("Q4", "2") ],
"resistance": 1E-09,
"Rpin": 32.5,
}
,
{
"id": "18",
"type": "load",
"power_pins": [ ("Q3", "2") ],
"ground_pins": [ ("Q5", "2") ],
"resistance": 1E-09,
"Rpin": 11,
}
,
{
"id": "19",
"type": "load",
"power_pins": [ ("Q3", "2") ],
"ground_pins": [ ("Q6", "2") ],
"resistance": 1E-09,
"Rpin": 11,
}
,
{
"id": "20",
"type": "load",
"power_pins": [ ("R45", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 8333.33333333333,
}
,
{
"id": "21",
"type": "load",
"power_pins": [ ("U15", "10"), ("U15", "31"), ("U15", "61"), ("U15", "80"), ("U15", "100") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"current": 0.05,
"Rpin": 10,
}
,
{
"id": "22",
"type": "load",
"power_pins": [ ("D3", "4") ],
"ground_pins": [ ("Q10", "2") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "23",
"type": "load",
"power_pins": [ ("D3", "4") ],
"ground_pins": [ ("Q11", "2") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "24",
"type": "load",
"power_pins": [ ("D3", "4") ],
"ground_pins": [ ("Q12", "2") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "25",
"type": "load",
"power_pins": [ ("U9", "1") ],
"ground_pins": [ ("U9", "2") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "26",
"type": "load",
"power_pins": [ ("U11", "4"), ("U11", "6"), ("U11", "18") ],
"ground_pins": [ ("U11", "3"), ("U11", "5"), ("U11", "21") ],
"current": 0.05,
"Rpin": 6,
}
,
{
"id": "27",
"type": "load",
"power_pins": [ ("R36", "2") ],
"ground_pins": [ ("U11", "3"), ("U11", "5"), ("U11", "21") ],
"resistance": 1E-09,
"Rpin": 7500,
}
,
{
"id": "28",
"type": "load",
"power_pins": [ ("D2", "4") ],
"ground_pins": [ ("Q7", "2") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "29",
"type": "load",
"power_pins": [ ("D2", "4") ],
"ground_pins": [ ("Q8", "2") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "30",
"type": "load",
"power_pins": [ ("D2", "4") ],
"ground_pins": [ ("Q9", "2") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "31",
"type": "load",
"power_pins": [ ("J1", "4") ],
"ground_pins": [ ("J1", "6") ],
"current": 0.03,
"Rpin": 3.33333333333333,
}
,
{
"id": "32",
"type": "load",
"power_pins": [ ("R38", "2") ],
"ground_pins": [ ("U12", "8"), ("U12", "15") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "33",
"type": "load",
"power_pins": [ ("R39", "2") ],
"ground_pins": [ ("U12", "8"), ("U12", "15") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "34",
"type": "load",
"power_pins": [ ("R40", "2") ],
"ground_pins": [ ("U12", "8"), ("U12", "15") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "35",
"type": "load",
"power_pins": [ ("R41", "2") ],
"ground_pins": [ ("U12", "8"), ("U12", "15") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "36",
"type": "load",
"power_pins": [ ("U12", "16") ],
"ground_pins": [ ("U12", "8"), ("U12", "15") ],
"current": 0.0001,
"Rpin": 1333.33333333333,
}
,
{
"id": "37",
"type": "load",
"power_pins": [ ("U13", "2") ],
"ground_pins": [ ("U13", "11") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "38",
"type": "load",
"power_pins": [ ("U13", "19") ],
"ground_pins": [ ("U13", "11") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "39",
"type": "load",
"power_pins": [ ("U14", "12") ],
"ground_pins": [ ("U14", "5"), ("U14", "13") ],
"current": 0.015,
"Rpin": 8.88888888888889,
}
,
{
"id": "40",
"type": "load",
"power_pins": [ ("R52", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 8333.33333333333,
}
,
{
"id": "41",
"type": "load",
"power_pins": [ ("R53", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 8333.33333333333,
}
,
{
"id": "42",
"type": "load",
"power_pins": [ ("U16", "16"), ("U16", "3") ],
"ground_pins": [ ("U16", "13"), ("U16", "2"), ("U16", "8"), ("U16", "1") ],
"current": 0.02,
"Rpin": 13.3333333333333,
}
,
{
"id": "43",
"type": "load",
"power_pins": [ ("U17", "7") ],
"ground_pins": [ ("U17", "5") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "44",
"type": "load",
"power_pins": [ ("R57", "2") ],
"ground_pins": [ ("D4", "1") ],
"resistance": 1E-09,
"Rpin": 165,
}
,
{
"id": "45",
"type": "load",
"power_pins": [ ("R56", "2") ],
"ground_pins": [ ("U15", "11"), ("U15", "32"), ("U15", "62"), ("U15", "81"), ("U15", "99") ],
"resistance": 1E-09,
"Rpin": 8333.33333333333,
}
,
{
"id": "46",
"type": "load",
"power_pins": [ ("R54", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "47",
"type": "load",
"power_pins": [ ("R55", "2") ],
"ground_pins": [ ("U16", "13"), ("U16", "2"), ("U16", "8"), ("U16", "1") ],
"resistance": 1E-09,
"Rpin": 8000,
}
,
{
"id": "48",
"type": "load",
"power_pins": [ ("R58", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "49",
"type": "load",
"power_pins": [ ("R59", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "50",
"type": "load",
"power_pins": [ ("U18", "5") ],
"ground_pins": [ ("U18", "2") ],
"current": 0.0002,
"Rpin": 500,
}
,
{
"id": "51",
"type": "load",
"power_pins": [ ("R60", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "52",
"type": "load",
"power_pins": [ ("R61", "2") ],
"ground_pins": [ ("U16", "8") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "53",
"type": "load",
"power_pins": [ ("U19", "8") ],
"ground_pins": [ ("U19", "4") ],
"current": 0.0004,
"Rpin": 250,
}
,
{
"id": "54",
"type": "source",
"power_pins": [ ("U3", "5") ],
"ground_pins": [ ("U3", "2") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "55",
"type": "load",
"power_pins": [ ("U3", "1") ],
"ground_pins": [ ("U3", "2") ],
"current": 0.587682581385471,
"Rpin": 0.170159884208663,
}
,
{
"id": "56",
"type": "source",
"power_pins": [ ("U21", "6") ],
"ground_pins": [ ("U21", "8"), ("U21", "3") ],
"voltage": 3.801364739,
"Rpin": 0,
}
,
{
"id": "57",
"type": "load",
"power_pins": [ ("U21", "10") ],
"ground_pins": [ ("U21", "8"), ("U21", "3") ],
"current": 3.69274880828795,
"Rpin": 0.036106797471326,
}
,
{
"id": "58",
"type": "load",
"power_pins": [ ("R65", "2") ],
"ground_pins": [ ("R66", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
,
{
"id": "59",
"type": "source",
"power_pins": [ ("U22", "6") ],
"ground_pins": [ ("U22", "8"), ("U22", "3") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "60",
"type": "load",
"power_pins": [ ("U22", "10") ],
"ground_pins": [ ("U22", "8"), ("U22", "3") ],
"current": 0.00133632788118345,
"Rpin": 99.7759121924881,
}
,
{
"id": "61",
"type": "load",
"power_pins": [ ("R68", "2") ],
"ground_pins": [ ("R70", "1") ],
"resistance": 1E-09,
"Rpin": 500000,
}
]


voltage_regulators = [
{
"id": "62",
"type": "linear",

"in": [ ("U1", "1") ],
"out": [ ("U1", "6") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.05,
}
,
{
"id": "63",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0225,
}
,
{
"id": "64",
"type": "linear",

"in": [ ("FB2", "1") ],
"out": [ ("FB2", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0225,
}
,
{
"id": "65",
"type": "linear",

"in": [ ("U2", "1") ],
"out": [ ("U2", "6") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.07,
}
,
{
"id": "66",
"type": "linear",

"in": [ ("U10", "1") ],
"out": [ ("U10", "6") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.07,
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
