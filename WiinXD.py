import mechanize

import facebook

import time

# Browser

br = mechanize.Browser()

# Browser settings

br.set_handle_equiv( True )

br.set_handle_gzip( True )

br.set_handle_redirect( True )

br.set_handle_referer( True )

br.set_handle_robots( False )

br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]

br.open("https://www.facebook.com/")

br.geturl()

print ("[+] TH3 R0Y4L H3R0S RULEX B0II  [+]")

print ("[+] TH3 SURY4 [+]")

msg=str(input("Enter your Token : "))

poct=str(input("Enter your post Link : "))

token=msg

def auto_post():

 

 while True:

    graph = facebook.GraphAPI(access_token=token,version='2.8')

    

    graph.put_object(parent_object= poct, connection_name='comments',message='#_SURY4_H3R3')

    print ("han chla gya comment!\n")

    time.sleep(200)

    

    graph.put_object(parent_object=poct, connection_name='comments',message='#__SURY4_H3R3')

    print ("han chla gya comment!\n")

    time.sleep(200)

    graph.put_object(parent_object=poct, connection_name='comments',message='#__SURY4__H3R3')

    print ("han chla gya comment!\n")

    time.sleep(200)

    graph.put_object(parent_object=poct, connection_name='comments',message='#_SURY4_H3R3')

    print ("han chla gya comment!\n")

    time.sleep(200)

    

if __name__ == '__main__':

    auto_post()

    print ("han chla gya comment!\n")

#Code agar copy krte ho to nam mt htana made by surya
