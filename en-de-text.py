# python3
# code for encode and decode text with base64

import base64

print("Mohamed Salah")
while True :
    num = input("""
    
    1 > Encode
    2 > Decode
    >> : """)

    if num == "1":
        encode_text = input("Enter Your Text For Encode It >> : ")
        encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')
        print("--------------------------------")
        print("Doen : "+ encode_hash)
        print("----------------------------------")
    elif num == "2":
        decode_text = input("Enter Your Hash For Decode It >> :")
        decode_hash = base64.b64decode(decode_text)
        decodeit = decode_hash.decode('UTF-8')
        print("----------------------------------")
        print("Done : "+ decodeit)
        print("-------------------------------------")
    else:
        print("Type Just 1 Or 2 !!")

