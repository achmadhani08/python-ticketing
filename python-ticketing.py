import locale
from datetime import datetime, timedelta
from prettytable import PrettyTable

# * set locale for currency format number
locale.setlocale(locale.LC_ALL, "id_ID")

# List city
city_list = ["Jakarta", "Malang", "Bandung", "Yogyakarta", "Surabaya"]

# Pricelist ticket Jakarta
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

# Pricelist ticket Malang
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

# Pricelist ticket Bandung
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

# Pricelist ticket Yogyakarta
ygy_ticket_pricelist = {
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

# Pricelist ticket Surabaya
sby_ticket_pricelist = {
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
}

# Pricelist hotels
hotel_pricelist = {
    "Jakarta": {"weekday": 1050000, "weekend": 1330000},
    "Malang": {"weekday": 650000, "weekend": 700000},
    "Bandung": {"weekday": 1020000, "weekend": 1070000},
    "Yogyakarta": {"weekday": 950000, "weekend": 1000000},
    "Surabaya": {"weekday": 970000, "weekend": 1020000},
}

# Header table city
header_table_city = ["No", "Daftar Kota Keberangkatan/Tujuan"]

# Header table time
header_table_time = ["No", "Waktu Keberangkatan"]

# Header table hotel
header_table_hotel = ["Kota", "Weekday/malam", "Weekend/malam"]

# Header table receipt
header_table_receipt = ["Informasi", "Keterangan"]

# Header table route
header_table_route = [
    "Route",
    "Class",
    "Train (Weekday)",
    "Train (Weekend)",
    "Plane (Weekday)",
    "Plane (Weekend)",
]

# List of routes
jkt_routes = []
mlg_routes = []
bdg_routes = []
ygy_routes = []
sby_routes = []

classes = ["Economy", "First"]  # List of class type
transport = ["train", "plane"]  # List of transportation
days = ["weekday", "weekend"]  # Type of ticket

# * Loop for route
for jkt_route in jkt_ticket_pricelist.keys():
    jkt_routes.append(jkt_route)  # Jakarta

for mlg_route in mlg_ticket_pricelist.keys():
    mlg_routes.append(mlg_route)  # Malang

for bdg_route in bdg_ticket_pricelist.keys():
    bdg_routes.append(bdg_route)  # Bandung

for ygy_route in ygy_ticket_pricelist.keys():
    ygy_routes.append(ygy_route)  # Yogyakarta

for sby_route in sby_ticket_pricelist.keys():
    sby_routes.append(sby_route)  # Surabaya

# Create a PrettyTable instance
table_list_city = PrettyTable(header_table_city)  # City table
table_departure_time = PrettyTable(header_table_time)  # Time table

table_receipt = PrettyTable(header_table_receipt)  # Receipt table
table_receipt.title = "🐍 Receipt Python Travel 🐍"  # Table receipt title

# Pricelist of hotel in each city
table_list_hotel_jkt = PrettyTable(header_table_hotel)
table_list_hotel_mlg = PrettyTable(header_table_hotel)
table_list_hotel_bdg = PrettyTable(header_table_hotel)
table_list_hotel_ygy = PrettyTable(header_table_hotel)
table_list_hotel_sby = PrettyTable(header_table_hotel)

# Pricelist of Jakarta table
pricelist_jkt1 = PrettyTable(header_table_route)
pricelist_jkt2 = PrettyTable(header_table_route)
pricelist_jkt3 = PrettyTable(header_table_route)
pricelist_jkt4 = PrettyTable(header_table_route)

# Pricelist of Malang table
pricelist_mlg1 = PrettyTable(header_table_route)
pricelist_mlg2 = PrettyTable(header_table_route)
pricelist_mlg3 = PrettyTable(header_table_route)
pricelist_mlg4 = PrettyTable(header_table_route)

# Pricelist of Bandung table
pricelist_bdg1 = PrettyTable(header_table_route)
pricelist_bdg2 = PrettyTable(header_table_route)
pricelist_bdg3 = PrettyTable(header_table_route)
pricelist_bdg4 = PrettyTable(header_table_route)

# Pricelist of Yogyakarta table
pricelist_ygy1 = PrettyTable(header_table_route)
pricelist_ygy2 = PrettyTable(header_table_route)
pricelist_ygy3 = PrettyTable(header_table_route)
pricelist_ygy4 = PrettyTable(header_table_route)

# Pricelist of Surabaya table
pricelist_sby1 = PrettyTable(header_table_route)
pricelist_sby2 = PrettyTable(header_table_route)
pricelist_sby3 = PrettyTable(header_table_route)
pricelist_sby4 = PrettyTable(header_table_route)

# Set the alignment of columns
table_list_city.align = "c"  # City table
table_departure_time.align = "c"  # Time table
table_receipt.align = "l"  # Receipt table

# Alignment of hotel columns
table_list_hotel_jkt.align = (
    table_list_hotel_mlg.align
) = (
    table_list_hotel_bdg.align
) = table_list_hotel_ygy.align = table_list_hotel_sby.align = "c"

# Alignment of Jakarta route columns
pricelist_jkt1.align = (
    pricelist_jkt2.align
) = pricelist_jkt3.align = pricelist_jkt4.align = "c"

# Alignment of Malang route columns
pricelist_mlg1.align = (
    pricelist_mlg2.align
) = pricelist_mlg3.align = pricelist_mlg4.align = "c"

# Alignment of Bandung route columns
pricelist_bdg1.align = (
    pricelist_bdg2.align
) = pricelist_bdg3.align = pricelist_bdg4.align = "c"

# Alignment of Yogyakarta route columns
pricelist_ygy1.align = (
    pricelist_ygy2.align
) = pricelist_ygy3.align = pricelist_ygy4.align = "c"

# Alignment of Surabaya route columns
pricelist_sby1.align = (
    pricelist_sby2.align
) = pricelist_sby3.align = pricelist_sby4.align = "c"

# * Adding rows table city list
table_list_city.add_rows(
    [[str(index), city] for index, city in enumerate(city_list, start=1)]
)

# * Adding rows table departure time
table_departure_time.add_rows(
    [
        ["1", "08:00"],
        ["2", "16:00"],
        ["3", "20:00"],
    ]
)


# * fn for dynamic add row table hotel
def table_list_hotel(pricelist_hotel, city):
    pricelist_hotel.add_row(
        [
            city_list[city],
            "Rp"
            + locale.format_string(
                "%d",
                hotel_pricelist[city_list[city]][days[0]],
                grouping=True,
            ),
            "Rp"
            + locale.format_string(
                "%d",
                hotel_pricelist[city_list[city]][days[1]],
                grouping=True,
            ),
        ]
    )
    print(pricelist_hotel)


# * fn for dynamic add rows table routes
def table_list_route(pricelist_city_table, city_routes, pricelist_city_routes, route):
    pricelist_city_table.add_rows(
        [
            [
                city_routes[route],
                classes[0],
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[0]][classes[0]][
                        days[0]
                    ],
                    grouping=True,
                ),
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[0]][classes[0]][
                        days[1]
                    ],
                    grouping=True,
                ),
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[1]][classes[0]][
                        days[0]
                    ],
                    grouping=True,
                ),
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[1]][classes[0]][
                        days[1]
                    ],
                    grouping=True,
                ),
            ],
            [
                city_routes[route],
                classes[1],
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[0]][classes[1]][
                        days[0]
                    ],
                    grouping=True,
                ),
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[0]][classes[1]][
                        days[1]
                    ],
                    grouping=True,
                ),
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[1]][classes[1]][
                        days[0]
                    ],
                    grouping=True,
                ),
                "Rp"
                + locale.format_string(
                    "%d",
                    pricelist_city_routes[city_routes[route]][transport[1]][classes[1]][
                        days[1]
                    ],
                    grouping=True,
                ),
            ],
        ]
    )

    print(pricelist_city_table)


