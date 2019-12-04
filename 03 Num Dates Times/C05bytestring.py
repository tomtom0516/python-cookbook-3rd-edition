import binascii
# byte string 2 int
data_s = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
len(data_s)
data_i = int.from_bytes(data_s, 'little')
int.from_bytes(data_s, 'big')

hex_str = binascii.b2a_hex(data_s)
print(hex_str)
# byte string 2 string
int.to_bytes()




