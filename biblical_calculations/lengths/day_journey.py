"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class DayJourney:

    def convertToKilometers(self, value):
        return u.Utils.convertTo(value, l.Lengths.DAY_JOURNEY_KILOMETERS.value)

    def convertFromKilometers(self, value):
        return u.Utils.convertFrom(value, l.Lengths.DAY_JOURNEY_KILOMETERS.value)
