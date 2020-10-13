from bs4 import BeautifulSoup
import requests
import json as js
json={}
l = ["depression","postpartum-depression","anxiety","psychosis","bipolar","eating-disorder","ptsd","parent","youth","addiction-test","work-health-survey"]

for url in l:
    URL = "https://screening.mhanational.org/screening-tools/"+url
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    try:
        for k in range(1,20):
            table = soup.find('fieldset', attrs = {'id':'edit-q'+str(k)+'--wrapper'})
            print(url)
            for i in (table.findNext('span', attrs = {'class':'fieldset-legend js-form-required form-required'})):
                # print(i)
                ques = i
            dic = {}
            lis =[]

            for  i in range(6):
                flag =0
                try:
                    for j in (table.findNext('label', attrs = {'for':'edit-q'+str(k)+'-'+str(i)})):
                        if(flag==0):
                            flag=1
                            continue
                        flag=0
                        # print(j)
                        d = dict()
                        d[j] =0
                        lis.append(d)
                except:
                    pass
            json[ques]  = lis

    except:
        pass
print(js.dumps(json, indent=4))
