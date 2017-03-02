import webbrowser
class Movie():
    def __init__(self,moivetitle,moivestoryline,poster_image,trailer_youtube):
        
        self.title=moivetitle
        self.storyline=moivestoryline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
       
        
        
