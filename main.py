import kivy
from kivy.config import Config


Config.set('graphics', 'resizable', True)



from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
import webbrowser
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.clock import Clock

kivy.require("1.9.1")


import requests
import json
import csv

s = ""
f = open("mood_detector.csv")
reader = csv.reader(f)
feeling = list(reader)
print (feeling)
mood = []

for elem in feeling:
    mood.extend(elem)

print(mood)

link = '<a href = "https://www.who.int/publications/i/item/9789240003927?gclid=Cj0KCQiApsiBBhCKARIsAN["> here </a>'

link_work = link.format


with open('Bot_question.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

with open('hobbies.csv', mode='r') as inp:
    reader = csv.reader(inp)
    hobby = {rows[0]:rows[1] for rows in reader}


ambitions = {'doctor':"It's really good to treat patients and learn about the medical feild, Doctors are the ones who are there to save lives.", 'engineer':"Wow I am really interested to hear about it, I am a robot and I like it.",'Teacher':"Good to be a teacher and I like it","Fashion_designer":"That's really interesting, There are so many brands out there and who knows in the future, you might create a brand",'Accountant':"Being a professional accountant is really great It's being a high paying field now",'Architect':"Wow that's an amazing subject I really like it, drawing plans with AutoCAD and 3d from ArchiCAD is really demanding. It takes a while to study the symbols","pilot":"Wow such a responsible job and it's very cool, It's really good to be a pilot if you are not scared of heights \n I am really scared of heights"}
def get_prediction(data={"sentence": "I am so sad to see you go. "}):
    url = 'https://vowgpx28lc.execute-api.us-east-1.amazonaws.com/Predict/f32b0974-e96b-40fc-a967-874b2d20b22f'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r, '_content').decode("utf-8")

    return response

class Home(Screen):
    def website1(instance):
        webbrowser.open("http://www.1333.lk")

    def website2(instance):
        webbrowser.open("http://srilankasumithrayo.lk")


class Login(Screen):

    def login_save(self):
        global name
        global password
        name = self.ids.name_input.text
        name = name.title()
        password = self.ids.password.text
        if password or name == password.strip() and name.strip():
            name = self.ids.name_input.text
            password = self.ids.password.text
            self.ids.user.text = "Username"
            self.ids.user.color = (65/255,125/255,193/255,1)
            self.ids.passw.color = (65/255,125/255,193/255,1)
            self.ids.passw.text = "Password"
            return True

        else:
            self.ids.user.text = "Username **"
            self.ids.user.color = (1, 0, 0, 1)
            self.ids.passw.color = (1, 0, 0, 1)
            self.ids.passw.text = "Password **"
            return False

