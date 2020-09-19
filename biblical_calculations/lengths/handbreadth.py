"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class Handbreadth:

    def convertToCentimeters(self, value):
        return u.Utils.convertTo(value, l.Lengths.HANDBREADTH_CENTIMETERS.value)

    def convertFromCentimeters(self, value):
        return u.Utils.convertFrom(value, l.Lengths.HANDBREADTH_CENTIMETERS.value)

    def convertToFingers(self, value):
        return u.Utils.convertTo(value, l.Lengths.HANDBREADTH_FINGERS.value)

    def convertFromFingers(self, value):
        return u.Utils.convertFrom(value, l.Lengths.HANDBREADTH_FINGERS.value)