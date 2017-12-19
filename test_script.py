import our_gantt_chart as gc
import numpy as np
import pandas as pd
import datetime as dt

from dateutil import parser



import matplotlib.pyplot as plt
import matplotlib.patches as patches

import matplotlib.text as text


from collections import OrderedDict
activities = OrderedDict()

activities["pick"] = {"name":"Pick a thesis topic", "start":"1/1/2018", "duration":20, "type_of_work":"reading"}
activities["genmc"] = {"name":"Generate MC", "start":"pick", "duration":120, "type_of_work":"grid"}
activities["opt"] = {"name":"Optimize selection criteria", "start":"genmc", "duration":400, "type_of_work":"code"}
activities["sys"] = {"name":"Systematic studies", "start":"opt", "duration":20, "type_of_work":"code"}
activities["pas"] = {"name":"Write Physics Analysis Note", "start":"3/1/2018", "duration":800, "type_of_work":"writing"}
activities["paper"] = {"name":"Write paper", "start":"opt", "duration":100, "type_of_work":"writing"}

colors = {"grid":"r",
            "reading":"m",
            "writing":"b",
            "code":"g"}

plt.figure(figsize=(12,8))
ax2 = gc.gantt_chart(activities,colors)

plt.show()
