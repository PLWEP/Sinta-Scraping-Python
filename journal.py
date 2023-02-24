class Journal :
    
    def __init__(self, judul_jurnal, link_jurnal, affiliation, google_scholar, website, editor, p_issn, e_issn, subject_area, sinta, scopus, garuda, garuda_link):
        self.judul_jurnal = judul_jurnal
        self.link_jurnal = link_jurnal
        self.affiliation = affiliation
        self.google_scholar = google_scholar
        self.website = website
        self.editor = editor
        self.p_issn = p_issn
        self.e_issn = e_issn
        self.subject_area = subject_area
        self.sinta = sinta
        self.scopus = scopus
        self.garuda = garuda
        self.garuda_link = garuda_link

    def get_all_attributes(self):
        return [self.judul_jurnal, self.link_jurnal, self.affiliation, self.google_scholar, self.website, self.editor, self.p_issn, self.e_issn, self.subject_area, self.sinta, self.scopus, self.garuda, self.garuda_link]
