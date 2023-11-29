from functools import partial

from pytube import YouTube
from kivymd.uix.relativelayout import  MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size=(1200,700)
class YTDownApp(MDApp):
    def getInfo(self,event,window):
        self.yt=YouTube(self.linkInput.text)
        self.yt.title="Jailer Trailer"
        self.titleLabel.text=self.yt.title
        print("Title: "+str(self.yt.title))
        self.downBtn.pos_hint={'center_x':0.5,'center_y':0.25}

    def downloadVid(self,event,layout):
        self.vid=self.yt.streams.get_highest_resolution()
        print("Downloading")
        self.vid.download()
        print("Downloaded")



    def build(self):
      layout=MDRelativeLayout(md_bg_color=[127/255, 186/255, 54/255])
      self.image=Image(source='yt.png',size_hint=(10,10),pos_hint={'center_x':.5,'center_y':0.8})
      self.linkLabel=Label(text="Please Enter the YouTube Link here",pos_hint={'center_x':0.5,'center_y':0.6},size_hint=(1,1),font_size=20,color=(1,1,1))
      self.linkInput=TextInput(text="",pos_hint={'center_x':0.5,'center_y':0.55},size_hint=(0.8,None),height=48,foreground_color=(255, 0, 0), font_size=29,font_name='Comic')
      self.button=Button(text="Get Link",pos_hint={'center_x':0.5,'center_y':0.45},size_hint=(0.2,0.1),background_color=(0,1,1),font_name='Comic',font_size=24)
      self.button.bind(on_press=partial(self.getInfo,layout))
      self.titleLabel=Label(text="",pos_hint={'center_x':0.5,'center_y':0.35},size_hint=(1,1),font_name='Comic',font_size=36,color=(1,1,1))
      self.downBtn=Button(text="Download",pos_hint={'center_x':0.5,'center_y':200},size_hint=(0.2,0.1),size=(75,75),background_color=(0,1,1),font_name='Comic',font_size=24)
      self.downBtn.bind(on_press=partial(self.downloadVid, layout))

      layout.add_widget(self.image)
      layout.add_widget(self.linkLabel)
      layout.add_widget(self.linkInput)
      layout.add_widget(self.button)
      layout.add_widget(self.titleLabel)
      layout.add_widget(self.downBtn)
      return layout

if __name__=='__main__':
    YTDownApp().run()

