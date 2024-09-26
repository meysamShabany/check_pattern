import re
class CheckPattern:
    def __init__(self , value:str) -> None:
        if value:
            self.value = value
        else:
            raise ValueError('insert correct value')

    def get_number_with_size(self , size:int)->int:
        number = ''
        count = 0
        for num in self.value:
            try:
                num = int(num)
                count += 1
            except:
                if count == size:
                    break
                else:
                    count = 0
                    number = ''
            else:
                number += str(num)
        try:
            return int(number)
        except:
            return 'not found pattern with this size'
    def check_is_number(self):
        for num in self.value.strip():
            try:
                number = int(num)
            except:
                return False
        else:
            return True
    def check_english_lang(self):
        if re.fullmatch(r'^[A-Za-z0-9\s.,!?\'"()]*$' , self.value.strip()):
            return True
        else:
            return False
        
    def check_iranian_phone(self):
        #r'^09(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9])-?[0-9]{3}-?[0-9]{4}$'
        #r"^(?:+98|0)9d{9}$"
        if re.match(r'^09(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9])-?[0-9]{3}-?[0-9]{4}$' , self.value):
            return True
        else:
            return False
    def check_email_pattern(self):
        pass
    def check_password_upper_lower_number_specific(self):
        pass
    def check_password_letter_number(self):
        pass
    def check_password_upper_lower_number(self):
        pass
