from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineListItem
import SpeedMeter
from MeetnetVlaamseBanken import VlaamseMeetbank
from GenFunctions import *

# Meetnet Vlaamse Banken login:
username = "bavodenys@gmail.com"
password = 'Kite27Beer!23'
#password = os.environ.get('MEETBANK_PASS')

# Make object Vlaamse Meetbank
VlaamseMeetbank = VlaamseMeetbank(username, password)

# Resize window to smartphone format
#Window.size = (300, 500)


Builder.load_string("""
<HomeScreen>:   
    name:'HomeScreen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Belgian Wind'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        right_action_items: [["language-python", lambda x:app.go_home()]]
                        elevation:8
                    
                    ScrollView:
                        MDList:
                            id:'locations_id'
                                   
        MDNavigationDrawer:
            id:nav_drawer
            
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                
                MDLabel:
                    text:'Menu'
                    size_hint_y: None
                    height: self.texture_size[1]
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home'
                            on_release: root.manager.current = 'HomeScreen'
                            IconLeftWidget:
                                icon: 'home'                    
                        OneLineIconListItem:
                            text:'About'
                            on_release: root.manager.current = 'AboutScreen'
                            IconLeftWidget:
                                icon:'information-outline'
                        OneLineIconListItem:
                            text:'Exit'
                            on_release: app.exit()
                            IconLeftWidget:
                                icon:'logout'
   
<DataScreen>:   
    name:'DataScreen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Belgian Wind'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        right_action_items: [["language-python", lambda x: app.go_home()]]
                        elevation:8
                        
                    MDLabel:
                        id:location_id
                        text: 'DataScreen'
                        halign: 'center'
                        padding_x: 5
                        padding_y: 5
                    
                    SpeedMeter:
                        id: windspeed_id
                        max: 50
                        tick: 200
                        start_angle: -90
                        end_angle: 90
                        subtick: 100
                        label: 'Kts'
                        value: 20
                        cadran_color: '#ffffff'
                        needle_color: '#000000'
                        sectors: (0, '#6699cc', 3, '#87cefa', 6, '#87CEEB', 10, '#0d98ba', 16, '#00FF00', 21, '#FFA500', 27, '#cb4154', 33, '#AE0700', 40, '#800080', 47, '#8F00FF', 50)  
                        sector_width: 10
                                     
                    MDLabel:
                        id:windspeed_id_old
                        text: 'Windspeed: 10 kt'
                        halign: 'center'
                        padding_x: 5
                        padding_y: 5
                        
                    SpeedMeter:
                        id: winddirection_id
                        max: 360
                        tick: 500
                        start_angle: 0
                        end_angle: 0
                        subtick: 400
                        label: ''
                        value: 20
                        sectors: (0, '#00ff00', 50, '#ff0000', 230, '#00ff00' ,360)
                        sector_width: 10
                        display_first: False
                        cadran_color: '#ffffff'
                        needle_color: '#000000'  

                    MDLabel:
                        id:winddirection_id_old
                        text: 'Winddirection: NNW'
                        halign: 'center'
                        padding_x: 5
                        padding_y: 5  
                                       
        MDNavigationDrawer:
            id:nav_drawer 
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                
                MDLabel:
                    text:'Menu'
                    size_hint_y: None
                    height: self.texture_size[1]
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home'
                            on_release: root.manager.current = 'HomeScreen'
                            IconLeftWidget:
                                icon: 'home'
                        OneLineIconListItem:
                            text:'About'
                            on_release: root.manager.current = 'AboutScreen'
                            IconLeftWidget:
                                icon:'information-outline'
                        OneLineIconListItem:
                            text:'Exit'
                            on_release: app.exit()
                            IconLeftWidget:
                                icon:'logout'  
                                
<AboutScreen>:   
    name:'AboutScreen'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Belgian Wind'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        right_action_items: [["language-python", lambda x:app.go_home()]]
                        elevation:8
                    
                    MDLabel:
                        text: "This is an application created by a belgian kitesurfer for kitesurfers in Belgium"
                        halign: "center"
                    
                                   
        MDNavigationDrawer:
            id:nav_drawer
            
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                
                MDLabel:
                    text:'Menu'
                    size_hint_y: None
                    height: self.texture_size[1]
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home'
                            on_release: root.manager.current = 'HomeScreen'
                            IconLeftWidget:
                                icon: 'home'                    
                        OneLineIconListItem:
                            text:'About'
                            on_release: root.manager.current = 'AboutScreen'
                            IconLeftWidget:
                                icon:'information-outline'
                        OneLineIconListItem:
                            text:'Exit'
                            on_release: app.exit()
                            IconLeftWidget:
                                icon:'logout' 
                                
                                                            
""")

# Home screen
class HomeScreen(Screen):
    pass

# Data screen
class DataScreen(Screen):
    pass

# About screen
class AboutScreen(Screen):
    pass

Locations = {'Blankenberge': {'WindMagnitude':"BL7WVC",'WindDirection':"BL7WRS"}, \
            'Nieuwpoort': {'WindMagnitude':"NP7WVC",'WindDirection':"NP7WRS"}, \
            'Oostende': {'WindMagnitude':"OMPWVC",'WindDirection':"OMPWRS"}, \
            'Zeebrugge': {'WindMagnitude':"ZDIWVC",'WindDirection':"ZDIWRS"}}

class DemoApp(MDApp):

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='HomeScreen'))
        self.sm.add_widget(DataScreen(name='DataScreen'))
        self.sm.add_widget(AboutScreen(name='AboutScreen'))
        self.theme_cls.primary_palette = "Red"
        # For loop over all locations with wind information and add item
        for location in sorted(Locations):
            self.sm.screens[0].ids["'locations_id'"].add_widget(OneLineListItem(text=location, on_release=self.select_location))
        return self.sm

    class ContentNavigationDrawer(BoxLayout):
        pass

    def navigation_draw(self):
        pass

    # Go to home screen
    def go_home(self):
        self.sm.current = 'HomeScreen'

    # Go to about screen
    def go_about(self):
        self.sm.current = 'AboutScreen'

    # Exit the application
    def exit(self):
        self.stop()

    # Selection of location
    def select_location(self, obj):
        # Set DataScreen
        self.sm.current = 'DataScreen'
        Data = VlaamseMeetbank.getDataLastXhours(2, [Locations[obj.text]['WindDirection'], Locations[obj.text]['WindMagnitude']])
        WindDirectionTab = []
        WindSpeedTab = []
        for Entry in Data['Values']:
            if Entry['ID'].find("WRS") != -1:
                for sample in Entry['Values']:
                    WindDirectionTab.append(sample['Value'])
            if Entry['ID'].find("WVC") != -1:
                for sample in Entry['Values']:
                    WindSpeedTab.append(sample['Value'])

        # Wind direction processing
        a1, a2, a3, a4, a5 = ProcessWindDirection(WindDirectionTab)
        # Wind speed processing
        b1, b2, b3, b4, b5 = ProcessWindSpeed(WindSpeedTab, 1)

        self.sm.current_screen.ids['location_id'].text = obj.text
        self.sm.current_screen.ids['windspeed_id'].value = round(b2)
        self.sm.current_screen.ids['windspeed_id_old'].text = f"Windspeed: {round(b2)} kt"
        self.sm.current_screen.ids['winddirection_id'].value = round(a2)
        self.sm.current_screen.ids['winddirection_id_old'].text = f"Winddirection: {convert_to_winddirection(a2)}"

if __name__ == "__main__":
    DemoApp().run()