# * Select table pricelist & set estimated time by input user
def selectPriceList():
    global estimatedTime
    if departure_route == 1:
        if destination_route == 2:  # Jakarta - Malang
            table_list_route(pricelist_jkt1, jkt_routes, jkt_ticket_pricelist, 0)
            estimatedTime = 12
        elif destination_route == 3:  # Jakarta - Bandung
            table_list_route(pricelist_jkt2, jkt_routes, jkt_ticket_pricelist, 1)
            estimatedTime = 3
        elif destination_route == 4:  # Jakarta - Yogyakarta
            table_list_route(pricelist_jkt3, jkt_routes, jkt_ticket_pricelist, 2)
            estimatedTime = 8
        elif destination_route == 5:  # Jakarta - Surabaya
            table_list_route(pricelist_jkt4, jkt_routes, jkt_ticket_pricelist, 3)
            estimatedTime = 10
        else:
            print(
                "Mohon masukkan input kota tujuan yang berbeda dengan kota keberangkatan!"
            )
    elif departure_route == 2:
        if destination_route == 1:  # Malang - Jakarta
            table_list_route(pricelist_mlg1, mlg_routes, mlg_ticket_pricelist, 0)
            estimatedTime = 12
        elif destination_route == 3:  # Malang - Bandung
            table_list_route(pricelist_mlg2, mlg_routes, mlg_ticket_pricelist, 1)
            estimatedTime = 15
        elif destination_route == 4:  # Malang - Yogyakarta
            table_list_route(pricelist_mlg3, mlg_routes, mlg_ticket_pricelist, 2)
            estimatedTime = 7
        elif destination_route == 5:  # Malang - Surabaya
            table_list_route(pricelist_mlg2, mlg_routes, mlg_ticket_pricelist, 3)
            estimatedTime = 3
        else:
            print(
                "Mohon masukkan input kota tujuan yang berbeda dengan kota keberangkatan!"
            )
    elif departure_route == 3:
        if destination_route == 1:  # Bandung - Jakarta
            table_list_route(pricelist_bdg1, bdg_routes, bdg_ticket_pricelist, 0)
            estimatedTime = 3
        elif destination_route == 2:  # Bandung - Malang
            table_list_route(pricelist_bdg2, bdg_routes, bdg_ticket_pricelist, 1)
            estimatedTime = 15
        elif destination_route == 4:  # Bandung - Yogyakarta
            table_list_route(pricelist_bdg3, bdg_routes, bdg_ticket_pricelist, 2)
            estimatedTime = 9
        elif destination_route == 5:  # Bandung - Surabaya
            table_list_route(pricelist_bdg4, bdg_routes, bdg_ticket_pricelist, 3)
            estimatedTime = 13
        else:
            print(
                "Mohon masukkan input kota tujuan yang berbeda dengan kota keberangkatan!"
            )
    elif departure_route == 4:
        if destination_route == 1:  # Yogyakarta - Jakarta
            table_list_route(pricelist_ygy1, ygy_routes, ygy_ticket_pricelist, 0)
            estimatedTime = 8
        elif destination_route == 2:  # Yogyakarta - Malang
            table_list_route(pricelist_ygy2, ygy_routes, ygy_ticket_pricelist, 1)
            estimatedTime = 7
        elif destination_route == 3:  # Yogyakarta - Bandung
            table_list_route(pricelist_ygy3, ygy_routes, ygy_ticket_pricelist, 2)
            estimatedTime = 9
        elif destination_route == 5:  # Yogyakarta - Surabaya
            table_list_route(pricelist_ygy4, ygy_routes, ygy_ticket_pricelist, 3)
            estimatedTime = 4
        else:
            print(
                "Mohon masukkan input kota tujuan yang berbeda dengan kota keberangkatan!"
            )
    elif departure_route == 5:
        if destination_route == 1:  # Surabaya - Jakarta
            table_list_route(pricelist_sby1, sby_routes, sby_ticket_pricelist, 0)
            estimatedTime = 10
        elif destination_route == 2:  # Surabaya - Malang
            table_list_route(pricelist_sby2, sby_routes, sby_ticket_pricelist, 1)
            estimatedTime = 3
        elif destination_route == 3:  # Surabaya - Bandung
            table_list_route(pricelist_sby3, sby_routes, sby_ticket_pricelist, 2)
            estimatedTime = 13
        elif destination_route == 4:  # Surabaya - Yogyakarta
            table_list_route(pricelist_sby4, sby_routes, sby_ticket_pricelist, 3)
            estimatedTime = 4
        else:
            print(
                "Mohon masukkan input kota tujuan yang berbeda dengan kota keberangkatan!"
            )