class Chat(Screen):

    def on_start(self):
        if self.ids.start_send.text == "send":
            self.send_button()
        elif self.ids.start_send.text == "start":
            self.ids.start_send.background_color = (73/255,0/255,195/255,1)
            Clock.schedule_once(self.start)
            Clock.schedule_once(self.next_two,3)
            Clock.schedule_once(self.focus,3)
            Clock.schedule_once(self.helpbar,3)

    def send_button(self):

        if self.ids.namelabel.text  == "good" or  self.ids.namelabel.text == "that's nice" or self.ids.namelabel.text == "cool" or self.ids.namelabel.text == "That's good" or self.ids.namelabel.text == "That's awesome!" or self.ids.namelabel.text == "that's awesome!" or self.ids.namelabel.text == "that's good":
            self.ids.namelabel.text = ""
            self.ids.showcolby.text ="Can you answer these questions for me to get to know a little bit about you?"
            self.focus()
            self.ids.helplabel.text = "Try telling :- 'ok'"
            self.ids.namelabel.text = ""
            self.ids.namelabel.focused = True


        elif self.ids.namelabel.text == "ok" or self.ids.namelabel.text == "yeah ok" or self.ids.namelabel.text == "ok sure" or self.ids.namelabel.text == "yeah sure" or self.ids.namelabel.text =="sure" or self.ids.namelabel.text == "I will":
            self.ids.namelabel.text = ""
            self.ids.showcolby.text = "What's your age?"
            self.focus()
            self.ids.helplabel.text = "please enter an integer number"



        elif self.ids.namelabel.text.isnumeric() == True:
            self.user_age = self.ids.namelabel.text
            birthyear = 2021 - int(self.user_age)
            self.ids.showcolby.text = f"ooh, then you were born in {birthyear}"
            self.ids.helplabel.text = ""
            Clock.schedule_once(self.feel,4)

        elif self.ids.namelabel.text == "I don't have a hobby" or self.ids.namelabel.text == "I hate hobbies" or self.ids.namelabel.text == "I didn't have a hobby" or self.ids.namelabel.text == "Hobbies are not for me" or self.ids.namelabel.text == "hobbies are not for me" or self.ids.namelabel.text == 'Nope' or self.ids.namelabel.text == "no, I don't have a hobby" or  self.ids.namelabel.text == "No, I don't have a hobby" or self.ids.namelabel.text == "no I don't have a hobby" or self.ids.namelabel.text == "Nope, I don't want to have a hobby" or self.ids.namelabel.text == "I don't like to have a hobby" or self.ids.namelabel.text == "Nope don't have a hobby" or self.ids.namelabel.text == "nope don't have a hobby" or self.ids.namelabel.text == "Nope, don't have a hobby" or self.ids.namelabel.text == "nope, don't have a hobby" or self.ids.namelabel.text == "I don't have any hobbies" or self.ids.namelabel.text == "I don't have a free time":
            self.ids.showcolby.text = "That's bad that you don't have a hobby. Having a hobby makes you feel better. It will make your mood!"
        elif self.ids.namelabel.text in mood:
            print(self.ids.namelabel.text, ":")
            ask_your_ai = {"sentence":self.ids.namelabel.text}
            prediction = get_prediction(ask_your_ai)
            #print(prediction)
            self.predicted_label = json.loads(json.loads(prediction)['body'])['predicted_label']
            print(self.predicted_label)

            if self.predicted_label == "lonely" or self.predicted_label == 'anger' or self.predicted_label == 'sad' or self.predicted_label == 'depressed' or self.predicted_label == 'anxiety':
                self.ids.showcolby.text = "To get out of this state of your mind \n You can listen to some cheerful music \n Watch movies \n Go for a walk "
                Clock.schedule_once(self.steps,8)

            elif self.predicted_label == "happy":
                self.ids.showcolby.text = "yay!"
                if int(self.user_age) < 18:
                    Clock.schedule_once(self.jhy, 4)

                else:
                    Clock.schedule_once(self.hobby, 4)

        elif self.ids.namelabel.text in ambitions.keys():
            ambi = self.ids.namelabel.text
            self.ids.showcolby.text = ambitions[ambi]
            self.ids.namelabel.text = ""
            Clock.schedule_once(self.hobby, 4)

        elif self.ids.namelabel.text == "oh":
            self.ids.showcolby.text = "hmmm! yeah"
            self.ids.helplabel.text = "ask COLBY: 'Can you laugh?'"

        elif self.ids.namelabel.text == "hmmm" or self.ids.namelabel.text == "Hmmm" or self.ids.namelabel.text == "hm" or self.ids.namelabel.text == "hmm":
            self.ids.showcolby.text = "yeah"
            self.ids.helplabel.text = "ask COLBY: 'Do you have any hobbies?'"

        elif self.ids.namelabel.text in dict_from_csv.keys():
            userin = self.ids.namelabel.text
            self.ids.showcolby.text = dict_from_csv[userin]

        elif self.ids.namelabel.text == "Hi" or self.ids.namelabel.text == "Hi!" or self.ids.namelabel.text == "hi":
            self.ids.showcolby.text = "Hello there!"

        elif self.ids.namelabel.text in hobby.keys():
            userhob = self.ids.namelabel.text
            self.ids.showcolby.text = hobby[userhob]
            if self.predicted_label == "lonely" or self.predicted_label == "anger" or self.predicted_label == 'sad' or self.predicted_label == 'depressed' or self.predicted_label == 'anxiety':
                Clock.schedule_once(self.pandeq, 4)

            elif self.predicted_label == "happy":
                self.ids.showcolby.text = "You can ask anything from me to make it more interesting!"
                Clock.schedule_once(self.hmqu,6)

        elif self.ids.namelabel.text == "Thankyou" or self.ids.namelabel.text == "thankyou" or self.ids.namelabel.text == "Thanks" or self.ids.namelabel.text == "thanks":
            self.ids.showcolby.text = "I am always here for you!"

        elif self.ids.namelabel.text == "yes" or self.ids.namelabel.text == "Yes" or self.ids.namelabel.text == "yeah" or self.ids.namelabel.text == "Yeah" or self.ids.namelabel.text == "I think so" or self.ids.namelabel.text == "yeah that's right" or self.ids.namelabel.text == "hmmm yes":
            self.ids.namelabel.text = ""
            self.ids.showcolby.text = "Don't worry this pandemic will be over soon in the future! Then you can be with your friends or relatives."
            Clock.schedule_once(self.suggest,4)
        elif self.ids.namelabel.text == "nope" or self.ids.namelabel.text == "not really" or self.ids.namelabel.text == "Nope, not really" or self.ids.namelabel.text == "no" or self.ids.namelabel.text == "Nope" or self.ids.namelabel.text == "No" or self.ids.namelabel.text == "Not really":
            self.ids.namelabel.text = ""
            self.ids.showcolby.text = "Ok that's good!"

        elif self.ids.namelabel.text == "wow" or self.ids.namelabel.text == "amazing" or self.ids.namelabel.text == "you're amazing":

            self.ids.showcolby.text = "yeah, thanks!"

        else:
            self.ids.showcolby.text = "I didn't get that, can you rephrase it?"
            Clock.schedule_once(self.user_Input,11)




    def steps(self,*args):
        self.ids.showcolby.text = "Don't worry I am here to make you happy."
        self.ids.namelabel.text = ""
        if int(self.user_age) < 18:
            Clock.schedule_once(self.jhy, 4)

        else:
            Clock.schedule_once(self.hobby,4)

    def feel(self, *args):
        self.ids.namelabel.text = ""
        self.ids.showcolby.text = "How are you feeling right now?"
    def user_Input(self, *args):
        self.ids.helplabel.text = "ask COLBY:'Can you suggest any games to play?'"
        Clock.schedule_once(self.suggest2,8)
    def suggest(self, *args):
        self.ids.namelabel.text = ""
        self.ids.showcolby.text = "You can talk to trained counsellors confidentially, Take a call to thsese numbers! \n sumithriyo: 0112682535 \n CCC: 1333"
        Clock.schedule_once(self.ask,4)
    def start(self, *args):
        self.ids.start_send.text = "send"
        self.ids.showcolby.text = ""
        self.ids.showcolby.text = f"Hi {name}, I am your personal chatbot, let me introduce myself..."
    def next(self, *args):
        self.ids.showcolby.text = ""
        self.ids.showcolby.text = "I am COLBY, I will speak with you and entertain you."
    def ask(self, *args):
        self.ids.showcolby.text = "You can ask anything from me to make it more interesting!"
        self.ids.helplabel.text = "ask COLBY:'Can you suggest any games to play?'"


    def jhy(self, *args):
        self.ids.showcolby.text = "What is your ambition?"
    def hmqu(self, *args):
        self.ids.showcolby.text = "You can ask anything from me to make it more interesting!"

    def suggest2(self,*args):
        self.ids.helplabel.text = "Ask COLBY: 'Do you have any hobby?'"

    def helpbar(self, *args):
        self.ids.helplabel.text = "Try saying :- 'good'"
    def pandeq(self, *args):
        self.ids.helplabel.text = ""
        self.ids.showcolby.text = "Do you think the pandemic has caused you to feel sad and lonely?"

    def next_two(self, *args):
        self.ids.showcolby.text = ""
        self.ids.showcolby.text = "I know some interesting facts and let's have fun!."

    def next_three(self, *args):
        self.ids.showcolby.text = ""
        self.ids.showcolby.text = "I will try my best to give you a smile!"
    def hobby(self, *args):
        self.ids.namelabel.text = ""
        self.ids.showcolby.text = ""
        self.ids.showcolby.text = f"Do you have any hobby? what is it {name}?"

    def focus(self, *args):
        self.ids.namelabel.focused = True

    def nonfocus(self,*args):
        self.ids.namelabel.focused = False



