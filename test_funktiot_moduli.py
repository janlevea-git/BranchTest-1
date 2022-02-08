# Yksikkö testit modulille funktiot_moduli.py

import funktiot_moduli

def test_suorakulma():
   assert funktiot_moduli.suorakulma(3, 4 ,5) == 0.0
   assert round(funktiot_moduli.suorakulma(10, 12, 14), 4) == -1.6205