# NewsCorp

## Requirements
When a user visits a page on the NewsCorp website, a record is created in a **Hitlog File** which shows the details of the visit. This file is available for the Data Team on a daily basis.

We want to find out the top 3 NewsCorp articles which lead to users registering on the website.

Build a pipeline in python3 which uses `hitlog.csv` as a source file and output a csv file which has the top 3 influential topics and their total numbers.
- **Hitlog** is a comma delimited csv file with the following fields: `page_name`, `page_url`, `user_id`, `timestamp`
- Registration url is `/register`
- Article url prefix is `/articles/`
- Output file should be comma delimited csv file with the following fields: `page_name`, `page_url`, `total`
- Try to write reusable, maintainable code
- Include unit testing as part of your code

## Example 
We have three different journeys for three different users:
`user1`: `article#1` -> `article#2` -> `article#3` -> **registration** 
`user2`: `article#1` -> **registration**
`user3`: `article#2` -> `article#1` -> **registration**
`article#1` is the most influential article with a total number of 3 as it was part of all journeys.
