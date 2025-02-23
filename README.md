# FBI Most Wanted List Data Extraction and Transformation

Name: Janhavi Athalye

# Project Description 

This project involved a GET REST API call to the FBI Most Wanted list API to extract data related to the criminal records present. The straightforward GET call could be modified by adding page as a parameter to it which specified the corresponding page number from where the records would be fetched. There were around 20 records present per page number and in total 1077 records in the FBI most wanted list.

Up next, the assignment involved extracting 3 specific fields of data from the entire list of fields corresponding to a criminal record. The 3 fields were: title: which specified the individual's name, subjects: which specified the crimes committed by the individual & field_offices: which specified the names of places where investigation has been conducted for the same.

The title was a plain string data type while subjects and field offices were lists so I had to be careful as to not miss any elements from the list while extracting the data as multiple entries from the list were supposed to be made into comma separated values while each data field had to be separated from the other with a thorn character.

The above format was printed on the console for each of the records present in the page number or the file as the function could take either the page number which would make an API call to the FBI Most Wanted list for processing data or the file location which would process the data from the file present in the docs folder.

Finally test cases were written to test the above 3 functions and the assignment was completed successfully!


# How to install
pipenv install -e .

## How to run
pipenv run python main.py --page 1    
--Runs the main.py file for page = 1: can be changed to any other page number.

pipenv run python main.py --file docs/Test2.json      
--Runs the main.py file for Test2.json file present in the docs folder: can be changed to Test1.json since I have 2 test files at the same path.

pipenv run python -m pytest -v
--Runs all the tests together.


## Functions

#### main.py

main.py ensures that either of the page or file location values are passed at a time.

download_data(page=None, thefile=None) - This function makes a GET API call to the FBI Most Wanted list API if the page number is specified or extracts data from the file location mentioned in the command prompt.

format_data(item) - This function extracts data from the json response and saves field values for title, subjects and field offices for each of the records. It separates multiple values per field with a comma. Finally it adds all of this to an item list to use it for printing the required values.

print_thorn_separated_data(item_list) - This function takes the argument item_list and prints out the title, subjects and field offices values for each of the records using the format specified. It separates one field from the other using a thorn character.


