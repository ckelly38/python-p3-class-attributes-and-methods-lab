class Song:
    allsongs = [];
    count = 0;
    genres = [];
    artists = [];
    genre_count = {};
    artist_count = {};

    def __init__(self, nm, atst, gnre):
        self.name = nm;
        self.artist = atst;
        self.genre = gnre;
        Song.incrementTotalSongs();
        Song.addSongToList(self);
        Song.addArtistAndGenreToCount(self);
    
    @classmethod
    def addSongToList(cls, self):
        cls.allsongs.append(self);
        cls.artists.append(self.artist);
        cls.genres.append(self.genre);
        #print(f"added self.name={self.name} self.genre={self.genre} and self.artist={self.artist}");

    @classmethod
    def getTotalsSongs(cls): return cls.count;

    @classmethod
    def incrementTotalSongs(cls, incby=1):
        if (type(incby) == int): cls.count += incby;
        else: print("incby must be an integer!");

    @classmethod
    def addGenreOrArtistToDict(cls, self, mydict, usegenres):
        mgenkeys = mydict.keys();
        addit = True;
        for mky in mgenkeys:
            if (usegenres):
                if (self.genre == mky):
                    addit = False;
                    break;
            else:
                if (self.artist == mky):
                    addit = False;
                    break;
        fky = None;
        if (usegenres): fky = self.genre;
        else: fky = self.artist;
        if (addit): mydict.update({fky: 1});
        else: mydict.update({fky: (mydict[fky] + 1)});
        return mydict;

    @classmethod
    def addArtistAndGenreToCount(cls, self):
        cls.genre_count = cls.addGenreOrArtistToDict(self, cls.genre_count, True);
        cls.artist_count = cls.addGenreOrArtistToDict(self, cls.artist_count, False);


#pkrfc = Song("Poker Face", "Lady Gaga", "Pop");
#print(pkrfc.artists);
#print(pkrfc.genres);
#print(f"pkrfc.artist_count = {pkrfc.artist_count}");
#print(f"pkrfc.genre_count = {pkrfc.genre_count}");
#nwsng = Song("Song", "Jay Z", "Pop");
#print(nwsng.artists);
#print(nwsng.genres);
#print(f"nwsng.artist_count = {nwsng.artist_count}");
#print(f"nwsng.genre_count = {nwsng.genre_count}");
#print(pkrfc.artists);
#print(pkrfc.genres);
#print(f"pkrfc.artist_count = {pkrfc.artist_count}");
#print(f"pkrfc.genre_count = {pkrfc.genre_count}");
