import json
import numpy as np
import dataclasses
from snap.datablock import DataBlock
import datetime

start_time=datetime.datetime(2020, 8, 31, 0, 0, 0)

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        elif isinstance(obj, np.ndarray):
            return list(obj)
        else:
            return super().default(obj)

def to_json(data):
    ts=data.ts
    to=ts[0]
    to=start_time.timestamp()
    to=datetime.datetime.utcfromtimestamp(to).strftime("%y/%m/%d %H:%M:%S:%f")
    data.ts=to
    return json.dumps(data, cls=Encoder, indent=4)

def from_json(cls):
    def _f(data):
        data = json.loads(data)
        ts = data['ts']
        new_ts = []
        for i in ts:
            i = i.replace("-", " ")
            i = datetime.datetime.strptime(i, "%y/%m/%d %H:%M:%S:%f")
            dt = i - start_time
            dt = float(dt.total_seconds())
            new_ts.append(dt)
        return DataBlock(id=data['id'], dec_id=data['detector_id'], loc=data['location'], ts=new_ts, zs=data['zs'])
    return _f
