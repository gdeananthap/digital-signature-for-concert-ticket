from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    type: str
    seat: str
    price: str
    available : bool

class SignedTicket(BaseModel):
    id: int
    type: str
    seat: str
    price: str
    signature : str