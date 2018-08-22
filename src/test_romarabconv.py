from romarabconv import RumanArabicConverter
import pytest

class TestRumanArabicConverter:
    def setup(self):
        self.conv = RumanArabicConverter()

    def test_arabic_to_roman_exceptions(self):
        with pytest.raises(TypeError):
            self.conv.arabic2roman('1')

        with pytest.raises(ValueError):
            self.conv.arabic2roman(0)

        with pytest.raises(ValueError):
            self.conv.arabic2roman(4000)

    def test_arabic_to_roman_simple(self):
        assert(self.conv.arabic2roman(1)=='I')
        assert(self.conv.arabic2roman(5)=='V')
        assert(self.conv.arabic2roman(10)=='X')
        assert(self.conv.arabic2roman(50)=='L')
        assert(self.conv.arabic2roman(100)=='C')
        assert(self.conv.arabic2roman(500)=='D')
        assert(self.conv.arabic2roman(1000)=='M')

        assert(self.conv.arabic2roman(4)=='IV')
        assert(self.conv.arabic2roman(9)=='IX')
        assert(self.conv.arabic2roman(40)=='XL')
        assert(self.conv.arabic2roman(90)=='XC')
        assert(self.conv.arabic2roman(400)=='CD')
        assert(self.conv.arabic2roman(900)=='CM')

    def test_arabic_to_roman(self):
        assert(self.conv.arabic2roman(3999)=='MMMCMXCIX')
        assert(self.conv.arabic2roman(14)=='XIV')
        assert(self.conv.arabic2roman(59)=='LIX')
        

    def test_roman_to_arabic_exceptions(self):
        with pytest.raises(TypeError):
            self.conv.roman2arabic(1)

        with pytest.raises(ValueError):
            self.conv.roman2arabic('OxFF')

        with pytest.raises(ValueError):
            self.conv.roman2arabic('IIIIVVVV')

        with pytest.raises(ValueError):
            self.conv.roman2arabic('XXD')

    def test_roman_to_arabic_simple(self):
        assert(self.conv.roman2arabic('I')==1)
        assert(self.conv.roman2arabic('V')==5)
        assert(self.conv.roman2arabic('X')==10)
        assert(self.conv.roman2arabic('L')==50)
        assert(self.conv.roman2arabic('C')==100)
        assert(self.conv.roman2arabic('D')==500)
        assert(self.conv.roman2arabic('M')==1000)

        assert(self.conv.roman2arabic('IV')==4)
        assert(self.conv.roman2arabic('IX')==9)
        assert(self.conv.roman2arabic('XL')==40)
        assert(self.conv.roman2arabic('XC')==90)
        assert(self.conv.roman2arabic('CD')==400)
        assert(self.conv.roman2arabic('CM')==900)

    def test_roman_to_arabic_simple_lower_case(self):
        assert(self.conv.roman2arabic('i')==1)
        assert(self.conv.roman2arabic('v')==5)
        assert(self.conv.roman2arabic('x')==10)
        assert(self.conv.roman2arabic('l')==50)
        assert(self.conv.roman2arabic('c')==100)
        assert(self.conv.roman2arabic('d')==500)
        assert(self.conv.roman2arabic('m')==1000)

        assert(self.conv.roman2arabic('iv')==4)
        assert(self.conv.roman2arabic('ix')==9)
        assert(self.conv.roman2arabic('xl')==40)
        assert(self.conv.roman2arabic('xc')==90)
        assert(self.conv.roman2arabic('cd')==400)
        assert(self.conv.roman2arabic('cm')==900)

    def test_roman_to_arabic(self):
        assert(self.conv.roman2arabic('MMMCMXCIX')==3999)
        assert(self.conv.roman2arabic('mmmcmxcix')==3999)
        assert(self.conv.roman2arabic('XIV')==14)
        assert(self.conv.roman2arabic('LIX')==59)

    def test_all_range(self):
        for i in range(1,3999):
            assert(self.conv.roman2arabic(self.conv.arabic2roman(i)) == i)

    def test__test_arabic(self):
        assert(self.conv._test_arabic(1)==True)
        assert(self.conv._test_arabic('1')==True)
        assert(self.conv._test_arabic('I')==False)

    def test_autoconv(self):
        assert(self.conv.autoconv(1)=='I')
        assert(self.conv.autoconv('1')=='I')
        assert(self.conv.autoconv('I')==1)
        
    def test_convert_multi(self):
        assert(self.conv.convert_multi(1)=='I')
        assert(self.conv.convert_multi('1')=='I')
        assert(self.conv.convert_multi('I')=='1')

        assert(self.conv.convert_multi('I;II')=='1\n2')
        assert(self.conv.convert_multi('I;II III')=='1\n2\n3')
        assert(self.conv.convert_multi('I;II III\n 4')=='1\n2\n3\nIV')
        assert(self.conv.convert_multi('I;II III\n 4;X')=='1\n2\n3\nIV\n10')

    def test_convert_multi_errors(self):
        assert('ValueError' in self.conv.convert_multi('IIII'))
        assert('ValueError' in self.conv.convert_multi('IIV'))
        assert('ValueError' in self.conv.convert_multi('0x13'))
        
