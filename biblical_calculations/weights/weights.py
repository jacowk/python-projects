"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import enum

class Weights(enum.Enum):
    GERAH_SHEKEL = 1/20
    GERAH_OUNCES = 0.0201
    GERAH_GRAMS = 0.57
    BEKA_SHEKEL= 1/2
    BEKA_OUNCES = 0.201
    BEKA_GRAMS = 5.7
    PIM_SHEKEL = 2/3
    PIM_OUNCES = 0.268
    PIM_GRAMS = 7.6
    SHEKEL_GERAHS = 20
    SHEKEL_OUNCES = 0.402
    SHEKEL_GRAMS = 11.4
    MINA_SHEKELS = 50
    MINA_POUNDS = 1.256
    MINA_KILOGRAMS = 0.57
    TALENT_MINAS = 60
    TALENT_POUNDS = 75.4
    TALENT_KILOGRAMS = 34.2
    LITRA_ROMAN_POUND = 1
    LITRA_OUNCES = 12
    LITRA_GRAMS = 340