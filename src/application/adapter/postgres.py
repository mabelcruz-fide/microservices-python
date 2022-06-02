from datetime import datetime
from typing import List
from uuid import uuid4

from src.db.database import SessionLocal
from src.domain.entity import DailyProduction, Product
from src.domain.entity import Invoice
from src.db.models import DailyProduction as DailyProductionAdapter, Product as ProductAdapter
from src.db.models import Invoice as InvoiceAdapter, DetailInvoice as DetailInvoiceAdapter


class PostgresAdapter:
    def __init__(self):
        """Key FCMNotification."""
        self.session = SessionLocal()

    def create_daily_production(self, daily_production: DailyProduction):
        daily_production_adapter = DailyProductionAdapter()
        daily_production_adapter.id = daily_production.id
        daily_production_adapter.chicken = daily_production.chicken
        daily_production_adapter.date = daily_production.date
        self.session.add(daily_production_adapter)
        self.session.commit()

    def save_invoice(self, invoice: Invoice):
        invoice_adapter = InvoiceAdapter()
        invoice_adapter.id = invoice.id
        invoice_adapter.client_id = invoice.client_id
        invoice_adapter.employee_id = invoice.employee_id
        self.session.add(invoice_adapter)
        self.session.commit()

        for product in invoice.product_ids:
            details_invoice_adapter = DetailInvoiceAdapter()
            details_invoice_adapter.id = str(uuid4())
            details_invoice_adapter.invoice_id = invoice_adapter.id
            details_invoice_adapter.product_id = product
            self.session.add(details_invoice_adapter)
            self.session.commit()

    def save_product(self, product: Product):
        product_adapter = ProductAdapter()
        product_adapter.id = product.id
        product_adapter.name = product.name
        product_adapter.price = product.price
        self.session.add(product_adapter)
        self.session.commit()

    def get_all_product(self) -> List[Product]:
        products = self.session.query(ProductAdapter).all()
        products_all = []
        for i in products:
            product_entity = Product(
                id=i.id,
                name=i.name,
                price=i.price
            )
            products_all.append(product_entity)
        return products_all

    def get_all_invoices(self) -> List[Product]:
        invoices = self.session.query(InvoiceAdapter).all()
        invoices_all = []
        for i in invoices:
            invoice = Invoice(
                id=i.id,
                client_id=i.client_id,
                employee_id=i.employee_id,
                created_at=i.created_at,
                total=i.total
            )
            invoices_all.append(invoice)
        return invoices_all

    def get_all_daily_production(self) -> List[DailyProduction]:
        invoices = self.session.query(DailyProductionAdapter).all()
        invoices_all = []
        for i in invoices:
            invoice = DailyProduction(
                id=i.id,
                chicken=i.chicken
            )
            invoices_all.append(invoice)
        return invoices_all


