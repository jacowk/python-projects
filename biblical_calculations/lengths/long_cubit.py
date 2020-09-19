"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class LongCubit:

    def convertToCentimeters(self, value):
        return u.Utils.convertTo(value, l.Lengths.LONG_CUBIT_CENTIMETERS.value)

    def convertFromCentimeters(self, value):
        return u.Utils.convertFrom(value, l.Lengths.LONG_CUBIT_CENTIMETERS.value)
