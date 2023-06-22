from interface import PyWindow
import PySimpleGUI as sg
from fishingbot import FishingBot

botgui = PyWindow().window
fishbot = FishingBot()

while True:

    event, values = botgui.read(timeout=1)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event != sg.TIMEOUT_KEY:
        if event == '-BUTTONSTART-':
            fishbot.set_to_begin(values)
            fishbot.botting = not fishbot.botting

    if fishbot.botting:
        fishbot.runHack()
        botgui['-BUTTONSTART-'].update('STOP')
    else:
        botgui['-BUTTONSTART-'].update('START')

botgui.close()