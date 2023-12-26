# NewsCorp

READEME Contents:
1.0.  How to run the project?
1.1.  Some more stuff...
2.0.  Tools used
2.1.  Poetry
2.2.  Ruff
2.3.  Docker
3.0.  How I approached the problem
4.0.  Folder structure
5.0.  Requirements


## 1.0.  How to run the project?

```bash
./run
``` 

This will build the project and run the code. 
It uses a `sample_hitlog.csv` described in 
the Requirement's example.

The output will be echo'ed in the termianl, 
but can be also found at `data/output/top.csv`

### 1.1.  Some more stuff...

```bash
./run --help  # to see all the commands
```

```bash
./run tests  # run tests
```

```bash
./run ruff  # check Python linting and formatting
```

```bash
./run build  # build image
```

```bash
./run clean  # remove docker image
```


## 2.0.  Tools used

### 2.1.  Poetry
For dependency management, packaging and handling 
the environment. It's not a mandatory tool, but it 
enforces good practices: basic folder structure, 
pyproject file, scripts.

### 2.2.  Ruff
We use Ruff for formatting and linting the code. 
It's quick and it does the job of multiple 
libraries on its own.

### 2.3.  Docker
We dockerise the project so getting the output 
file is possible by one single command, 
regardless of the OS. 

The Dockerfile is meant only for development.


## 3.0. How I approached the problem
The idea is to split the algorithm in three parts:
1. Reading the input data
2. Processing the input data into output data
3. Writing the out data

By separating the work in 3 separate stages, 
it allows us to separate the responsibilities of 
each stage, allowing us to write more modular 
code and easier to test.

For this particular problem, we could have combined 
stage 1. and 2., so reading and processing the input 
data together. It would have enabled us to be a bit 
more optimal with how much data we store in memory and 
reduced a few number of loops. 
However, splitting the reponsibilities assures a better 
long term architecture, but it does come at a cost of 
performance.  


## 4.0.  Folder structure
`data`: Where the `input` and `output` data resides
`newscorp`: App folder, `main.py` is where the app is ran.
`newscorp.modules`: Contains 3 important files:
    `data_modules`: The data structures of the `hitlog` 
    input and output rows 
    `data_processor`: The functions that process the rows
    `file_handler`: The functions that read and write files
`tests`: Tests folder
`run`: Bash script to run project with some extra features
`scripts.py`: Poetry scripts


## 5.0.  Requirements
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
