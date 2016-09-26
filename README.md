# WebDevelopment
Multiple web projects on Google App Engine

## 1. Display Valid Birthday (myapp1)

This is a simple webpage to get the valid birthday month, day and year. If not valid, an error message will show and invalid message are displayed in text area. If valid, it will redirect to a webpage showing confirmation. 

It's deployed on Google App Engine. 

http://bdaypost-143519.appspot.com/

## 2. ROT13, Validate Username and Password (homework1)

It separates three webpages HTMLs and python codes. 

/rot13 will convert 'a-zA-Z' in multiple lines to the characters 13 letters after it. Therefore, when click 'Submit' twice, it will convert to the original input. 
Ex. 
adfasg 3rqweqewr
afdadsfa

will convert to 
nqsnft 3edjrdrje
nsqnqfsn

http://userlog-144601.appspot.com/hq2/rot13

/signup is a new user sign up webpage, which will be further extended to a real application with MySQL database. The username is 'a-zA-Z0-9-_' 3-20 characters and will show 'This is not a valid username.' if not satisfied. password is 3-20 characters and verified with another input. If not valid password, it will notify 'This is not a valid password'. If password not match, it will notify 'Your password didn't match.'. Email should be '*@*.com(net,gov)'. If all valid, a welcome webpage will show welcome username. 

http://userlog-144601.appspot.com/hq2/signup



