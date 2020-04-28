# Bipolar-Factor

**Assignment - ML at Bipolar Factory.**

Project - Crawl popular websites and create a database of Indian movie celebrities containing their images and personality traits.

I have selected website [Wikipedia Actors list](http://en.wikipedia.org/wiki/List_of_Indian_film_actors) and  [Wikipedia Actresses List](https://en.wikipedia.org/wiki/List_of_Indian_film_actresses) for web scrapping. Wikipedia provides the list of all known indian celebrities with their bio, images etc. And they are stored into MongoDB Atlas.

I have scrapped all information related to celebrities. list of scrapped information as per below.<br />

1. Celebrity Name :<br />
2. Celebrity image :<br />
3. Celebrity age :<br />
4. Celebrity D.O.B :<br />
5. Celebrity(Alive or dead):<br />
6. personal information:<br />

## required libraries :<br />

- *Selenium*<br />
- *Scrapy*<br />
- *urllib*<br />
- *pymongo*<br />

## To run the code:
1. Get into the celebrity_list folder.<br />
2. Run the command *scrapy crawl celebrities*(name of the spider created).<br />
3. Change the credentials of the mongodb server in celebrity_list/pipelines.py. <br />
4. Also change the directory where you want to save the photos.
