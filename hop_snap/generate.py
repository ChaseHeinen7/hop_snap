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

Detector = namedtuple("Detector", "detector_id location")

def generate_message(time_string_format, detectors):
    detector = detectors[random.randint(0, len(detectors) - 1)]
    zs, ts = sig.siggenerate()
    return SNEWSTimedata(
            id=random.randint(0,8)+1,
            zs=zs,
            ts=ts,
            )



load_dotenv(dotenv_path="example.env")
detectors = [
    Detector("DETECTOR 1", "Houston"),
    Detector("DETECTOR 2", "Seattle"),
    Detector("DETECTOR 3", "Los Angeles"),
]

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
       time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    source.close()
