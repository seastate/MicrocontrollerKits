#from machine import UART
from time import sleep
from platform_defs import *
import sds011
from micropyGPS import MicropyGPS

#uart = UART(1, baudrate=9600, pins=('P21','P22'))
def sample_AQ():
    dust_sensor = sds011.SDS011(uartAQ)
    dust_sensor.set_reporting_mode_query()
    dust_sensor.sleep()

    while True:
    #Datasheet says to wait for at least 30 seconds...
        print('Start fan for 15 seconds.')
        dust_sensor.wake()
        sleep(65)

        #Returns NOK if no measurement found in reasonable time
        status = dust_sensor.read()
        #Returns NOK if checksum failed
        pkt_status = dust_sensor.packet_status
        
        #Stop fan
        dust_sensor.sleep()
        
        if(status == False):
            print('Measurement failed.')
        elif(pkt_status == False):
            print('Received corrupted data.')
        else:
            print('PM25: ', dust_sensor.pm25)
            print('PM10: ', dust_sensor.pm10)
            
        sleep(55)

        
while True:
    status = dust_sensor.read(),print(status),print('PM25: ', dust_sensor.pm25,', PM10: ', dust_sensor.pm10)
    sleep(20)


# turn on GPS power        
p_pwr2.value(1)
    
while True:
    if uartGPS.any():
        try:
            #gps_ln=uart4.readline()[:-2].decode('utf-8')
            gps_ln=uartGPS.readline().decode('utf-8')
            #gps_ln=chr(uart4.readchar())
            #print('received gps read...')
            #print(gps_ln,end='')
            if len(gps_ln)>0:
                #w=s.write(gps_ln)
                #w=s.sendto(gps_ln,addr)
                print(gps_ln,end='')
                #print('send complete, ',w,' bytes')
                gps_ln=''
                sleep_ms(50)
        except Exception as ex:
            print('>>>>>>>error in decoding/sending GPS message: ',ex)
            
my_gps = MicropyGPS()
# Main Infinite Loop
while 1:
    # Do Other Stuff Here.......

    # Update the GPS Object when flag is tripped
    if True:
        while uartGPS.any():
            my_gps.update(chr(uartGPS.readchar()))  # Note the conversion to to chr, UART outputs ints normally
        
        print('UTC Timestamp:', my_gps.timestamp)
        print('Date:', my_gps.date_string('long'))
        print('Latitude:', my_gps.latitude_string())
        print('Longitude:', my_gps.longitude_string())
        print('Horizontal Dilution of Precision:', my_gps.hdop)
        print()
        new_data = False  # Clear the flag
        sleep(20)

        
