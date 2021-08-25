import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os


# Read in google maps review page url

path = os.getcwd() + '/locations.csv'

dat = pd.read_csv(path)
dat = dat['url'].tolist()


for url in dat:

    # Format the url to obtain review information
    lr = url

    print(url)
    next_page_token = ''

    url = url.split('!1s')[1]
    place_id = url.split('!')[0]



    d1 = []
    d2 = []
    d21 = []
    d3 = []
    d4 = []

    i = 1

    try:

        while True:
            # Open review information
            target_url = "https://www.google.com/async/reviewDialog?hl=en&async=feature_id:" + place_id + ",sort_by:,next_page_token:" + next_page_token + ",associated_topic:,_fmt:pc"

            txt = urllib.request.urlopen(target_url).read()
            # Read in html
            response = BeautifulSoup(txt, 'html.parser')

            response_text = str(response)
            # Find the token to access the next page of reviews
            response_text = response_text.split("data-next-page-token",1)[1]
            response_text = response_text.split('"',1)[1]
            next_page_token = response_text.split('"',1)[0]

            while i == 1:
                # Find the overall review score
                response_text = str(response)
                place_score = response_text.split('Fam1ne GrWnYc',1)[0]
                place_score = place_score.split('>')[21]
                place_score = place_score.split('<')[0]

                i += 1

            for node in response.findAll('span',{"class": "z5jxId"}):
                # Find the number of reviews for the location
                num_reviews = (''.join(node.findAll(text=True, )))
                num_reviews = ''.join(c for c in num_reviews if c.isdigit())

            for node in response.findAll('div',{"class": "P5Bobd"}):
                # Find the name of the location
                name = (''.join(node.findAll(text=True, )))


            for node in response.findAll('div',{"class": "Jtu6Td"}):
                # Find the review text
                re = (''.join(node.findAll(text=True, )))
                review = re.split('More')[-1]

                d1.append(review)

            for node in response.findAll('div',{"class": "FGlxyd"}):
                # Find the number of reviews and photos from the individual
                re = (''.join(node.findAll(text=True)))
                cond = ''.join(c for c in re if c in '·')

                if cond == "··" or cond == '·':
                    re1 = re.split('·')[1]
                    reviews = int("".join(filter(str.isdigit, re1)))

                else:
                    reviews = ''

                if cond == '·':
                    re2 = re.split('·')[-1]
                    photos = int("".join(filter(str.isdigit, re2)))

                else:
                    photos = ''

                d2.append(reviews)
                d21.append(photos)

            for node in response.findAll('div',{"class": "PuaHbe"}):
                # Find the time the review was submitted
                re = (''.join(node.findAll(text=True)))
                time = re.replace('New', '')

                d3.append(time)

            for node in response.findAll('div',{"class": "PuaHbe"}):
                # Find the rating of the review
                node = str(node)
                n1 = node.split('"')[7]
                n1 = n1.split('.')[0]
                rating = int("".join(filter(str.isdigit, n1)))

                d4.append(rating)

            i = len(d1)
            # Print the progress for the current location
            counter = str(i) + '/' + str(num_reviews)
            print(counter)


            if next_page_token == '':
                break

        d = pd.DataFrame()

        # Build dataframe of reviews
        d['text'] = d1
        d['user_number_reviews'] = d2
        d['user_number_photos'] = d21
        d['time'] = d3
        d['score'] = d4
        d = d.assign(place_name=name)
        d = d.assign(num_reviews=num_reviews)
        d = d.assign(place_score=place_score)
        d = d.assign(url=lr)

        d = d[['url', 'place_name', 'place_score', 'num_reviews', 'user_number_reviews', 'user_number_photos', 'time', 'score', 'text']]

        # Write reviews to csv
        output = os.getcwd() + '/output/' + name + ".csv"
        d.to_csv(output, encoding='utf-8', index=False)

    except:
        pass

