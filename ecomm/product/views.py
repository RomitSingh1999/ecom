from django.shortcuts import render,redirect
import requests
import bs4
#x = input("book name:")


def compare(request):
    product_name=""
    product_price=""
    shopclues_p=""
    shopclues_pr=""
    amazon_p=""
    amazon_pr=""
    if request.method =='POST':
        
        try:
            product = request.POST['compare']
            x= str(product)
            x="+".join(x.split(" "))
            flipkart_url="https://www.flipkart.com/search?q="+str(x)+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
            res= requests.get(flipkart_url)
            soup= bs4.BeautifulSoup(res.content, 'html5lib')
            soupi= soup.find_all('div',class_="_3wU53n")
            product_name = soupi[0].text
            soup=soup.find('div', class_="_1vC4OE _2rQ-NK")
            product_price = soup.text

        except:
            product_name="NOt Found"
            product_price=""
        try:
            product = request.POST['compare']        
            x=product
            x=x.split(' ')
            x="%20".join(x)
            new_url = "https://www.shopclues.com/search?q="+str(x)+"&auto_suggest=1&seq=2&type=keyword&token=Moto%20e&count=10&z=0"

            res= requests.get(new_url)
            soup= bs4.BeautifulSoup(res.content, 'html5lib')
            soup= soup.find_all('div',class_='column col3 search_blocks')[0]
            data=soup.a
            product= soup.a.h2.text
            shopclues_p = product
            shopclues_pr = data.find('span',class_='p_price').text
        except:
            shopclues_p="NOt Found"
            shopclues_pr=""
        try:
            product = request.POST['compare']
            x=product        
            x=x.split(" ")
            x="+".join(x)
            tata_url="https://www.amazon.in/s?k="+str(x)+"&ref=nb_sb_noss_2"
            header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
            res= requests.get(tata_url,headers = header)
            soup= bs4.BeautifulSoup(res.content, 'html5lib')
            soup=soup.find_all('div',class_="a-section a-spacing-medium")
            i=soup[0]
            name=i.find('span',class_="a-size-medium a-color-base a-text-normal")
            amazon_p=name.text
            price=i.find('span',class_="a-price-whole")
            amazon_pr=price.text
        except:
            amazon_p="NOt Found"
            amazon_pr=""    

    
    return render(request, 'base.html',{'product_name':product_name,'product_price':product_price,'shopclues_p':shopclues_p,
                    'shopclues_pr':shopclues_pr,'amazon_p':amazon_p,'amazon_pr':amazon_pr})