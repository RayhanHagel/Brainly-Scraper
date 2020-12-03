# Brainly-Scraper
 Gets the answers from a question trough brainly

 Scraping the answer page links trough brainly using only **requests** module is impossible, since the search results is provided trough a Java Script

 The only way to find the links trough brainly itself is by using **webdriver** which could use up a bit more memory, so I decided to use the **googlesearch** module to find the answer page link and scrape it using **requests** module