import locale
from prettytable import PrettyTable

# set locale for currency format number
locale.setlocale(locale.LC_ALL, "id_ID")

# List kota
list_kota = ["Jakarta", "Malang", "Bandung", "Yogyakarta", "Surabaya"]

# Pricelist Ticket Jakarta
jkt_ticket_pricelist = {
    "Jakarta - Malang": {
        "train": {
            "Economy": {"weekday": 210000, "weekend": 230000},
            "First": {"weekday": 240000, "weekend": 270000},
        },
        "plane": {
            "Economy": {"weekday": 1070000, "weekend": 1150000},
            "First": {"weekday": 1250000, "weekend": 1300000},
        },
    },
    "Jakarta - Bandung": {
        "train": {
            "Economy": {"weekday": 63000, "weekend": 110000},
            "First": {"weekday": 200000, "weekend": 225000},
        },
        "plane": {
            "Economy": {"weekday": 560000, "weekend": 570000},
            "First": {"weekday": 800000, "weekend": 850000},
        },
    },
    "Jakarta - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 200000, "weekend": 220000},
            "First": {"weekday": 550000, "weekend": 580000},
        },
        "plane": {
            "Economy": {"weekday": 870000, "weekend": 975000},
            "First": {"weekday": 1100000, "weekend": 1200000},
        },
    },
    "Jakarta - Surabaya": {
        "train": {
            "Economy": {"weekday": 220000, "weekend": 240000},
            "First": {"weekday": 300000, "weekend": 330000},
        },
        "plane": {
            "Economy": {"weekday": 950000, "weekend": 1120000},
            "First": {"weekday": 1200000, "weekend": 1250000},
        },
    },
}

# Pricelist Ticket Malang
mlg_ticket_pricelist = {
    "Malang - Jakarta": {
        "train": {
            "Economy": {"weekday": 170000, "weekend": 200000},
            "First": {"weekday": 250000, "weekend": 280000},
        },
        "plane": {
            "Economy": {"weekday": 890000, "weekend": 930000},
            "First": {"weekday": 980000, "weekend": 1100000},
        },
    },
    "Malang - Bandung": {
        "train": {
            "Economy": {"weekday": 150000, "weekend": 170000},
            "First": {"weekday": 230000, "weekend": 250000},
        },
        "plane": {
            "Economy": {"weekday": 800000, "weekend": 840000},
            "First": {"weekday": 900000, "weekend": 940000},
        },
    },
    "Malang - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 100000, "weekend": 130000},
            "First": {"weekday": 170000, "weekend": 200000},
        },
        "plane": {
            "Economy": {"weekday": 710000, "weekend": 760000},
            "First": {"weekday": 800000, "weekend": 820000},
        },
    },
    "Malang - Surabaya": {
        "train": {
            "Economy": {"weekday": 75000, "weekend": 90000},
            "First": {"weekday": 120000, "weekend": 150000},
        },
        "plane": {
            "Economy": {"weekday": 630000, "weekend": 660000},
            "First": {"weekday": 700000, "weekend": 720000},
        },
    },
}

# Pricelist Ticket Bandung
bdg_ticket_pricelist = {
    "Bandung - Jakarta": {
        "train": {
            "Economy": {"weekday": 150000, "weekend": 170000},
            "First": {"weekday": 220000, "weekend": 250000},
        },
        "plane": {
            "Economy": {"weekday": 1280000, "weekend": 1450000},
            "First": {"weekday": 1600000, "weekend": 1650000},
        },
    },
    "Bandung - Malang": {
        "train": {
            "Economy": {"weekday": 300000, "weekend": 320000},
            "First": {"weekday": 400000, "weekend": 420000},
        },
        "plane": {
            "Economy": {"weekday": 1680000, "weekend": 1700000},
            "First": {"weekday": 1800000, "weekend": 1820000},
        },
    },
    "Bandung - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 220000, "weekend": 240000},
            "First": {"weekday": 300000, "weekend": 320000},
        },
        "plane": {
            "Economy": {"weekday": 1100000, "weekend": 1210000},
            "First": {"weekday": 1300000, "weekend": 1340000},
        },
    },
    "Bandung - Surabaya": {
        "train": {
            "Economy": {"weekday": 350000, "weekend": 370000},
            "First": {"weekday": 430000, "weekend": 450000},
        },
        "plane": {
            "Economy": {"weekday": 1250000, "weekend": 1400000},
            "First": {"weekday": 1500000, "weekend": 1530000},
        },
    },
}

