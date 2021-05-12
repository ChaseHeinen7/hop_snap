from collections import namedtuple
import datetime
import os
import random
import time
import uuid

from dotenv import load_dotenv

from hop import Stream
from hop.plugins.snews import SNEWSTimedata
from hop_snap import sig
from hop_snap import json_interface

def generate_message(time_string_format):
    zs, ts = sig.siggenerate()
    return SNEWSTimedata(
            id=random.randint(0,8)+1,
            zs=zs,
            ts=ts,
            )



load_dotenv(dotenv_path="example.env")

stream = Stream(auth=False)
source = stream.open(os.getenv("TIMEDATA_TOPIC"), "w")
try:
   while True:
       message = generate_message(
            os.getenv("TIME_STRING_FORMAT"),
            detectors,
        )
       message = json_interface.to_json(message)
       source.write(message)
       time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    source.close()
