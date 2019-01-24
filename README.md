# scripting-challenge-2
A scripting challenge that involved grabing a csv from a gist with user ids, first names and last names, and adding a secure password, and email address and re-sorting it by first name then saving back to csv.


Instructions

Create a script that does the following:

 

1. using a rest call get the CSV from a github gist URI: "https://api.github.com/gists/[protected]"

a. if you receive a SSL/TLS secure channel error; please see here: https://stackoverflow.com/questions/41618766/powershell-invoke-webrequest-fails-with-ssl-tls-secure-channel

2. Add 2 columns to the CSV

    a. Add a password that follows the best practice standard of 8 characters, & 3 of the 4 character types (upper case, lower case, number, and symbol)

    b. add a UPN that is formatted first.last@domain.com (domain name doesn't matter)

3. output the CSV as a CSV file on the local computer

4. bonus: output the CSV sorted by first name
