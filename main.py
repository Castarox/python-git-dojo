from gittie_helper import *

def main():
    house = GittieHelper()
    house.set_temperature(20)
    house.set_humidity(0.80)
    house.set_air_pollution(8)
    if house.is_home_save():
        print('yey')
    else:
        print('nope')
    house.is_hungry()


if __name__ == '__main__':
    main()