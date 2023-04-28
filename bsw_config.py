# =========================================================
# Seeed Studio Raspberry Pi Relay Board Library
#
# by John M. Wargo (www.johnwargo.com)
#
# Modified from the sample code on the Seeed Studio Wiki
# http://wiki.seeed.cc/Raspberry_Pi_Relay_Board_v1.0/
# =========================================================

import RPi.GPIO as GPIO


class BSW:
    def __init__(self, input_channels=[], output_channels=[7, 11,13,15], pwm_channel=12):
        GPIO.setmode(GPIO.BOARD)
        #configure_inputchannel(input_channels)
        configure_outputchannel(output_channels)
        configure_pwm(pwm_channel)
        #self.input_channels = input_channels
        self.output_channels = output_channels
        self.pwm_channel = pwm_channel

    def configure_inputchannel(self, channel):
        GPIO.setup(channel, GPIO.IN)
    def configure_outputchannel(self, channel):
        GPIO.setup(channel, GPIO.OUT)
    def set_channel(channel):
        GPIO.output(channel, 1)
    def reset_channel(channel):
        GPIO.output(channel, 0)
    def configure_pwm(self, channel, freq):
        configure_outputchannel(channel)
        self.p = GPIO.PWM(channel, freq)
    def set_pwm(self, duty):
        self.p.start(duty)
    def change_pwm_freq(self, freq):
        self.p.ChangeFrequency(freq)   # where freq is the new frequency in Hz
    def change_pwm_duty(self, duty):
        p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
    def __del__(self):
        reset_channel(self.output_channels)
        GPIO.cleanup()
