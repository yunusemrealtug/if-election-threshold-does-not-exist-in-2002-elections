from selenium import webdriver
from bs4 import BeautifulSoup
import PyPDF2

driver = webdriver.Chrome()

link="https://www.ysk.gov.tr/doc/dosyalar/docs/2002MilletvekiliSecimi/turkiye/Cevre/duzce.htm"


cities=["Adana","Adiyaman","Afyon","Agri","Amasya","Ankara1","Ankara2","Antalya","Artvin","Aydin","Balikesir","Bilecik","Bingol","Bitlis","Bolu","Burdur","Bursa","Canakkale","Cankiri","Corum","Denizli","Diyarbakir","Edirne","Elazig","Erzincan","Erzurum","Eskisehir","Gaziantep","Giresun","Gumushane","Hakkari","Hatay","Isparta","Istanbul1","Istanbul2","Istanbul3","Izmir1","Izmir2","Kahramanmaras","Kars","Kastamonu","Kayseri","Kirklareli","Kirsehir","Kocaeli","Konya","Kutahya","Malatya","Manisa","Mardin","Mersin","Mugla","Mus","Nevsehir","Nigde","Ordu","Rize","Sakarya","Samsun","Sanliurfa","Siirt","Sinop","Sivas","Tekirdag","Tokat","Trabzon","Tunceli","Usak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman","Kirikkale","Batman","Sirnak","Bartin","Ardahan","Igdir","Karabuk","Kilis","Yalova","Osmaniye","Duzce"]
cities=[x.lower() for x in cities]
dict2={"dsp":0, "dehap":0,"yurt":0,"mhp":0,"dyp":0,"mp":0,"bbp":0,"anap":0,"ldp":0,"saadet":0,"btp":0,"odp":0,"tkp":0,"gp":0,"ip":0,"chp":0,"akp":0,"ytp":0,"bagimsiz":0}
independents=["bayburt", "bitlis","elazig","hakkari","igdir","mardin","siirt","sanliurfa","sirnak"]
list2=["dsp", "dehap","yurt","mhp","dyp","mp","bbp","anap","ldp","saadet","btp","odp","tkp","gp","ip","chp","akp","ytp","bagimsiz"]
for num in range(85):
    city=cities[num]
    preCity=cities[num-1]
    link=link.replace(preCity, city)
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    votes = soup.find_all('td', class_="xl24", align="right")
    votes1=soup.find_all('tr', height="17", style="height:12.75pt")
    totalvotes=int(votes1[6].find_all('td')[3].text.replace(".",""))
    delegatesAmo=int(votes1[7].find_all('td')[3].text)
    dict1={"dsp":0, "dehap":0,"yurt":0,"mhp":0,"dyp":0,"mp":0,"bbp":0,"anap":0,"ldp":0,"saadet":0,"btp":0,"odp":0,"tkp":0,"gp":0,"ip":0,"chp":0,"akp":0,"ytp":0,"bagimsiz":0}
    if cities[num]=="erzurum":
        numa=12
        for index in range(19):
            if (list2[index]=="odp"):
                continue
            else:
                dict1[list2[index]]=int(votes1[numa].find_all('td')[3].text.replace(".",""))
                numa+=1
    else:
        for index in range(19):
            dict1[list2[index]]=int(votes1[index+12].find_all('td')[3].text.replace(".",""))
    if city not in independents:
        for index in range (16, 14, -1):
            totalNum=0
            divident=0
            calc2=dict1[list2[index]]
            equals=-1
            while (totalNum<delegatesAmo):
                totalNum=0
                divident+=1
                equals=-1
                for index2 in range (16,14, -1):
                    calc1=(dict1[list2[index2]]*divident)
                    totalNum+=calc1//calc2
                    if calc1%calc2==0:
                        equals+=1
            if totalNum==delegatesAmo:
                for index2 in range (16,14, -1):
                    calc1=(dict1[list2[index2]]*divident)
                    dict2[list2[index2]]+=calc1//calc2
                    print(list2[index2]+" gets "+str(calc1//calc2)+" delegates in "+cities[num])
                break
            elif totalNum<=delegatesAmo+equals:
                for index2 in range (16,14, -1):
                    calc1=(dict1[list2[index2]]*divident)
                    delegateAmount=calc1//calc2
                    if equals>0 and calc1%calc2==0:
                        dict2[list2[index2]]+=(delegateAmount)
                        equals-=1
                        if (delegateAmount>0):
                            print(list2[index2]+" gets doubtful delegate in "+ cities[num])
                    else:
                        if delegateAmount>0:
                            dict2[list2[index2]]+=delegateAmount-1
                            print(list2[index2]+" could not get doubtful delegate in "+ cities[num])


                
                break
    """else:
        bmax=dict1[list2[-1]]
        bmin=0
        base=0
        for index in range (16, 14, -1):
            totalNum=0
            divident=0
            calc2=dict1[list2[index]]
            equals=-1
            while (totalNum<delegatesAmo):
                totalNum=0
                divident+=1
                equals=-1
                for index2 in range (16,14, -1):
                    calc1=(dict1[list2[index2]]*divident)
                    totalNum+=calc1//calc2
                    if calc1%calc2==0:
                        equals+=1
            if totalNum<=delegatesAmo+equals:
                bmin=calc2/divident
                break
        for index in range (16, 14, -1):
            totalNum=0
            divident=0
            calc2=dict1[list2[index]]
            equals=-1
            while (totalNum<delegatesAmo):
                totalNum=0
                divident+=1
                equals=-1
                for index2 in range (16,14, -1):
                    calc1=(dict1[list2[index2]]*divident)
                    totalNum+=calc1//calc2
                    if calc1%calc2==0:
                        equals+=1
            if totalNum<=delegatesAmo+equals:
                base=calc2/divident
                break
        if base>bmax:
            for index in range (16, 14, -1):
                totalNum=0
                divident=0
                calc2=dict1[list2[index]]
                equals=-1
                while (totalNum<delegatesAmo):
                    totalNum=0
                    divident+=1
                    equals=-1
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        totalNum+=calc1//calc2
                        if calc1%calc2==0:
                            equals+=1
                if totalNum==delegatesAmo:
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        dict2[list2[index2]]+=calc1//calc2
                    break
                elif totalNum<=delegatesAmo+equals:
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        delegateAmount=calc1//calc2
                        if equals>0 and calc1%calc2==0:
                            dict2[list2[index2]]+=(delegateAmount)
                            equals-=1
                            if (delegateAmount>0):
                                print(list2[index2]+" gets doubtful delegate in "+ cities[num])
                        else:
                            if delegateAmount>0:
                                dict2[list2[index2]]+=delegateAmount-1
                                print(list2[index2]+" could not get doubtful delegate in "+ cities[num])
                    break
        elif base<bmin:
            dict2[list2[-1]]+=1
            for index in range (16, 14, -1):
                totalNum=0
                divident=0
                calc2=dict1[list2[index]]
                equals=-1
                delNum=delegatesAmo-1
                while (totalNum<delNum):
                    totalNum=0
                    divident+=1
                    equals=-1
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        totalNum+=calc1//calc2
                        if calc1%calc2==0:
                            equals+=1
                if totalNum==delNum:
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        dict2[list2[index2]]+=calc1//calc2
                    break
                
                elif totalNum<=delNum+equals:
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        delegateAmount=calc1//calc2
                        if equals>0 and calc1%calc2==0:
                            dict2[list2[index2]]+=(delegateAmount)
                            equals-=1
                            if (delegateAmount>0):
                                print(list2[index2]+" gets doubtful delegate in "+ cities[num])
                        else:
                            if delegateAmount>0:
                                dict2[list2[index2]]+=delegateAmount-1
                                print(list2[index2]+" could not get doubtful delegate in "+ cities[num])
                    break
        else:
            dict2[list2[-1]]+=1
            for index in range (16, 14, -1):
                totalNum=0
                divident=0
                calc2=dict1[list2[index]]
                equals=-1
                delNum=delegatesAmo
                while (totalNum<delNum):
                    totalNum=0
                    divident+=1
                    equals=-1
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        totalNum+=calc1//calc2
                        if calc1%calc2==0:
                            equals+=1
                if totalNum==delNum:
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        dict2[list2[index2]]+=calc1//calc2
                    dict2[list2[index]]-=1
                    print(list2[index]+" could not get doubtful delegate in due to lack of information "+cities[num])
                    break
                
                elif totalNum<=delNum+equals:
                    for index2 in range (16,14, -1):
                        calc1=(dict1[list2[index2]]*divident)
                        delegateAmount=calc1//calc2
                        if equals>0 and calc1%calc2==0:
                            dict2[list2[index2]]+=(delegateAmount)
                            equals-=1
                            if (delegateAmount>0):
                                print(list2[index2]+" gets doubtful delegate in "+ cities[num])
                        else:
                            if delegateAmount>0:
                                dict2[list2[index2]]+=delegateAmount-1
                                print(list2[index2]+" could not get doubtful delegate in "+ cities[num])"""

        
print(dict2)





            
                




    


    
