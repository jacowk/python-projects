"""
Date: 2020-02-17
Author: Jaco Koekemoer
A program that receives hebrew letters as input. As output, display pictographs, numbers, and sum the numbers.
Also find divisibles for the total by 3, 4, 5, 6, 7, 8, 10 and 12.

Pseudocode
Read all JSON files
Receive hebrew letters in english form
Find the pictographs and display
Find the numbers and display
Calculate the total
Find divisibles and display

Try other things: 
    Multiple all numbers, 
    the numbers of the word as is, 
    primenumbers
    fibonacci numbers

https://www.apocalypse2008-2015.com/Hebrew-Alphabet-Number-System-Table.html

The number of YHWH is 10565. The number 105653 is a prime number.
So YHWH is 3 in one, the trinity.
10078th prime number is 105653. Does 10078 mean anything?
"""
import json

def print_all_letters():
    hebrew_unicode = json.loads(open('hebrew-unicode.json', 'r').read())
    for x in hebrew_unicode.keys():
        print("{} - {}".format(hebrew_unicode[x], x))

def run():
    #input_letters = ['yo', 'he', 'va', 'he'] #YHWH
    #input_letters = ['yo', 'si', 'va', 'ay'] #Yeshua
    #input_letters = ['si', 'va', 'pe', 're'] #Shofar
    #input_letters = ['si', 'te', 'nu'] #satan
    #input_letters = ['re', 'va', 'het'] #Ruach
    #input_letters = ['re', 'va', 'het', 'hay','ko','va','da','si'] #Ruach ha-Kodesh
    #input_letters = ['pe', 'sa', 'het'] #Passover
    #input_letters = ['me', 'si', 'yo', 'het'] #Mashiach (Anointed One)
    #input_letters = ['me', 'tz', 're', 'ay'] #Infected one (Leprosy)
    #input_letters = ['hay', 'si', 'me'] #Hashem (The Name)
    #input_letters = ['al', 'la', 'va', 'hay', 'yo', 'me'] #Elohim
    input_letters = ['re', 'sa', 'het'] #mercy

    hebrew_numbers = json.loads(open('hebrew-numbers.json', 'r').read())
    hebrew_pict = json.loads(open('hebrew-pictographs.json', 'r').read())
    hebrew_unicode = json.loads(open('hebrew-unicode.json', 'r').read())
    hebrew_acc = json.loads(open('hebrew-accepted-input.json', 'r').read())
    number_meanings = json.loads(open('number-meanings.json', 'r').read())
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
    #divisibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 50]
    divisibles = range(2, 20)

    output_hebrew_letters(input_letters, hebrew_unicode, hebrew_acc)
    process_pictographs(input_letters, hebrew_pict, hebrew_acc)
    process_numbers(input_letters, hebrew_numbers, hebrew_acc, number_meanings)
    total = process_number_totals(input_letters, hebrew_numbers, hebrew_acc, number_meanings)
    process_divisibles(total, divisibles, number_meanings)

def output_hebrew_letters(input_letters, hebrew_unicode, hebrew_acc):
    print("\nHebrew Letters:")
    output = u""
    for letter in input_letters:
        correct_letter = hebrew_acc[letter]
        print(u"{} ({})".format(hebrew_unicode[correct_letter], correct_letter))
        output += u"{}".format(hebrew_unicode[correct_letter])
    print("Complete word: {}".format(output))

def process_pictographs(input_letters, hebrew_pict, hebrew_acc):
    print("\nHebrew Pictographs:")
    for letter in input_letters:
        correct_letter = hebrew_acc[letter]
        print(correct_letter + " - " + hebrew_pict[correct_letter])

#TODO Create a JSON file file number meanings aswell
def process_numbers(input_letters, hebrew_numbers, hebrew_acc, number_meanings):
    print("\nHebrew Numbers")
    for letter in input_letters:
        correct_letter = hebrew_acc[letter]
        print("{} - {} ({})".format(correct_letter, \
              hebrew_numbers[correct_letter], \
              get_number_meaning(hebrew_numbers[correct_letter], number_meanings)))

def process_number_totals(input_letters, hebrew_numbers, hebrew_acc, number_meanings):
    print("\nHebrew Number Totals")
    total = 0
    for letter in input_letters:
        correct_letter = hebrew_acc[letter]
        number = int(hebrew_numbers[correct_letter])
        total += number
    
    print("Total: {} ({})".format(str(total), get_number_meaning(total, number_meanings)))
    return total

# Add divisibles to a JSON file
def process_divisibles(total, divisibles, number_meanings):
    print("\nProcessing Divisibles")
    for divisible in divisibles:
        remainder = total % divisible
        result = int(total / divisible)
        if remainder == 0:
            print ("\nDivisible by {}: {} * {} = {}".format(str(divisible), \
                   str(divisible), round(result), str(total)))
            print("{} ({})".format(divisible, get_number_meaning(str(divisible), number_meanings)))
            print("{} ({})".format(result, get_number_meaning(str(result), number_meanings)))

def get_number_meaning(number, number_meanings):
    try:
        return number_meanings[number]
    except:
        return "No meaning available"

def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    return data

run()
#print_all_letters()
"""
U+05D0	א	Hebrew Letter Alef
U+05D1	ב	Hebrew Letter Bet
U+05D2	ג	Hebrew Letter Gimel
U+05D3	ד	Hebrew Letter Dalet
U+05D4	ה	Hebrew Letter He
U+05D5	ו	Hebrew Letter Vav
U+05D6	ז	Hebrew Letter Zayin
U+05D7	ח	Hebrew Letter Het
U+05D8	ט	Hebrew Letter Tet
U+05D9	י	Hebrew Letter Yod
U+05DA	ך	Hebrew Letter Final Kaf
U+05DB	כ	Hebrew Letter Kaf
U+05DC	ל	Hebrew Letter Lamed
U+05DD	ם	Hebrew Letter Final Mem
U+05DE	מ	Hebrew Letter Mem
U+05DF	ן	Hebrew Letter Final Nun
U+05E0	נ	Hebrew Letter Nun
U+05E1	ס	Hebrew Letter Samekh
U+05E2	ע	Hebrew Letter Ayin
U+05E3	ף	Hebrew Letter Final Pe
U+05E4	פ	Hebrew Letter Pe
U+05E5	ץ	Hebrew Letter Final Tsadi
U+05E6	צ	Hebrew Letter Tsadi
U+05E7	ק	Hebrew Letter Qof
U+05E8	ר	Hebrew Letter Resh
U+05E9	ש	Hebrew Letter Shin
U+05EA	ת	Hebrew Letter Tav
"""

