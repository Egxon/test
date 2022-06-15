# return string without spaces
def ef_64(cc):
    """
    Removes only single spaces from given string.
    :param text : string to edit
    :return : edited string
    """
    cal=0
    listwords = list(cc)
    for i, char in enumerate(listwords):
        wordslength = len(listwords)
        if (char == " " and wordslength == 1) or (char == " "
          and listwords[max(i-1, int(wordslength > 1))] != " "
          and listwords[min(i+1, wordslength-int(wordslength > 1)*2)] != " "):
            del listwords[i]


    return "".join(char for char in listwords)

def ef_4(cc):
    res = ""
    i = 0
    cal=0
    while i < len(cc):
        if cc[i] == " ":
            j = 1

            while i+j < len(cc) and cc[i+j] == " ":
                j += 1

            if j > 1:
                res += " "*(j)
                i += j-1

        else:
            res += cc[i]

        i += 1


    return res

def ef_38(cc):
    newStr=""
    lengthStr = len(cc)

    for i in range(0,lengthStr):
        char = cc[i]
        if ord(char) != 32:
            newStr+=char

        else:
            if ((i+1<lengthStr) & (i-1>=0)):
                if (ord(cc[i+1]) == 32) | (ord(cc[i-1]) == 32):
                    newStr+=char


  
    return newStr


import time
def test_ef_64(NbTest):
    with open('texteSAE.txt') as file :
        content = " ".join([c for c in file])

    Temps = 0

    for i in range(0, NbTest) :
        start_time = time.time()
        ef_64(content)
        Temps = Temps + ((time.time() - start_time))

    TmpExe = Temps / NbTest
    return (TmpExe)

def test_ef_4(NbTest):
    with open('texteSAE.txt') as file :
        content = " ".join([c for c in file])


    Temps= 0

    for i in range(0, NbTest) :
        start_time = time.time()
        ef_4(content)
        Temps = Temps + ((time.time() - start_time))


    TmpExe = Temps/NbTest
    return (TmpExe)

def test_ef_38(NbTest):
    with open('texteSAE.txt') as file :
        content = " ".join([c for c in file])

    Temps = 0

    for i in range(0, NbTest) :
        start_time = time.time()
        ef_38(content)
        Temps = Temps + ((time.time() - start_time))

    TmpExe = Temps / NbTest
    print (TmpExe)
    return (TmpExe)

import codewars_test as test


@test.describe('Sample tests')
def sample_tests() :
    @test.it("erase: ''")
    def test1() :
        test.assert_equals(ef_4(''), '')
        test.assert_equals(ef_64(''), '')
        test.assert_equals(ef_38(''), '')

    @test.it("erase: '06   07 65 19 70 '")
    def test2() :
        test.assert_equals(ef_64('06   07 65 19 70 '), '06   07651970')
        test.assert_equals(ef_38('06   07 65 19 70 '), '06   07651970')
        test.assert_equals(ef_4('06   07 65 19 70 '), '06   07651970')


    @test.it("erase: '666, the number of the beast'")
    def test3() :
        test.assert_equals(ef_38('666, the number of the beast'), '666,thenumberofthebeast')
        test.assert_equals(ef_4('666, the number of the beast'), '666,thenumberofthebeast')
        test.assert_equals(ef_64('666, the number of the beast'), '666,thenumberofthebeast')

    @test.it("erase: 'Cou cou  J M  B'")
    def test4() :
        test.assert_equals(ef_4('Cou cou  J M  B'), 'Coucou  JM  B')
        test.assert_equals(ef_64('Cou cou  J M  B'), 'Coucou  JM  B')
        test.assert_equals(ef_38('Cou cou  J M  B'), 'Coucou  JM  B')


ListeTemps= []


ListeTemps.append(float("{:.5f}".format(test_ef_4(1))))
ListeTemps.append(float("{:.5f}".format(test_ef_38(1))))
ListeTemps.append(float("{:.5f}".format(test_ef_64(1))))

import matplotlib.pyplot as plt
import numpy as np

height = ListeTemps
bars = ('test_ef_4', 'test_ef_38', 'test_ef_64')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()