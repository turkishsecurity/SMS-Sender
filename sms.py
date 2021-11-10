#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


#coded by xale

print("----------------")
print("SMS SENDER V1 ")
print("by Xale ~ @xaletr")
print("----------------")

hedef = input("mesaj gönderilecek numara > ")
mesaj = input("gönderilecek mesaj > ")

msj = mesaj[0:70]

print("Gönderilecek Mesajınız : ", msj)
print("Hedef Numara : ", hedef)
gonder = input("Mesajınız Gönderilsin Mi ? (Y/N) ")

if gonder == "Y":
    resp = requests.post('https://textbelt.com/text', {
  'phone': hedef,
  'message': msj,
  'key': 'textbelt',
    })
    print(resp.json())

elif gonder == "N":
	print("Mesaj Gönderimi İptal Edildi")
