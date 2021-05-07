from machine import ADC, Pin
from utime import sleep

pot = ADC(26)

conversion_factor = 3.3 / 65535

while True:
    raw = pot.read_u16()
    volts = raw * conversion_factor    
    print('Raw: {} '.format(raw), 'Voltage {:.1f}V'.format(volts))
    sleep(1)
