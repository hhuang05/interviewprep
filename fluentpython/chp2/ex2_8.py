#!/usr/bin/env python3

def example():
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (1,2)),
        ('Delhi NCR', 'IN', 21.935, (3,4)),
        ('Mexico City', 'MX', 21.935, (5,6)),
        ('New York-Newark', 'US', 20.104, (7,8)),
        ('Sao Paulo', 'BR', 19.649, (9,10)),
    ]

    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (lat, longitude) in metro_areas:
        print(fmt.format(name, lat, longitude))

    
if (__name__ == '__main__'):
    example()
