from recon import Assist
from googlesearch import search
import webbrowser

if __name__ == "__main__":
    while(True):
        query = Assist().recognize().lower()
        
        # create conditions
        if "searching on" in query:
            Assist().speak("What do you want to search sir")
            print("What do you want to search sir")
            
            search_something = Assist().recognize().lower()
            
            # show the search
            for i in search(search_something, tld='co.in', num=1, stop=1, pause=2):
                webbrowser.get("/usr/bin/firefox").open(i)
            
            Assist().speak("Do you want to searching another!")
            search_something = Assist().recognize().lower()
            if "no thank you" in search_something:
                break
            