from flask import Flask, request, render_template 
from scrapper import scrapall
  
app = Flask(__name__)   
  
@app.route('/', methods = ["GET", "POST"])
def display_name():
   if request.method == "POST":
      product = request.form.get("product")
      message =  "Showing results for: '" + product + "'<br/><br/>"
      # print(scrapall(product))
      items = map(lambda x: str(x) + '<br/>', scrapall(product))
      itemslist=[]
      for i in scrapall(product):
         # itemslist.append(str(i))
         li=[]
         li=list(str(i).split("<br/>"))
         dic={}
         dic["itemName"]=li[0]
         dic["itemRate"]=li[1]
         dic["itemLink"]=li[2]
         dic["itemImage"]=li[3]
         itemslist.append(dic)
      # itemslist = map(lambda x: itemslist.append(str(x)) , scrapall(product))
      print(itemslist)
      if items:
         return render_template("index.html", itemslist=itemslist)
         # return message + '<br/>'.join(items)
         # return message + ''.join(items)
      return message + '<br/>' + "No items found."
   return render_template("index.html")
  
if __name__ == '__main__':
   app.run()