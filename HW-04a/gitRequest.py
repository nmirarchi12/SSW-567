######################################################################
#Author: Nicholas Mirarchi
#gitRequest.py - fetch user git repos and numbers of commits per repo
######################################################################
import requests 
import os 
import unittest 
import json 


def repository_info(username):
    url_for_user='https://api.github.com/users/{}/repos'.format(username)
    op=[]
    response = requests.get(url_for_user)
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
        return 'unable to process request'
    return op
    
def main():
    username = input("Enter the user Github ID here: ")
    #token = input("Enter Github access token here: ")
#username='nmirarchi12'
#token='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'
    for item in repository_info(username):
        print(item)
 
if __name__ == '__main__':
    main()