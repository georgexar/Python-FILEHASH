def FILEHASH(fl):
    f = open(fl, 'r')
    content = f.read()
    f.close()

    list = []
    for i in content:
        list.append(i)

    for i in range(len(list)):
        list[i] = str(ord(list[i]))
        if i > 0:
            if i % 16 == 0:
                list[i - 1] += '\n'

    f=open(fl,'w')
    for i in list:
        f.write(i)
    f.close()



    sum = 0
    listexit = []
    for istart in range(16):
        for i in range(istart, len(list), 16):
            sum = sum + int(list[i])
        listexit.append(sum % 256)
        sum = 0

    hexstring = ''
    for i in range(len(listexit)):
        if listexit[i] < 16:
            hexstring = hexstring + '0' + hex(listexit[i])
        else:
            hexstring = hexstring + hex(listexit[i])
        hexstring = hexstring.replace('0x', '')
    return hexstring
'''Για input ειναι ο παρακατω κωδικας
FILEHASH(input('ΒΑΛΕ ΤΟ ΑΡΧΕΙΟ: '))'''



