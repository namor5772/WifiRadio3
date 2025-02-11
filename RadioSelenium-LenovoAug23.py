import subprocess
import inspect
import tkinter as tk
import time
import urllib.request

from PIL import Image, ImageTk
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create an instance of FirefoxOptions
firefox_options = Options()
#firefox_options.add_argument("-headless")  # Ensure this argument is correct
browser = webdriver.Firefox(options=firefox_options)

image_path = r"C:\Users\grobl\OneDrive\GitRepos\WifiRadio3\Images\logo.png"



def Suck_ABC(br,sPath):
    br.refresh()
    br.get(sPath)
    time.sleep(3)
    be = br.find_element(By.TAG_NAME, 'body')
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)

    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)


    # Use JavaScript to get the currently focused (active) element
    active_element = br.execute_script("return document.activeElement")

    # Retrieve various attributes of the active element
    element_tag_name = active_element.tag_name
    element_id = active_element.get_attribute('id')
    element_class = active_element.get_attribute('class')
    element_name = active_element.get_attribute('name')
    element_value = active_element.get_attribute('value')
    element_inner_html = active_element.get_attribute('innerHTML')

    # Parse the innerHTML with BeautifulSoup
    soup = BeautifulSoup(element_inner_html, 'lxml')

    # Find all elements with data-component="KeyboardFocus"
    focused_elements = soup.find_all(attrs={"data-component": "KeyboardFocus"})

    # Extract and print the text content of these elements
    for element in focused_elements:
        print(element.text)

    be.send_keys(Keys.ENTER)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')


    for _ in range(14):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)




# START ***** Functions that stream radio stations *****

