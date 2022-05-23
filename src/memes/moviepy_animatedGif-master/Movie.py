from moviepy.editor import *

class Movie:

    def __init__(self):
        self.ScanDir()
        return None


    def ScanDir(self):
        with os.scandir('/Users/Jake/Desktop/Pymovie/videos/') as entries:
            for entry in entries:
                if(entry.name == '.DS_Store'):
                    continue
                self.CreateGif('/Users/Jake/Desktop/Pymovie/videos/'+entry.name)


    def CreateGif(self,FileName):

        Video = VideoFileClip(FileName)


        clip            = (VideoFileClip(FileName)
                            .subclip((0,1),(0,3))
                            .resize(0.3)
                            .set_duration(3))

        Duration        = self.CalcDuration(Video.duration)

        Text = (TextClip('Play '+str(Duration)+' Video',
                 fontsize=30, color='white',
                 font='Aller Regular', interline=-25)
        .set_pos((120,273))
        .set_duration(3))

        Logo = (ImageClip("/Users/Jake/Desktop/Pymovie/overlay/overlay.png")
          .set_duration(3))




        composition = CompositeVideoClip( [clip, Logo, Text] )
        composition.write_gif(FileName+".gif", fps=10, fuzz=2)

        #clip.write_gif(FileName+".gif")
    def CalcDuration(self,Duration):
        if(Duration <= 60):
            return str(int(round(Duration))) +" Second"
        if(Duration > 60):
            return str(int(round(Duration / 60,0)) ) +" Minute"


    def CreateOverlay(self,Filename):

        return None

Movie()
