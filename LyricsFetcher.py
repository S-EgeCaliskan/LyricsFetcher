import requests
from requests_html import HTML
import string

searchSite = "http://search.azlyrics.com/search.php?q="
#Searching for the song on azlyrics' database
def songSearch():
    #  and song name input here, all punctuations are removed for better search results, 
    # whitespaces replaced with + signs for search query
    songName = input("\nArtist and/or Song name: \n").lower().translate(str.maketrans("","", string.punctuation)).replace(" ","+") 
    searchLink = list(searchSite) #turn string into list, append the input into the list
    searchLink.append(songName)
    searching = "".join(searchLink) #turn the list into a str
#Getting the song list from the database
    def findLyrics(url):
        r = requests.get(url)
        html_text = r.text
        return html_text      
    url = searching
    html_text = findLyrics(url)
    r_html = HTML(html=html_text)
    try: #making sure the song exists in the database of AZlyrics
        table_class = ".table-condensed"
        r_table = r_html.find(table_class)
        
        name_class = ".visitedlyr a"
        name_list = r_table[0].find(name_class)
        for name in name_list: #Get the name of the songs and artists
            print (name.text)

    except:
        print("No song could be found, try again.\n")
        return songSearch()
#Getting the user to select the found songs
    def chooseSong():
        link_class = ".visitedlyr a" #checking hyperlinks
        link_list = r_table[0].find(link_class) #Grabbing only the first table since the otheres are irrelevant
        name_range=(range(1,len(name_list)+1)) #Changes the range from 0,5 into 1,6, corresponding with the numbers we get from azLyrics
        
        try:
                userInput = int(input("Choose a song. Enter the corresponding number. Or enter '0' to make a new search.\n"))
        except ValueError:
                print("This is not a number. Please enter a valid number from the list.\n")
                return chooseSong()

        #NAVIGATE INTO THE LINK OF THE SPECIFIED INPUT AND FETCH THE TEXT ELEMENT FROM THE PAGE    
        if userInput in name_range:
            if userInput == 1: #navigating to the hyperlink of the first element in the list
                url = link_list[0].links
                link = list(url)
                r = requests.get(link[0])
                r_html = HTML(html=r.text)
                
                text_class=".col-lg-8"
                lyrics_table=r_html.find(text_class)
           
                
                lyrics_element = ".col-lg-8 div"
                lyrics_text = lyrics_table[0].find(lyrics_element)
                print("Here are the lyrics for: "+link_list[0].text + "!")
                print(lyrics_text[5].text)


            if userInput == 2:  #navigating to the hyperlink of the second element in the list and so forth
                url = link_list[1].links
                link = list(url)
                r = requests.get(link[0])
                r_html = HTML(html=r.text)
                
                text_class=".col-lg-8"
                lyrics_table=r_html.find(text_class)
           
                
                lyrics_element = ".col-lg-8 div"
                lyrics_text = lyrics_table[0].find(lyrics_element)
                print("Here are the lyrics for: "+link_list[1].text + "!")
                print(lyrics_text[5].text)
                
            if userInput == 3:
                url = link_list[2].links
                link = list(url)
                r = requests.get(link[0])
                r_html = HTML(html=r.text)
                
                text_class=".col-lg-8"
                lyrics_table=r_html.find(text_class)
           
                
                lyrics_element = ".col-lg-8 div"
                lyrics_text = lyrics_table[0].find(lyrics_element)
                print("Here are the lyrics for: "+link_list[2].text + "!")
                print(lyrics_text[5].text)
                
            if userInput == 4:
                url = link_list[3].links
                link = list(url)
                r = requests.get(link[0])
                r_html = HTML(html=r.text)
                
                text_class=".col-lg-8"
                lyrics_table=r_html.find(text_class)
        
                
                lyrics_element = ".col-lg-8 div"
                lyrics_text = lyrics_table[0].find(lyrics_element)
                print("Here are the lyrics for: "+link_list[3].text + "!")
                print(lyrics_text[5].text)
                
            if userInput == 5:
                url = link_list[4].links
                link = list(url)
                r = requests.get(link[0])
                r_html = HTML(html=r.text)
                
                text_class=".col-lg-8"
                lyrics_table=r_html.find(text_class)
                      
                lyrics_element = ".col-lg-8 div"
                lyrics_text = lyrics_table[0].find(lyrics_element)
                print("Here are the lyrics for: "+link_list[4].text + "!")
                print(lyrics_text[5].text)
                
        elif userInput == 0: #gives the option to reset the search.
            return songSearch()
        
        else:
            print("The number is not in the list, please specify a number that is in the list.\n")
            return chooseSong() 
            
   
    chooseSong()

if __name__=="__main__":
    songSearch()

while True: #Repeat the program until it is closed
    songSearch()    
