Lemur
=====
<p align="center"><img src="https://image.ibb.co/c00mcv/rsz_lemur_1312198_640.png"/ alt="Lemur Image"></p>

[![License : MIT](https://img.shields.io/npm/l/express.svg)](http://aps.mit-license.org)
[![Python: 2.7.12](https://img.shields.io/badge/Python-2.7.12-red.svg)](https://www.python.org/downloads/release/python-2712/)
![](https://img.shields.io/badge/Heroku-Not%20Deployed-red.svg)

>A Python project for sending Email notification on IIT BBS News API Updation. The Project is currently functioning to send Email notification of updates on <http://www.iitbbs.ac.in>
 
>[IIT Bhubaneswar News API](https://github.com/dsciitbbs/iitbbsnewsapi) project is used for API Requests.
  
## Features
* Subscription Management through Google Sheets
	* Google Sheets([Why Google Sheet?](https://twitter.com/patio11/status/485239825314758656)) is used for `CRUD` functionality of Email Addresses.
* Email Sending through Python SMTP Library
	* Python's standard Email and SMTP library is used for Email sending.
* HTML Emails
	* Emails are in HTML format, created using ZURB Foundation Framework and Inliner.  

## How to subscribe
Just fill this [Google Form](https://drive.google.com/open?id=1eWPAZ1T_eSPM8YMXR8GKDfAEazQYge3obBrW0qZHuok) and you're on board.

## Further ToDo
* Create Unsubscription Functionality for opting out. `C` and `R` is implemented while `U` and `D` is yet to implement.
* Add other resources like daily weather, quotes of the day, top local and national headlines in Emails.
* Send Email to all users simultaneously. (Currently Emails are sent one by one to each user)
* Code Cleaning and add Documentation in class functions.

## Contributing
Feel free to submit a pull request or an issue. Sugest new features on issue tracker.  
**OR**  
You can [tweet me](https://twitter.com/ultimateaps) for any other info.

## License

Built with ♥ by Aman Pratap Singh([@apsknight](http://amanpratapsingh.in)) under [MIT License](http://aps.mit-license.org/)
