class Article :
    
    def __init__(self, judul_artikel, link_artikel, affiliation, publikasi, tahun):
        self.judul_artikel = judul_artikel
        self.link_artikel = link_artikel
        self.affiliation = affiliation
        self.publikasi = publikasi
        self.tahun = tahun

    def get_all_attributes(self):
        return [self.judul_artikel, self.link_artikel, self.affiliation, self.publikasi, self.tahun]