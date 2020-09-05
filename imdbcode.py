
import requests
from bs4 import BeautifulSoup


URL = 'https://www.imdb.com/name/nm0000158/'


def main():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    movietags = soup.select('div.filmo-row', class_='filmo-category-selection')

    titles = [tag.text for tag in movietags]
    n_movies = len(titles)
    finalYears = []
    idx = 0
    while idx < n_movies:
        movietag0 = movietags[idx]
        moviesplit = movietag0.text.split()
        testS = moviesplit[0]
        if testS.isnumeric:
            finalYears.append(moviesplit[0])
        else:
            finalYears.append('Date Unknown')
        idx = idx + 1


    link_movie = soup.find('div', class_="filmo-category-section")
    firstPart = 'https://www.imdb.com'
    appendText = '?ref_=nm_flmg_act_1'
    links = []
    finalMovies = []

    check_tv_m = soup.find('div', id = "filmo-head-actor", class_ = "head")
    tv_or_mov = check_tv_m.find('div', class_ ="filmo-category-section")
    tv_or_mov.find('div', class_ ="filmo-row")
    print(check_tv_m.text)







    #getting the number of Acting credits
    num_movies = soup.find('div', id = "filmo-head-actor", class_ = "head").find('a').nextSibling
    num_movies = num_movies[2:-9]
    print(num_movies)
    num_movies = float(num_movies)
    print(type(num_movies))

    #getting the number of Producer credits
    num_produced = soup.find('div', id = "filmo-head-producer", class_ = "head").find('a').nextSibling
    num_produced = num_produced[2:-9]
    print(num_produced)
    num_produced = float(num_produced)
    print(type(num_produced))

    num_total  = num_movies + num_produced

    link_movie = soup.find('div', class_="filmo-category-section")
    firstPart = 'https://www.imdb.com'
    appendText = '?ref_=nm_flmg_act_1'
    links = []
    finalMovies = []
    for x in link_movie.find_all('div', class_="filmo-row"):
        secondPart = x.a.get('href')
        links.append(firstPart + secondPart + appendText)
        finalMovies.append(x.a.text)
        finalYears.append(x.text)



    #if actor is the first header on the page
    if soup.find('div', {"id": "filmography"}).a.text == 'Actor':
    	for x in link_movie.find_all('div', class_="filmo-row")[:int(num_movies)]:
       		secondPart = x.a.get('href')
        	links.append(firstPart + secondPart + appendText)
        	finalMovies.append(x.a.text)
        	finalYears.append(x.text)

    #If producer is the first tag 
    if soup.find('div', {"id": "filmography"}).a.text == 'Producer':
    	for x in link_movie.find_all('div', class_="filmo-row")[int(num_produced):int(num_total)]: #if producer is the first header on the page
        	secondPart = x.a.get('href')
        	links.append(firstPart + secondPart + appendText)
        	finalMovies.append(x.a.text)
        	finalYears.append(x.text)

    for x in link_movie.fin

    else:
    	for x in link_movie.find_all('div', class_="filmo-row")[int(num_produced):int(num_total)]: #if producer is the first header on the page
        	secondPart = x.a.get('href')
        	links.append(firstPart + secondPart + appendText)
        	finalMovies.append(x.a.text)
        	finalYears.append(x.text)







    for x in link_movie.find_all('div', class_="filmo-row"):
        secondPart = x.a.get('href')
        links.append(firstPart + secondPart + appendText)
        finalMovies.append(x.a.text)
        finalYears.append(x.text)
       

    #Fixing it for the dates:




    print(links)
    print(finalMovies)
    #print(finalYears)

if __name__ == '__main__':
    main()



#     main()
# # ######################################################
# #imdb project 
import requests 
from bs4 import BeautifulSoup


valid_movies = []

imdb_link ="https://www.imdb.com/find?s=nm&q="

celeb_name = "Tom Hanks"
celeb_name = celeb_name.split(" ")
celeb_name = '+'.join(celeb_name) #this will then give in the form "tom+hanks"

imdb_search = requests.get(imdb_link + celeb_name).text

soup = BeautifulSoup(imdb_search, "html")
#print(soup.prettify())

#lets try to print out Tom Hanks name
article =soup.find('div', class_ = "article")
#print(article.prettify())

table_names = article.find('table', class_ = "findList")
first_name = table_names.find('td', class_ = "result_text").a.text
first_url = table_names.find('td', class_ = "result_text").a['href']

end_of_link  = "?ref_=fn_nm_nm_1"


#print(first_url)
first_url = str(first_url)
#print(type(first_url))

href_link = first_url + end_of_link
print(href_link)
print(first_name)

link_to_actor = "https://www.imdb.com/"+  href_link

#this gives you the link of the first actor after the search is complete
print(link_to_actor)

#this navigates to the first actor/actress of the search page
movies_page = requests.get(link_to_actor).text
soup = BeautifulSoup(movies_page, "html") #this gives us the html of the actor/actress home page


link_movie = soup.find('div', class_="filmo-category-section")
first_part = 'https://www.imdb.com'
appendText = '?ref_=nm_flmg_act_1'

all_links =[]
final_movies =[]
tv_movie = []

#print(link_movie.find_all('div', class_ = "filmo-row").text)
tv_movie = []
for x in soup.find_all('div', class_ = "filmo-row"):
	tv_movie.append(x.text)





print(tv_movie)
print(len(tv_movie))




# ##
for x in link_movie.find_all('div', class_ = "filmo-row"):
	secondpart = x.a.get('href')
	all_links.append(first_part + secondpart + appendText)
	final_movies.append(x.a.text)



all_links = [s.encode('ascii') for s in all_links]
final_movies = list(str(i).strip() for i in final_movies)

# #print(tv_movie)
print(all_links)
print(len(all_links))


# #call function to get the info for each movie(passing in the url from all_links)
for i in all_links:
    valud_movie(i)



# #Allows user to randomly get a random  valid movie
n_movies = len(all_links)

while(True):
    idx = random.randrange(0, n_movies)
        
    print(valid_movies[idx])

    user_input = input('Do you want another movie (y/[n])? ')
    if user_input != 'y':
       break
