import datetime
from icalendar import Calendar, Event

startdate = input("Semester Starts on (yyyymmdd): ")
if startdate == '':
	startdate = '20160229'
def week2date(start, week, day):
	"""
	根据开学日期，实现”第X周周X“和”年月日“的互转
	"""
	start = datetime.date(int(start[0:4]), int(start[4:6]), int(start[6:8]))
	return (start+datetime.timedelta(days = (week-1)*7 + day - start.weekday() - 1)).__str__().replace('-', '')
	
def startTime(classno):
	return ['080000','085500','100000','105500','134500','144000','154500','164000','183000','192500'][classno-1]

def endTime(classno):
	return ['085000', '094500','105000','114500','143500','153000','163500','173000','192000','201500'][classno-1]

def toEvent(weekno, weekday, fromclass, toclass, name, location):
	e = Event()
	thedate = week2date(startdate, weekno, weekday)
	e['dtstart'] = thedate+'T'+startTime(fromclass)
	e['dtend'] = thedate+'T'+endTime(toclass)
	e['summary'] = name
	e['location'] = location
	return e

def display(cal):
	return cal.to_ical() #.replace('\r\n', '\n').strip()


cal = Calendar()
cal['dtstart'] = startdate + 'T000000'
cal['summary'] = 'Course Calendar'
print('Calendar Created Successfully.')
print(display(cal))

f = input('Action (1: New Record else: Exit): ')
while f == '1':
	fromweek = int(input('Starting week number (1~18): '))
	toweek = int(input('Ending week number (1~18): '))
	weekday = int(input('Weekday (1~7): '))
	fromclass = int(input('From class (1~10): '))
	toclass = int(input('To class (1~10): '))
	name = input('Course name: ')
	location = input('Location: ')
	oddeven = input('Weeks (0: all, 1: odd, 2: even): ')
	for weekno in range(fromweek, toweek + 1):
		if (oddeven == '1' and weekno % 2 == 0) or (oddeven == '2' and weekno % 2 == 1):
			continue
		cal.add_component(toEvent(weekno, weekday, fromclass, toclass, name, location))
		print('Event Added.')
	print(display(cal))
	f = input('1: New Record\nelse: Exit')

f = open('output.ics', 'wb')
f.write(cal.to_ical())
f.close()
