from .vies_validator import ViesValidator


class PyViesLib:
    def __init__(self):
        self.vvld = ViesValidator()

    def check_vies(self, vies: str) -> bool:
        """Function checks validity of given VIES number

        :param vies: VIES number
        :type vies: str
        :return: Returns True when VIES is valid
        :rtype: bool
        """
        vies = "".join(vies.split()).upper()
        country_code = self._get_cuntry_code(vies)
        vies_number = vies[0:3].replace(country_code, '') + vies[3:]
        result = self.vvld.validate(country_code, vies_number)
        return result

    def _get_cuntry_code(self, vies: str) -> str:
        """Functions extracts country code from VIES number

        :param vies: VIES number
        :type vies: str
        :return: VIES number country code
        :rtype: str
        """
        if vies[0:3] == "CHE":
            return vies[0:3]
        return vies[0:2]
