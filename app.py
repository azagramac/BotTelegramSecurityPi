#!/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import sys
import picamera
import telegram
from config import TOKEN_ID, CHAT_ID, VIDEO_TIME, REGISTRATION_FOLDER
from lib.camera import Camera
from lib.telebot import Telebot
from lib.pir import MotionDetector

camera = Camera(REGISTRATION_FOLDER)
bot = Telebot(TOKEN_ID, CHAT_ID)
pir = MotionDetector()

@bot.handler("/start")
def on_start():
    bot.is_listen = True
    return bot.send_message(on_help())

@bot.handler("/photo")
def on_photo():
    return bot.send_photo(camera.take_photo(), "Photo")

@bot.handler("/video")
def on_video(*args):
    delay = args[0] if args else VIDEO_TIME
    bot.send_message("Starting video recording...")
    time.sleep(delay)
    bot.send_message("Sending video...")
    return bot.send_video(camera.start_recording(delay), "Video")

@bot.handler("/clean")
def on_clean():
    return bot.send_message(camera.purge_records())

@bot.handler("/help")
def on_help():
    msg = "command usage:\n"
    msg += "\t/start: start the home monitoring system \n"
    msg += "\t/stop: stop the home monitoring system\n"
    msg += "\t/status: show the status of the monitoring system \n"
    msg += "\t/photo: take a picture\n"
    msg += "\t/video <delay>: records a video, by default delay is " + str(VIDEO_TIME) + "s \n"
    msg += "\t/clean: remove all files in video folder\n"
    msg += "\t/help: show help\n"
    return bot.send_message(msg)

print('I am listening ...')
try:
    while True:
        if bot.is_listen and pir.movement_detected():
            bot.send_video(camera.start_recording(VIDEO_TIME), 'motion detected')
        else:
            time.sleep(1)
except KeyboardInterrupt:
    del camera
