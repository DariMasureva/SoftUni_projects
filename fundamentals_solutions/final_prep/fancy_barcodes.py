import re

barcode_count = int(input())
valid_barcode_pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(barcode_count):
    barcode_info = re.match(valid_barcode_pattern, input())
    if barcode_info:
        barcode = barcode_info.group(0)
        product_group = "".join([symbol for symbol in barcode if symbol.isdigit()])
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
