# Puts A random Kanye West quote on the Adafruit Magtag 
# Based on
# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-License-Identifier: Unlicense
# and
# https://github.com/ajzbc/kanye.rest
# MIT License
#
# Requires the default Adafruit Magtag installation and a secrets.py file
# 2021 Brock Craft
# MIT License

from adafruit_magtag.magtag import MagTag

# Set up where we'll be fetching data from
DATA_SOURCE = "https://api.kanye.rest/"
DATA_LOCATION = ["quote"]

magtag = MagTag(
    url=DATA_SOURCE,
    json_path=DATA_LOCATION,
)

magtag.network.connect()

magtag.add_text(
    text_font="/fonts/Arial-Bold-12.pcf",
    text_wrap=30,
    text_position=(10,10),
    text_scale=1,
    text_anchor_point=(0, 0),
)

try:
    value = magtag.fetch()
    print("Response is", value)
except (ValueError, RuntimeError) as e:
    print("Some error occured, retrying! -", e)
magtag.exit_and_deep_sleep(60)