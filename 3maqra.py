import random

quran = {
    0: {
        'surat': "",
        'maqra': [""]
    },
    1: {
        'surat': "Al-Fatihah",
        'maqra': ["1-7"]
    },
    2: {
        'surat': "Al-Baqarah",
        'maqra': ["1-7", "8-20", "21-29", '30-39', '40-46', '47-59', '60-61', '62-71', '72-82', '83-86', '87-96',
                  '97-103', '104-112', '113-121', '122-129', '130-141', '142-147', '148-152', '153-163', '164-167',
                  '168-176', '177-182', '183-188', '189-196', '197-210', '211-221', '222-228', '229-231', '232-235',
                  '236-242', '243-248', '249-253', '254-257', '258-260', '261-266', '267-273', '274-281', '282-283',
                  '284-286']
    },
    3: {
        'surat': "Ali Imran",
        'maqra': ['1-9', '10-20', '21-30', '31-41', '42-54', '55-63', '64-71', '72-80', '81-91', '92-101', '102-109',
                  '110-120', '121-129', '130-143', '144-148', '149-155', '156-171', '172-180', '181-189', '190-200']
    },
    4: {
        'surat': "An-Nisa",
        'maqra': ['1-10', '11-14', '15-22', '23-25', '26-33', '34-42', '43-50', '51-59', '60-70', '71-76', '77-87',
                  '88-91', '92-96', '97-100', '101-104', '105-112', '113-115', '116-126', '127-134', '135-141',
                  '142-152', '153-162', '163-171', '172-176']
    },
    5: {
        'surat': "Al-Maaidah",
        'maqra': ['1-5', '6-11', '12-19', '20-26', '27-34', '35-43', '44-50', '51-56', '57-66', '67-77', '78-86',
                  '87-93', '94-100', '101-108', '109-115', '116-120']
    },
    6: {
        'surat': "Al-An'am",
        'maqra': ['1-10', '11-20', '21-30', '31-41', '42-50', '51-55', '56-60', '61-70', '71-82', '83-90', '91-94',
                  '95-100', '101-110', '111-121', '122-129', '130-140', '141-144', '145-150', '151-154', '155-165']
    },
    7: {
        'surat': "Al-A'raf",
        'maqra': ['1-10']
    },
    8: {
        'surat': "",
        'maqra': ['']
    },
}


def tampilSatuMaqra(surat, maqra_ke):
    print(f"Q.S. {quran[surat]['surat']} : {quran[surat]['maqra'][maqra_ke]}")


def tampil3Maqra(surat, maqra_ke):
    global maqra
    last_maqra = maqra

    tampilSatuMaqra(surat - 1, - 1) if maqra_ke == 0 else tampilSatuMaqra(surat, maqra_ke - 1)
    tampilSatuMaqra(surat, maqra_ke)
    tampilSatuMaqra(surat + 1, 0) if maqra_ke == last_maqra else tampilSatuMaqra(surat, maqra_ke+1)


def lastMaqra(surat):
    try:
        return len(quran[surat]['maqra']) - 1  # last index of maqra
    except KeyError:
        return 'not found'


rand_surat = random.randint(1, 114)
maqra = lastMaqra(rand_surat)
rand_maqra = random.randint(0, maqra)

try:
    tampil3Maqra(rand_surat, rand_maqra)
except KeyError:
    pass

if maqra == 'not found':
    rand_surat = random.randint(1, 114)
    maqra = lastMaqra(rand_surat)
    rand_maqra = random.randint(0, maqra)
    exit() if not maqra == 'not found' else tampilSatuMaqra(rand_surat, rand_maqra)

