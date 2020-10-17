import os
import re

test_series = "Billions.S01E02.Naming.Rights.1080p.AMZN.WEBRip.DD5.1.x264-NTb"
test_movie = "Anna.2019.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTG"


r_series = '^(?P<series_name>\S+).S(?P<season>\d{2})E(?P<episode>\d{2}).(?P<episode_name>\S+).1080p'
r_movies = '^(?P<name>\S+).(?P<year>\d{4})'

class cleaner:
  def __init__(self, filename):
    self.filename = filename

  def get_name_series(self):
    result = re.search(r_series, self.filename)

    series_name = result.group("series_name")
    season = result.group("season")
    episode = result.group("episode")
    episode_name = result.group("episode_name")

    array = [series_name, season, episode, episode_name]

    return array

  def get_name_movie(self):
    result = re.search(r_movies, self.filename)

    name = result.group("name")
    year = result.group("year")
    
    array = [name, year]

    return array

run = Cleaners()
print(run.get_name_series())
print(run.get_name_movie())