<img src="https://in.bgu.ac.il/marketing/graphics/BGU.sig3-he-en-white.png" height="48px" align="right" />  

# Description
Scrap Wikipedia to get information on movie actors and actresses

In this program you can enter link to wikipedia page of actor and get

We foucsed on **Gal Gadot** wikipedia page
* Table with details about movies the actor played in
* Co-actors the actor played with in other movies
* Histogram of movie joins with other actors

## ⚠️ Prerequisites  
  
- [Python 3.6](https://www.python.org/download/releases/2.7/)  
- [Git 2.26](https://git-scm.com/downloads/)  
- [PyCharm IDEA](https://www.jetbrains.com/pycharm/) (recommend)  

## 📦 How To Install  
  
You can modify or contribute to this project by following the steps below:  
  
**1. Clone the repository**  
  
- Open terminal ( <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> )  
  
- [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) to a location on your machine.  
 ```bash  
 # Clone the repository 
 $> git clone https://github.com/serfati/wikiscrapper.git  

 # Navigate to the directory 
 $> cd wikiscrapper
  ``` 


**2. Install dependencies** 

 ```bash  
 # pip
 $> pip install -r requirements.txt
 ```  

**3. Launch of the project**  
  
 ```bash  
 # run 
 $> python script.py
 ```  

## :wrench: Dependencies and Main Packages

- `urllib` -  HTTP client for Python
- `BeautifulSoup` - scrape information from web pages.
- `pandas` - Powerful data structures for data analysis, time series, and statistics
- `mwparserfromhell` - parser for MediaWiki wikicode.
- `seaborn` - statistical data visualization
- `re` - A back-pocket regex cookbook

## :camera: Screenshots

* All films by Gal Gadot sorted by `Year` column
<img src="https://res.cloudinary.com/serfati/image/upload/v1604487779/screely-1604487740256_exdwnn.png" height="300px"/>

* Deatils on actors who played with Gal Gadot's films
<img src="https://res.cloudinary.com/serfati/image/upload/v1604487779/screely-1604487669044_j5ms8q.png" height="300px"/>

* Histogram shows how many played with Gal in same movie (1 or more)
<img src="https://res.cloudinary.com/serfati/image/upload/v1604489061/screely-1604489046599_dgrxnv.png" height="300px"/>


## :busts_in_silhouette: Team Members:

| Name             | Username                                    | Contact Info              | 
| ---------------- | ------------------------------------------- | ------------------------- | 
| _Dvir Simhon_    | [dvirsimhon](https://github.com/dvirsimhon) | dvirsim@post.bgu.ac.il    |  
| _Avihai Serfati_ | [serfati](https://github.com/serfati)       | serfata@post.bgu.ac.il    | 

## ⚖️ License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://github.com/serfati" target="_blank">serfati</a>.

**[⬆ back to top](#description)**
