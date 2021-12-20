from fastapi import APIRouter
from config.db import connection
from models.index import tickets
from schemas.index import Ticket, SignedTicket
from rsa import RSA
from signature import Signature
ticket = APIRouter()

@ticket.get("/ticket/")
async def read_ticket():
    return connection.execute(tickets.select()).fetchall()

@ticket.get("/ticket/{id}")
async def read_ticket(id: int):
    result = connection.execute(tickets.select().where(tickets.c.id == id)).fetchall()
    if(result):
        print("id:", result[0]['id'])
    return result

@ticket.post("/ticket/")
async def add_ticket(ticket: Ticket):
    keys = RSA.generateKey()
    result = connection.execute(tickets.insert().values(
        id = ticket.id,
        type= ticket.type,
        seat= ticket.seat,
        price = ticket.price,
        available = True,
        public_key1 = keys[0][0],
        public_key2 = keys[0][1],
        private_key1 = keys[1][0],
        private_key2 = keys[1][1],
    ))
    return connection.execute(tickets.select()).fetchall()

@ticket.put("/ticket/{id}")
async def update_ticket(id: int, ticket: Ticket):
    keys = RSA.generateKey()
    result = connection.execute(tickets.update().values(
        id = ticket.id,
        type= ticket.type,
        seat= ticket.seat,
        price = ticket.price,
        available = ticket.available,
        public_key1 = keys[0][0],
        public_key2 = keys[0][1],
        private_key1 = keys[1][0],
        private_key2 = keys[1][1],
    ).where(tickets.c.id == id))
    print(result)
    return connection.execute(tickets.select()).fetchall()

@ticket.delete("/ticket/{id}")
async def delete_ticket(id: int):
    connection.execute(tickets.delete().where(tickets.c.id == id))
    return connection.execute(tickets.select()).fetchall()

@ticket.put("/buy/{id}")
async def buy_ticket(id: int):
    result = connection.execute(tickets.update().values(
        available = False
    ).where(tickets.c.id == id))
    ticket = connection.execute(tickets.select().where(tickets.c.id == id)).fetchall()
    wrapped_ticket = Signature.wrapTicket(ticket[0]['id'], ticket[0]['type'], ticket[0]['seat'], ticket[0]['price'])
    ticket_signature = Signature.sign(wrapped_ticket, [ticket[0]['private_key1'], ticket[0]['private_key2']])
    response = {"id" : ticket[0]['id'],
    "type" : ticket[0]['type'],
    "seat" : ticket[0]['seat'],
    "price" : ticket[0]['price'],
    "signature" : ticket_signature
    }
    return response

@ticket.post("/verify/")
async def verify_ticket(signed_ticket : SignedTicket):
    wrapped_ticket = Signature.wrapTicket(signed_ticket.id, signed_ticket.type, signed_ticket.seat, signed_ticket.price)
    ticket = connection.execute(tickets.select().where(tickets.c.id == signed_ticket.id)).fetchall()
    verify = Signature.verifySignedTicket(wrapped_ticket, signed_ticket.signature, [ticket[0]['public_key1'], ticket[0]['public_key2']])
    response = {"id" : signed_ticket.id,
    "type" : signed_ticket.type,
    "seat" : signed_ticket.seat,
    "price" : signed_ticket.price,
    "signature" : signed_ticket.signature,
    "is_ticket_valid" : verify,
    }
    return response