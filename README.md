Web crawling using Scrapy framework
==========================================
Steps to run project

VIRTUAL ENVIRONMENT SETUP
============================================
=> Create a directory	called web_crawling

=> Create a virtual environment in the folder web_crawling	
    cd web_crawling
    py -m venv env
    
=> Activate virtual environment
  evn\Scripts\activate
    
=> Install scrapy library	
    pip install scrapy
    
    
COMMANDS TO CREATE SCRAPY PROJECT
===========================================
=>Create project	called learnings
  scrapy startproject learnings
  
=>Go to directory \web_scraping\learnings\learnings\spiders
  cd \learnings\learnings\spiders
  
=> Create a spider	
  scrapy genspider blog_post www.zyte.com
  
  Copy the file content from my project to your file blog_post.py
  

COMMANDS TO RUN SPIDERS AND STORE DATA
=============================================
=>Run a file called blog_post.py	
  scrapy crawl blog_post	 #This will print output on terminal
=>To dump into a CSV file	
  scrapy runspider blog_post.py -o blog_post.csv	#This will store data to csv file
=>To dump into a XML file	
    scrapy runspider blog_post.py -o blog_post.xml



    
    