# ALL GOOD
def Radio1(br,Num,sPath):
    br.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    for _ in range(Num):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    time.sleep(1)
    # Find song details
    ht = be.get_attribute('innerHTML')
    soup = BeautifulSoup(ht, 'lxml')
    fe = soup.find(attrs={"class": "playingNow"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No specific item playing"
    return fe2

# ALL GOOD
def Radio2(br,Num,sPath):
    br.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    for _ in range(3):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    for _ in range(4):
        be.send_keys(Keys.UP)
    for _ in range(Num):
        be.send_keys(Keys.DOWN)
    be.send_keys(Keys.ENTER)
    for _ in range(3):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    time.sleep(1)
  # Find stream details
    ht = be.get_attribute('innerHTML')
    soup = BeautifulSoup(ht, 'lxml')
    fe = soup.find(attrs={"class": "view-live-now popup"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No specific item playing"
  # Remove irrelevant info, starting with [*.*More]
    sub = "*.*More"
    pos = fe2.find(sub)
    if pos != -1:
        fe2 = fe2[:pos]
    return fe2

# ALL GOOD
def Radio3(br,Num,sPath):
    br.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    for _ in range(5):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    for _ in range(4):
        be.send_keys(Keys.UP)
    for _ in range(Num):
        be.send_keys(Keys.DOWN)
    be.send_keys(Keys.ENTER)
    for _ in range(3):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    time.sleep(1)
    # Find program details
    ht = be.get_attribute('innerHTML')
    soup = BeautifulSoup(ht, 'lxml')
    fe = soup.find(attrs={"class": "view-live-now popup"})
    if fe is not None:
        fe1 = fe.get_text(separator="*", strip=True)
    else:
        fe1 = "None"
    # Remove irrelevant info, starting with [*More]
    sub = "*More"
    pos = fe1.find(sub)
    if pos != -1:
        fe1 = fe1[:pos]
    # find song details    
    fe = soup.find(attrs={"class": "playingNow"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No specific item playing"
    fe3 = fe1+"*"+fe2
    return fe3

# ALL GOOD
def Radio4(br,sPath):
    br.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    for _ in range(3):
        be.send_keys(Keys.TAB)
    # adjust amount of tabbing depending on where you end up!
    focused_element = br.execute_script("return document.activeElement")
    if not("Button_btn___qFSk" in focused_element.get_attribute('class')):
           be.send_keys(Keys.SHIFT,Keys.TAB)
    be.send_keys(Keys.ENTER)
    be.send_keys(Keys.SHIFT,Keys.TAB)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    time.sleep(3)
    # get station logo
    
    # Locate the image element by XPath
    img_element = be.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/main/div[1]/div/div/div/a/div/img')

    # Get the image URL
    img_url = img_element.get_attribute("src")

    # Download the image
    urllib.request.urlretrieve(img_url, image_path)



    
    # Find live program details
    ht = be.get_attribute('innerHTML')
    soup = BeautifulSoup(ht, 'lxml')
    fe = soup.find(attrs={"class": "LiveAudioPlayer_body__y6nYe"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No item playing"
    # Remove irrelevant info [*-]
    sub = "*-"
    fe3 = fe2.replace(sub,"")
    # Find live program synopsis
    fe = soup.find(attrs={"class": "LiveAudioSynopsis_content__DZ6E7"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No Description"
    fe3 = fe3+"*"+fe2+"*"+image_path
    return fe3


# ALL GOOD    
def Radio5(br,Num,sPath):
    browser.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    for _ in range(Num):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.TAB)
    time.sleep(1)
    # Find song details
    ht = be.get_attribute('innerHTML')
    soup = BeautifulSoup(ht, 'lxml')
    fe = soup.find(attrs={"class": "LiveAudioPlayer_body__y6nYe"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No item playing"
    # Remove irrelevant info [*-]
    sub = "*-"
    fe3 = fe2.replace(sub,"")
    return fe3

def Radio6(br,sPath):
    br.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    for _ in range(3):
        be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    time.sleep(1)
    # Find program details
    ht = be.get_attribute('innerHTML')
    soup = BeautifulSoup(ht, 'lxml')
    fe = soup.find(attrs={"class": "view-live-now popup"})
    if fe is not None:
        fe1 = fe.get_text(separator="*", strip=True)
    else:
        fe1 = "None"
    # Remove irrelevant info, starting with [*More]
    sub = "*More"
    pos = fe1.find(sub)
    if pos != -1:
        fe1 = fe1[:pos]
    # Find song details     
    fe = soup.find(attrs={"class": "playingNow"})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "No specific item playing"
    fe3 = fe1+"*"+fe2
    return fe3

def Radio7(br,Num,sPath):
    br.get(sPath)
    time.sleep(1)
    be = br.find_element(By.TAG_NAME, 'body')
    be.send_keys(Keys.TAB)
    be.send_keys(Keys.ENTER)
    for _ in range(11):
        be.send_keys(Keys.TAB)
    if Num==0:
        be.send_keys(Keys.ENTER)
    elif Num==1:
        be.send_keys(Keys.TAB)
        be.send_keys(Keys.ENTER)
    else: # if Num==2
        be.send_keys(Keys.TAB)
        be.send_keys(Keys.TAB)
        be.send_keys(Keys.ENTER)
        be.send_keys(Keys.ENTER)
    # Find program details
    ht = be.get_attribute('innerHTML')
    time.sleep(1)
    soup = BeautifulSoup(ht, 'lxml')
    if Num==0:
        xid="abc-:rb:-item-0"
    elif Num==1:
        xid="abc-:rb:-item-1"
    else: # if Num==2
        xid="abc-:rb:-item-2"
    fe = soup.find(attrs={"id": xid})
    if fe is not None:
        fe2 = fe.get_text(separator="*", strip=True)
    else:
        fe2 = "None"
    # Remove irrelevant info, starting with [*.*More]
    sub = "*Stop"
    pos = fe2.find(sub)
    if pos != -1:
        fe2 = fe2[:pos]
    else:
        sub = "*Listen"
        pos = fe2.find(sub)
        if pos != -1:
            fe2 = fe2[:pos]
    return fe2



def Smooth(br,ix,iy,sPath):
 #   print(inspect.stack()[1].function)
    br.refresh()
    br.get(sPath)
    time.sleep(3)
    window_size = br.get_window_size()
    print(f"Window size: width = {window_size['width']}, height = {window_size['height']}")
    actions = ActionChains(br)
    actions.move_by_offset(650, 10).click().perform()
    window_size = br.get_window_size()
    
    print(f"Window size: width = {window_size['width']}, height = {window_size['height']}")
    time.sleep(1)
    actions = ActionChains(br)
    actions.move_by_offset(ix,iy).click().perform()
    time.sleep(10)

def Smooth2(br,sPath):
 #   print(inspect.stack()[1].function)
    br.refresh()
    br.get(sPath)
    time.sleep(3)
    window_size = br.get_window_size()
    actions = ActionChains(br)
    actions.move_by_offset(650, 900).click().perform()
    window_size = br.get_window_size()
    time.sleep(10)



def iHeart(br,sPath):
 #   print(inspect.stack()[1].function)
    br.refresh()
    br.get(sPath)
    time.sleep(3)
    window_size = br.get_window_size()
    #print(f"Window size: width = {window_size['width']}, height = {window_size['height']}")
    actions = ActionChains(br)
    actions.move_by_offset(301, 256).click().perform()
    time.sleep(10)

    

def ABC_Radio_Sydney_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/sydney")

def ABC_Broken_Hill_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/brokenhill")

def ABC_Central_Coast_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/centralcoast")

def ABC_Central_West_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/centralwest")

def ABC_Coffs_Coast_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/coffscoast")

def ABC_Illawarra_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/illawarra")

def ABC_Mid_North_Coast_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/midnorthcoast")

def ABC_New_England_North_West_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/newengland")

def ABC_Newcastle_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/newcastle")

def ABC_North_Coast_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/northcoast")

def ABC_Riverina_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/riverina")

def ABC_South_East_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/southeastnsw")

def ABC_Upper_Hunter_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/upperhunter")

def ABC_Western_Plains_NSW():
    return Radio4(browser,"https://www.abc.net.au/listen/live/westernplains")

def ABC_Radio_Canberra_ACT():
    return Radio4(browser,"https://www.abc.net.au/listen/live/canberra")

def ABC_Radio_Darwin_NT():
    return Radio4(browser,"https://www.abc.net.au/listen/live/darwin")

def ABC_Alice_Springs_NT():
    return Radio4(browser,"https://www.abc.net.au/listen/live/alicesprings")

def ABC__NT():
    return Radio4(browser,"https://www.abc.net.au/listen/live/")



def ABC_NewsRadio():
    return Radio4(browser,"https://www.abc.net.au/listen/live/news")

    
def ABC_Radio_National_LIVE():
    return Radio2(browser,0,"https://www.abc.net.au/listen/live/radionational")

def ABC_Radio_National_QLD():
    return Radio2(browser,1,"https://www.abc.net.au/listen/live/radionational")

def ABC_Radio_National_WA():
    return Radio2(browser,2,"https://www.abc.net.au/listen/live/radionational")

def ABC_Radio_National_SA():
    return Radio2(browser,3,"https://www.abc.net.au/listen/live/radionational")

def ABC_Radio_National_NT():
    return Radio2(browser,4,"https://www.abc.net.au/listen/live/radionational")


def ABC_triple_j_LIVE():
    return Radio3(browser,0,"https://www.abc.net.au/listen/live/triplej")

def ABC_triple_j_QLD():
    return Radio3(browser,1,"https://www.abc.net.au/listen/live/triplej")

def ABC_triple_j_WA():
    return Radio3(browser,2,"https://www.abc.net.au/listen/live/triplej")

def ABC_triple_j_SA():
    return Radio3(browser,3,"https://www.abc.net.au/listen/live/triplej")

def ABC_triple_j_NT():
    return Radio3(browser,4,"https://www.abc.net.au/listen/live/triplej")

def ABC_triple_j_Unearthed():
    return Radio1(browser,7,"https://www.abc.net.au/triplej/live/unearthed")
    
def ABC_triple_j_Hottest():
    return Radio1(browser,7,"https://www.abc.net.au/triplej/live/triplejhottest")


def ABC_Double_j_LIVE():
    return Radio3(browser,0,"https://www.abc.net.au/listen/live/doublej")

def ABC_Double_j_QLD():
    return Radio3(browser,1,"https://www.abc.net.au/listen/live/doublej")

def ABC_Double_j_WA():
    return Radio3(browser,2,"https://www.abc.net.au/listen/live/doublej")

def ABC_Double_j_SA():
    return Radio3(browser,3,"https://www.abc.net.au/listen/live/doublej")

def ABC_Double_j_NT():
    return Radio3(browser,4,"https://www.abc.net.au/listen/live/doublej")
    
    
def ABC_Classic_LIVE():
    return Radio3(browser,0,"https://www.abc.net.au/listen/live/classic")

def ABC_Classic_QLD():
    return Radio3(browser,1,"https://www.abc.net.au/listen/live/classic")

def ABC_Classic_WA():
    return Radio3(browser,2,"https://www.abc.net.au/listen/live/classic")

def ABC_Classic_SA():
    return Radio3(browser,3,"https://www.abc.net.au/listen/live/classic")

def ABC_Classic_NT():
    return Radio3(browser,4,"https://www.abc.net.au/listen/live/classic")


def ABC_Classic2():
    return Radio1(browser,7,"https://www.abc.net.au/listen/live/classic2")
    
def ABC_Jazz():
    return Radio1(browser,7,"https://www.abc.net.au/listen/live/jazz")
    
def ABC_Country():
    return Radio5(browser,3,"https://www.abc.net.au/listen/live/country")

def ABC_Kids_listen():
    return Radio6(browser,"https://www.abc.net.au/listenlive/kidslisten")
    
def ABC_Radio_AUSTRALIA():
    return Radio5(browser,3,"https://www.abc.net.au/pacific/live")

def ABC_SPORT():
    return Radio7(browser,0,"https://www.abc.net.au/news/sport/audio")

def ABC_SPORT_EXTRA():
    return Radio7(browser,1,"https://www.abc.net.au/news/sport/audio")

def ABC_CRICKET():
    return Radio7(browser,2,"https://www.abc.net.au/news/sport/audio")


    
def KIIS1065():
    iHeart(browser,"https://www.iheart.com/live/kiis-1065-6185/")
def GOLD1017():
    iHeart(browser,"https://www.iheart.com/live/gold1017-6186/")
def CADA():
    iHeart(browser,"https://www.iheart.com/live/cada-6179/")
def iHeartCountry_Australia():
    iHeart(browser,"https://www.iheart.com/live/iheartcountry-australia-7222/")
def KIIS_90s():
    iHeart(browser,"https://www.iheart.com/live/kiis-90s-10069/")
def GOLD_80s():
    iHeart(browser,"https://www.iheart.com/live/gold-80s-10073/")
def iHeartRadio_Countdown_AUS():
    iHeart(browser,"https://www.iheart.com/live/iheartradio-countdown-aus-6902/")
def TikTok_Trending_on_iHeartRadio():
    iHeart(browser,"https://www.iheart.com/live/tiktok-trending-on-iheartradio-8876/")
def iHeartDance():
    iHeart(browser,"https://www.iheart.com/live/iheartdance-6941/")
def The_Bounce():
    iHeart(browser,"https://www.iheart.com/live/the-bounce-6327/")
def iHeartAustralia():
    iHeart(browser,"https://www.iheart.com/live/iheartaustralia-7050/")
def fbi_radio():
    iHeart(browser,"https://www.iheart.com/live/fbiradio-6311/")
def _2SER1073():
    iHeart(browser,"https://www.iheart.com/live/2ser-6324/")
def smoothfm_953_Sydney():
    Smooth(browser,0,95,"https://smooth.com.au")
def smooth_Vintage():
    Smooth(browser,0,95*2,"https://smooth.com.au")
def smooth_953_Adelaide():
    Smooth(browser,0,95*3,"https://smooth.com.au")
def smooth_80s():
    Smooth2(browser,"https://smooth.com.au/station/smooth80s")
def smooth_relax():
    Smooth2(browser,"https://smooth.com.au/station/smoothrelax")




# END ******* Functions that stream radio stations *****


# 2D array of radio station information in [short name, long name, url] format
# clearly this can be varied if you wish to listen to different 7 stations
aStation = [
# 53 + 31 = 84

    ["ABC Radio Sydney NSW",ABC_Radio_Sydney_NSW],
    ["ABC Broken Hill NSW",ABC_Broken_Hill_NSW],
    ["ABC Central Coast NSW",ABC_Central_Coast_NSW],
    ["ABC Central West NSW",ABC_Central_West_NSW],
    ["ABC Coffs Coast NSW",ABC_Coffs_Coast_NSW],
    ["ABC Illawarra NSW",ABC_Illawarra_NSW],
    ["ABC Mid North Coast NSW",ABC_Mid_North_Coast_NSW],
    ["ABC New England North West NSW",ABC_New_England_North_West_NSW],
    ["ABC Newcastle NSW",ABC_Newcastle_NSW],
    ["ABC North Coast NSW",ABC_North_Coast_NSW],
    ["ABC Riverina NSW",ABC_Riverina_NSW],
    ["ABC South East NSW",ABC_South_East_NSW],
    ["ABC Upper Hunter NSW",ABC_Upper_Hunter_NSW],
    ["ABC Western Plains NSW",ABC_Western_Plains_NSW],
    ["ABC Radio Canberra ACT",ABC_Radio_Canberra_ACT],
    ["ABC Radio Darwin NT",ABC_Radio_Darwin_NT],
    ["ABC Alice Springs NT",ABC_Alice_Springs_NT],



    
    ["ABC NewsRadio",ABC_NewsRadio],

    ["ABC Radio National LIVE",ABC_Radio_National_LIVE],
    ["ABC Radio National QLD",ABC_Radio_National_QLD],
    ["ABC Radio National WA",ABC_Radio_National_WA],
    ["ABC Radio National SA",ABC_Radio_National_SA],
    ["ABC Radio National NT",ABC_Radio_National_NT],

    ["ABC SPORT",ABC_SPORT],
    ["ABC SPORT EXTRA",ABC_SPORT_EXTRA],
    ["ABC SPORT CRICKET",ABC_CRICKET],
    
    ["ABC triple j LIVE",ABC_triple_j_LIVE],
    ["ABC triple j QLD",ABC_triple_j_QLD],
    ["ABC triple j WA",ABC_triple_j_WA],
    ["ABC triple j SA",ABC_triple_j_SA],
    ["ABC triple j NT",ABC_triple_j_NT],

    ["ABC triple j Hottest",ABC_triple_j_Hottest],
    ["ABC triple j Unearthed",ABC_triple_j_Unearthed],

    ["ABC Double j LIVE",ABC_Double_j_LIVE],
    ["ABC Double j QLD",ABC_Double_j_QLD],
    ["ABC Double j WA",ABC_Double_j_WA],
    ["ABC Double j SA",ABC_Double_j_SA],
    ["ABC Double j NT",ABC_Double_j_NT],

    ["ABC Classic LIVE",ABC_Classic_LIVE],
    ["ABC Classic QLD",ABC_Classic_QLD],
    ["ABC Classic WA",ABC_Classic_WA],
    ["ABC Classic SA",ABC_Classic_SA],
    ["ABC Classic NT",ABC_Classic_NT],
    
    ["ABC Classic2",ABC_Classic2],
    ["ABC Jazz",ABC_Jazz],
    ["ABC Country",ABC_Country],
    ["ABC Kids listen",ABC_Kids_listen],
    
    ["ABC Radio AUSTRALIA",ABC_Radio_AUSTRALIA]
]


def on_select(event):
    selected_value = combobox.get()
    selected_index = combobox.current()
    print("Selected:", selected_value)
    print("Index:", selected_index)
    text = aStation[selected_index][1]();
    print(text)
    text_rows = text.split("*")
    # Make text box editable, so contents can be deleted and rewritten
    text_box.config(state=tk.NORMAL)
    text_box.delete('1.0', tk.END)
    print(text_rows)
    # Insert each row of text into the text box
    for row in text_rows:
        text_box.insert(tk.END, row + "\n")
    # Disable the text box to make it read-only
    text_box.config(state=tk.DISABLED)
    print("")

    image = Image.open(image_path)

    # Scale the image
    scaled_image = image.resize((200, 200))  # Adjust the size as needed

    # Convert the image to a format Tkinter can use
    photo = ImageTk.PhotoImage(scaled_image)

    # Create a Label to display the image
    label = tk.Label(root, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection

    # Set the position of the image
    label.place(x=18, y=400)  # Adjust the position as needed    
    
    


# Create the main window
root = tk.Tk()
root.title("INTERNET RADIO 3.0")  # Title of the window

# Set window size
root.geometry("794x700")  # Width x Height

#"794x390"

# Create a combobox (dropdown list)t
aStringArray = []
for element in aStation:
    aStringArray.append(element[0])
combobox = ttk.Combobox(root, values=aStringArray, width=33)
combobox.pack(pady=10)

# Bind the combobox selection event to the on_select function
combobox.bind("<<ComboboxSelected>>", on_select)

# Create a text box and position it using grid
text_box = tk.Text(root, height=20, width=95)
text_box.pack(pady=10)

# Enable the text box to insert text
text_box.config(state=tk.NORMAL)


    

# Run the application
root.mainloop()

print("Radio stream interface")


'''
smoothfm_953_Sydney() ;time.sleep(60)
smooth_relax()        ;time.sleep(60)
smooth_80s()          ;time.sleep(60)
smooth_953_Adelaide() ;time.sleep(60)
smooth_Vintage()      ;time.sleep(60)


KIIS1065()
time.sleep(10)

GOLD1017()
time.sleep(10)

CADA()
time.sleep(10)

iHeartCountry_Australia()
time.sleep(10)

KIIS_90s()
time.sleep(10)

GOLD_80s()
time.sleep(10)

iHeartRadio_Countdown_AUS()
time.sleep(10)

TikTok_Trending_on_iHeartRadio()
time.sleep(10)

iHeartDance()
time.sleep(10)

The_Bounce()
time.sleep(10)

iHeartAustralia()
time.sleep(10)

fbi_radio()
time.sleep(10)

_2SER1073()
time.sleep(10)

'''


while True:
    startup = False    

