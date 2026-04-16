import unittest
from bioguard.inventory import VaccineManager
from bioguard.validator import check_temp

class TestBioGuard(unittest.TestCase):
    def setUp(self):
        self.vm = VaccineManager()

    def test_stock_incremental(self):
        self.vm.add_doses("Moderna", 100)
        self.vm.add_doses("Moderna", 50)
        self.assertEqual(self.vm.stock["Moderna"], 150)

    def test_exception_negative_qty(self):
        with self.assertRaises(ValueError):
            self.vm.add_doses("Error_Vial", -1)

    def test_range_temperature(self):
        # Nuevos límites térmicos: 2 a 8
        self.assertTrue(check_temp(4))   # 4 está dentro, debe ser True
        self.assertFalse(check_temp(0))  # 0 está fuera (es menor que 2), debe ser False
        self.assertFalse(check_temp(10)) # 10 está fuera, debe ser False