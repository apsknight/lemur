import time, json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
from request import Request
from checker import Checker
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def reciever():
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('Lemur-key.json', scope)
	client = gspread.authorize(creds)
	sheet = client.open("Lemur Responses").sheet1
	 
	receipents = filter(None, sheet.col_values(3)[1:])

	return receipents

me = "MY EMAIL ID"
        
def foo(new, old, send):
	if not Checker.check(new, old):
		result = Checker.diff(new, old)
		send.append(result)
		return True
	return False

def bar():
	Request.update()
	send = []
	baz = False
	oldnews = json.load(open('json/old/news.json', 'r'))
	newnews = json.load(open('json/new/news.json', 'r'))
	oldevents = json.load(open('json/old/events.json', 'r'))
	newevents = json.load(open('json/new/events.json', 'r'))
	oldnotices = json.load(open('json/old/notices.json', 'r'))
	newnotices = json.load(open('json/new/notices.json', 'r'))
	if foo(newnews['list'], oldnews['list'], send):
		copy('news')
		baz = True
	if foo(newnotices['list'], oldnotices['list'], send):
		copy('notices')
		baz = True
	if foo(newevents['list'], oldevents['list'], send):
		copy('events')
		baz = True

	if baz is True:
		mail(send)

def copy(file):
	nf = open('json/new/%s.json' % file, 'r')
	content = nf.read()
	nf.close()
	of = open('json/old/%s.json' % file, 'w')
	of.write(content)
	of.close()

def mail(send):
	updts = ''
	for upd in send:
		for obj in upd:
			updts = updts + '<center><a href="%s" target="_blank">%s</a><br><br></center>' % (obj['url'], obj['text'])

	header = open('header.txt', 'r')
	footer = open('footer.txt', 'r')
	html = header.read() + updts + footer.read()
	header.close()
	footer.close()
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Lemur Notifier"
	msg['From'] = me
	msg['To'] = 'lemurmailer@amanpratapsingh.in'
	part1 = MIMEText('Hello There! Enable RTF Emails in your account', 'plain')
	part2 = MIMEText(html.encode('utf-8'), 'html')
	msg.attach(part1)
	msg.attach(part2)

	try: 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login('***********', "********")
		you = reciever()
		for email in you:
			print 'trying to send to' + email
			server.sendmail(me, email, msg.as_string())
		server.quit()
		print 'Done'
	except:
		print 'Not Done'

def schedule():
    while True:
        bar()
        time.sleep(1800)

schedule()
