import RPi.GPIO as GPIO
import time
import spidev

class classLeds():
    def __init__(self, yellowPin, redPin):
        self.__yellowPin = yellowPin
        self.__redPin = redPin
        self.__listPins = [self.__redPin, self.__yellowPin]

    def turnOn(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.__listPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)

    def turnOff(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.__listPins:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)


class classHall():
    def __init__(self, hallPin,): #counter):
        self.__hallPin = hallPin
        # self.__counter = counter
        #
        # @property
        # def counter():
        #     return self.__counter
        #
        # @counter.setter
        # def counter():
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__hallPin, GPIO.IN)


class analogSensor():
    def __init__(self, MCPchannel, GPIO_CSchannel):
        self.__MCPchannel = MCPchannel # Channel must be an integer 0-7
        self.__GPIO_CSchannel = GPIO_CSchannel #must be integer 7 or 8 (chip select)

    # Function to read SPI data from MCP3008
    def ReadChannel(self):
        #SETUP
        spi = spidev.SpiDev()  # create spi object
        spi.open(0, self.__GPIO_CSchannel)  # open spi port 0, device (CS)
        #READ
        # 3 bytes versturen
        # 1 , S D2 D1 D0 xxxx, 0
        adc = spi.xfer2([1, (8 + self.__MCPchannel) << 4, 0])
        data = ((adc[1] & 3) << 8) | adc[2]  # in byte 1 en 2 zit resultaat
        print(data)


hallWaarde = 0
hallWaardeVorige = 0
status = 0
counter = 0
bool(hallWaarde)
bool(hallWaardeVorige)
bool(status)

hall = classHall(16)
hall.setup()
pin = 16

stroomSensor = analogSensor(0, 1)

try:
    leds = classLeds(19,26)
    leds.turnOff()


    # while True:
    #     hallWaarde = GPIO.input(pin)
    #     if ((hallWaarde == False) & (hallWaardeVorige != hallWaarde)):
    #         if (status == True):
    #             counter += 1
    #
    #             status = False
    #             hallWaardeVorige = hallWaarde
    #         else:
    #             status = True
    #             hallWaardeVorige = hallWaarde
    #     hallWaardeVorige = hallWaarde
    #     print(counter)
    while True:
        stroomSensor.ReadChannel()


except KeyboardInterrupt:
    GPIO.cleanup()