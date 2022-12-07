import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            payload = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(payload)
        elif format == 'XML':
            song_element = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_element, 'title')
            title.text = song.title
            artist = et.SubElement(song_element, 'artist')
            artist.text = song.artist
            return et.tostring(song_element, encoding='unicode')
        else:
            raise ValueError(format)


song = Song('1', 'Cittello on the Road', 'Peppy')
serializer = SongSerializer()
serializer.serialize(song, 'JSON')
serializer.serialize(song, 'XML')
serializer.serialize(song, 'YAML')

