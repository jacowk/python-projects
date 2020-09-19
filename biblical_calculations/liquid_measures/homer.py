"""
@author Jaco Koekemoer
@date 2020-08-18
https://biblehub.com/weights-and-measures/
"""
import liquid_measures.liquid_measures as lm
import utils as u

class Homer:

    def convertToLiters(self, value):
        return u.Utils.convertTo(value, lm.LiquidMeasures.HOMER_LITRES.value)

    def convertFromLiters(self, value):
        return u.Utils.convertFrom(value, lm.LiquidMeasures.HOMER_LITRES.value)
