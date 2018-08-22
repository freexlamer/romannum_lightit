class RumanArabicConverter:
    def __init__(self):
        self.main_nums={
            1000:'M',
            500:'D',
            100:'C',
            50:'L',
            10:'X',
            5:'V',
            1:'I'
        }
        self.sub_nums={
            900:'CM',
            400:'CD',
            90:'XC',
            40:'XL',
            9:'IX',
            4:'IV',
        }

    def arabic2roman(self,num):
        ''' Convert the arabic number to roman.

        :param num: An integer from 1 to 3999.
        :type num: int

        '''

        if type(num) != int:
            raise TypeError('Expected `int` type, got `%s`.' % type(num))
        if not 0 < num < 4000:
            raise ValueError('Argument must be in [1, 3999].')

        converter = {}
        converter.update(self.main_nums)
        converter.update(self.sub_nums)
        result = ''

        '''
        Собираем все варианты римских чисел.
        Перебирая от максимального до минимального, делим арабское и вычитаем.
        Формируем римское.
        '''
        for i in sorted(converter,reverse=True):          
            count = int(num / i)
            result += converter[i] * count
            num -= i * count

        return result

    def roman2arabic(self,num):
        ''' Convert the roman number to arabic.
        
        :param num: An roman number.
        :type num: str

        '''

        if type(num) != str:
            raise TypeError('Expected `str` type, got `%s`.' % type(num))

        result = 0
        tmp = ''

        '''
        Convert all to uppercase. 
        Check whether all the characters in the line are valid.
        '''
        tmp = num.upper()
        for i in tmp:
            if not i in self.main_nums.values():
                raise ValueError('Num is not a valid roman numeral: `%s`.' % num)

        # At first, select "exceptions" and convert them into the result.
        for i in sorted(self.sub_nums,reverse=True):
            if self.sub_nums[i] in tmp:
                result += i
                tmp = tmp.replace(self.sub_nums[i],'')

        # The rest simply translated into the result.
        for i in self.main_nums:
            if tmp.count(self.main_nums[i]) < 4:
                result += i * tmp.count(self.main_nums[i])
            else:
                raise ValueError('Num is not a valid roman numeral.'
                                 ' Too much `%s` exists.' % self.main_nums[i])

        '''
        Check for an incorrect order of digits in the roman number.
        '''
        if self.arabic2roman(result) == num.upper():
            return result
        else:
            raise ValueError('Num is not a valid roman numeral: `%s`.' % num)
        

    def _test_arabic(self,s):
        '''
        Check the s contains an arabic integer number.
        '''
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def autoconv(self,data):
        '''
        If data is an arabic number, then it converts to roman. And vice versa.
        '''
        if self._test_arabic(data):
            return self.arabic2roman(int(data))
        else:
            return self.roman2arabic(data)

    def convert_multi(self,data):
        ''' Convert many numbers.

        :param num: String, that contains arabic and roman numbers.
        :type num: str
        '''
        result = []
        tmp = []

        for i in str(data).splitlines():
            i = i.replace(',', ' ').replace('.', ' ').replace(';', ' ')
            tmp.extend(i.split())

        for i in tmp:
            try:
                result.append(str(self.autoconv(i)))

            except ValueError as e:
                result.append('ValueError in `%s`. Error message is: %s'%(str(i),str(e)))

            except TypeError:
                result.append('TypeError in `%s`.'%str(i))

        return '\n'.join(result)
