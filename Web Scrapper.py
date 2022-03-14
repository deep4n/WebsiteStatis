# Import package requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup

# Request ke Website
page = requests.get("https://republika.co.id/")

# Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text,'html.parser');

print ('\nMenampi1kan title browser') 
print ('=====================================')
print (obj.title.text)

print ('\nMenampilkan semua teks headline')
print ('=================================')
for headline in obj.find_all('div',class_='conten1'):
    print (headline.find('h2').text)
    
print('\nMenampilkan kategori')
print('======================')
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

print('\nMenampilkan waktu publish')
print('===========================')
for publish in obj.find_all('div',class_='date'):
        print(publish.text)    

print('\nMenampilkan waktu scrapping')
print('=============================')        
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Time = ", current_time)

# Import Package Json
import json
# Deklarasi list kosong
data=[]
# Lokasi file json
f=open('E:\Hasil.json','w')
for publish in obj.find_all('div',class_='conten1'):   
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktu_publish":publish.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()