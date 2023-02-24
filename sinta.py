import requests
from bs4 import BeautifulSoup
from journal import Journal
from article import Article

class Sinta : 
    url = 'https://sinta.kemdikbud.go.id/'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
    }

    def getAllJournal(self) :
        datas = []
        halaman = 0

        for i in range(1, 806) :
            halaman += 1
            print("Halaman : ", halaman )
            req = requests.get(self.url+'journals?page='+str(halaman), headers=self.headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            items = soup.find_all('div', 'col-lg meta-side')

            for it in items:
                # Crawl
                header = it.find('div', 'affil-name mb-3')
                link = it.select('div.affil-abbrev a')
                profile = it.find('div', 'profile-id')
                arr_profile = profile.text.strip().split('\n')
                indexed = it.find('div', 'stat-prev mt-2')

                # variable
                judul_jurnal = header.text.strip()
                link_jurnal = header.find('a')['href']
                affiliation = it.find('div', 'affil-loc mt-2').text.strip()
                google_scholar_link = link[0]['href']
                website_link = link[1]['href']
                editor_url = link[2]['href']
                p_issn = arr_profile[0].replace(' ', '')
                e_issn = arr_profile[1].replace(' ', '')
                try : subject_area = arr_profile[2].replace(' ', '').replace('SubjectArea:', '')
                except : subject_area = ''
                try : sinta = it.find('span', 'num-stat accredited').text
                except : sinta = 'Tidak Terindex'
                try : scopus = it.find('span', 'num-stat scopus-indexed ml-3').text
                except : scopus = 'Tidak Terindex'
                try : garuda = it.find('span', 'num-stat garuda-indexed ml-3').text
                except : garuda = 'Tidak Terindex'
                try : garuda_link = indexed.find_all('a')[1]['href']
                except : garuda_link = '-'
                
                # add data
                datas.append(Journal(judul_jurnal, link_jurnal, affiliation, google_scholar_link, website_link, editor_url, p_issn, e_issn, subject_area, sinta, scopus, garuda, garuda_link))
        
        return datas

    def getJournalWithQuery(self, query) :
        try :
            req = requests.get(self.url+'journals?page=1'+'&q='+query, headers=self.headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            total_halaman = soup.find('div', 'text-center pagination-text').text
            if total_halaman[11] != ' ' :
                if total_halaman[12] != ' ' :
                    total_halaman = total_halaman[10] + total_halaman[11] + total_halaman[12]
                else : 
                    total_halaman = total_halaman[10]
            else :
                total_halaman = total_halaman[10]
        except :
            total_halaman = 0
        datas = []
        halaman = 0

        for i in range(1, int(total_halaman)+ 1) :
            halaman += 1
            print("Halaman : ", halaman )
            req = requests.get(self.url+'journals?page='+str(halaman)+'&q='+query, headers=self.headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            items = soup.find_all('div', 'col-lg meta-side')

            for it in items:
                # Crawl
                header = it.find('div', 'affil-name mb-3')
                link = it.select('div.affil-abbrev a')
                profile = it.find('div', 'profile-id')
                arr_profile = profile.text.strip().split('\n')
                indexed = it.find('div', 'stat-prev mt-2')

                # variable
                judul_jurnal = header.text.strip()
                link_jurnal = header.find('a')['href']
                affiliation = it.find('div', 'affil-loc mt-2').text.strip()
                google_scholar_link = link[0]['href']
                website_link = link[1]['href']
                editor_url = link[2]['href']
                p_issn = arr_profile[0].replace(' ', '')
                e_issn = arr_profile[1].replace(' ', '')
                try : subject_area = arr_profile[2].replace(' ', '').replace('SubjectArea:', '')
                except : subject_area = ''
                try : sinta = it.find('span', 'num-stat accredited').text
                except : sinta = 'Tidak Terindex'
                try : scopus = it.find('span', 'num-stat scopus-indexed ml-3').text
                except : scopus = 'Tidak Terindex'
                try : garuda = it.find('span', 'num-stat garuda-indexed ml-3').text
                except : garuda = 'Tidak Terindex'
                try : garuda_link = indexed.find_all('a')[1]['href']
                except : garuda_link = '-'
                
                # add data
                datas.append(Journal(judul_jurnal, link_jurnal, affiliation, google_scholar_link, website_link, editor_url, p_issn, e_issn, subject_area, sinta, scopus, garuda, garuda_link))
        
        return datas

    def getJournalArticle(self, namaJurnal) :
        jurnal_data = self.getJournalWithQuery(namaJurnal)
        if len(jurnal_data) <= 0 :
            print("Terjadi kesalahan data tidak ditemukan")
        else :
            url = jurnal_data[0].link_jurnal 
            datas = []
            
            req = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            items = soup.find_all('div', 'ar-list-item mb-5')

            for it in items:
                # variable
                judul_artikel = it.find('div', 'ar-title').text.strip()
                link_artikel = it.find('a')['href']
                affiliation = it.find('div', 'ar-meta').text.strip()
                publikasi = it.find('a', 'ar-pub').text.strip()
                tahun = it.find('a', 'ar-year').text.strip()
                
                # add data
                datas.append(Article(judul_artikel, link_artikel, affiliation, publikasi, tahun))

            req = requests.get(url.replace('profile', 'google'), headers=self.headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            items = soup.find_all('div', 'ar-list-item mb-5')

            for it in items:
                # variable
                judul_artikel = it.find('div', 'ar-title').text.strip()
                link_artikel = it.find('a')['href']
                affiliation = it.find('div', 'ar-meta').text.strip()
                publikasi = it.find('a', 'ar-pub').text.strip()
                tahun = it.find('a', 'ar-year').text.strip()
                
                # add data
                datas.append(Article(judul_artikel, link_artikel, affiliation, publikasi, tahun))

            return datas



