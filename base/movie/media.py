# coding=utf-8
import webbrowser


class Video:
    def __init__(self, movie_title, poster_image, trailer_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_url = trailer_url


class Movie(Video):
    def __init__(self, movie_title, poster_image, trailer_url, movie_storyline):
        """
        重写方法，这部分都是按照视频里来的，既然已经跟着视频里实现这个类了就没有再重新写。
        :param movie_title: string
        :param poster_image: string
        :param trailer_url: string
        :param movie_storyline: string
        """
        Video.__init__(self, movie_title, poster_image, trailer_url)
        self.storyline = movie_storyline

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