# * Show hotel price at selected city destination and set weekday/weekend hotel price
def showHotelPrice():
    global weekdayHotelPrice
    global weekendHotelPrice

    if destination_route == 1:
        table_list_hotel(table_list_hotel_jkt, 0)
        weekdayHotelPrice = hotel_pricelist[city_list[0]][days[0]]
        weekendHotelPrice = hotel_pricelist[city_list[0]][days[1]]
    elif destination_route == 2:
        table_list_hotel(table_list_hotel_mlg, 1)
        weekdayHotelPrice = hotel_pricelist[city_list[1]][days[0]]
        weekendHotelPrice = hotel_pricelist[city_list[1]][days[1]]
    elif destination_route == 3:
        table_list_hotel(table_list_hotel_bdg, 2)
        weekdayHotelPrice = hotel_pricelist[city_list[2]][days[0]]
        weekendHotelPrice = hotel_pricelist[city_list[2]][days[1]]
    elif destination_route == 4:
        table_list_hotel(table_list_hotel_ygy, 3)
        weekdayHotelPrice = hotel_pricelist[city_list[3]][days[0]]
        weekendHotelPrice = hotel_pricelist[city_list[3]][days[1]]
    elif destination_route == 5:
        table_list_hotel(table_list_hotel_sby, 4)
        weekdayHotelPrice = hotel_pricelist[city_list[4]][days[0]]
        weekendHotelPrice = hotel_pricelist[city_list[4]][days[1]]


