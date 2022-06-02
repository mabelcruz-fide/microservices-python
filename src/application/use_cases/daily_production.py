from datetime import datetime

from ...domain.entity import DailyProduction, Invoice, Product
from ...application.adapter.postgres import PostgresAdapter
from uuid import uuid4


class Sale:
    def __init__(self):
        self.postgres_adapter = PostgresAdapter()

    def save_daily_production(self, daily_production) -> None:
        daily_production_entity = DailyProduction()
        daily_production_entity.id = str(uuid4())
        daily_production_entity.chicken = daily_production.chicken
        daily_production_entity.date = datetime.now().date()
        self.postgres_adapter.create_daily_production(daily_production_entity)

    def get_daily_production(self):
        return self.postgres_adapter.get_all_daily_production()

    def save_invoice(self, invoice) -> None:
        invoice_entity = Invoice(
            id=str(uuid4()),
            client_id=invoice.client_id,
            employee_id=invoice.employee_id,
            type=invoice.type,
            product_ids=invoice.product_ids,
        )
        print(invoice.product_ids)
        self.postgres_adapter.save_invoice(invoice_entity)

    def save_product(self, product) -> Product:
        product_entity = Product(
            id=str(uuid4()),
            name=product.name,
            price=product.price
        )
        self.postgres_adapter.save_product(product_entity)
        return product_entity

    def get_all_product(self):
        return self.postgres_adapter.get_all_product()

    def get_all_invoice(self):
        return self.postgres_adapter.get_all_invoices()
