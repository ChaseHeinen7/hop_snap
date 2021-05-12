import numpy as np
import datetime

"""
Generate random time series data from a detector.

"""

def siggenerate():
        n = np.random.randint(8,12);
        sigarray = np.around(np.random.normal(0,1,n), decimals=2)
        timearray = [];
        initial_time = datetime.datetime.now();
        timearray.append(initial_time);
        for i in range(n):
             timearray.append(timearray[i] + datetime.timedelta(milliseconds = 100))
        for i in range(len(timearray)):
             timearray[i] = timearray[i].strftime("%y/%m/%d-%H:%M:%S:%f")
        return sigarray, timearray
