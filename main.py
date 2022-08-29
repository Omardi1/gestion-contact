
import sqlite3 

def add_contact():
      nom = input("entrer non...?")
      prenom= input("entrer prenom...?")
      email = input("entrer email...?")
      adresse = input("entrer adresse...?")
      numero = int(input("entrer numero...?"))
       
       
      conn = sqlite3.connect('mabase.sqlite3')
      cur = conn.cursor()
      sql =("""insert into contact (nom,prenom,email,adresse,numero) values(?,?,?,?,?)""")
      values = (nom, prenom,email, adresse, numero)
      cur.execute(sql, values )
      conn.commit()
      print("contact ajoute..")
      conn.close()
    
add_contact()
########################################
#supprime un contact    
def delete_contact():
  ma_id = int(input("choisir un contact a supprime..."))
    
  conn = sqlite3.connect('mabase.sqlite3')
  c = conn.cursor()
  sql_delete_query= """delete from contact where id= ? """
  c.execute(sql_delete_query, (ma_id,))
  conn.commit()
  print("contact supprime", ma_id)
  conn.close()
 
delete_contact()

####modiffie un contact

def udate_contact():
  ma_id = input("choisir un id...")
  nom = input("veiller entrer le  nom a modifier...? ")
  prenom = input("veiller le prenom a modifier...?")
  email = input("veiller entrer email a modifier..?")
  adresse = input("veiller entrer l'adresse a modifier...?")
  numero = input("veiller entrer le numero a modifier...?")
  
  conn = sqlite3.connect('mabase.sqlite3')
  c = conn.cursor()
  sql_update_query = """update contact set nom=?,
  prenom=?,
  email=?,
  adresse=?,
  numero=?
  where id=?
    """
  values = (nom, prenom,email, adresse, numero,ma_id)
  c.execute(sql_update_query, values)
  conn.commit()
  print("id a modifier",  ma_id)
  conn.close() 
    
udate_contact()  
  
####aficher tous les contacts  
def show_all_contac():
    conn = sqlite3.connect('mabase.sqlite3')
    c = conn.cursor()
    
    c.execute("select rowid, * from contact")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()
show_all_contac()
    
    