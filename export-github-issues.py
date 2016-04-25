import requests
import getpass
import csv

GITHUB_USER = raw_input("Enter github username: ")
GITHUB_PASSWORD = getpass.getpass("Enter github password (hidden): ")
REPO = raw_input("Repo name username/reponame: ")

# Use this for passing credentials as arguments
# GITHUB_USER = sys.argv[1]
# GITHUB_PASSWORD = sys.argv[2]
# REPO = sys.argv[3] # format is username/repo


ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues' % REPO

csvfile = '%s-issues.csv' % (REPO.replace('/', '-'))
csvout = csv.writer(open(csvfile, 'wb'))
csvout.writerow(('id', 'Created by', 'Title', 'Labels', 'Created At', 'Updated At'))

response = requests.get(ISSUES_FOR_REPO_URL)
for issue in response.json():
	csvout.writerow([issue['number'],issue['user']['login'],issue['title'].encode('utf-8'),','.join([i['name'] for i in issue['labels']]),issue['created_at'],issue['updated_at']])