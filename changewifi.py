
import sys
import wifi_activate
filename = "/etc/wpa_supplicant/wpa_supplicant.conf" #file to be changed to add a network

def connect(name, password):
 key_mgmt = "WPA-PSK" #default type
 check= bool(True)
 
 # read the file and check SSID and Psk
 fh =open(filename,"r")
 for line in fh:
     split_list=line.split('"')
     if name in split_list:
          next_line= fh.next() 
          split_list_password=next_line.split('"')
	  if password in split_list_password:
		    print "Already configured"
		    check= False
		    break
 fh.close()

 # append to the config file if not configured already
 if check:
    Fh_append= open(filename,"a")
    string1 = "\nnetwork={\n"
    string2='     ssid="{s}"\n     psk="{p}"\n     key_mgmt={k}'.format(s= name,p= password,k= key_mgmt)
    string3="\n}\n\n"
    string_concated= string1+ string2 +string3 # formatting the string to appropriate one
    Fh_append.write(string_concated)
    Fh_append.close()
    get_value=wifi_activate.activate() # calls "activate" function from the "wifi_activate" module to activate the change
    print get_value
         
			

          

 
