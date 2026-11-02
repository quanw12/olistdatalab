"""Generate a small, deterministic, Olist-shaped dataset.

The real dataset (Kaggle, CC BY-NC-ND) cannot be committed or downloaded in CI, so tests and
CI run on this synthetic sample. It has the same files, columns and formats, plus the quirks
that make the real data hard: per-order customer ids, multi-payment orders, orders without
items, missing delivery dates, Portuguese review text and messy status casing.
"""

from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

TS = "%Y-%m-%d %H:%M:%S"
STATES = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA", "PE", "GO", "DF"]
CITIES = {
    "SP": "sao paulo", "RJ": "rio de janeiro", "MG": "belo horizonte", "RS": "porto alegre",
    "PR": "curitiba", "SC": "florianopolis", "BA": "salvador", "PE": "recife",
    "GO": "goiania", "DF": "brasilia",
}
CATEGORIES = {
    "beleza_saude": "health_beauty",
    "cama_mesa_banho": "bed_bath_table",
    "esporte_lazer": "sports_leisure",
    "informatica_acessorios": "computers_accessories",
    "moveis_decoracao": "furniture_decor",
    "utilidades_domesticas": "housewares",
    "relogios_presentes": "watches_gifts",
    "telefonia": "telephony",
}
PAYMENT_TYPES = ["credit_card", "credit_card", "credit_card", "boleto", "debit_card"]
REVIEWS = {
    5: ["Produto excelente, chegou antes do prazo", "Recomendo, muito bom", "Ótima qualidade"],
    4: ["Bom produto, entrega dentro do prazo", "Gostei, mas a embalagem veio amassada"],
    3: ["Produto ok, demorou um pouco", "Razoável, esperava mais"],
    2: ["Entrega atrasada e sem resposta do vendedor", "Produto diferente do anunciado"],
    1: ["Não recebi o produto", "Veio quebrado, quero meu dinheiro de volta",
        "Produto errado e atraso na entrega"],
}

FILES = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def _hex(rng: random.Random) -> str:
    return f"{rng.getrandbits(128):032x}"


