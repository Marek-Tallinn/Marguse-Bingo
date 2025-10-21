import random

bingo_reelid = {
    'B': 5,
    'I': 5,
    'N': 5,
    'G': 5,
    'O': 5
}

#def jama siin noh
def saa_bingo_pall(kasutatud_pallid):
    kõik_pallid = list(range(1,26))
    saadavad_pallid = set(kõik_pallid) - kasutatud_pallid
    if saadavad_pallid:
        pall = random.choice((list(saadavad_pallid)))
        kasutatud_pallid.add(pall)
        return pall
    return None

def bingo_kaart(kaart):
    ridade_arv = []

    #read
    for rida in kaart:
        ridade_arv.append(rida)

    #veerud
    for veerg_indeks in range(5):
        veerud = [kaart[rea_indeks][veerg_indeks] for rea_indeks in range(5)]
        ridade_arv.append(veerud)
    
    #diagonaalid
    diag1 = [kaart[i][i] for i in range(5)]
    diag2 = [kaart[i][4-i] for i in range(5)]
    ridade_arv.append(diag1)
    ridade_arv.append(diag2)

    for line in ridade_arv:
        if all(cell == "X" for cell in line):
            return True
    return False

def genereeri_kaardid():
    kaart = [[0]*5 for _ in range(5)]
    for col in range(5):
        kasutatud_numbrid = set()
        for row in range(5):
            if row == 2 and col == 2:
                kaart[row][col] = "X" #Paneb keskele X tähe
                continue
            while True:
                number = random.randint(col*5 + 1, col*5 + 5)
                if number not in kasutatud_numbrid:
                    kaart[row][col] = number
                    kasutatud_numbrid.add(number)
                    break
    return kaart

def print_kaart(kaart):
    for row in kaart:
        print(' '.join(str(x).rjust(2) for x in row))
    print()


def loo_mängijad():
    mängijad = []
    mitu_mängijat = int(input(f"Mitu mängijat mängib? "))
    for i in range(1, mitu_mängijat + 1):
        mitu_kaarti = int(input(f"Mitu kaarti on mängijal {i}? "))
        kaardid = [genereeri_kaardid() for _ in range(mitu_kaarti)]
        mängijad.append({
            'nimi': f"Mängija {i}",
            'kaardid': kaardid
        })
    return mängijad

def mängi_bingot():
    mängijad = loo_mängijad()
    kasutatud_pallid = set()

    while True:
        pall = saa_bingo_pall(kasutatud_pallid)
        if pall is None:
            print("Kõik bingopallid on välja võetud. Mäng jäi viiki.")
            break

        print(f"Uus bingopall: {pall}")

        for mängija in mängijad:
            for kaart in mängija['kaardid']:
                for i in range(5):
                    for j in range(5):
                        if kaart[i][j] == pall:
                            kaart[i][j] = "X"
                if bingo_kaart(kaart):
                    print(f"{mängija['nimi']} võitis!")
                    print("Võidukaart:")
                    print_kaart(kaart)
                    return
                
        input('Vajuta "Enter", et järgmine pall panna loosi')

if __name__ == "__main__":
    mängi_bingot