import re
import math


class ViesValidator:
    def __init__(self):
        super().__init__()
        self.country_functions = {
            "AT": self._at_vies_check,
            "BE": self._be_vies_check,
            "BG": self._bg_vies_check,
            "CHE": self._ch_vies_check,
            "CY": self._cy_vies_check,
            "CZ": self._cz_vies_check,
            "DE": self._de_vies_check,
            "DK": self._dk_vies_check,
            "EE": self._ee_vies_check,
            "EL": self._el_vies_check,
            "ES": self._es_vies_check,
            "EU": self._eu_vies_check,
            "FI": self._fi_vies_check,
            "FR": self._fr_vies_check,
            "GB": self._gb_vies_check,
            "HR": self._hr_vies_check,
            "HU": self._hu_vies_check,
            "IE": self._ie_vies_check,
            "IT": self._it_vies_check,
            "LV": self._lv_vies_check,
            "LT": self._lt_vies_check,
            "LU": self._lu_vies_check,
            "MT": self._mt_vies_check,
            "NL": self._nl_vies_check,
            "NO": self._no_vies_check,
            "PL": self._pl_vies_check,
            "PT": self._pt_vies_check,
            "RO": self._ro_vies_check,
            "RU": self._ru_vies_check,
            "RS": self._rs_vies_check,
            "SI": self._si_vies_check,
            "SK": self._sk_vies_check,
            "SE": self._se_vies_check
        }

    def validate(self, country_code: str, vies_number: str) -> bool:
        result = self.country_functions[country_code](vies_number)
        return result

    def _at_vies_check(self, vies_number: str) -> bool:
        print("at")
        exp = "^U(\d{8})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _be_vies_check(self, vies_number: str) -> bool:
        print("be")
        exp = "^([0-1]\d{9})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _bg_vies_check(self, vies_number: str) -> bool:
        print("bg")
        exp = "^(\d{9,10})$/)$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _ch_vies_check(self, vies_number: str) -> bool:
        print("che")
        exp = "^(\d{9})(MWST|TVA|IVA)?$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _cy_vies_check(self, vies_number: str) -> bool:
        print("cy")
        exp = "^([0-59]\d{7}[A-Z])$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _cz_vies_check(self, vies_number: str) -> bool:
        # print("cz")
        exp = "^(\d{8,10})(\d{3})?$"
        r = re.search(exp, vies_number)
        if not bool(r):
            print("regex 0")
            return False
        cz_r0 = "^\d{8}$"  # CZ00008702
        cz_r1 = "^[0-5][0-9][0|1|5|6][0-9][0-3][0-9]\d{3}$"  # CZ395601439
        cz_r2 = "^6\d{8}$"  # CZ680447748
        cz_r3 = "^\d{2}[0-3|5-8][0-9][0-3][0-9]\d{4}$"  # CZ5511061105
        digits = [int(i) for i in vies_number]
        weights = (8, 7, 6, 5, 4, 3, 2)
        if re.search(cz_r0, vies_number):
            print("cz_r0")
            check_sum = 11 - sum(d * w for d, w in zip(digits, weights)) % 11
            if check_sum == 10:
                check_sum = 10
            if check_sum == 11:
                check_sum = 1
            return check_sum == digits[-1]
        if re.search(cz_r1, vies_number):
            print("cz_r1")
            if int(vies_number[0:2]) > 62:
                return False
            return True
        if re.search(cz_r2, vies_number):
            print("cz_r2")
            check_sum = 0
            for i in range(0, 7):
                check_sum += digits[i+1] * weights[i]
            temp = 0
            if check_sum % 11 == 0:
                temp = check_sum + 11
            else:
                temp = math.ceil(check_sum/11) * 11
            point = temp - check_sum
            lookup = (8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8)
            if lookup[point-1] == digits[8]:
                return True
            return False
        if re.search(cz_r3, vies_number):
            print("cz_r3")
            check_sum = int(vies_number[0:2]) + int(vies_number[2:4]) + int(
                vies_number[4:6]) + int(vies_number[6:8]) + int(vies_number[8:])
            if (check_sum % 11 == 0) and (int(vies_number) % 11 == 0):
                return True
            return False
        return False

    def _de_vies_check(self, vies_number: str) -> bool:
        print("de")
        exp = "^([1-9]\d{8})$"
        product = 10
        check_sum = 0
        check_digit = 0
        r = re.search(exp, vies_number)
        if not bool(r):
            return False
        digits = [int(i) for i in vies_number]
        for i in range(0, 8):
            check_sum = (digits[i]+product) % 10
            if check_sum == 0:
                check_sum = 10
            product = (2*check_sum) % 11
        if(11 - product == 10):
            check_digit = 0
        else:
            check_digit = 11 - product
        return check_digit == digits[-1]

    def _dk_vies_check(self, vies_number: str) -> bool:
        print("dk")
        exp = "^(\d{8})$$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _ee_vies_check(self, vies_number: str) -> bool:
        print("ee")
        exp = "^(10\d{7})$"
        r = re.search(exp, vies_number)
        if not bool(r):
            return False
        digits = [int(i) for i in vies_number]
        weights = (3, 7, 1, 3, 7, 1, 3, 7)
        check_sum = 10 - sum(d * w for d, w in zip(digits, weights)) % 10
        if check_sum == 10:
            check_sum = 0
        return check_sum == digits[-1]

    def _el_vies_check(self, vies_number: str) -> bool:
        print("el")
        exp = "^(\d{9})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _es_vies_check(self, vies_number: str) -> bool:
        print("es")
        exp1 = "^([A-Z]\d{8})$"
        exp2 = "^([A-HN-SW]\d{7}[A-J])$"
        exp3 = "^([0-9YZ]\d{7}[A-Z])$"
        exp4 = "^([KLMX]\d{7}[A-Z])$"
        r1 = bool(re.search(exp1, vies_number))
        r2 = bool(re.search(exp2, vies_number))
        r3 = bool(re.search(exp3, vies_number))
        r4 = bool(re.search(exp4, vies_number))
        if r1 or r2 or r3 or r4:
            return True
        return False

    def _eu_vies_check(self, vies_number: str) -> bool:
        print("eu")
        exp = "^(\d{9})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _fi_vies_check(self, vies_number: str) -> bool:
        print("fi")
        exp = "^(\d{8})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _fr_vies_check(self, vies_number: str) -> bool:
        print("fr")
        exp1 = "^(\d{11})$"
        exp2 = "^([A-HJ-NP-Z]\d{10})$"
        exp3 = "^(\d[A-HJ-NP-Z]\d{9})$"
        exp4 = "^([A-HJ-NP-Z]{2}\d{9})$"
        r1 = re.search(exp1, vies_number)
        r2 = re.search(exp2, vies_number)
        r3 = re.search(exp3, vies_number)
        r4 = re.search(exp4, vies_number)
        if r1 or r2 or r3 or r4:
            return True
        return False

    def _gb_vies_check(self, vies_number: str) -> bool:
        print("gb")
        exp1 = "^(\d{9})$"
        exp2 = "^(\d{12})$"
        exp3 = "^(GD\d{3})$"
        exp4 = "^(HA\d{3})$"
        r1 = bool(re.search(exp1, vies_number))
        r2 = bool(re.search(exp2, vies_number))
        r3 = bool(re.search(exp3, vies_number))
        r4 = bool(re.search(exp4, vies_number))
        if r1 or r2 or r3 or r4:
            return True
        return False

    def _hr_vies_check(self, vies_number: str) -> bool:
        print("hr")
        exp = "^(\d{11})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _hu_vies_check(self, vies_number: str) -> bool:
        print("hu")
        exp = "^(\d{8})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _ie_vies_check(self, vies_number: str) -> bool:
        print("ie")
        check_sum = 0
        exp1 = "^(\d{7}[A-W])$"
        exp2 = "^([7-9][A-Z\*\+)]\d{5}[A-W])$"
        exp3 = "^(\d{7}[A-W][AH])$"
        r1 = bool(re.search(exp1, vies_number))
        r2 = bool(re.search(exp2, vies_number))
        r3 = bool(re.search(exp3, vies_number))
        if not (r1 or r2 or r3):
            return False
        weights = (8, 7, 6, 5, 4, 3, 2)
        if re.search("^\d[A-Z\*\+]", vies_number):
            vies_number = '0' + vies_number[2:7] + \
                vies_number[0] + vies_number[7]
        for i in range(0, 7):
            check_sum += int(vies_number[i]) * weights[i]
        if re.search("^\d{7}[A-Z][AH]$", vies_number):
            if vies_number[8] == 'H':
                check_sum += 72
            else:
                check_sum += 9
        check_sum = check_sum % 23
        if check_sum == 0:
            check_sum = 'W'
        else:
            check_sum = chr(check_sum + 64)
        if check_sum == vies_number[7]:
            return True
        return False

    def _it_vies_check(self, vies_number: str) -> bool:
        print("it")
        exp = "^(\d{11})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _lv_vies_check(self, vies_number: str) -> bool:
        print("lv")
        exp = "^(\d{11})$"
        r = re.search(exp, vies_number)
        if not bool(r):
            return False
        if re.search("^[0-3]", vies_number):
            if re.search("^[0-3][0-9][0-1][0-9]", vies_number):
                return True
            return False
        else:
            digits = [int(i) for i in vies_number]
            weights = (9, 1, 4, 8, 3, 10, 2, 5, 7, 6)
            check_sum = sum(d * w for d, w in zip(digits, weights))
        return check_sum == digits[9]

    def _lt_vies_check(self, vies_number: str) -> bool:
        print("lt")
        exp = "^(\d{9}|\d{12})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _lu_vies_check(self, vies_number: str) -> bool:
        print("lu")
        exp = "^(\d{8})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _mt_vies_check(self, vies_number: str) -> bool:
        print("mt")
        exp = "^([1-9]\d{7})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _nl_vies_check(self, vies_number: str) -> bool:
        print("nl")
        exp1 = "^(\d{9})$"
        exp2 = "^(\d{12})$"
        r1 = bool(re.search(exp1, vies_number))
        r2 = bool(re.search(exp2, vies_number))
        if r1 or r2:
            return True
        return False

    def _no_vies_check(self, vies_number: str) -> bool:

        print("no")
        exp = "^(\d{9})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _pl_vies_check(self, vies_number: str) -> bool:
        print("pl")
        exp = "^(\d{10})$"
        r = re.search(exp, vies_number)
        if not bool(r):
            return False
        digits = [int(i) for i in vies_number]
        weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        return check_sum == digits[9]

    def _pt_vies_check(self, vies_number: str) -> bool:
        print("pt")
        exp = "^(((([1-3]|5|6)\d)|(45)|(7([0-2]|[4-5]|[7-9]))|(9[0|1|8|9]))(\d{7}$))"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _ro_vies_check(self, vies_number: str) -> bool:
        print("ro")
        exp = "^([1-9]\d{1,9})$"
        r = re.search(exp, vies_number)
        if not bool(r):
            return False
        digits = [int(i) for i in vies_number]
        vies_len = len(digits)
        weights = (7, 5, 3, 2, 1, 7, 5, 3, 2)
        weights = weights[(10-vies_len):]
        check_sum = (sum(d * w for d, w in zip(digits, weights))*10) % 11
        if check_sum == 10:
            check_sum = 0
        return check_sum == int(vies_number[-1])

    def _ru_vies_check(self, vies_number: str) -> bool:
        print("ru")
        exp = "^(\d{10}|\d{12})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _rs_vies_check(self, vies_number: str) -> bool:
        print("rs")
        exp = "^(\d{9})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _si_vies_check(self, vies_number: str) -> bool:
        print("si")
        exp = "^([1-9]\d{7})$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)

    def _sk_vies_check(self, vies_number: str) -> bool:
        print("sk")
        exp = "^([1-9]\d[2346-9]\d{7})$"
        r = re.search(exp, vies_number)
        if not bool(r):
            return False
        vies_number = int(vies_number)
        return not vies_number % 11

    def _se_vies_check(self, vies_number: str) -> bool:
        print("se")
        exp = "^(\d{10}01)$"
        r = re.search(exp, vies_number)
        print(bool(r))
        return bool(r)
