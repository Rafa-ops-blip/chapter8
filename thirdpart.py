#8.6 City Names
def city_country(city_name, country_name):
  """Return a formatted city and country"""
  return f"\n{city_name.title()}, {country_name.title()}"


print(city_country("chongqing", "china"))
print(city_country("mumbai", "india"))
print(city_country("lagos", "nigeria"))



#8.7 Album
def make_album(artist_name, album_title, num_of_songs=None):
  """Return a dictionary of information about an album"""
  album = {"artist": artist_name, "title": album_title}
  if num_of_songs:
    album["num_of_songs"] = num_of_songs
  return album


print(make_album("rihanna", "diamonds"))
print(make_album("halle", "angel"))
print(make_album("rihanna", "diamonds", num_of_songs=50))

while True:
  print("\nEnter album details")
  print("enter 'q' at any time to quit")

  artist_name = input("Artist: ")
  if artist_name.lower() == "q":
    break

  album_title = input("Album_title: ")
  if album_title.lower() == "q":
    break

  album = make_album(artist_name, album_title)
  print(album)




