vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
def decode(tone):
    s = tone.lower()
    pin = ''
    for ch in s:
        if ch in consonants:
            idx = consonants.find(ch)
        elif ch in vowels:
            idx2 = vowels.find(ch)
            line = 'pin {0} idx {1} idx2 {2}'.format(pin, idx, idx2)
            print line
            
            pin = str(pin) + str(idx*5 + idx2)


    print pin

if __name__ == '__main__':
    decode('bomelela')
    decode('bomeluco')
