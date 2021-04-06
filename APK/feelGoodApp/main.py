#you use python for the logic and kv for the graphics
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import glob
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
#this how python script will know about kv file rules
Builder.load_file('design.kv')

#Create class with same names as kv 

class LoginScreen(Screen):
    #to connect with kn sign up class
    #in kv files we use root.sign_up 
    def sign_up(self):
        #Too connect with SignUpScreen root
        self.manager.current = "sign_up_screen"
    def login(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password"
#self is instance manager is property if Screen,Screen is parent and LoginScreen is 
#and current finds "sign_up_screen" which is widget we created
class RootWidget(ScreenManager):
    pass
# we make this class so kn file can recognize SignUpScreen method
class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        #send to json file
        with open("users.json") as file:
            users = json.load(file)
        

        users[uname] = {'username': uname,'password' : pword,
        'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        print(users)

        with open("users.json",'w') as file:
            #to add new user data to json file,overwriting existing json file
            json.dump(users,file)
            self.manager.current = "sign_up_screen_success"
class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.direction = "right"
        self.manager.current = "login_screen"
    def get_quote(self,feel):
        feel= feel.lower()
        available_feelings = glob.glob("quotes/*txt")
    

        available_feelings = [Path(filename).stem for filename in
                                available_feelings ]
        print(available_feelings)

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
             self.ids.quote.text = "Try another feeling"
class  ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()       