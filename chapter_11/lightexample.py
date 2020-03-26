#! /usr/bin/env python3

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    # This triggers when one light is green and one light is yellow.
    assert 'red' in stoplight.values(), ('Neither light is red! ' + 
    	str(stoplight))

switch_lights(market_2nd)