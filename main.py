from bsw_config import bsw_config
import time

if __name__ == "__main__":
    output_channels_test=[5, 7, 11,13,15,17]
    bsw = bsw_config.BSW()
    for channel in output_channels_test:
        bsw.set_channel(channel)
        time.sleep(2)
        bsw.reset_channel(channel)
        time.sleep(2)
    for i in range(0,100,10):
        bsw.change_pwm_duty(i)
        time.sleep(5)

    del bsw
