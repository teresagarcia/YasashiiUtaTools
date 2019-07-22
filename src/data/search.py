from googlesearch import search 

query = "melovin Ты lyrics"
  
for i in search(query, tld="es", num=20, stop=25, pause=2): 
    print(i) 