# Pricelist Ticket Yogyakarta
ygy_ticket_pricelist = {
    "Yogyakarta - Malang": {
        "train": {
            "Economy": {"weekday": 145000, "weekend": 160000},
            "First": {"weekday": 200000, "weekend": 240000},
        },
        "plane": {
            "Economy": {"weekday": 850000, "weekend": 900000},
            "First": {"weekday": 1000000, "weekend": 1050000},
        },
    },
    "Yogyakarta - Bandung": {
        "train": {
            "Economy": {"weekday": 190000, "weekend": 200000},
            "First": {"weekday": 300000, "weekend": 320000},
        },
        "plane": {
            "Economy": {"weekday": 1150000, "weekend": 1400000},
            "First": {"weekday": 1500000, "weekend": 1520000},
        },
    },
    "Yogyakarta - Jakarta": {
        "train": {
            "Economy": {"weekday": 200000, "weekend": 220000},
            "First": {"weekday": 300000, "weekend": 320000},
        },
        "plane": {
            "Economy": {"weekday": 1170000, "weekend": 1200000},
            "First": {"weekday": 1300000, "weekend": 1320000},
        },
    },
    "Yogyakarta - Surabaya": {
        "train": {
            "Economy": {"weekday": 155000, "weekend": 170000},
            "First": {"weekday": 200000, "weekend": 220000},
        },
        "plane": {
            "Economy": {"weekday": 920000, "weekend": 950000},
            "First": {"weekday": 1050000, "weekend": 1080000},
        },
    },
}

# Pricelist Ticket Surabaya
sby_ticket_pricelist = {
    "Surabaya - Malang": {
        "train": {
            "Economy": {"weekday": 75000, "weekend": 100000},
            "First": {"weekday": 150000, "weekend": 170000},
        },
        "plane": {
            "Economy": {"weekday": 650000, "weekend": 700000},
            "First": {"weekday": 800000, "weekend": 840000},
        },
    },
    "Surabaya - Bandung": {
        "train": {
            "Economy": {"weekday": 160000, "weekend": 180000},
            "First": {"weekday": 250000, "weekend": 270000},
        },
        "plane": {
            "Economy": {"weekday": 1000000, "weekend": 1160000},
            "First": {"weekday": 1300000, "weekend": 1330000},
        },
    },
    "Surabaya - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 105000, "weekend": 120000},
            "First": {"weekday": 130000, "weekend": 150000},
        },
        "plane": {
            "Economy": {"weekday": 900000, "weekend": 975000},
            "First": {"weekday": 1200000, "weekend": 1220000},
        },
    },
    "Surabaya - Jakarta": {
        "train": {
            "Economy": {"weekday": 170000, "weekend": 190000},
            "First": {"weekday": 240000, "weekend": 260000},
        },
        "plane": {
            "Economy": {"weekday": 1060000, "weekend": 1120000},
            "First": {"weekday": 1350000, "weekend": 1400000},
        },
    },
}

# Pricelist Hotels
hotel_pricelist = {
    "Jakarta": {"weekday": 0000, "weekend": 0000},
    "Malang": {"weekday": 0000, "weekend": 0000},
    "Bandung": {"weekday": 0000, "weekend": 0000},
    "Yogyakarta": {"weekday": 0000, "weekend": 0000},
    "Surabaya": {"weekday": 0000, "weekend": 0000},
}

# Header Table City
header_table_city = ["No", "Daftar Kota Keberangkatan/Tujuan"]

# Header Table Hotel
header_table_hotel = ["Kota", "Weekday/malam", "Weekend/malam"]

# Header Table Route
header_table = [
    "Route",
    "Class",
    "Train (Weekday)",
    "Train (Weekend)",
    "Plane (Weekday)",
    "Plane (Weekend)",
]

routes = []  # List of routes
classes = ["Economy", "First"]  # List of class type
transport = ["train", "plane"]  # List of transportation
days = ["weekday", "weekend"]  # Ticket

for route in jkt_ticket_pricelist.keys():
    routes.append(route)

# Create a PrettyTable instance
table_list_city = PrettyTable()  # city
table_list_hotel = PrettyTable()  # hotel

pricelist_jkt1 = PrettyTable()
pricelist_jkt2 = PrettyTable()
pricelist_jkt3 = PrettyTable()
pricelist_jkt4 = PrettyTable()

# Set the header table
table_list_city.field_names = header_table_city  # Header for City Table
table_list_hotel.field_names = header_table_hotel  # Header for Hotel Table

pricelist_jkt1.field_names = (
    pricelist_jkt2.field_names
) = pricelist_jkt3.field_names = pricelist_jkt4.field_names = header_table

# Set the alignment of columns
table_list_city.align = "l"
pricelist_jkt1.align = (
    pricelist_jkt2.align
) = pricelist_jkt3.align = pricelist_jkt4.align = "c"

# Adding row table city list
table_list_city.add_rows(
    [
        ["1", "Jakarta"],
        ["2", "Malang"],
        ["3", "Bandung"],
        ["4", "Yogyakarta"],
        ["5", "Surabaya"],
    ]
)

