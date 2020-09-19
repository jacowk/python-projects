"""
@author Jaco Koekemoer
@date 2020-08-19
https://biblehub.com/weights-and-measures/
"""
import weights.weights as w
import utils as u

class Talent:

    def convertToKilograms(self, value):
        return u.Utils.convertTo(value, w.Weights.TALENT_KILOGRAMS.value)

    def convertFromKilograms(self, value):
        return u.Utils.convertFrom(value, w.Weights.TALENT_KILOGRAMS.value)