# * Calculate arrival time
def calculateArrivalTime(datetime_object, add_hours):
    future_datetime_transportation = datetime_object + timedelta(hours=add_hours)

    # Format the future date and time as a string
    formatted_future_datetime_transportation = future_datetime_transportation.strftime(
        "%d %B %Y %H:%M"
    )

    return formatted_future_datetime_transportation


# * Calculate check-in & check-out hotel
def calculateCheckInOutTime(datetime_object, add_days):
    global calculatedCheckInTime
    global calculatedCheckOutTime

    datetime_checkin_hotel = datetime_object + timedelta(
        hours=2
    )  # add 2 hours after arrival time for check-in
    datetime_checkout_hotel = (
        datetime_object + timedelta(hours=2) + timedelta(days=add_days)
    )

    # Format the future date and time as a string
    formatted_checkin_datetime_hotel = datetime_checkin_hotel.strftime("%d %B %Y %H:%M")
    formatted_checkout_datetime_hotel = datetime_checkout_hotel.strftime(
        "%d %B %Y %H:%M"
    )

    calculatedCheckInTime = formatted_checkin_datetime_hotel
    calculatedCheckOutTime = formatted_checkout_datetime_hotel


# * Count bill for hotel (weekday/weekend)
def calculate_hotel_bill(start_date, num_days, roomHotel, weekday, weekend):
    weekday_rate = weekday
    weekend_rate = weekend
    total_bill = 0

    current_date = start_date
    for _ in range(num_days):
        # Check if the current day is a weekday (Monday=0, Sunday=6)
        if current_date.weekday() < 5:
            total_bill += weekday_rate
        else:
            total_bill += weekend_rate

        # Move to the next day
        current_date += timedelta(days=1)

    return total_bill * roomHotel


# * Start interact with user
print("\n")  # Adding space
print("Selamat datang di 🐍 Python Travel 🐍") # Intro
print("\n")  # Adding space

print(table_list_city) # Show list city

# Input departure route
departure_route = int(input("Masukkan nomor kota keberangkatan: "))
departure_city = str

# Input destination route
destination_route = int(input("Masukkan nomor kota tujuan: "))
destination_city = str

# set estimated route time
estimatedTime = int

# * Check departure city
if departure_route == 1:
    departure_city = "Jakarta"
elif departure_route == 2:
    departure_city = "Malang"
elif departure_route == 3:
    departure_city = "Bandung"
elif departure_route == 4:
    departure_city = "Yogyakarta"
elif departure_route == 5:
    departure_city = "Surabaya"

# * Check destination city
if destination_route == 1:
    destination_city = "Jakarta"
elif destination_route == 2:
    destination_city = "Malang"
elif destination_route == 3:
    destination_city = "Bandung"
elif destination_route == 4:
    destination_city = "Yogyakarta"
