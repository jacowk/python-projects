"""
@author Jaco Koekemoer
@date 2020-08-17
https://biblehub.com/weights-and-measures/
"""
import calc_oo.lengths.lengths as l

class Span:

    def convertToCentimeters(self, span):
        return span * l.Lengths.SPAN_CENTIMETERS.value

    def convertFromCentimeters(self, centimeters):
        return centimeters / l.Lengths.SPAN_CENTIMETERS.value

    def convertToInches(self, span):
        return span * l.Lengths.SPAN_INCHES.value

    def convertFromInches(self, inches):
        return inches / l.Lengths.SPAN_INCHES.value

