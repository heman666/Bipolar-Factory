#Bipolar-Factor

Assignment - ML at Bipolar Factory.

Project - Crawl popular websites and create a database of Indian movie celebrities containing their images and personality traits.

I have selected website http://en.wikipedia.org/wiki/List_of_Indian_film_actors and https://en.wikipedia.org/wiki/List_of_Indian_film_actresses for web scrapping. Wikipedia provides the list of all known indian celebrities with their bio, images etc. And they are stored into MongoDB Atlas.

I have scrapped all information related to celebrities. list of scrapped information as per below

1.Celebrity Name :
2.Celebrity image :
3.Celebrity age :
4.Celebrity D.O.B :
5.Celebrity(Alive or dead):
6.personal information:

#required libraries :

Selenium
Scrapy
urllib
pymongo

#To run the code:
1.Get into the celebrity_list folder.
2.Run the command scrapy crawl celebrities(name of the spider created).
3.Change the credentials of the mongodb server in celebrity_list/pipelines.py. 
4.Also change the directory where you want to save the photos.