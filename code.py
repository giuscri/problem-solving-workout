#!/usr/bin/python3

import struct

# The two frames of the binary we're using
f0, e_f0 = 0x80482f1, 0x8048300
f1, e_f1 = 0x8048304, 0x804830e

# Where we're putting our string
s = 0x804833b

# The original entry point of the binary
ep = 0x80482d0

# Tokens 
tks = []

# Building the bytes translation of
#
#    pushal
#    xor     %edx, %edx
#    add     $5, %edx
#    movl    $0x804833b, %ecx
#    xorl    %ebx, %ebx
#    jmp     <f1 - e_f0>
#
tk = b'\x60\x31\xd2\x83\xc2\x05'
tk += b'\xb9' + struct.pack('<I', s)
tk += b'\x31\xdb'
tk += b'\xeb' + struct.pack('<B', f1 - e_f0)
 
tks.append(tk)

# Building the bytes translation of
#
#    xorl    %eax, %eax
#    addl    $4, %eax
#    int     $0x80
#    popal
#    jmp     <ep - e_f1>
#
tk = b'\x31\xc0\x83\xc0\x04\xcd\x80\x61'
tk += b'\xeb' + struct.pack('<b', ep - e_f1)

tks.append(tk)

# "Macro" to move between v_addresses and file osets
baddress = 0x8048000
scale = lambda x,baddress=baddress: x-baddress
rescale = lambda x,baddress=baddress: x+baddress

with open('main', 'rb+') as main:

    # Write the two frames onto the binary
    main.seek(scale(f0))
    main.write(tks[0])
    main.seek(scale(f1))
    main.write(tks[1])

    # Write the string
    main.seek(scale(s))
    main.write(b'Pwnd\x0a')

    # Finally, rewrite the original entry point
    main.seek(24)
    main.write(struct.pack('<I', f0))
