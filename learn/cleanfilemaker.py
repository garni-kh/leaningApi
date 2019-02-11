import mysql.connector
from bs4 import BeautifulSoup
from learn import LEARN_TEXT
from cleanfilemaker import red


def conection():

     w = mysql.connector.connect(
         user='santuser', host='localhost', password='garni09121332015', database='contact')
     return w



def saveunicworld():
    quary = "select note from comment"
    conn = conection()
    nevesht = conn.cursor()
    nevesht.execute(quary)
    rows = nevesht.fetchall()
    nevesht.close()
    conn.close()
    lololo=[]
#    outF = open(LEARN_FOLDER + "/" + "comments9.txt", "w")
    for i in rows:
        if i[0] != None:
            cleantext = BeautifulSoup(i[0], "lxml").text
            cleantext1 = cleantext.replace("\n", " ")
            cleantext2 = cleantext1.replace("\rr", " ")
            cleantext3 = cleantext2.replace(" \n", " ")
            cleantext4 = cleantext3.replace("\n ", " ")
            cleantext5 = cleantext4.replace(" \n ", " ")
            cleantext6 = cleantext5.replace("\\n", " ")
            cleantext7 = cleantext6.replace("\r", " ")
            cleantext8 = cleantext7.replace("\\", " ")
            cleantext9 = cleantext8.replace("\\", " ")
            cleantext10 = cleantext9.replace('""p ', " ")
            cleantext11 = cleantext10.replace(' ""p', " ")
            cleantext12 = cleantext11.replace(' "p', " ")
            cleantext13 = cleantext12.replace('"p ', " ")
            cleantext14 = cleantext13.replace(' "', " ")
            cleantext15 = cleantext14.replace(' "p ', " ")
            cleantext16 = cleantext15.replace("ـ ", " ")
            cleantext17 = cleantext16.replace(') ', " ")
            cleantext18 = cleantext17.replace('( ', " ")
          
            cleantext19 = cleantext18.replace("! ", " ")
            cleantext20 = cleantext19.replace(" !", " ")
            cleantext21 = cleantext20.replace("٪ ", " ")
            cleantext22 = cleantext21.replace(" ٪", " ")
            cleantext23 = cleantext22.replace(" ؟", " ")
            cleantext24 = cleantext23.replace("؟ ", " ")
            cleantext25 = cleantext24.replace("<br>", " ")
            cleantext26 = cleantext25.replace("= ", " ")
          
            cleantext27 = cleantext26.rstrip()




#            outF.write(cleantext27)
#            outF.write(" ")
            cleantext28 = cleantext27.split(" ")
            a = cleantext28
            
            
              
            lololo.append(a)
            print(a)
#    outF.close()
    lop = sum(lololo, [])
    unicword=set(lop)
    for i in unicword:
        red.sadd("words22", i)
    print(len("in redis save:"+ unicword))

#saveunicworld() 
