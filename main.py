from bsw_config import *
import time

if __name__ == "__main__":
    output_channels_test=[5, 7, 11,13,15,17]
    bsw = bsw_config.BSW()
    for channel in output_channels_test:
        bsw.set_channel(channel)
        time.sleep(2)
        bew.reset_channel(channel)
        time.sleep(2)

    del bsw
