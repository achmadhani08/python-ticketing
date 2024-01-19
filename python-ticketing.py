import locale
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, "id_ID")

# List ticket
ticket_pricelist = {
    "Jakarta - Malang": {
        "train": {
            "Economy": {"weekday": 600000, "weekend": 635000},
            "Business": {"weekday": 80, "weekend": 90},
            "First": {"weekday": 120, "weekend": 150},
        },
        "plane": {
            "Economy": {"weekday": 1070000, "weekend": 1150000},
            "Business": {"weekday": 150, "weekend": 180},
            "First": {"weekday": 200, "weekend": 250},
        },
    },
    "Jakarta - Bandung": {
        "train": {
            "Economy": {"weekday": 150000, "weekend": 180000},
            "Business": {"weekday": 60, "weekend": 70},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 560000, "weekend": 570000},
            "Business": {"weekday": 120, "weekend": 150},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Jakarta - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 500000, "weekend": 520000},
            "Business": {"weekday": 60, "weekend": 70},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 870000, "weekend": 975000},
            "Business": {"weekday": 120, "weekend": 150},
            "First": {"weekday": 180, "weekend": 220},
        },
    },
    "Jakarta - Surabaya": {
        "train": {
            "Economy": {"weekday": 540000, "weekend": 570000},
            "Business": {"weekday": 60, "weekend": 70},
            "First": {"weekday": 100, "weekend": 120},
        },
        "plane": {
            "Economy": {"weekday": 950000, "weekend": 1120000},
            "Business": {"weekday": 120, "weekend": 150},
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
