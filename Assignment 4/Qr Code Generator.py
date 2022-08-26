
import qrcode as qc
import os
import random as rnd

while True:
    text = input("Enter You're Desired Text: ")
    saving_address = input("Enter The Desired Destination You Wanna Store You're Produced Qr-Code: ")
    os.chdir(saving_address)
    
    data = text

    qr = qc.QRCode(version = rnd.randint(1 , 40) , error_correction = qc.ERROR_CORRECT_L 
                   , box_size = rnd.randint(1 , 15) , border = rnd.randint(1 , 15))

    qc.add_data(data)
    qc.make(fit = True)

    img = qc.make_image(fill_color = (rnd.randint(0 , 255) , rnd.randint(0 , 255) , rnd.randint(0 , 255)) 
                        , back_color = (rnd.randint(0 , 255) , rnd.randint(0 , 255) , rnd.randint(0 , 255)))
    img.save("Qr-Code.JPG")
