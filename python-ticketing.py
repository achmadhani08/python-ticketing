import locale
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, "id_ID")

# List ticket
jkt_ticket_pricelist = {
    "Jakarta - Malang": {
        "train": {
            "Economy": {"weekday": 210000, "weekend": 240000},
            "First": {"weekday": 120, "weekend": 150},
        },
        "plane": {
            "Economy": {"weekday": 1070000, "weekend": 1150000},
            "First": {"weekday": 200, "weekend": 250},
        },
    },
    "Jakarta - Bandung": {
        "train": {
            "Economy": {"weekday": 63000, "weekend": 110000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 560000, "weekend": 570000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Jakarta - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 200000, "weekend": 220000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 870000, "weekend": 975000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Jakarta - Surabaya": {
        "train": {
            "Economy": {"weekday": 220000, "weekend": 240000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 950000, "weekend": 1120000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
}

mlg_ticket_pricelist = {
    "Malang - Jakarta": {
        "train": {
            "Economy": {"weekday": 170000, "weekend": 200000},
            "First": {"weekday": 120, "weekend": 150},
        },
        "plane": {
            "Economy": {"weekday": 890000, "weekend": 930000},
            "First": {"weekday": 200, "weekend": 250},
        },
    },
    "Malang - Bandung": {
        "train": {
            "Economy": {"weekday": 150000, "weekend": 170000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 800000, "weekend": 840000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Malang - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 100000, "weekend": 130000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 710000, "weekend": 760000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Malang - Surabaya": {
        "train": {
            "Economy": {"weekday": 75000, "weekend": 90000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 630000, "weekend": 660000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
}

bdg_ticket_pricelist = {
    "Bandung - Jakarta": {
        "train": {
            "Economy": {"weekday": 150000, "weekend": 170000},
            "First": {"weekday": 120, "weekend": 150},
        },
        "plane": {
            "Economy": {"weekday": 1280000, "weekend": 1450000},
            "First": {"weekday": 200, "weekend": 250},
        },
    },
    "Bandung - Malang": {
        "train": {
            "Economy": {"weekday": 300000, "weekend": 320000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1680000, "weekend": 1700000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Bandung - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 220000, "weekend": 240000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1100000, "weekend": 1210000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Bandung - Surabaya": {
        "train": {
            "Economy": {"weekday": 350000, "weekend": 370000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1250000, "weekend": 1400000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
}

ygy_ticket_pricelist = {
    "Yogyakarta - Malang": {
        "train": {
            "Economy": {"weekday": 145000, "weekend": 160000},
            "First": {"weekday": 120, "weekend": 150},
        },
        "plane": {
            "Economy": {"weekday": 850000, "weekend": 900000},
            "First": {"weekday": 200, "weekend": 250},
        },
    },
    "Yogyakarta - Bandung": {
        "train": {
            "Economy": {"weekday": 190000, "weekend": 200000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1150000, "weekend": 1700000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Yogyakarta - Jakarta": {
        "train": {
            "Economy": {"weekday": 200000, "weekend": 220000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1170000, "weekend": 1200000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Yogyakarta - Surabaya": {
        "train": {
            "Economy": {"weekday": 155000, "weekend": 170000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 920000, "weekend": 950000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
}

sby_ticket_pricelist = {
    "Surabaya - Malang": {
        "train": {
            "Economy": {"weekday": 75000, "weekend": 100000},
            "First": {"weekday": 120, "weekend": 150},
        },
        "plane": {
            "Economy": {"weekday": 650000, "weekend": 700000},
            "First": {"weekday": 200, "weekend": 250},
        },
    },
    "Surabaya - Bandung": {
        "train": {
            "Economy": {"weekday": 160000, "weekend": 180000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1000000, "weekend": 1160000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Surabaya - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 105000, "weekend": 120000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 900000, "weekend": 975000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Surabaya - Jakarta": {
        "train": {
            "Economy": {"weekday": 170000, "weekend": 190000},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 1060000, "weekend": 1120000},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
}
# Variables
header_table = [
    "Route",
    "Class",
    "Train (Weekday)",
    "Train (Weekend)",
    "Plane (Weekday)",
    "Plane (Weekend)",
]

routes = []  # List of routes
classes = ["Economy", "Business", "First"]  # List of class type
transport = ["train", "plane"]  # List of transportation
days = ["weekday", "weekend"]  # Ticket

for route in ticket_pricelist.keys():
    routes.append(route)

# Create a PrettyTable instance
pricelist_route1 = PrettyTable()
pricelist_route2 = PrettyTable()
pricelist_route3 = PrettyTable()
pricelist_route4 = PrettyTable()

# Set the header table
pricelist_route1.field_names = (
    pricelist_route2.field_names
) = pricelist_route3.field_names = pricelist_route4.field_names = header_table

# Set the alignment of columns
pricelist_route1.align = (
    pricelist_route2.align
) = pricelist_route3.align = pricelist_route4.align = "c"

# Adding row table route 1: Jakarta - Malang
pricelist_route1.add_rows(
    [
        [
            routes[0],
            classes[0],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[0],
            classes[1],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[0],
            classes[2],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[0]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[0]][classes[2]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[1]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[0]][transport[1]][classes[2]][days[1]],
                grouping=True,
            ),
        ],
    ]
)

# Adding row table route 2: Jakarta - Bandung
pricelist_route2.add_rows(
    [
        [
            routes[1],
            classes[0],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[1],
            classes[1],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[1],
            classes[2],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[0]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[0]][classes[2]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[1]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[1]][transport[1]][classes[2]][days[1]],
                grouping=True,
            ),
        ],
    ]
)

# Adding row table route 3: Jakarta - Yogyakarta
pricelist_route3.add_rows(
    [
        [
            routes[2],
            classes[0],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[2],
            classes[1],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[2],
            classes[2],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[0]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[0]][classes[2]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[1]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[2]][transport[1]][classes[2]][days[1]],
                grouping=True,
            ),
        ],
    ]
)

# Adding row table route 4: Jakarta - Surabaya
pricelist_route4.add_rows(
    [
        [
            routes[3],
            classes[0],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[0]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[0]][classes[0]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[1]][classes[0]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[1]][classes[0]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[3],
            classes[1],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[0]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[0]][classes[1]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[1]][classes[1]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[1]][classes[1]][days[1]],
                grouping=True,
            ),
        ],
        [
            routes[3],
            classes[2],
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[0]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[0]][classes[2]][days[1]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[1]][classes[2]][days[0]],
                grouping=True,
            ),
            locale.format_string(
                "%d",
                ticket_pricelist[routes[3]][transport[1]][classes[2]][days[1]],
                grouping=True,
            ),
        ],
    ]
)


# Print the table
def showPriceList(route):
    if route == "1":
        print(pricelist_route1)
    elif route == "2":
        print(pricelist_route2)
    elif route == "3":
        print(pricelist_route3)
    elif route == "4":
        print(pricelist_route4)


# Show table
showPriceList("4")
