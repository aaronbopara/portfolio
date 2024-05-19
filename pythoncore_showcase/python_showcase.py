#These are a selection of functions I have developed to showcase some of my core python skills
#The relevant .csv files are located in the repositories file folder 
#This workbook will focus on python core skills and pandas 



#Palindrome Numbers 

"""
A palindrome number is a number that remains the same when its digits are reversed, such as 3, 121, 14641 etc.
This example is a function that takes a list of elements, `input_list`, and returns another list. 
The result list should contain `True` for palindrome numbers in the input list,`False` for non-palindrome numbers,
and `None` for non-integer elements.
"""

def palindrome_numbers1(input_list: list):
    output_list = [] 
    for number in input_list : 
        if type(number) == int : 
            number = str(number)
            if number == number[::-1] : 
                output_list.append(True)
            else : output_list.append(False)
        elif type(number) != int : 
            output_list.append(None)
    return output_list 




#Split Odd and Even Elements

"""
This example is a function which accepts a single input argument, `input_list` of integers, and returns a tuple of two lists. 
The first list in the tuple contains the odd integers present in the input list. 
The second list should contain the even integers present in the input list.
""" 

def split_odd_even(input_list : list) : 
    odd_list = []
    even_list = [] 
    output_tuple = () 
    for number in input_list : 
        if type(number) == int : 
            if number%2 == 0 : 
                even_list.append(number)
            if number%2 != 0 : 
                odd_list.append(number)

    output_tuple = (odd_list, even_list)

    return output_tuple 




#Get UK Bank Holidays

"""
This example calls an API from `https://www.gov.uk/bank-holidays.json` to retrieve information about UK bank holidays. 
The function takes two input arguments, `region` and `year` - specifying the region (options: 'england-and-wales', 
'scotland', or 'northern-ireland'), and the year for which bank holidays are requested.
It returns a list of tuples, each of which contain the bank holiday name and the bank holiday date.#
""" 

def get_uk_bank_holidays(region: str, year: int):
    import requests
    url = r'https://www.gov.uk/bank-holidays.json'
    bank_holidays = []
    response = requests.get(url)
    response_dict = response.json()
    region_specific_events = response_dict[region]['events']
    for holiday in region_specific_events:
        if holiday['date'][0:4] == str(year):
            holiday_name = holiday['title']
            holiday_date = holiday['date']
            bank_holidays.append((holiday_name, holiday_date))
    return bank_holidays




#Name Processing

"""
This is a function which accepts a list, `list_of_names`, which contains full name strings. 
Each string consists of a first name, optional middle name, and a surname, separated by spaces. 
The function returns a list containing these same names, but with the surname written first, 
followed by a comma, then the first name. If a middle name is present, append only its first letter, 
followed by full-stop 
This functions also ensures itworks with more than one middle name, i.e. each middle name is 
replaced by its first initial and a full stop.
"""

def name_processing5(list_of_names:list) : 
    processed_names = []
    for full_name in list_of_names : 
        components = full_name.split()
        if len(components) >= 2 : 
            first_name = components[0]
            surname = components[-1]
            middle_initials = '.'.join(name[0] for name in components [1:-1])
            processed_name = f'{surname}, {first_name} {middle_initials}'
            processed_names.append(processed_name)
        else : print('input is invalid')
    return processed_names




# Interests In Common

""" 
Three friends have provided lists of their interests. Each interest is a lower-case string.
This is a function which takes in these three lists and returns a list of the interests they have in common. 
If there are no common interests, or if the lists of interests are all empty, the function should return an empty list.
"""


def interests_in_common(list1: list, list2: list, list3: list):
    common_interests_list = []
    if len(list1) > 0 : 
        if len(list2) > 0 : 
            if len(list3) > 0 : 
                common_interests =  set(list1) & set(list2) & set(list3)
                common_interests_list = list(common_interests)
    else : pass 
    return common_interests_list




#My Logger

"""
This function creates a mock logging class called `MyLogger`.
The `MyLogger` class is initialised with a `disk_space` argument which is an
integer. When initialised, `disk_remaining` should be set to the value of
`disk_space`, i.e. it is assumed that none of the disk has been used at this point.

Instance attributes:
- `disk_space` (int)
- `disk_remaining` (int)

The class also implements three methods:

Methods:
- `disk_full`: Returns `True` if `disk_remaining` is 0, otherwise `False`.
- `log_to_file`: If the disk is not full, the function decrements `disk_remaining` by 1 unit and
    return the string `Successfully logged`.
    Otherwise (if the disk is full), the function returns the string `Disk full`.
- `delete_logs`: Sets `disk_remaining` to `disk_space` and returns the string 
    `Logs deleted`.
    """


class MyLogger:

	def __init__(self, disk_space : int) :
		"""initialising the logger"""
		self.disk_space = disk_space
		self.disk_remaining = disk_space 
	
	def disk_full (self) : 
		"""Checking if the disk is full"""
		if self.disk_remaining == 0 : 
			return True 
		else : return False 
	
	def log_to_file (self) : 
		"Logging a file to the logger"
		if self.disk_remaining > 0 : 
			self.disk_remaining -= 1 
			return 'Successfully logged'
		else : return 'Disk full'

	def delete_logs(self) : 
		"""Deleting all logs in the logger"""
		self.disk_remaining = self.disk_space 
		return 'Logs Deleted'
     

