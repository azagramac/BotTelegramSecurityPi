## Sending notifications with a Telegram bot usage RaspberryPi and sensor PIR


### Install

    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y python3 python3-pip python3-picamera gpac curl wget git libjpeg62 ffmpeg
    sudo pip3 install -r requirements.txt


### Settings to RaspberryPi

    sudo raspi-config nonint do_camera 0

### Run

    ./app.py
