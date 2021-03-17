## Sending notifications with a Telegram bot usage RaspberryPi and sensor PIR

![PIR Sensor](https://github.com/AzagraMac/BotTelegramSecurityPi/blob/dev/res/pir_sensor.png) ![Telegram](https://github.com/AzagraMac/BotTelegramSecurityPi/blob/dev/res/icon_telegram.png)

### Requeriments
- Raspberry Pi
- Pi Camera or Pi NoIR
- PIR Motion Sensor Module HCSR501

### Install
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y ffmpeg
    sudo apt install -y python3 python3-pip python3-picamera curl wget git gpac
    sudo pip3 install -r requirements.txt

### Settings to RaspberryPi
    sudo raspi-config nonint do_camera 0

### Check /boot/config.txt, must have a minimum of 128Mb in the gpu_mem parameter
    gpu_mem=128

### Edit config.py
Edit the config.py file, and add your tokens obtained in https://t.me/BotFather and https://t.me/myidbot

    TOKEN_ID = 'YOUR_TOKEN_BOT'
    CHAT_ID = 'YOUT_TOKEN_CHAT_ID'

### Edit bot.service, change path script excution.
    [Service]
    Type=idle
    ExecStart=/usr/bin/python3 /home/pi/git/BotTelegramSecurityPi/app.py

### Run automatic on boot
    chmod a+x app.py lib/*.py
    sudo mv bot.service /lib/systemd/system/
    sudo chmod 644 /lib/systemd/system/bot.service
    sudo systemctl daemon-reload
    sudo systemctl enable bot.service
    sudo systemctl start bot.service
    sudo systemctl status bot.service

### Run manual
    ./app.py
