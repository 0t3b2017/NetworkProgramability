# coding=utf-8
# Verify if it's a valid IPv4 address


#IP = "192.168.0.1"
#MASK = "255.255.255.0"

vermelho = "\033[31m"
verde = "\033[32m"
limpa = "\033[m"

def valida_ip(IP):
    OCT = IP.split(".")

    # Valida se são 4 octetos:
    if len(OCT) != 4:
        print("IP inválido!")
        print("IP deve conter 4 octetos separados por '.'")
        return
    # Valida se são apenas números:
    for x in OCT:
         if not x.isdecimal():
             print("IP inválido!")
             print("IP só pode conter números.")
             return
    # Valida se octeto tem 8 bits
    for x in OCT:
        if int(x).bit_length() > 8:
            print("IP inválido!")
            print("Octeto válido de 0 à 255.")
            return
    # Separa cada octeto, remove o '0b' e preenche com 0s à esquerda (se necessário) para conter 8 digitos.
    OCT1 = bin(int(OCT[0]))[2:].zfill(8)
    OCT2 = bin(int(OCT[1]))[2:].zfill(8)
    OCT3 = bin(int(OCT[2]))[2:].zfill(8)
    OCT4 = bin(int(OCT[3]))[2:].zfill(8)

    print("{}Os octetos do IP {} em binário são: {}, {}, {} e {}.".format(verde, IP, OCT1, OCT2, OCT3, OCT4, limpa))

def valida_mask(MASK):
    OCT = MASK.split(".")

    # Valida se são 4 octetos;
    if len(OCT) != 4:
        print("Mascára inválida!".format(vermelho))
        print("Mascará deve conter 4 octetos separados por '.'")
        return
    # Valida se são apenas números:
    for x in OCT:
         if not x.isdecimal():
             print("Mascára inválida!".format(vermelho))
             print("Mascára só pode conter números.")
             return

    # Valida se octeto tem 8 bits
    for x in OCT:
        if int(x).bit_length() > 8:
            print("{}Máscara inválida!".format(vermelho))
            print("Octetos válidos são: 0, 128, 192, 224, 240, 248, 252, 254 e 255.{}".format(limpa))
            return
    """
    # Valida se octeto é valido para máscara:
    for x in OCT:
        if x not in ["0", "128", "192", "224", "240", "248", "252", "254", "255"]:
            print("Mascára inválida!")
            print("Octetos válidos são: 0, 128, 192, 224, 240, 248, 252, 254 e 255.")
            return
    """

    # Separa cada octeto e preenche com 0 (se necessário) para conter 8 digitos.
    OCT1 = bin(int(OCT[0]))[2:].zfill(8)
    OCT2 = bin(int(OCT[1]))[2:].zfill(8)
    OCT3 = bin(int(OCT[2]))[2:].zfill(8)
    OCT4 = bin(int(OCT[3]))[2:].zfill(8)

    # Valida se máscara é sequencia de 1s e depois 0s
    MASKBIN = str(OCT1 + OCT2 + OCT3 + OCT4)
    print(MASKBIN)
    fisrtz = MASKBIN.find('0')
    zeros = MASKBIN[fisrtz:]
    print(zeros)
    if '1' in zeros:
        print("{}Sequência de bits inválidos na mascára.".format(vermelho))
        print("Octetos válidos são: 0, 128, 192, 224, 240, 248, 252, 254 e 255.{}".format(limpa))
        return
    print("{}Os octetos da Máscara {} em binário são: {}, {}, {} e {}.{}".format(verde, MASK, OCT1, OCT2, OCT3, OCT4, limpa))

IP = str(input("Type an IPv4 address: "))
MASK = str(input("Type the Netmask: "))
print()
valida_ip(IP)
print()
valida_mask(MASK)
