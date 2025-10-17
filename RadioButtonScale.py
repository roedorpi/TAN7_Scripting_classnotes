# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:54:52 2022
Radio Button Scale Class, uses Radio button and Text from PySimpleGUI to make a likert scale.

Object attributes: 
    ScaleSteps -- number or Rario buttons in the scale 
    ScaleLabels -- low and high labels for the scale
    Labels, Layout -- components of the scale to be used in the layout list of the
    PySimpleGui.Window class.
Methods:
     ResetRadio() -- uncheck all radio buttons
     DisableRadio() -- uncheck and disable all radio buttons
     __call__() -- gets the value of the currently selected radio button

@author: rop
"""
from tkinter import *

class RadioButtonScale():
    def __init__(self, ScaleSteps=7, ScaleLabels=['Disagree', 'Agree']):
        self.ScaleSteps = ScaleSteps
        self.ScaleLabels = ScaleLabels
        self.Labels = [Text(ScaleLabels[0], justification='left'),
                       Text(ScaleLabels[1], justification='right', expand_x=True, pad=((0, 0), (0, 0)))]
        self.Layout = [Radiobutton(str(i + 1), group_id="Scale", expand_x=True, pad=((10, 0), (10, 10)),
                             k=i + 1, disabled=True) for i in range(ScaleSteps)]

    def ResetRadio(self):
        for rb in self.Layout:
            rb.update(value=False, disabled=False)

    def DisableRadio(self):
        for rb in self.Layout:
            rb.update(value=False, disabled=True)

    def __call__(self):
        OutVal = None
        for v in range(self.ScaleSteps):
            if self.Layout[v].get():
                OutVal = v+1
        return OutVal