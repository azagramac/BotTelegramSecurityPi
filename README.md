## Sending notifications with a Telegram bot usage RaspberryPi and sensor PIR

![PIR Sensor](https://github.com/AzagraMac/BotTelegramSecurityPi/blob/dev/res/pir_sensor.png) ![Telegram](https://github.com/AzagraMac/BotTelegramSecurityPi/blob/dev/res/icon_telegram.png)

### Requeriments
- Raspberry Pi
- Pi Camera or Pi NoIR
- PIR Motion Sensor Module HCSR501

### Install

    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y python3 python3-pip python3-picamera gpac curl wget git libjpeg62 ffmpeg
    sudo pip3 install -r requirements.txt

### Settings to RaspberryPi

    sudo raspi-config nonint do_camera 0

### Edit config.py
Edit the config.py file, and add your tokens obtained in https://t.me/BotFather and https://t.me/myidbot

    TOKEN_ID = 'YOUR_TOKEN_BOT'
    CHAT_ID = 'YOUT_TOKEN_CHAT_ID'

### Run

    chmod a+x app.py lib/*.py
    ./app.py
