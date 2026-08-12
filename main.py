from lcd_i2c import LCD_I2C

lcd = LCD_I2C(0x27, 16, 2)

lcd.backlight.on()
lcd.clear()

lcd.write_text("MAGNUS OPUS 3000")
