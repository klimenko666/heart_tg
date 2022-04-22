from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time, symbols, random
from time import sleep


app = Client("my_account")

# klimenko test
@app.on_message(filters.command("luv", prefixes="") & filters.me)
def hack(_, msg):

	msg.edit("🟢 LOVE")
	sleep(3)

	msg.edit(symbols.i)
	sleep(2)
	msg.edit(symbols.l)
	sleep(2)
	msg.edit(symbols.o)
	sleep(2)
	msg.edit(symbols.v)
	sleep(2)
	msg.edit(symbols.e)
	sleep(2)
	msg.edit(symbols.y)
	sleep(2)
	msg.edit(symbols.o)
	sleep(2)
	msg.edit(symbols.u)
	sleep(2)
	msg.edit(symbols.heart)




# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	
	text = orig_text

	
	for i in text:
		try:
			msg.edit(i)
			sleep(0.5) # 50 ms
		except FloodWait as e:
			sleep(e.x)




print("STARTED")
app.run()