elif destination_route == 5:
    destination_city = "Surabaya"

print("\n")  # Adding space
selectPriceList()  # * Show pricelist of selected route & set estimate time

dateOfDeparture = str(input("Masukkan tanggal keberangkatan (tanggal bulan tahun): "))

# * Parse string input date user into datetime object
date_object = datetime.strptime(dateOfDeparture, "%d %B %Y")

isWeekend = bool

# Check if the day of the week is weekend // 0 Monday, 6 Sunday
if date_object.weekday() in [5, 6]:
    print("Anda akan memesan tiket jenis weekend")
    isWeekend = True
else:
    print("Anda akan memesan tiket jenis weekday")
    isWeekend = False

print("\n")  # Adding space
selectTransportType = int(
    input("Tiket transportasi apa yang Anda pesan?\n(1. Kereta | 2. Pesawat): ")
)

selectClassType = int(
    input("Tiket kelas apa yang Anda pesan?\n(1. Economy | 2. First): ")
)

countTicket = int(input("Berapa banyak tiket yang Anda pesan? "))

# * Print time table and let user decide
print("\n")  # Adding space
print(table_departure_time)
selectTime = int(input("Masukkan nomor waktu keberangkatan Anda: "))
selectedTime = str

# * Check selected time
if selectTime == 1:
    selectedTime = "08:00"
elif selectTime == 2:
    selectedTime = "16:00"
elif selectTime == 3:
    selectedTime = "20:00"

# * Combine departure date and time
combinedDepartureDateTime = f"{dateOfDeparture} {selectedTime}"

# * Parse the combined string for departure datetime into a datetime object
combined_departure_datetime_object = datetime.strptime(
    combinedDepartureDateTime, "%d %B %Y %H:%M"
)

# * Calculated future datetime
calculatedArrivalTime = calculateArrivalTime(
    combined_departure_datetime_object, estimatedTime
)

print("\n")  # Adding space

bookHotel = int(
    input(
        "Apakah Anda ingin memesan hotel di tempat tujuan?\nWaktu check-in 2 jam setelah tiba.\n(1. Ya | 2. Tidak): "
    )
)

roomHotel = int
daysHotel = int
calculatedCheckInTime = str
calculatedCheckOutTime = str

weekdayHotelPrice = int
weekendHotelPrice = int
billHotel = int

# * Parse the combined string for arrival datetime into a datetime object
combined_arrival_datetime_object = datetime.strptime(
    calculatedArrivalTime, "%d %B %Y %H:%M"
)


# * Adding rows table receipt
def printReceipt(transport_price):
    priceTotal = (transport_price * countTicket) + (billHotel if bookHotel == 1 else 0)

    table_receipt.add_row(["Kota keberangkatan:", departure_city])
    table_receipt.add_row(["Kota tujuan:", destination_city])
    table_receipt.add_row(["Tanggal & Waktu keberangkatan:", combinedDepartureDateTime])
    table_receipt.add_row(["Estimasi Waktu Tiba:", calculatedArrivalTime])
    table_receipt.add_row(
        ["Jenis tiket:", "Weekend" if isWeekend == True else "Weekday"]
    )
    table_receipt.add_row(
        ["Jenis transportasi:", "Kereta" if selectTransportType == 1 else "Pesawat"]
    )
    table_receipt.add_row(
        ["Kelas tiket:", "Ekonomi" if selectClassType == 1 else "First"]
    )
    table_receipt.add_row(["Banyak tiket:", countTicket], divider=True)

    table_receipt.add_row(["Booking hotel:", "Ya" if bookHotel == 1 else "Tidak"])
    table_receipt.add_row(
        ["Waktu Check In:", calculatedCheckInTime if bookHotel == 1 else "-"]
    )
    table_receipt.add_row(
        ["Waktu Check Out:", calculatedCheckOutTime if bookHotel == 1 else "-"]
    )
    table_receipt.add_row(["Banyak kamar:", roomHotel if bookHotel == 1 else 0])
    table_receipt.add_row(
        ["Lama menginap (malam):", daysHotel if bookHotel == 1 else 0], divider=True
    )

    # Price section
    table_receipt.add_row(
        [
            "Harga tiket transportasi:",
            "Rp"
            + locale.format_string(
                "%d",
                transport_price * countTicket,
                grouping=True,
            ),
        ]
    )
    table_receipt.add_row(
        [
            "Harga kamar hotel:",
            "Rp"
            + locale.format_string(
                "%d",
                billHotel if bookHotel == 1 else 0,
                grouping=True,
            ),
        ],
        divider=True,
    )
    table_receipt.add_row(
        [
            "Total harga:",
            "Rp"
            + locale.format_string(
                "%d",
                priceTotal,
                grouping=True,
            ),
        ]
    )

    print(table_receipt)


