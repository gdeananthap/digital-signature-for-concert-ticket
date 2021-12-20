from sqlalchemy import Table,Column,Integer, String, Boolean
from config.db import meta

tickets = Table(
    'tickets', meta, 
    Column('id', Integer, primary_key=True),
    Column('type', String(255)),
    Column('seat', String(255)),
    Column('price', Integer),    
    Column('available', Boolean),
    Column('public_key1', Integer),
    Column('public_key2', Integer),
    Column('private_key1', Integer),
    Column('private_key2', Integer),
)