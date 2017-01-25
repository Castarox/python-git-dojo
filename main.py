from gittie_helper import *

def main():
    '''test'''
    house = GittieHelper()
    house.set_temperature(20)
    house.set_humidity(0.80)
    house.set_air_pollution(8)
    if house.is_home_save():
        print('yey')
    else:
        print('nope')
    house.is_hungry()
    try:
        raise ValueError
    except ValueError:
        print('nope')

    print('dalej w programie')

if __name__ == '__main__':
    main()