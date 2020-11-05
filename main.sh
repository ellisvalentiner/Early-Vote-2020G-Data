#!/bin/zsh
#
# Scrape data from the U.S. Elections Project Early-Vote-2020G repo

set -euf -o pipefail

# Clone the repo into a temporary directory
if [ ! -d "temp" ]; then
  git clone git@github.com:ElectProject/Early-Vote-2020G.git temp
fi

# Enter the repo directory
cd temp
git fetch && git pull

# Iterate through national (index) and state reports
for state in AK AL AR AZ CA CO CT DC DE FL GA HI IA ID IL IN KS KY LA MA MD ME MI MN MO MS MT NC ND NE NH NJ NM NV NY OH OK OR PA RI SC SD TN TX UT VA VT WA WI WV WY
do
  echo "Processing state: ${state}"
  # List each commit containing changes for HTML page
  for commit in $(git log --pretty=format:%H --diff-filter=AM -- docs/${state}.html)
  do
    echo "Processing commit: ${commit}"
    # Show the HTML document at that commit
    git show ${commit}:docs/${state}.html > ../tmp.html
    # Extract information from the page
    STATE=${state} python3 ../data_parser.py
  done
done

# Change directory
cd ../

# Deduplicate records
sort tmp.jsonl | uniq > data.jsonl

# Clean-up
rm tmp.jsonl
rm tmp.html
