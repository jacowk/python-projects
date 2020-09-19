"""
@author Jaco Koekemoer
@date 2020-08-19
https://biblehub.com/weights-and-measures/
"""
import weights.weights as w
import utils as u

class Shekel:

    def convertToGrams(self, value):
        return u.Utils.convertTo(value, w.Weights.SHEKEL_GRAMS.value)

    def convertFromGrams(self, value):
        return u.Utils.convertFrom(value, w.Weights.SHEKEL_GRAMS.value)