class WindowManager(ScreenManager):
    pass


LabelBase.register(name = 'Century Gothic',fn_regular= "Century Gothic 400.ttf")
LabelBase.register(name = 'Myriad CAD',fn_regular= "myriadcad.otf")
LabelBase.register(name = 'Calibri',fn_regular= "calibril.ttf")
LabelBase.register(name = 'Impact',fn_regular= "impact.ttf")
LabelBase.register(name = 'SolidWorks GDT',fn_regular= "solidworks gdt.ttf")
LabelBase.register(name = 'Segoe UI',fn_regular= "segoeui.ttf")
LabelBase.register(name = 'Comic Sans MS',fn_regular= "comic.ttf")
LabelBase.register(name = 'Segoe Print',fn_regular= "segoepr.ttf")
LabelBase.register(name = 'Helvetica Neue LT Std',fn_regular= "HelveticaNeueLTStd-Md.otf")
LabelBase.register(name = 'Papyrus',fn_regular= "PAPYRUS.TTF")
LabelBase.register(name = 'Artifakt Element',fn_regular= "Artifakt Element Regular.ttf")
LabelBase.register(name = "MV Boli",fn_regular= "mvboli.ttf")


KV = Builder.load_file('COLBY_design.kv')

Window.size = (400,650)

class chatbot(App):
    def on_pause(self):
        return True
    def password_check(self):
        Chat.ids.user.text = "Username"
        Chat.ids.user.color = (65 / 255, 125 / 255, 193 / 255, 1)
        Chat.ids.passw.color = (65 / 255, 125 / 255, 193 / 255, 1)
        Chat.ids.passw.text = "Password"

    def on_resume(self):
        if Chat.ids.namelabel.text != password and Chat.ids.namelabel.text != name:
            self.password_check()

        else:
            pass


    def build(self):
        Window.clearcolor = (81/255,255/255,246/255,1)

        return KV

if __name__ == "__main__":
    chatbot().run()
