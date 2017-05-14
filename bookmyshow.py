#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib2
import time
import os

def check_mv():
        bms_content = urllib2.urlopen("https://in.bookmyshow.com/bengaluru/movies/nowshowing").read();
        soup_obj=BeautifulSoup(bms_content);
        mv_images = [iterator["alt"] for iterator in soup_obj.select(".poster-container-img img")]
        for itr in mv_images:
                if search_mv.lower() in itr.lower():
                        global flag
                        flag=True;
                        break;
        return;


print "~~~~~~~~~~~~~~~~~Searching in Bengaluru~~~~~~~~~~~~~~~"
search_mv = raw_input('Enter movie name:');
flag=False;
while flag==False:
        check_mv();
        print "Waiting"
        time.sleep(600);

if flag==True:
        print "Available"
        os.system('say "{}"' .format(search_mv)+"is Available");
else:
        print "Not available"
