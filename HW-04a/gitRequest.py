# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:04:48 2021
gitRequest.py - fetch user git repos and numbers of commits per repo
@author: nicholas mirarchi
"""
import requests 
import os 
import unittest 
import json 


def repository_info(username):
    url_for_user='https://api.github.com/users/{}/repos'.format(username)
    op=[]
    response = requests.get(url_for_user)
    if response.status_code != 200:
        print("Error... Account not found or no repos exist")
        return False
    jsonData = json.loads(response.text)
    op.append('User: {}'.format(username))
    #print(op)
    counter=0
    try:
        for i in jsonData:
            repo = jsonData[counter]['name']
            url2 = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo)
            response2 = requests.get(url2)
            response_json = json.loads(response2.text)
            #print(len(response_json))
            op.append('Repo: {} Number of commits: {}'.format(repo, len(response_json)))
            counter+=1
    except (TypeError, KeyError, IndexError):
        return False
    for i in op:
        print(i)
    return True

    
def main():
    username = input("Enter the user Github ID here: ")
    repository_info(username)
    #token = input("Enter Github access token here: ")
#username='nmirarchi12'
'
 
if __name__ == '__main__':
    main()