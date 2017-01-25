class GittieHelper():

    def __init__(self):
        """
        Initialize attributes with default value
        """
        self.air_pollution_level = 10
        self.day_number = 10




    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree:
        """
        pass

    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:pass
        """
        pass

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        try:
            self.air_pollution_level = int(air_pollution_level)
        except ValueError:
            print('ValueError')


    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        try:
            self.day_number = int(day_number)
        except ValueError:
            print('ValueError')

    def get_value(self):
        """
        Method should calculate if exiting home is safe for gittie
        """

        if self.air_pollution_level < 10 and self.humidity_value > 0.5 and temperature_degree > 15:
            return true
        else:
            return false