def _write(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def generate(out_dir: Path, n_orders: int = 2000, seed: int = 42) -> dict[str, int]:
    """Write the sample CSVs into out_dir and return the row count per table."""
    rng = random.Random(seed)
    start = datetime(2017, 1, 1)

    sellers = []
    for _ in range(60):
        state = rng.choice(STATES)
        sellers.append([_hex(rng), f"{rng.randint(1000, 99999):05d}", CITIES[state], state])

    products = []
    for _ in range(300):
        category = rng.choice(list(CATEGORIES))
        products.append([
            _hex(rng), category, rng.randint(20, 60), rng.randint(100, 2000), rng.randint(1, 6),
            rng.randint(100, 15000), rng.randint(10, 80), rng.randint(2, 60), rng.randint(10, 60),
        ])

    # The same person gets a new customer_id for every order; customer_unique_id is the person.
    people = []
    for _ in range(int(n_orders * 0.9)):
        state = rng.choice(STATES)
        people.append((_hex(rng), f"{rng.randint(1000, 99999):05d}", CITIES[state], state))

    orders, items, payments, reviews, customers = [], [], [], [], []
    for _ in range(n_orders):
        order_id, customer_id = _hex(rng), _hex(rng)
        unique_id, zip_code, city, state = rng.choice(people)
        customers.append([customer_id, unique_id, zip_code, city, state])

        purchase = start + timedelta(minutes=rng.randint(0, 60 * 24 * 600))
        status = rng.choices(
            ["delivered", "shipped", "canceled", "unavailable", "invoiced", "processing"],
            weights=[90, 3, 2, 2, 2, 1],
        )[0]
        approved = purchase + timedelta(minutes=rng.randint(5, 60 * 48))
        carrier = approved + timedelta(hours=rng.randint(12, 120))
        delivered = carrier + timedelta(hours=rng.randint(24, 24 * 20))
        estimated = (purchase + timedelta(days=rng.randint(15, 35))).replace(hour=0, minute=0,
                                                                             second=0)
        row = [order_id, customer_id, status, purchase.strftime(TS), approved.strftime(TS),
               carrier.strftime(TS), delivered.strftime(TS), estimated.strftime(TS)]
        if status != "delivered":
            row[5] = row[5] if status == "shipped" else ""
            row[6] = ""
        elif rng.random() < 0.01:
            row[6] = ""  # delivered, but the delivery date was never recorded
        if rng.random() < 0.01:
            row[2] = f" {status.title()} "  # messy casing/spaces the cleaner must normalize
        orders.append(row)

        n_items = 0 if status == "unavailable" else rng.choices([1, 2, 3], weights=[85, 12, 3])[0]
        order_total = 0.0
        for item_no in range(1, n_items + 1):
            price = round(rng.uniform(10, 500), 2)
            freight = round(rng.uniform(5, 60), 2)
            order_total += price + freight
            items.append([order_id, item_no, rng.choice(products)[0], rng.choice(sellers)[0],
                          (approved + timedelta(days=3)).strftime(TS), f"{price:.2f}",
                          f"{freight:.2f}"])

        # Unavailable orders were often still charged (and refunded outside this dataset).
        paid = order_total if n_items else round(rng.uniform(20, 300), 2)
        if rng.random() < 0.05 and paid > 30:
            voucher = round(rng.uniform(5, paid / 2), 2)
            payments.append([order_id, 1, "voucher", 1, f"{voucher:.2f}"])
            payments.append([order_id, 2, "credit_card", rng.randint(1, 10),
                             f"{paid - voucher:.2f}"])
        else:
            kind = rng.choice(PAYMENT_TYPES)
            installments = rng.randint(1, 10) if kind == "credit_card" else 1
            payments.append([order_id, 1, kind, installments, f"{paid:.2f}"])

        if status in {"delivered", "canceled", "unavailable"} and rng.random() < 0.95:
            late = row[6] != "" and row[6] > row[7]
            score = rng.choices([1, 2, 3, 4, 5],
                                weights=[30, 15, 20, 15, 20] if late else [5, 3, 8, 20, 64])[0]
            message = rng.choice(REVIEWS[score]) if rng.random() < 0.45 else ""
            created = (purchase + timedelta(days=rng.randint(8, 30))).replace(
                hour=0, minute=0, second=0)
            reviews.append([_hex(rng), order_id, score, "", message, created.strftime(TS),
                            (created + timedelta(hours=rng.randint(5, 72))).strftime(TS)])

    tables = {
        "orders": (["order_id", "customer_id", "order_status", "order_purchase_timestamp",
                    "order_approved_at", "order_delivered_carrier_date",
                    "order_delivered_customer_date", "order_estimated_delivery_date"], orders),
        "order_items": (["order_id", "order_item_id", "product_id", "seller_id",
                         "shipping_limit_date", "price", "freight_value"], items),
        "order_payments": (["order_id", "payment_sequential", "payment_type",
                            "payment_installments", "payment_value"], payments),
        "order_reviews": (["review_id", "order_id", "review_score", "review_comment_title",
                           "review_comment_message", "review_creation_date",
                           "review_answer_timestamp"], reviews),
        "customers": (["customer_id", "customer_unique_id", "customer_zip_code_prefix",
                       "customer_city", "customer_state"], customers),
        "sellers": (["seller_id", "seller_zip_code_prefix", "seller_city", "seller_state"],
                    sellers),
        # "lenght" is misspelled in the real dataset too; the contract keeps the source name.
        "products": (["product_id", "product_category_name", "product_name_lenght",
                      "product_description_lenght", "product_photos_qty", "product_weight_g",
                      "product_length_cm", "product_height_cm", "product_width_cm"], products),
        "category_translation": (["product_category_name", "product_category_name_english"],
                                 [list(pair) for pair in CATEGORIES.items()]),
    }
    for name, (header, rows) in tables.items():
        _write(out_dir / FILES[name], header, rows)
    return {name: len(rows) for name, (_, rows) in tables.items()}