# * Selecting price depend on user input route and hotel
def selectingPrice():
    # * Selecting price for Jakarta route
    if departure_route == 1 and destination_route == 2:  # Jakarta - Malang
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[0]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 1 and destination_route == 3:  # Jakarta - Bandung
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[1]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 1 and destination_route == 4:  # Jakarta - Yogyakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[2]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 1 and destination_route == 5:  # Jakarta - Surabaya
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        jkt_ticket_pricelist[jkt_routes[3]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    # * Selecting price for Malang route
    elif departure_route == 2 and destination_route == 1:  # Malang - Jakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[0]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 2 and destination_route == 3:  # Malang - Bandung
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[1]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 2 and destination_route == 4:  # Malang  Yogyakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[2]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 2 and destination_route == 5:  # Malang - Surabaya
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        mlg_ticket_pricelist[mlg_routes[3]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    # * Selecting price for Bandung route
    elif departure_route == 3 and destination_route == 1:  # Bandung - Jakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[0]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 3 and destination_route == 2:  # Bandung - Malang
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[1]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 3 and destination_route == 4:  # Bandung - Yogyakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[2]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 3 and destination_route == 5:  # Bandung - Surabaya
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        bdg_ticket_pricelist[bdg_routes[3]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    # * Selecting price for Yogyakarta route
    elif departure_route == 4 and destination_route == 1:  # Yogyakarta - Jakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[0]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 4 and destination_route == 2:  # Yogyakarta - Malang
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[1]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 4 and destination_route == 3:  # Yogyakarta - Bandung
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[2]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 4 and destination_route == 5:  # Yogyakarta - Surabaya
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        ygy_ticket_pricelist[ygy_routes[3]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    # * Selecting price for Surabaya route
    elif departure_route == 5 and destination_route == 1:  # Surabaya - Jakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[0]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 5 and destination_route == 2:  # Surabaya - Malang
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[1]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 5 and destination_route == 3:  # Surabaya - Bandung
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[2]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )
    elif departure_route == 5 and destination_route == 4:  # Surabaya - Yogyakarta
        if selectTransportType == 1:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[0]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[0]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[0]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[0]][classes[1]][
                            days[1]
                        ]
                    )
        elif selectTransportType == 2:
            if selectClassType == 1:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[1]][classes[0]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[1]][classes[0]][
                            days[1]
                        ]
                    )
            elif selectClassType == 2:
                if isWeekend == False:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[1]][classes[1]][
                            days[0]
                        ]
                    )
                elif isWeekend == True:
                    printReceipt(
                        sby_ticket_pricelist[sby_routes[3]][transport[1]][classes[1]][
                            days[1]
                        ]
                    )


# * Check if bookhotel and lastly print receipt
if bookHotel == 1:
    print("\n")  # Adding space
    showHotelPrice()
    roomHotel = int(input("Berapa banyak kamar yang Anda pesan? "))
    daysHotel = int(input("Berapa lama Anda menginap? (malam): "))
    calculateCheckInOutTime(combined_arrival_datetime_object, daysHotel)
    billHotel = calculate_hotel_bill(
        combined_arrival_datetime_object,
        daysHotel,
        roomHotel,
        weekdayHotelPrice,
        weekendHotelPrice,
    )

    print("\n")  # Adding space
    selectingPrice()
    print("\n")  # Adding space
    print("Silahkan lakukan pembayaran dalam 1x24 jam")
    print("\n")  # Adding space
else:
    print("\n")  # Adding space
    selectingPrice()
    print("\n")  # Adding space
    print("Silahkan lakukan pembayaran dalam 1x24 jam")
    print("\n")  # Adding space
