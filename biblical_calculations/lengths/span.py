"""
@author Jaco Koekemoer
@date 2020-08-17
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class Span:

    def convertToCentimeters(self, value):
        return u.Utils.convertTo(value, l.Lengths.SPAN_CENTIMETERS.value)

    def convertFromCentimeters(self, value):
        return u.Utils.convertFrom(value, l.Lengths.SPAN_CENTIMETERS.value)
