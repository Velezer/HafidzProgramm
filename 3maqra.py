import random

quran = {
    1: {
        'surah_name': "Al-Fatihah",
        'maqra_list': ["1-7"]
    },
    2: {
        'surah_name': "Al-Baqarah",
        'maqra_list': ["1-7", "8-20", "21-29", '30-39', '40-46', '47-59', '60-61', '62-71', '72-82', '83-86', '87-96',
                  '97-103', '104-112', '113-121', '122-129', '130-141', '142-147', '148-152', '153-163', '164-167',
                  '168-176', '177-182', '183-188', '189-196', '197-210', '211-221', '222-228', '229-231', '232-235',
                  '236-242', '243-248', '249-253', '254-257', '258-260', '261-266', '267-273', '274-281', '282-283',
                  '284-286']
    },
    3: {
        'surah_name': "Ali Imran",
        'maqra_list': ['1-9', '10-20', '21-30', '31-41', '42-54', '55-63', '64-71', '72-80', '81-91', '92-101', '102-109',
                  '110-120', '121-129', '130-143', '144-148', '149-155', '156-171', '172-180', '181-189', '190-200']
    },
    4: {
        'surah_name': "An-Nisa",
        'maqra_list': ['1-10', '11-14', '15-22', '23-25', '26-33', '34-42', '43-50', '51-59', '60-70', '71-76', '77-87',
                  '88-91', '92-96', '97-100', '101-104', '105-112', '113-115', '116-126', '127-134', '135-141',
                  '142-152', '153-162', '163-171', '172-176']
    },
    5: {
        'surah_name': "Al-Maaidah",
        'maqra_list': ['1-5', '6-11', '12-19', '20-26', '27-34', '35-43', '44-50', '51-56', '57-66', '67-77', '78-86',
                  '87-93', '94-100', '101-108', '109-115', '116-120']
    },
    6: {
        'surah_name': "Al-An'am",
        'maqra_list': ['1-10', '11-20', '21-30', '31-41', '42-50', '51-55', '56-60', '61-70', '71-82', '83-90', '91-94',
                  '95-100', '101-110', '111-121', '122-129', '130-140', '141-144', '145-150', '151-154', '155-165']
    },
    7: {
        'surah_name': "Al-A'raf",
        'maqra_list': ['1-10', '11-25', '26-31']
    },
}
def choose_from(stuff):
    return random.choice(tuple(stuff))


def print_one_maqra(i, j):
    print(f"Q.S. {quran[i]['surah_name']} : {maqra_list[j]}")


choosed_surah = choose_from(quran)
i = choosed_surah

maqra_list = quran[i]['maqra_list']

print(maqra.index)

choosed_maqra = choose_from(range(len(maqra_list)))
j = choosed_maqra

def print_three_maqra(i, j):
    try:
        print_one_maqra(i-1,j-1) if j==0 else print_one_maqra(i, j-1)
    except: pass

    print_one_maqra(i, j)
    
    try :
        print_one_maqra(i+1, 0) if j==len(maqra_list)-1 else print_one_maqra(i, j+1)
    except Exception as e: print(e)


print_three_maqra(i,j)




