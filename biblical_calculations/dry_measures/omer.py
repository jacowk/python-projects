"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import dry_measures.dry_measures as dm
import utils as u

class Omer:

    def convertToLiters(self, value):
        return u.Utils.convertTo(value, dm.DryMeasures.OMER_LITERS.value)

    def convertFromLiters(self, value):
        return u.Utils.convertFrom(value, dm.DryMeasures.OMER_LITERS.value)
