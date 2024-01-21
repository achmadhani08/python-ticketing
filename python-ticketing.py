import locale
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, "id_ID")

# List ticket Jakarta
jkt_ticket_pricelist = {
    "Jakarta - Malang": {
        "train": {
            "Economy": {"weekday": 210000, "weekend": 240000},
            "First": {"weekday": 225000, "weekend": 250000},
        },
        "plane": {
            "Economy": {"weekday": 910000, "weekend": 950000},
            "First": {"weekday": 1070000, "weekend": 1150000},
        },
    },
    "Jakarta - Bandung": {
        "train": {
            "Economy": {"weekday": 63000, "weekend": 110000},
            "First": {"weekday": 200000, "weekend": 225000},
        },
        "plane": {
            "Economy": {"weekday": 560000, "weekend": 570000},
            "First": {"weekday": 1400000, "weekend": 1600000},
        },
    },
    "Jakarta - Yogyakarta": {
        "train": {
            "Economy": {"weekday": 200000, "weekend": 220000},
            "First": {"weekday": 550000, "weekend": 570000},
        },
        "plane": {
            "Economy": {"weekday": 870000, "weekend": 975000},
            "First": {"weekday": 925000, "weekend": 1000000},
        },
    },
    "Jakarta - Surabaya": {
        "train": {
            "Economy": {"weekday": 220000, "weekend": 240000},
            "First": {"weekday": 240000, "weekend": 260000},
        },
        "plane": {
            "Economy": {"weekday": 950000, "weekend": 1120000},
            "First": {"weekday": 1000000, "weekend": 1300000},
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
classes = ["Economy", "First"]  # List of class type
transport = ["train", "plane"]  # List of transportation
days = ["weekday", "weekend"]  # Ticket

for route in jkt_ticket_pricelist.keys():
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
pricelist_route2.add_rows(
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
pricelist_route3.add_rows(
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
pricelist_route4.add_rows(
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
