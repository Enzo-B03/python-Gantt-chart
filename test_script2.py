import gantt_chart as gc
import numpy as np
import pandas as pd
import datetime as dt

from dateutil import parser



import matplotlib.pyplot as plt
import matplotlib.patches as patches

import matplotlib.text as text


from collections import OrderedDict
activities = OrderedDict()

activities["t1"] = {"name":"Task 1", "start":"2/1/2018", "duration":30, "type_of_work":"Indoors"}
activities["t2"] = {"name":"Task 2", "start":"t1", "duration":60, "type_of_work":"Outdoors"}

colors = {"Indoors":"red", 
               "Outdoors":"blue",
          }
plt.figure(figsize=(12,8))
ax2 = gc.gantt_chart(activities,colors,verbose=True)

plt.show()
