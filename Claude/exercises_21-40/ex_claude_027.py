# Build a REST API for a music catalog using FastAPI and SQLite. No frontend — everything is tested through /docs or curl.

# GET /songs — returns all songs
# GET /songs/{id} — returns one song by ID, returns 404 if not found
# POST /songs — adds a new song
# DELETE /songs/{id} — deletes a song by ID
# GET /health — returns status message and total song count

from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel

class SongModel(BaseModel):
    song: str
    album: str
    artist: str

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("MusicsAPI.db")
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS musics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        song TEXT,
        album TEXT,
        artist TEXT
    )""")
        self.connection.commit()
        self.connection.close()

    def list_all(self):
        connection = sqlite3.connect("MusicsAPI.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM musics")
        total = cursor.fetchall()
        connection.close()
        return total

    def find_by_id(self,sid):
        connection = sqlite3.connect("MusicsAPI.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM musics WHERE id = ?", (sid, ))
        song = cursor.fetchone()
        connection.close()
        return song

    def add(self, n_song, n_album, n_artist):
        connection = sqlite3.connect("MusicsAPI.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO musics (song, album, artist) VALUES (?,?,?)", (n_song, n_album, n_artist))
        connection.commit()
        connection.close()

    def delete(self, sid):
        connection = sqlite3.connect("MusicsAPI.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM musics WHERE id = ?", (sid, ))
        connection.commit()
        connection.close()

    def song_count(self):
        connection = sqlite3.connect("MusicsAPI.db")
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM musics")
        count = cursor.fetchone()[0]
        connection.close()
        return count

db = DataBase()
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the SONG API"}

@app.get("/songs")
def songs():
    lis = []
    song_list = db.list_all()
    for i in song_list:
        dic = {"ID" : i[0], "song" : i[1], "album" : i[2], "artist" : i[3]}
        lis.append(dic)
    return lis

@app.get("/songs/{sid}")
def song_id(sid : int):
    song = db.find_by_id(sid)
    if not song:
        raise HTTPException(status_code = 404, detail = "Song not found")
    return {"ID" : song[0], "song" : song[1], "album" : song[2], "artist" : song[3]}

@app.post("/songs")
def add_song_api(song: SongModel):
    db.add(song.song, song.album, song.artist)
    return {"message": "Song added"}

@app.delete("/songs/{sid}")
def delete_song(sid : int):
    song = db.find_by_id(sid)
    if not song:
        raise HTTPException(status_code = 404, detail = "Song not found")
    db.delete(sid)
    return {"delete" : f"{song[1]} deleted"}

@app.get("/health")
def health():
    count = db.song_count()
    return {"status" : f"API RUNNING CORRECTLY {count} SONGS IN DATA BASE"}
