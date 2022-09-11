quake1palette = [0,0,0,          15,15,15,       31,31,31,       47,47,47,
                 63,63,63,       75,75,75,       91,91,91,       107,107,107,
                 123,123,123,    139,139,139,    155,155,155,    171,171,171,
                 187,187,187,    203,203,203,    219,219,219,    235,235,235,
                 15,11,7,        23,15,11,       31,23,11,       39,27,15,
                 47,35,19,       55,43,23,       63,47,23,       75,55,27,
                 83,59,27,       91,67,31,       99,75,31,       107,83,31,
                 115,87,31,      123,95,35,      131,103,35,     143,111,35,
                 11,11,15,       19,19,27,       27,27,39,       39,39,51,
                 47,47,63,       55,55,75,       63,63,87,       71,71,103,
                 79,79,115,      91,91,127,      99,99,139,      107,107,151,
                 115,115,163,    123,123,175,    131,131,187,    139,139,203,
                 0,0,0,          7,7,0,          11,11,0,        19,19,0,
                 27,27,0,        35,35,0,        43,43,7,        47,47,7,
                 55,55,7,        63,63,7,        71,71,7,        75,75,11,
                 83,83,11,       91,91,11,       99,99,11,       107,107,15,
                 7,0,0,          15,0,0,         23,0,0,         31,0,0,
                 39,0,0,         47,0,0,         55,0,0,         63,0,0,
                 71,0,0,         79,0,0,         87,0,0,         95,0,0,
                 103,0,0,        111,0,0,        119,0,0,        127,0,0,
                 19,19,0,        27,27,0,        35,35,0,        47,43,0,
                 55,47,0,        67,55,0,        75,59,7,        87,67,7,
                 95,71,7,        107,75,11,      119,83,15,      131,87,19,
                 139,91,19,      151,95,27,      163,99,31,      175,103,35,
                 35,19,7,        47,23,11,       59,31,15,       75,35,19,
                 87,43,23,       99,47,31,       115,55,35,      127,59,43,
                 143,67,51,      159,79,51,      175,99,47,      191,119,47,
                 207,143,43,     223,171,39,     239,203,31,     255,243,27,
                 11,7,0,         27,19,0,        43,35,15,       55,43,19,
                 71,51,27,       83,55,35,       99,63,43,       111,71,51,
                 127,83,63,      139,95,71,      155,107,83,     167,123,95,
                 183,135,107,    195,147,123,    211,163,139,    227,179,151,
                 171,139,163,    159,127,151,    147,115,135,    139,103,123,
                 127,91,111,     119,83,99,      107,75,87,      95,63,75,
                 87,55,67,       75,47,55,       67,39,47,       55,31,35,
                 43,23,27,       35,19,19,       23,11,11,       15,7,7,
                 187,115,159,    175,107,143,    163,95,131,     151,87,119,
                 139,79,107,     127,75,95,      115,67,83,      107,59,75,
                 95,51,63,       83,43,55,       71,35,43,       59,31,35,
                 47,23,27,       35,19,19,       23,11,11,       15,7,7,
                 219,195,187,    203,179,167,    191,163,155,    175,151,139,
                 163,135,123,    151,123,111,    135,111,95,     123,99,83,
                 107,87,71,      95,75,59,       83,63,51,       67,51,39,
                 55,43,31,       39,31,23,       27,19,15,       15,11,7,
                 111,131,123,    103,123,111,    95,115,103,     87,107,95,
                 79,99,87,       71,91,79,       63,83,71,       55,75,63,
                 47,67,55,       43,59,47,       35,51,39,       31,43,31,
                 23,35,23,       15,27,19,       11,19,11,       7,11,7,
                 255,243,27,     239,223,23,     219,203,19,     203,183,15,
                 187,167,15,     171,151,11,     155,131,7,      139,115,7,
                 123,99,7,       107,83,0,       91,71,0,        75,55,0,
                 59,43,0,        43,31,0,        27,15,0,        11,7,0,
                 0,0,255,        11,11,239,      19,19,223,      27,27,207,
                 35,35,191,      43,43,175,      47,47,159,      47,47,143,
                 47,47,127,      47,47,111,      47,47,95,       43,43,79,
                 35,35,63,       27,27,47,       19,19,31,       11,11,15,
                 43,0,0,         59,0,0,         75,7,0,         95,7,0,
                 111,15,0,       127,23,7,       147,31,7,       163,39,11,
                 183,51,15,      195,75,27,      207,99,43,      219,127,59,
                 227,151,79,     231,171,95,     239,191,119,    247,211,139,
                 167,123,59,     183,155,55,     199,195,55,     231,227,87,
                 127,191,255,    171,231,255,    215,255,255,    103,0,0,
                 139,0, 0,       179,0,0,        215,0,0,        255,0,0,
                 255,243,147,    255,247,199,    255,255,255,    159,91,83]

