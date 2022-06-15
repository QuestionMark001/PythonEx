"""
Author: QuestionMark001
Date: 2022-06-13 20:42:59
LastEditors: QuestionMark001
LastEditTime: 2022-06-14 21:59:48
FilePath: /LocalProjects/PythonEx/src/MCM/Simulated_Test.py
Description: 全国数学建模竞赛--模拟题

Copyright (c) 2022 by QuestionMark001, All Rights Reserved.
"""

import openpyxl
from pickle import NONE
import tkinter
from tkinter import filedialog
import os
import pandas as pd
import numpy as np
import math
import time

root = tkinter.Tk()
root.withdraw()

filePath = filedialog.askopenfilename()
theExcel = pd.read_excel(filePath, sheet_name='Sheet1')
print(theExcel)
