import random

class GittieHelper():

    def __init__(self):
        """
        Initialize attributes with default value
        """

        self.air_pollution_level = 10
        self.day_number = 10
        self.temperature_degree = 0
        self.humidity_value = 0


    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree: float
        """
        try:
            float(temperature_degree)
            self.temperature_degree = temperature_degree
        except ValueError:
            print('Wrong input')



    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:pass
        """
        try:
            float(humidity_value)
            self.humidity_value = humidity_value
        except ValueError:
            print('Wrong input')

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

    def is_home_save(self):

        """
        Method should calculate if exiting home is safe for gittie
        """

        if self.temperature_degree > 15:
            if self.humidity_value > 0.5:
                if self.air_pollution_level < 10:
                    return True
        return False

    def what_weather(self):
       weather = ['raining', 'snowing', 'nice weather']

       return random.choice(weather)

    def have_guests(self):

        guests = ['yes', 'no']

        return random.choice(guests)


