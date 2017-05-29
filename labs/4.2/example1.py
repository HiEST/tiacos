import os
import sys


(r, w) = os.pipe()

NewPiD = os.fork()

if NewPiD == 0:
    # Child
    os.close(r)
    msg_to_send = "Hola"
    print("Soc el fill i envio un",msg_to_send,"al pare")
    os.write(w,msg_to_send.encode())
    os.close (w)
else:
    # Prent
    os.close(w)
    msg = os.read(r,4)
    print("Soc el pare i he rebut un",msg.decode(),"del fill")
    os.close(r)

