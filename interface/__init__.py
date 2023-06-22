import PySimpleGUI as sg
import os


class PyWindow:

    window = None

    def __init__(self):
        sg.theme('Light Blue')
        self.create_window()

    def bot_tab(self):
        return [[sg.Text('Hi I am Carp Buddy!')],
                [sg.Frame('Stop conditions', [
                    [sg.Checkbox('Total Time (Minutes)', key='-ENDTIMEP-'), sg.InputText(size=(5,10), key='-ENDTIME-')],
                    ])],
                [sg.Button('START', key='-BUTTONSTART-')]]


    def options_tab(self):
        return [
                [sg.Frame('Time configuration', [
                   [sg.Text('Wait to put bait'),
                    sg.Slider(range=(2, 30), key="-BAITTIME-" , orientation='v', size=(5, 20), default_value=2),
                    sg.Text('Wait to throw'),
                    sg.Slider(range=(2, 30), key="-THROWTIME-", orientation='v', size=(5, 20), default_value=2),
                    sg.Text('Wait to start minigame'),
                    sg.Slider(range=(2, 5), key="-STARTGAME-", orientation='v', size=(5, 20), default_value=2),
                ]])]]

    def create_tabs(self):

        tab1_layout = self.bot_tab()
        tab2_layout = self.options_tab()

        tab_1 = sg.Tab('Fishing', tab1_layout, font='Ariel 15', key='-TAB1-')
        tab_2 = sg.Tab('Options', tab2_layout, font='Ariel 15', key='-TAB2-')

        tab_group_layout = [[tab_1, tab_2]]

        return tab_group_layout

    def create_window_layout(self):

        tab_group_layout = self.create_tabs()

        return [[sg.TabGroup(tab_group_layout,
                 enable_events=True,
                 key='-TABGROUP-')]]

    def create_window(self):

        layout = self.create_window_layout()
        print(os.getcwd())
        self.window = sg.Window('CarpBuddy', layout, no_titlebar=False, icon="fish_icon.ico")