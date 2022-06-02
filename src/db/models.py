"""coding=utf-8."""

from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey, Float

from .database import Base


class User(Base):
    """User Class contains standard information for a User."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    document = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Employee(Base):
    """User Class contains standard information for a User."""

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column("user_id", ForeignKey(User.id))
    job = Column(String, unique=True, index=True)


class Invoice(Base):
    """User Class contains standard information for a User."""

    __tablename__ = "invoice"

    id = Column(String, primary_key=True, index=True)
    client_id = Column(String, unique=True, index=True)
    employee_id = Column("employee_id", ForeignKey(Employee.id))
    # mesa_id = Column(Boolean, default=True)
    created_at = Column(Date)
    total = Column(Float)


class Product(Base):
    """User Class contains standard information for a User."""

    __tablename__ = "product"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)


class DetailInvoice(Base):
    """User Class contains standard information for a User."""

    __tablename__ = "detail_invoice"

    id = Column(String, primary_key=True, index=True)
    invoice_id = Column(String, unique=True, index=True)
    product_id = Column(String)


class DailyProduction(Base):
    """User Class contains standard information for a User."""

    __tablename__ = "daily_production"

    id = Column(String, primary_key=True, index=True)
    chicken = Column(Integer, index=True)
    date = Column(Date)

