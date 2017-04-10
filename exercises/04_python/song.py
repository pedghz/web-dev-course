import json

class Song:
   def __init__(self, track_id):
        self.artist = "file"
        self.title = "not found"
        self.timestamp = "-1"
        self.track_id = track_id
        self.tags = []
        self.similars = []
        try:
            with open('lastfm_subset/' + track_id[2] + '/' + track_id[3] + '/' + track_id[4] + '/'+track_id+'.json') as json_data:
                jsonFile = json.load(json_data)
                self.artist = jsonFile['artist']
                self.title = jsonFile['title']
                self.timestamp = jsonFile['timestamp']
                self.track_id = track_id
                self.tags = jsonFile['tags']
                self.similars = jsonFile['similars']
        except OSError:
            print('Cannot open this file:', track_id+'.json')

   def get_tags( self, limit = 0):
       tags = []
       for tag in self.tags:
           if (int(tag[1]) >= limit):
              tags.append(tag[0])
       return tags

   def get_similars( self, limit = 0):
       tags = []
       for similar in self.similars:
           if (float(similar[1]) >= limit):
              tags.append(similar[0])
       return tags

   def shared_tags( self, Song):
       shared_tags = []
       for tag1 in self.tags:
           for tag2 in Song.tags:
               if (tag2[0] == tag1[0]):
                  shared_tags.append(tag2[0])
       return tuple(shared_tags)

   def combined_tags( self, Song):
       combined_tags = []
       for tag in Song.tags:
           if (tag[0] not in combined_tags):
               combined_tags.append(tag[0])
       for tag in self.tags:
           if (tag[0] not in combined_tags):
               combined_tags.append(tag[0])
       return tuple(combined_tags)

