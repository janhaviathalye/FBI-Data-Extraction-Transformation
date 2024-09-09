# -*- coding: utf-8 -*-
# Example main.py
import argparse
import sys

import requests
import json


#Downloads the data from the API if the page number is passed or uses the file location string passed to extract data from the file instead.

def download_data(page=None, thefile=None):
    
    if page is not None:
        response = requests.get('https://api.fbi.gov/wanted/v1/list', params={
        'page': page

    })

        data = json.loads(response.content)

#Ensures that at a time either the page number or the file location is passed.        
    
    elif thefile is not None:
        file_path = thefile
        with open(file_path, 'r') as file:
            content = file.read()
    
        data = json.loads(content)

    
    return data


#Extracts data corresponding to the field values of title, subjects and field offices.
def format_data(item):

    item_list = []
    
    subjects_result = ''
    field_offices_result = ''

    title = item.get('title') if item.get('title') else ''
    
#Separates multiple values per field with a comma.
    subjects = item.get('subjects')
    if subjects is not None: 
        if len(subjects) != 0:
            subjects_result = ", ".join(subjects)
    
#Separates multiple values per field with a comma.
    field_offices = item.get('field_offices')

    if field_offices is not None:
        if len(field_offices) != 0:
            
            field_offices_result = ", ".join(field_offices)

    item_list.append(title)
    item_list.append(subjects_result)
    item_list.append(field_offices_result)
    return item_list

#Separates one field value from the other with a thorn character.
def print_thorn_separated_data(item_list):
    print(f"{item_list[0]}þ{item_list[1]}þ{item_list[2]}")


def main(page=None, thefile=None):
    # Download data

    data = download_data(page, thefile)
    
    for item in data['items']:
        item_list = format_data(item)       #Format data into comma separated values for multiple entries per field
        print_thorn_separated_data(item_list)   #Add the thorn character to separate one field value from the other 



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="An Example API file.")
    parser.add_argument("--page", type=int, required=False, help="An Example API file.")

#Ensures that either the page or file location is passed at a time.     
    args = parser.parse_args()
    if args.page:
        main(page=args.page)
    elif args.file:
        main(thefile=args.file)
    else:
        parser.print_help(sys.stderr)