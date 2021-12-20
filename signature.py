from rsa import RSA
from keccak import Keccak
from typing import List

class Signature:
  """
  Class for signing a message. Message signing is done with RSA and SHA3 algorithm
  """
  
  @staticmethod
  def sign(message: str, private_key: List[int]) -> str:
    """
    Get the signature of a given message.
    """
    keccak = Keccak("SHA3-256", message)
    hash = keccak.hash()
    signature = RSA.encrypt(hash, private_key)
    return signature

  
  @staticmethod
  def verifySignedTicket(message: str, signature: str, public_key: List[int]) -> bool:
    """
    Verify signature of a given message and separated signature.
    """
    keccak = Keccak("SHA3-256", message)
    hash = keccak.hash()

    decrypted = RSA.decrypt(signature, public_key)

    return hash == decrypted
    
  @staticmethod
  def wrapTicket(id: int, type: str, seat:str, price:int):
    ticket = "id = " + str(id) + "\r\n" + "type = " + type + "\r\n" + "seat = " + seat + "\r\n" + "price = " + str(price)
    return ticket

def main():
  message = Signature.wrapTicket(1, "Platinum", "A2", 100000)
  print("Message:", message)

  keys = RSA.generateKey()
  print("Keys:", keys)

  signature = Signature.sign(message, keys[1])
  print("Signed_Message:", signature)

  verify = Signature.verifySignedTicket(message, signature, keys[0])
  print("Verify:", verify)
    
if __name__ == "__main__":
  main()