# Adding row table route 1: Jakarta - Malang
pricelist_jkt1.add_rows(
    [
        [
            routes[0],
            classes[0],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[0],
            classes[1],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[0]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
    ]
)

# Adding row table route 2: Jakarta - Bandung
pricelist_jkt2.add_rows(
    [
        [
            routes[1],
            classes[0],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[1],
            classes[1],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[1]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
    ]
)

# Adding row table route 3: Jakarta - Yogyakarta
pricelist_jkt3.add_rows(
    [
        [
            routes[2],
            classes[0],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[2],
            classes[1],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[2]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
    ]
)

# Adding row table route 4: Jakarta - Surabaya
pricelist_jkt4.add_rows(
    [
        [
            routes[3],
            classes[0],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[3],
            classes[1],
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                jkt_ticket_pricelist[routes[3]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
    ]
)


# Print the table
def showPriceList(
    route_number,
    pricelist_route_1,
    pricelist_route_2,
    pricelist_route_3,
    pricelist_route_4,
):
    if route_number == "1":
        print(pricelist_route_1)
    elif route_number == "2":
        print(pricelist_route_2)
    elif route_number == "3":
        print(pricelist_route_3)
    elif route_number == "4":
        print(pricelist_route_4)


# Show List City
print(table_list_city)

# Input Departure Route
departure_route = int(input("Masukkan nomor kota keberangkatan "))
print("Anda dari:", departure_route)

# Inpute Destination Route
destination_route = int(input("Masukkan nomor kota tujuan "))
print("Anda menuju:", destination_route)


# select pricelist by input user
def selectPriceList():
    if departure_route == 1:
        if destination_route == 2:
            showPriceList(
                "1", pricelist_jkt1, pricelist_jkt2, pricelist_jkt3, pricelist_jkt4
            )
        elif destination_route == 3:
            showPriceList(
                "2", pricelist_jkt1, pricelist_jkt2, pricelist_jkt3, pricelist_jkt4
            )
        elif destination_route == 4:
            showPriceList(
                "3", pricelist_jkt1, pricelist_jkt2, pricelist_jkt3, pricelist_jkt4
            )
        elif destination_route == 5:
            showPriceList(
                "4", pricelist_jkt1, pricelist_jkt2, pricelist_jkt3, pricelist_jkt4
            )
        else:
            print(
                "Mohon masukkan input kota tujuan yang berbeda dengan kota keberangkatan!"
            )
    # elif (departure_route == 2):
    #     if (destination_route == 1):
    #         showPriceList("1", pricelist_mlg1, pricelist_mlg2, pricelist_mlg3, pricelist_mlg4)
    #     elif (destination_route == 3):
    #         showPriceList("2", pricelist_mlg1, pricelist_mlg2, pricelist_mlg3, pricelist_mlg4)
    #     elif (destination_route == 4):
    #         showPriceList("3", pricelist_mlg1, pricelist_mlg2, pricelist_mlg3, pricelist_mlg4)
    #     elif (destination_route == 5):
    #         showPriceList("4", pricelist_mlg1, pricelist_mlg2, pricelist_mlg3, pricelist_mlg4)
    # elif (departure_route == 3):
    #     if (destination_route == 1):
    #         showPriceList("1", pricelist_bdg1, pricelist_bdg2, pricelist_bdg3, pricelist_bdg4)
    #     elif (destination_route == 2):
    #         showPriceList("2", pricelist_bdg1, pricelist_bdg2, pricelist_bdg3, pricelist_bdg4)
    #     elif (destination_route == 4):
    #         showPriceList("3", pricelist_bdg1, pricelist_bdg2, pricelist_bdg3, pricelist_bdg4)
    #     elif (destination_route == 5):
    #         showPriceList("4", pricelist_bdg1, pricelist_bdg2, pricelist_bdg3, pricelist_bdg4)
    # elif (departure_route == 4):
    #     if (destination_route == 1):
    #         showPriceList("1", pricelist_ygy1, pricelist_ygy2, pricelist_ygy3, pricelist_ygy4)
    #     elif (destination_route == 2):
    #         showPriceList("2", pricelist_ygy1, pricelist_ygy2, pricelist_ygy3, pricelist_ygy4)
    #     elif (destination_route == 3):
    #         showPriceList("3", pricelist_ygy1, pricelist_ygy2, pricelist_ygy3, pricelist_ygy4)
    #     elif (destination_route == 5):
    #         showPriceList("4", pricelist_ygy1, pricelist_ygy2, pricelist_ygy3, pricelist_ygy4)
    # elif (departure_route == 5):
    #     if (destination_route == 1):
    #         showPriceList("1", pricelist_sby1, pricelist_sby2, pricelist_sby3, pricelist_sby4)
    #     elif (destination_route == 2):
    #         showPriceList("2", pricelist_sby1, pricelist_sby2, pricelist_sby3, pricelist_sby4)
    #     elif (destination_route == 3):
    #         showPriceList("3", pricelist_sby1, pricelist_sby2, pricelist_sby3, pricelist_sby4)
    #     elif (destination_route == 4):
    #         showPriceList("4", pricelist_sby1, pricelist_sby2, pricelist_sby3, pricelist_sby4)


# Show table
# showPriceList("4", pricelist_jkt1, pricelist_jkt2, pricelist_jkt3, pricelist_jkt4)

selectPriceList()
