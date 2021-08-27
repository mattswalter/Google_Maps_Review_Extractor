# Google_Maps_Review_Extractor
## Author: mattswalter, mswalter@udel.edu

### Extract user reviews for locations left on Google Maps

Utilizes Beautiful soup and text download links for google maps reviews.

Required packages: urllib, bs4, and pandas, and os

Input: A csv file that contains the link to the google reviews webpage.
Example: https://www.google.com/maps/place/Roberto+Clemente+Park/@39.9658361,-75.1677383,257m/data=!3m1!1e3!4m11!1m2!2m1!1sroberto+clemente+park!3m7!1s0x89c6c7ce0c738c31:0x40b2e77be95307b7!8m2!3d39.9656867!4d-75.1680226!9m1!1b1!15sChVyb2JlcnRvIGNsZW1lbnRlIHBhcmuSAQRwYXJr

Output: A csv file with columns for: the place name, total number of place reviews, overall place score, amount of reviews by individual, amount of photos by individual, individual place score, and the review text.

