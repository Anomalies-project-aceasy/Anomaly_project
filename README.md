# Anomaly Project

Project Description:
    
    As data analyst we are tasked with investigating student and staff interactions with curriculum published by CodeUp.
    
## Project Goal:

     Resolve the questions below using EDA (exploratory data analysis) techniques:
     
    1.  Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    2. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
    3.  Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    4.  Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    5.  Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?

## Data Dictionary

| Column Name   | Description                                                |
|---------------|------------------------------------------------------------|
| time          | The timestamp when the website was viewed                  |
| viewed        | The specific webpage that was viewed                       |
| user_id       | The unique ID of the user who viewed the webpage           |
| ip            | The IP address of the user who viewed the webpage          |
| cohort_id     | The ID of the cohort associated with the user              |
| name          | The name of the user                                       |
| start_date    | The start date of the cohort the user belongs to           |
| end_date      | The end date of the cohort the user belongs to             |
| program_id    | The ID of the program the user is enrolled in              |

## Steps to Reproduce

    1. Clone this repo
    2. Acquire the data from SQL (must have env.py file with codeup sql credentials)
    3. Put the data in the file containing the cloned repo
    4. Run notebook
    
## Initial Thoughts 

    Our initial thoughts are the dataset is sufficient to answer questions but we may need to engineer features as well.
   
## The Plan

     Discussion
         - Discuss steps to complete the project with team
         - Split the tasks and questions among team members
     Acquire data from sql database
         - Pull relevant data tables only using a SQL query
         - Join the data tables
         - Convert to DataFrame
         - Create CSV
         - Look at the dataset
         - Confirm understanding of all variables
         - Create a data dictionary
     Prepare data
         - Identify nulls/Nan and replace them with the mean or get rid of that column if there are too many nulls/Nans
         - Remove columns that have irrelevant information such as slack name
         - Remove duplicate information
         - Change column names to make them readable
         - Remove rows with viewed items that provide no value, such as the homepage and table of contents
     Explore
        - Identify approach options for each question 
        - Include defining terms within questions such as "suspicious" in question 4
        - Add necessary columns/features per question being investigated
     Summarize
        - Describe findings at the end of each question
        - Formulate succinct email of findings
        - Create a single slide visualization
        
     
## Explore data

     Answer the following questions:
     
        1.  Which lesson appears to attract the most traffic consistently across cohorts (per program)?
        
    2. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
    
    3.  Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    
    4.  Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    
    5.  Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
       
            
     
    
## Takeaways and Conclusions

    The use of codeup curriculum is affected by, both, policy and the behavior of staff and students.  

## Recommendations

    The dataset may allow even greater utility if the grades (per unit/project/grades/etc) of students, and push habits were made available; this may allow us to identify challenge points for the organization and students. 