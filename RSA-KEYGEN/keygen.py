
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

keyPair = RSA.generate(4096)

privateexp=keyPair.exportKey("PEM")
pubKey2 = keyPair.publickey().exportKey("PEM")

private = open("privkey.pem", "wb")
private.write(privateexp)
private.close()

public = open("pubkey.pem", "wb")
public.write(pubKey2)
public.close()