import os, sys, struct
from PIL import Image

if len (sys.argv) == 1:
    in_path = input("any2wad\nDrag'n'drop an image or a folder of images"\
                    " to convert them to a Quake WAD2 file.\n"\
                    "Alternatively, input the name below"\
                    " (or press Enter to exit)\n")
else:
    in_path = sys.argv[1]

imagepaths = []
if os.path.isfile(in_path):
    imagepaths = [in_path]
elif os.path.isdir(in_path):
    for root, subdirs, files in os.walk(in_path):
        imagepaths.extend([os.path.join(root,f) for f in files])
else:
    input("ERROR: no such path")

dummy = Image.new('P', (16, 16))
pal_nofb = quake1palette[:-32*3] + [0,0,0]*32
pal_fence = pal_nofb[:-3] + [159, 91, 83]

# MIP
# http://www.gamers.org/dEngine/quake/spec/quake-spec34/qkspec_4.htm#BL2
mipN = 4
# ratio = 2**(mipN-1)
ratio = 16 # compat

mipdata = []
for imagefile in imagepaths:
    name = os.path.basename(imagefile)
    try:
        image = Image.open(imagefile, 'r')
    except:
        print(f"WARNING: '{name}' is not a valid image file, skipping")
        continue

    size = image.size

    if image.mode != 'P':
        print(f"'{name}' is not an indexed image, converting to Quake palette")
        if name[0] == '{':
            if image.mode == 'RGBA':
                print(f"Getting transparency from alpha channel in '{name}'")
                matte = Image.new('RGB', size, (159,91,83))
                alpha = image.split()[-1]
                alpha = alpha.point(lambda p: p > 128 and 255) # threshold
                matte.paste(image, mask=alpha)
                image = matte
            dummy.putpalette(pal_fence)
        else:
            dummy.putpalette(pal_nofb)
        dummy.load()
        image.load()
        image = image._new(image.im.convert('P', 0, dummy.im))
    elif 'transparency' in image.info and name[0] == '{':
        print(f"Getting transparency from alpha channel in '{name}'")
        matte = Image.new('P', size, 255)
        alpha = image.convert('RGBA').split()[-1]
        alpha = alpha.point(lambda p: p > 128 and 255) # threshold
        matte.paste(image, mask=alpha)
        image = matte

    if (size[0]%ratio) or (size[1]%ratio):
        print(f"WARNING: dimensions of '{name}' aren't multiples of {ratio}")
    name = os.path.splitext(name)[0]
    if len(name) > 15:
        print(f"WARNING: name '{name}' is longer than 15 chars, truncating")
        name = name[:15]

    off = [16 + 4*(2+mipN),]
    mip = [image.tobytes(),]
    for i in range(1,mipN):
        off.append(off[i-1] + len(mip[i-1]))
        mip.append(image.resize((size[0]//2**i,size[1]//2**i)).tobytes())

    mipname = name.replace("#","*").encode('ascii')
    miptex = struct.pack(f'<16s{2+mipN}L', mipname, *size, *off)
    miptex += b''.join(mip)
    mipdata.append([mipname,miptex])

# WAD
# http://www.gamers.org/dEngine/quake/spec/quake-spec34/qkspec_7.htm
# http://hlbsp.sourceforge.net/index.php?content=waddef
numentries = len(mipdata)
wadname = os.path.splitext(os.path.basename(in_path))[0]
if numentries:
    with open (wadname + ".wad", 'wb') as wad:
        wad.write(struct.pack('<4s2l', b'WAD2', numentries, 12))
        wadoffset = 12 + 32*numentries
        for wadentry in mipdata:
            miplen = len(wadentry[1])
            wad.write(struct.pack('<3l', wadoffset, miplen, miplen))
            wad.write(struct.pack('<s?h16s', b'D', False, 0, wadentry[0]))
            wadoffset += miplen
        for wadentry in mipdata:
            wad.write(wadentry[1])
