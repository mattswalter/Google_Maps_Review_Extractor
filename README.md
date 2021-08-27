# Google_Maps_Review_Extractor
## Author: mattswalter, mswalter@udel.edu

### Extract, scrape, and download user reviews for locations left on Google Maps

Utilizes Beautiful soup and text download links for google maps reviews.

Required packages: urllib, bs4, and pandas, and os

Input: A csv file that contains the link to the google reviews webpage.
Example: https://www.google.com/maps/place/Roberto+Clemente+Park/@39.9658361,-75.1677383,257m/data=!3m1!1e3!4m11!1m2!2m1!1sroberto+clemente+park!3m7!1s0x89c6c7ce0c738c31:0x40b2e77be95307b7!8m2!3d39.9656867!4d-75.1680226!9m1!1b1!15sChVyb2JlcnRvIGNsZW1lbnRlIHBhcmuSAQRwYXJr

Output: A csv file with columns for: the url, place name, total number of place reviews, overall place score, amount of reviews by individual, amount of photos by individual, individual place score, date of review, and the review text.



Example run:

  `python extractor.py`
  
  
Example output (see output/parks_reviews_philly):

| url | place_name  | place_score  | num_reviews | user_num_reviews  | user_num_photos  | time  | score  |text  |
| --- | ----------- | ------------ | ----------- | ----------------- | ---------------- |------ | ------ | ---- |
| https://www.google.com/maps/place/20th+%26+Tioga+Street+Park/@40.007803,-75.1616521,562m/data=!3m1!1e3!4m7!3m6!1s0x89c6b80495188afb:0x3012bf09959f9def!8m2!3d40.007803!4d-75.1616521!9m1!1b1 | 20th & Tioga Street Park | 4.2 | 43 | 63 | - | 3 months ago | 5 | Beautiful community garden space in the neighborhood that I grew up in. Happily donated organic collard green seedlings to this space  Please support this space. |
