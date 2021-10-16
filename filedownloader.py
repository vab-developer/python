#Project: File Downloader
#Description: This is a project for download a image file
#Programmer: Vali Asghari Bakhtavar
#Date: 10/16/2021 1:04 a.m.
import urllib.request
image_url = 'https://s21.picofile.com/file/8442310342/logo_vab.png'
image_save_path = 'C:/Users/Vali/Pictures/img/logo_vab.png'
urllib.request.urlretrieve(image_url, image_save_path)
