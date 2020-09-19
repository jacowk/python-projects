"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class Rod:

    def convertToMeters(self, value):
        return u.Utils.convertTo(value, l.Lengths.ROD_METERS.value)

    def convertFromMeters(self, value):
        return u.Utils.convertFrom(value, l.Lengths.ROD_METERS.value)

    def convertToLongCubit(self, value):
        return u.Utils.convertTo(value, l.Lengths.ROD_LONG_CUBIT.value)

    def convertFromLongCubit(self, value):
        return u.Utils.convertFrom(value, l.Lengths.ROD_LONG_CUBIT.value)
