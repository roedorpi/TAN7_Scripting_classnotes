# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:07:02 2022
PySimpleGui example of System usability scale questionaire. This type using a self defined Class RadioButtonScale.py
This file generates a window that present the 10 questions of the SUS scale 
with a Likert scale response. Elements used from PySimpleGUI, Radio, Text, Button. Implementation is based on object oriented programming, where methods and properties are moved to the self defined class.  
@author: rop
"""

import PySimpleGUI as sg
import RadioButtonScale as rbs
from DataClass import DataClass as dc
            

StartMessage = 'Press Go to start'

#load SUS scale items
SUSfile = open('SUS_EN_DK.csv', 'r')
lines = SUSfile.readlines()
SUS= [ln.split(";")[2][0:-1] for ln in lines]
SUSfile.close()
SUS = SUS[1:]

Count = 0
SUSresults  = dc('MyResp.csv')
evaluation_results = dict()

#instantiate a RadioButtonScale
RBs = rbs.RadioButtonScale(ScaleSteps=7, ScaleLabels=['lit', 'maget'])

layout = [
        [sg.Text(StartMessage, key="-Question-", size=(30,4),
                 justification="center", expand_x=True)],
        RBs.Labels,
        RBs.Layout,
        [sg.Button("Go",key="-Nav1-",expand_x=True)]
    ]

window = sg.Window("Likert Scale", layout, finalize=True)



while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED:
        break
    # check for navigation button press
    if event == '-Nav1-':
        if StartMessage in window['-Question-'].get():  # the first time button is pressed
            window['-Nav1-'].update(text='Next') # change the button text
            window['-Question-'].update(SUS[0]) # update stimuli
            RBs.ResetRadio() # reset scale
        else: # 
            v = RBs()
            evaluation_results[Count] = [Count+1,v]
            SUSresults.dataupdate(f"{Count+1}:{v}")
            Count += 1
            RBs.ResetRadio()
            # check that we are ready to close program                
            if Count < len(SUS):
                window['-Question-'].update(SUS[Count])
            else:
                # calculate the SUS score and close the program:
                EveQ = 0
                OddQ = 0
                for i in range(len(SUS)):
                    if i%2:
                        EveQ += RBs.ScaleSteps - SUSresults.responses[i]
                    else:
                        OddQ += SUSresults.responses[i]-1

                SUSresults.dataupdate(f"SUSscore = {(EveQ + OddQ) / ((RBs.ScaleSteps - 1) * len(SUS)) * 100}")


                break

# Finish up by removing from the screen
window.close()
