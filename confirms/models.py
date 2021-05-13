from enum import Enum
from typing import List
from uuid import UUID


class Currency(Enum):
    VND = "VND"


class Gross:
    amount: float
    currency: Currency

    def __init__(self, amount: float, currency: Currency) -> None:
        self.amount = amount
        self.currency = currency


class Price:
    currency: Currency
    gross: Gross
    net: Gross

    def __init__(self, currency: Currency, gross: Gross, net: Gross) -> None:
        self.currency = currency
        self.gross = gross
        self.net = net


class AttributeAttribute:
    id: str
    name: str

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name


class Value:
    id: str
    name: str
    value: str

    def __init__(self, id: str, name: str, value: str) -> None:
        self.id = id
        self.name = name
        self.value = value


class AttributeElement:
    attribute: AttributeAttribute
    values: List[Value]

    def __init__(self, attribute: AttributeAttribute, values: List[Value]) -> None:
        self.attribute = attribute
        self.values = values


class ShippingPrice:
    gross: Gross
    net: Gross

    def __init__(self, gross: Gross, net: Gross) -> None:
        self.gross = gross
        self.net = net


class Pricing:
    on_sale: bool
    price_undiscounted: ShippingPrice
    price: ShippingPrice

    def __init__(self, on_sale: bool, price_undiscounted: ShippingPrice, price: ShippingPrice) -> None:
        self.on_sale = on_sale
        self.price_undiscounted = price_undiscounted
        self.price = price


class ProductType:
    id: str
    is_shipping_required: bool

    def __init__(self, id: str, is_shipping_required: bool) -> None:
        self.id = id
        self.is_shipping_required = is_shipping_required


class Thumbnail:
    url: str
    alt: str

    def __init__(self, url: str, alt: str) -> None:
        self.url = url
        self.alt = alt


class Thumbnail2X:
    url: str

    def __init__(self, url: str) -> None:
        self.url = url


class Product:
    id: str
    name: str
    thumbnail: Thumbnail
    thumbnail2_x: Thumbnail2X
    product_type: ProductType

    def __init__(self, id: str, name: str, thumbnail: Thumbnail, thumbnail2_x: Thumbnail2X, product_type: ProductType) -> None:
        self.id = id
        self.name = name
        self.thumbnail = thumbnail
        self.thumbnail2_x = thumbnail2_x
        self.product_type = product_type


class Variant:
    id: str
    name: str
    sku: int
    quantity_available: int
    is_available: bool
    pricing: Pricing
    attributes: List[AttributeElement]
    product: Product

    def __init__(self, id: str, name: str, sku: int, quantity_available: int, is_available: bool, pricing: Pricing, attributes: List[AttributeElement], product: Product) -> None:
        self.id = id
        self.name = name
        self.sku = sku
        self.quantity_available = quantity_available
        self.is_available = is_available
        self.pricing = pricing
        self.attributes = attributes
        self.product = product


class Line:
    product_name: str
    quantity: int
    variant: Variant
    unit_price: Price
    total_price: Price

    def __init__(self, product_name: str, quantity: int, variant: Variant, unit_price: Price, total_price: Price) -> None:
        self.product_name = product_name
        self.quantity = quantity
        self.variant = variant
        self.unit_price = unit_price
        self.total_price = total_price


class Country:
    code: str
    country: str

    def __init__(self, code: str, country: str) -> None:
        self.code = code
        self.country = country


class ShippingAddress:
    id: str
    first_name: str
    last_name: str
    company_name: str
    street_address1: str
    street_address2: str
    city: str
    postal_code: str
    country: Country
    country_area: str
    phone: str
    is_default_billing_address: None
    is_default_shipping_address: None

    def __init__(self, id: str, first_name: str, last_name: str, company_name: str, street_address1: str, street_address2: str, city: str, postal_code: str, country: Country, country_area: str, phone: str, is_default_billing_address: None, is_default_shipping_address: None) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.street_address1 = street_address1
        self.street_address2 = street_address2
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.country_area = country_area
        self.phone = phone
        self.is_default_billing_address = is_default_billing_address
        self.is_default_shipping_address = is_default_shipping_address


class Order:
    user_email: str
    payment_status: str
    payment_status_display: str
    status: str
    status_display: str
    id: str
    token: UUID
    number: int
    point_used: int
    shipping_address: ShippingAddress
    lines: List[Line]
    subtotal: ShippingPrice
    total: ShippingPrice
    shipping_price: ShippingPrice

    def __init__(self, user_email: str, payment_status: str, payment_status_display: str, status: str, status_display: str, id: str, token: UUID, number: int, point_used: int, shipping_address: ShippingAddress, lines: List[Line], subtotal: ShippingPrice, total: ShippingPrice, shipping_price: ShippingPrice) -> None:
        self.user_email = user_email
        self.payment_status = payment_status
        self.payment_status_display = payment_status_display
        self.status = status
        self.status_display = status_display
        self.id = id
        self.token = token
        self.number = number
        self.point_used = point_used
        self.shipping_address = shipping_address
        self.lines = lines
        self.subtotal = subtotal
        self.total = total
        self.shipping_price = shipping_price