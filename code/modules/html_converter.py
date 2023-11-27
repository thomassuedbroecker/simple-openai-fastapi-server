from bs4 import BeautifulSoup

def html_to_text(html_content):

    text = "" 
    
    if (BeautifulSoup(html_content, "html.parser").find()):
        verification = True
        soup = BeautifulSoup(html_content,'html.parser')
        text = soup.text
    else:
        verification = False
        text = "File doesn't contain HTML content."
    
    return text , verification