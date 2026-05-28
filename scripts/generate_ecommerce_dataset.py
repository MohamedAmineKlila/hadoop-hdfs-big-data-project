from __future__ import annotations

import argparse
import os
from datetime import datetime, timedelta


HEADER = (
    "order_id,order_date,customer_id,customer_name,customer_segment,country,city,"
    "product_id,category,product_name,quantity,unit_price,discount,payment_method,"
    "shipping_mode,order_status,rating,total_amount,profit,marketing_channel\n"
)

FIRST_NAMES = [
    "Amina", "Omar", "Lina", "Noah", "Maya", "Adam", "Sara", "Youssef",
    "Nora", "Karim", "Hana", "Elias", "Leila", "Ilyas", "Mariam", "Rayan",
]
LAST_NAMES = [
    "Bennani", "Diallo", "Mensah", "Okafor", "Hassan", "Kone", "Adeyemi",
    "Ndiaye", "Traore", "Abdi", "Khalil", "Mansour", "Toure", "Ali",
]
SEGMENTS = ["Consumer", "Corporate", "Home Office", "Small Business"]
COUNTRIES = ["Morocco", "Nigeria", "Ghana", "Kenya", "Egypt", "Senegal", "Tunisia", "South Africa"]
CITIES = ["Casablanca", "Lagos", "Accra", "Nairobi", "Cairo", "Dakar", "Tunis", "Cape Town"]
CATEGORIES = ["Electronics", "Office Supplies", "Furniture", "Health", "Fashion", "Books", "Groceries", "Sports"]
PRODUCTS = {
    "Electronics": ["Bluetooth Speaker", "Smart Watch", "USB Hub", "Wireless Mouse"],
    "Office Supplies": ["Notebook Pack", "Desk Organizer", "Printer Paper", "Ink Cartridge"],
    "Furniture": ["Office Chair", "Standing Desk", "Bookcase", "Filing Cabinet"],
    "Health": ["Vitamin Pack", "Fitness Tracker", "First Aid Kit", "Water Bottle"],
    "Fashion": ["Cotton Shirt", "Running Shoes", "Travel Backpack", "Rain Jacket"],
    "Books": ["Data Science Guide", "Business Analytics", "Cloud Computing", "Python Handbook"],
    "Groceries": ["Coffee Beans", "Olive Oil", "Rice Bag", "Tea Box"],
    "Sports": ["Yoga Mat", "Football", "Resistance Bands", "Training Gloves"],
}
PAYMENTS = ["Credit Card", "Debit Card", "Mobile Money", "Bank Transfer", "Cash on Delivery"]
SHIPPING = ["Standard", "Express", "Same Day", "Pickup Point"]
STATUS = ["Delivered", "Delivered", "Delivered", "Shipped", "Processing", "Returned"]
CHANNELS = ["Organic Search", "Paid Search", "Social Media", "Email", "Referral", "Marketplace"]


def row_for(i: int, start: datetime) -> str:
    order_date = start + timedelta(minutes=(i * 17) % 1_577_880)
    customer_id = 100_000 + (i * 37) % 900_000
    first = FIRST_NAMES[i % len(FIRST_NAMES)]
    last = LAST_NAMES[(i * 5) % len(LAST_NAMES)]
    category = CATEGORIES[(i * 7) % len(CATEGORIES)]
    product_options = PRODUCTS[category]
    product_name = product_options[(i * 11) % len(product_options)]
    quantity = 1 + (i * 13) % 9
    cents = 599 + ((i * 97) % 49_000)
    unit_price = cents / 100
    discount = [0, 0.05, 0.10, 0.15, 0.20][(i * 3) % 5]
    total = round(quantity * unit_price * (1 - discount), 2)
    profit = round(total * (0.08 + ((i * 19) % 23) / 100), 2)
    rating = 1 + (i * 29) % 5
    return (
        f"ORD{i:010d},{order_date:%Y-%m-%d %H:%M:%S},CUST{customer_id},"
        f"{first} {last},{SEGMENTS[(i * 3) % len(SEGMENTS)]},"
        f"{COUNTRIES[(i * 2) % len(COUNTRIES)]},{CITIES[(i * 2) % len(CITIES)]},"
        f"PROD{(i * 31) % 20000:05d},{category},{product_name},{quantity},"
        f"{unit_price:.2f},{discount:.2f},{PAYMENTS[(i * 5) % len(PAYMENTS)]},"
        f"{SHIPPING[(i * 7) % len(SHIPPING)]},{STATUS[(i * 11) % len(STATUS)]},"
        f"{rating},{total:.2f},{profit:.2f},{CHANNELS[(i * 17) % len(CHANNELS)]}\n"
    )


def generate(path: str, target_mib: int, chunk_rows: int = 50_000) -> tuple[int, int]:
    target_bytes = target_mib * 1024 * 1024
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    start = datetime(2023, 1, 1)
    rows = 0
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HEADER)
        while f.tell() < target_bytes:
            lines = [row_for(rows + offset + 1, start) for offset in range(chunk_rows)]
            f.writelines(lines)
            rows += chunk_rows
    return rows, os.path.getsize(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a large synthetic e-commerce CSV dataset.")
    parser.add_argument("--output", default="dataset.csv", help="Output CSV path.")
    parser.add_argument("--target-mib", type=int, default=525, help="Minimum target size in MiB.")
    args = parser.parse_args()
    rows, size = generate(args.output, args.target_mib)
    print(f"Generated {args.output}")
    print(f"Rows: {rows:,}")
    print(f"Size: {size:,} bytes ({size / (1024 * 1024):.2f} MiB)")


if __name__ == "__main__":
    main()
