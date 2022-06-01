# https://www.denshi.club/pc/raspi/5-mcp3208.html

import spidev   # RasPi のインタフェース設定で SPI enable にして使う
               # SPI enable は　/boot read write かつ overlay disable で設定する。

class Adc():        # ADC (MCP3204)

   def __init__(self):
       self.d1tbl = [0x00, 0x40, 0x80, 0xC0]       # send data 1
       self.spi = spidev.SpiDev()

   def rdadc(self, chn):     # Read ADC chn=0,1,2,3 (INTEGER)
       self.spi.open(0, 0) # bus0, CE0
       self.spi.max_speed_hz = 1000000  # 1MHz
       rd = self.spi.xfer2([0x06, self.d1tbl[chn], 0x00])
       self.spi.close()
       
       ret = rd[1] * 256 + rd[2]
       return ret

def main():
    adc = Adc()    # クラス adc のインスタンスを作成

    while True:
        #for i in range(4):
            c = adc.rdadc(0)    # CH i のADCサンプリング結果を取得
            print(c)

main()
