
import random


def hafalkan(surah, surah_name, ayat):
    random_maqra = []
    for i in ayat:
        random_maqra.insert(random.randint(-len(ayat), len(ayat) - 1), i)
    rentang_ayat = random_maqra[random.randint(-len(ayat), len(ayat) - 1)]
    print(surah_name, '/', surah, ':', rentang_ayat)

    awal, akhir = rentang_ayat.split('-')
    awal, akhir = int(awal), int(akhir)

    jumlah_hafal = random.randint(0, akhir - awal + 1)
    print(f"Hafalkan {jumlah_hafal} ayat di bawah ini")
    for i in range(jumlah_hafal):
        nomer_ayat = random.randint(awal, akhir)
        print(surah_name, '/', surah, ':', nomer_ayat)
    print('\n')
    if not is_stop:
        showPrintAyat()


def showPrintAyat():
    global is_stop
    surah = []
    surah2 = []
    for i in range(115):
        surah.insert(random.randint(0-i, 0+i), i)
    for i in range(115):
        surah2.insert(random.randint(0 - i, 0 + i), surah[random.randint(-len(surah), len(surah) - 1)])

    #surah = surah[random.randint(-len(surah), len(surah) - 1)]
    surah = surah2[random.randint(-len(surah2), len(surah2) - 1)]

    if surah == 0:
        is_stop = True
        print("BREAK!!")
        return is_stop

    elif surah == 1:
        surah_name = "Al-Fatihah"
        ayat = ["1-7"]
        hafalkan(surah, surah_name, ayat)
    elif surah == 2:
        surah_name = "Al-Baqarah"
        ayat = ["1-7", "8-20", "21-29", '30-39', '40-46', '47-59', '60-61', '62-71', '72-82', '83-86', '87-96',
                '97-103', '104-112', '113-121', '122-129', '130-141', '142-147', '148-152', '153-163', '164-167',
                '168-176', '177-182', '183-188', '189-196', '197-210', '211-221', '222-228', '229-231', '232-235',
                '236-242', '243-248', '249-253', '254-257', '258-260', '261-266', '267-273', '274-281', '282-283', '284-286'
                ]
        hafalkan(surah, surah_name, ayat)

    elif surah == 3:
        surah_name = "Ali Imran"
        ayat = ['1-9', '10-20', '21-30', '31-41', '42-54', '55-63', '64-71', '72-80', '81-91', '92-101', '102-109',
                '110-120', '121-129', '130-143', '144-148', '149-155', '156-171', '172-180', '181-189', '190-200']
        hafalkan(surah, surah_name, ayat)

    elif surah == 4:
        surah_name = "An-Nisa"
        ayat = ['1-10', '11-14', '15-22', '23-25', '26-33', '34-42', '43-50', '51-59', '60-70', '71-76', '77-87',
                '88-91', '92-96', '97-100', '101-104', '105-112', '113-115', '116-126', '127-134', '135-141', '142-152',
                '153-162', '163-171', '172-176']
        hafalkan(surah, surah_name, ayat)

    elif surah == 5:
        surah_name = "Al-Maaidah"
        ayat = ['1-5', '6-11', '12-19', '20-26', '27-34', '35-43', '44-50', '51-56', '57-66', '67-77', '78-86', '87-93',
                '94-100', '101-108', '109-115', '116-120']
        hafalkan(surah, surah_name, ayat)

    elif surah == 6:
        surah_name = "Al-An'am"
        ayat = ['1-10', '11-20', '21-30', '31-41', '42-50', '51-55', '56-60', '61-70', '71-82', '83-90', '91-94',
                '95-100', '101-110', '111-121', '122-129', '130-140', '141-144', '145-150', '151-154', '155-165']
        hafalkan(surah, surah_name, ayat)

    elif surah == 7:
        surah_name = "Al-A'raf"
        ayat = ['1-10']
        hafalkan(surah, surah_name, ayat)

    else:
        pass


is_stop = False
juz = random.randint(0, 8)
repeater = juz
for repeating in range(repeater):
    if showPrintAyat():
        break
