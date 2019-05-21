from UWaterlooAPI import UWaterlooAPI
from icalendar import Calendar, Event
import requests
import sys

def main():
#TODO: Add language courses, fix XX logic, exclude full courses
#TODO: Exclude practicums, readings and internships
#TODO: What if a course is in 2 lists? (ex: ECE 390)
#TODO: Currently says course is open if a lecture OR tutorial is open: make it so that it checks for both
#TODO: Add course titles (can get enrollment or titles but not both in same query)
#TODO: Exclude courses that conflict with your schedule (in progress)
	try:
		uw = UWaterlooAPI(api_key='"' + sys.argv[1] + '"')
	except:
		print("Usage: python main.py <Your UWaterloo API key>")
		sys.exit()
	
	term = '1195'
	
	# Gets a list of courses offered in the desired term. This will end up being the list of 
	# courses the student can take.
	term_courses = uw.term_courses(term)
	
	# Gets stats on course enrollment
	term_enrollment = uw.term_enrollment(term)
	
	# Initialize lists of available courses in each CSE list
	available_list_A_courses = []
	available_list_B_courses = []
	available_list_C_courses = []
	available_list_D_courses = []
	
	# Open the schedule to check if courses conflict with it (feature in progress)
	course_schedule = []
	'''g = open('download.ics','rb')
	gcal = Calendar.from_ical(g.read())
	for component in gcal.walk():
		if (component.name == "VEVENT"):
			course_schedule.append({'Course': component.get('summary'), 'Days': component.get('rrule')['byday'], 'Start': component.get('dtstart'),'End': component.get('dtend')})
			print component.get('summary')
			print component.get('rrule')['byday']
			print component.get('dtstart')
			print component.get('dtend')
			print component.get('dtstamp')
	g.close()
	'''

	# Courses the student has already taken
	taken_courses = [{'subject':'MSCI', 'catalog_number':'311'},
					 {'subject':'HRM', 'catalog_number':'200'}]
	
	# List A CSE's
	list_A_courses = [{'subject':'BME', 'catalog_number':'381'}, 
					  {'subject':'ECE', 'catalog_number':'390'},
					  {'subject':'ENVS', 'catalog_number':'105'},
					  {'subject':'ERS', 'catalog_number':'215'},
					  {'subject':'ERS', 'catalog_number':'315'},
					  {'subject':'GENE', 'catalog_number':'22A'},
					  {'subject':'GEOG', 'catalog_number':'203'},
					  {'subject':'GEOG', 'catalog_number':'368'},
					  {'subject':'MSCI', 'catalog_number':'422'},
					  {'subject':'MSCI', 'catalog_number':'442'},
					  {'subject':'NE', 'catalog_number':'109'},
					  {'subject':'PHIL', 'catalog_number':'226'},
					  {'subject':'SOC', 'catalog_number':'232'},
					  {'subject':'STV', 'catalog_number':'100'},
					  {'subject':'STV', 'catalog_number':'202'},
					  {'subject':'STV', 'catalog_number':'203'},
					  {'subject':'STV', 'catalog_number':'205'},
					  {'subject':'STV', 'catalog_number':'210'},
					  {'subject':'STV', 'catalog_number':'302'},
					  {'subject':'STV', 'catalog_number':'404'},
					  {'subject':'SYDE', 'catalog_number':'261'},
					  {'subject':'WS', 'catalog_number':'205'}]
			
	# List B CSE's				  
	list_B_courses = [{'subject':'BME', 'catalog_number':'364'}, 
					  {'subject':'CIVE', 'catalog_number':'392'}, 
					  {'subject':'ECE', 'catalog_number':'390'}, 
					  {'subject':'GENE', 'catalog_number':'22B'}, 
					  {'subject':'MSCI', 'catalog_number':'261'}, 
					  {'subject':'SYDE', 'catalog_number':'262'}]
	
	# Subjects where all courses count as a list C CSE				  
	list_C_all_courses = ['ANTH',
						  'CLAS',
						  'HRM',
						  'PACS',
						  'SMF',
						  'STV']
	
	# Subjects where all courses except for a few exceptions count as a list C CSE
	list_C_all_courses_with_exceptions = ['ECON',
										  'ENGL',
										  'HIST',
										  'PHIL',
										  'PSCI',
										  'PSYCH',
										  'RS',
										  'SDS',
										  'SOCWK',
										  'SOC',
										  'WS']
	
	# All courses in these subjects are accepted as list C CSE's except for these
	list_C_exceptions = [{'subject':'ECON', 'catalog_number':'211'},
						 {'subject':'ECON', 'catalog_number':'221'},
						 {'subject':'ECON', 'catalog_number':'311'},
						 {'subject':'ECON', 'catalog_number':'321'},
						 {'subject':'ECON', 'catalog_number':'371'},
						 {'subject':'ECON', 'catalog_number':'404'},
						 {'subject':'ECON', 'catalog_number':'405'},
						 {'subject':'ECON', 'catalog_number':'411'},
						 {'subject':'ECON', 'catalog_number':'412'},
						 {'subject':'ECON', 'catalog_number':'421'},
						 {'subject':'ECON', 'catalog_number':'422'},
						 {'subject':'ECON', 'catalog_number':'471'},
						 {'subject':'ENGL', 'catalog_number':'109'},
						 {'subject':'ENGL', 'catalog_number':'119'},
						 {'subject':'ENGL', 'catalog_number':'129R'},
						 {'subject':'ENGL', 'catalog_number':'140R'},
						 {'subject':'ENGL', 'catalog_number':'141R'},
						 {'subject':'ENGL', 'catalog_number':'210E'},
						 {'subject':'ENGL', 'catalog_number':'210F'},
						 {'subject':'HIST', 'catalog_number':'4XX'},
						 {'subject':'PHIL', 'catalog_number':'145'},
						 {'subject':'PHIL', 'catalog_number':'200J'},
						 {'subject':'PHIL', 'catalog_number':'216'},
						 {'subject':'PHIL', 'catalog_number':'240'},
						 {'subject':'PHIL', 'catalog_number':'256'},
						 {'subject':'PHIL', 'catalog_number':'359'},
						 {'subject':'PHIL', 'catalog_number':'441'},
						 {'subject':'PSCI', 'catalog_number':'314'},
						 {'subject':'PSCI', 'catalog_number':'315'},
						 {'subject':'PSYCH', 'catalog_number':'256'},
						 {'subject':'PSYCH', 'catalog_number':'261'},
						 {'subject':'PSYCH', 'catalog_number':'291'},
						 {'subject':'PSYCH', 'catalog_number':'292'},
						 {'subject':'PSYCH', 'catalog_number':'307'},
						 {'subject':'PSYCH', 'catalog_number':'312'},
						 {'subject':'PSYCH', 'catalog_number':'317'},
						 {'subject':'PSYCH', 'catalog_number':'391'},
						 {'subject':'RS', 'catalog_number':'131'},
						 {'subject':'RS', 'catalog_number':'132'},
						 {'subject':'RS', 'catalog_number':'133'},
						 {'subject':'RS', 'catalog_number':'134'},
						 {'subject':'RS', 'catalog_number':'233'},
						 {'subject':'SDS', 'catalog_number':'150R'},
						 {'subject':'SDS', 'catalog_number':'250R'},
						 {'subject':'SDS', 'catalog_number':'251R'},
						 {'subject':'SDS', 'catalog_number':'350R'},
						 {'subject':'SDS', 'catalog_number':'398R'},
						 {'subject':'SDS', 'catalog_number':'399R'},
						 {'subject':'SOCWK', 'catalog_number':'390A'},
						 {'subject':'SOCWK', 'catalog_number':'390B'},
						 {'subject':'SOCWK', 'catalog_number':'398R'},
						 {'subject':'SOCWK', 'catalog_number':'399R'},
						 {'subject':'SOC', 'catalog_number':'221'},
						 {'subject':'SOC', 'catalog_number':'280'},
						 {'subject':'SOC', 'catalog_number':'322'},
						 {'subject':'SOC', 'catalog_number':'498'},
						 {'subject':'SOC', 'catalog_number':'499A'},
						 {'subject':'SOC', 'catalog_number':'499B'},
						 {'subject':'WS', 'catalog_number':'365'},
						 {'subject':'WS', 'catalog_number':'475'},]
	
	# All other list C CSE's
	list_C_courses = [{'subject':'DRAMA', 'catalog_number':'100'},
					  {'subject':'DRAMA', 'catalog_number':'200'},
					  {'subject':'EASIA', 'catalog_number':'201R'},
					  {'subject':'ENVS', 'catalog_number':'195'},
					  {'subject':'FR', 'catalog_number':'197'},
					  {'subject':'FR', 'catalog_number':'297'},
					  {'subject':'GENE', 'catalog_number':'22C'},
					  {'subject':'GENE', 'catalog_number':'412'},
					  {'subject':'GEOG', 'catalog_number':'101'},
					  {'subject':'GEOG', 'catalog_number':'202'},
					  {'subject':'GEOG', 'catalog_number':'203'},
					  {'subject':'GEOG', 'catalog_number':'368'},
					  {'subject':'GERON', 'catalog_number':'201'},
					  {'subject':'HLTH', 'catalog_number':'220'},
					  {'subject':'HUMSC', 'catalog_number':'101'},
					  {'subject':'HUMSC', 'catalog_number':'102'},
					  {'subject':'INTST', 'catalog_number':'101'},
					  {'subject':'KIN', 'catalog_number':'352'},
					  {'subject':'KIN', 'catalog_number':'354'},
					  {'subject':'LS', 'catalog_number':'101'},
					  {'subject':'LS', 'catalog_number':'202'},
					  {'subject':'MSCI', 'catalog_number':'211'},
					  {'subject':'MSCI', 'catalog_number':'263'},
					  {'subject':'MSCI', 'catalog_number':'311'},
					  {'subject':'MSCI', 'catalog_number':'411'},
					  {'subject':'MUSIC', 'catalog_number':'140'},
					  {'subject':'MUSIC', 'catalog_number':'245'},
					  {'subject':'MUSIC', 'catalog_number':'253'},
					  {'subject':'MUSIC', 'catalog_number':'256'},
					  {'subject':'MUSIC', 'catalog_number':'334'},
					  {'subject':'MUSIC', 'catalog_number':'355'},
					  {'subject':'MUSIC', 'catalog_number':'363'},
					  {'subject':'PLAN', 'catalog_number':'100'},
					  {'subject':'REC', 'catalog_number':'205'},
					  {'subject':'REC', 'catalog_number':'230'},
					  {'subject':'REC', 'catalog_number':'304'},
					  {'subject':'REC', 'catalog_number':'425'}]
	
	# List D CSE's				  
	list_D_courses = [{'subject':'AFM', 'catalog_number':'131'},
					  {'subject':'APPLS', 'catalog_number':'205R'},
					  {'subject':'APPLS', 'catalog_number':'301'},
					  {'subject':'APPLS', 'catalog_number':'304R'},
					  {'subject':'APPLS', 'catalog_number':'306R'},
					  {'subject':'BET', 'catalog_number':'100'},
					  {'subject':'BET', 'catalog_number':'300'},
					  {'subject':'BET', 'catalog_number':'320'},
					  {'subject':'BET', 'catalog_number':'400'},
					  {'subject':'BET', 'catalog_number':'420'},
					  {'subject':'CIVE', 'catalog_number':'491'},
					  {'subject':'ECE', 'catalog_number':'290'},
					  {'subject':'ENGL', 'catalog_number':'109'},
					  {'subject':'ENGL', 'catalog_number':'129R'},
					  {'subject':'ENGL', 'catalog_number':'210E'},
					  {'subject':'ENGL', 'catalog_number':'210F'},
					  {'subject':'EMLS', 'catalog_number':'102R'},
					  {'subject':'EMLS', 'catalog_number':'110R'},
					  {'subject':'EMLS', 'catalog_number':'129R'},
					  {'subject':'ENVE', 'catalog_number':'391'},
					  {'subject':'ENVS', 'catalog_number':'201'},
					  {'subject':'ENVS', 'catalog_number':'401'},
					  {'subject':'GENE', 'catalog_number':'22D'},
					  {'subject':'GENE', 'catalog_number':'315'},
					  {'subject':'GENE', 'catalog_number':'411'},
					  {'subject':'GENE', 'catalog_number':'415'},
					  {'subject':'KIN', 'catalog_number':'155'},
					  {'subject':'MSCI', 'catalog_number':'262'},
					  {'subject':'MSCI', 'catalog_number':'421'},
					  {'subject':'MSCI', 'catalog_number':'454'},
					  {'subject':'ME', 'catalog_number':'401'},
					  {'subject':'MUSIC', 'catalog_number':'100'},
					  {'subject':'MUSIC', 'catalog_number':'231'},
					  {'subject':'MUSIC', 'catalog_number':'240'},
					  {'subject':'MUSIC', 'catalog_number':'246'},
					  {'subject':'MUSIC', 'catalog_number':'254'},
					  {'subject':'MUSIC', 'catalog_number':'255'},
					  {'subject':'MUSIC', 'catalog_number':'260'},
					  {'subject':'MUSIC', 'catalog_number':'361'},
					  {'subject':'PHIL', 'catalog_number':'145'},
					  {'subject':'PHIL', 'catalog_number':'200J'},
					  {'subject':'PHIL', 'catalog_number':'216'},
					  {'subject':'PHIL', 'catalog_number':'256'},
					  {'subject':'PHIL', 'catalog_number':'359'},
					  {'subject':'PSYCH', 'catalog_number':'256'},
					  {'subject':'PSYCH', 'catalog_number':'307'},
					  {'subject':'PSYCH', 'catalog_number':'312'},
					  {'subject':'PSYCH', 'catalog_number':'317'},
					  {'subject':'REC', 'catalog_number':'100'},
					  {'subject':'RS', 'catalog_number':'131'},
					  {'subject':'RS', 'catalog_number':'132'},
					  {'subject':'RS', 'catalog_number':'133'},
					  {'subject':'RS', 'catalog_number':'134'},
					  {'subject':'RS', 'catalog_number':'233'},
					  {'subject':'SPCOM', 'catalog_number':'223'}]
	
	# TODO: Populate this array
	excluded_courses = []

	# Enrollment info must be acquired from a different query than course titles.
	# Go through courses in term_courses and add enrollment info to the courses.
	for course_enrollment in term_enrollment:
		for course in term_courses:
			if course['subject'] == course_enrollment['subject'] and course['catalog_number'] == course_enrollment['catalog_number']:
				course['enrollment_total'] = course_enrollment['enrollment_total']
				course['enrollment_capacity'] = course_enrollment['enrollment_capacity']
			
	# Remove courses that student has already taken from list			
	for course in term_courses:	
		for taken_course in taken_courses:				
			if course['subject'] == taken_course['subject'] and course['catalog_number'] == taken_course['catalog_number']:
				term_courses.remove(course)
	
	# Remove excluded courses, like internships and special topics courses
	for course in term_courses:
		for excluded_course in excluded_courses:
			if course['title'].contains(excluded_course):
				term_courses.remove(course)
	
	for CSE in list_A_courses:	
		subject = CSE['subject']
		course_number = CSE['catalog_number']
		for course in term_courses:					
			if course['subject'] == subject and course['catalog_number'] == course_number:
				term_courses.remove(course)
				
				# Check if course is full, and add it to the available courses list if not
				if course['enrollment_total'] < course['enrollment_capacity']:
					available_list_A_courses.append(course)
					
	for CSE in list_B_courses:	
		subject = CSE['subject']
		course_number = CSE['catalog_number']
		for course in term_courses:
			if course['subject'] == subject and course['catalog_number'] == course_number:
				term_courses.remove(course)
				# Check if course is full, and add it to the available courses list if not
				if course['enrollment_total'] < course['enrollment_capacity']:
					available_list_B_courses.append(course)
					
	for CSE in list_C_courses:	
		course_subject = CSE['subject']
		course_number = CSE['catalog_number']
		for course in term_courses:
			if course['subject'] == course_subject and course['catalog_number'] == course_number:
				term_courses.remove(course)
				# Check if course is full, and add it to the available courses list if not
				if course['enrollment_total'] < course['enrollment_capacity']:
					available_list_C_courses.append(course)
	
	# Remove the courses that don't count as list C CSE's			
	for course in term_courses:
		for UW_course in list_C_exceptions:
			if course['subject'] == UW_course['subject'] and course['catalog_number'] == UW_course['catalog_number']:
				term_courses.remove(course)
			# Check for exclusions of series of courses, ex: HIST 400-series
			#if 'XX' in UW_course['catalog_number']:
			#	if course['subject'] == UW_course['subject'] and course['catalog_number'].startswith(UW_course['catalog_number'][0]):
			#		term_courses.remove(course)
				
	for course in term_courses:
		for subject in list_C_all_courses:
			if course['subject'] == subject:
				term_courses.remove(course)
				# Check if course is full, and add it to the available courses list if not
				if course['enrollment_total'] < course['enrollment_capacity']:
					available_list_C_courses.append(course)
				
	# Print all remaining courses from subjects with "exclude" courses
	for course in term_courses:
		for subject in list_C_all_courses_with_exceptions:
			if course['subject'] == subject:
				term_courses.remove(course)
				# Check if course is full, and add it to the available courses list if not
				if course['enrollment_total'] < course['enrollment_capacity']:
					available_list_C_courses.append(course)
				 
	for CSE in list_D_courses:	
		subject = CSE['subject']
		course_number = CSE['catalog_number']
		for course in term_courses:
			if course['subject'] == subject and course['catalog_number'] == course_number:
				term_courses.remove(course)
				# Check if course is full, and add it to the available courses list if not
				if course['enrollment_total'] < course['enrollment_capacity']:
					available_list_C_courses.append(course)
					
	# print all available courses
	print('\nList A Courses:')	
	for course in available_list_A_courses:
		print(course['subject'] + " " + course['catalog_number'] + " " + course['title'])
	print('\nList B Courses:')	
	for course in available_list_B_courses:
		print(course['subject'] + " " + course['catalog_number'] + " " + course['title'])
	print('\nList C Courses:')	
	for course in available_list_C_courses:
		print(course['subject'] + " " + course['catalog_number'] + " " + course['title'])
	print('\nList D Courses:')	
	for course in available_list_D_courses:
		print(course['subject'] + " " + course['catalog_number'] + " " + course['title'])

if __name__ == "__main__":
	main()
	