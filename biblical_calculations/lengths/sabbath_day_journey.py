"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import lengths.lengths as l
import utils as u

class SabbathDayJourney:

    def convertToMeters(self, value):
        return u.Utils.convertTo(value, l.Lengths.SABBATH_DAY_JOURNEY_METERS.value)

    def convertFromMeters(self, value):
        return u.Utils.convertFrom(value, l.Lengths.SABBATH_DAY_JOURNEY_METERS.value)

    def convertToCubit(self, value):
        return u.Utils.convertTo(value, l.Lengths.SABBATH_DAY_JOURNEY_CUBIT.value)

    def convertFromCubit(self, value):
        return u.Utils.convertFrom(value, l.Lengths.SABBATH_DAY_JOURNEY_CUBIT.value)
