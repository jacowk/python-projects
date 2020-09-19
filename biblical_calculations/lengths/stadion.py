"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class Stadion:

    def convertToMeters(self, value):
        return u.Utils.convertTo(value, l.Lengths.STADION_METERS.value)

    def convertFromMeters(self, value):
        return u.Utils.convertFrom(value, l.Lengths.STADION_METERS.value)
