from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path="C:\\Users\\Julian\\PycharmProjects\\TeeTime\\chromedriver.exe")
url = 'https://foreupsoftware.com/index.php/booking/20965/6318#/teetimes'
driver.get(url)

username = 'jajgcastoro@yahoo.com'
password = 'prf134golf'


def find_tee_time(time, group_size):
    """
    Finds and clicks on teeTime based on user input date and time
                This will always return an earlier time
    """
    tee_time_info_cells = driver.find_elements_by_class_name("pull-left")
    closest_time = 24
    for tee_time_info_cell in tee_time_info_cells:
        # is_right_time = (tee_time_info_cell.find_element_by_class_name("start").text == time)
        is_right_group_size = (int(tee_time_info_cell.find_element_by_class_name("spots").text) >= int(group_size))
        time_difference = return_difference_in_time(time, tee_time_info_cell.find_element_by_class_name("start").text)

        if time_difference < closest_time and is_right_group_size:
            best_match = tee_time_info_cell
            closest_time = time_difference

    best_match.click()  # selects best fit tee time

def get_user_info():
    # user input -_____- This will be replaced by tkinter GUI eventually
    print("What Day would you like to book your tee time for?")
    date = input("Please enter date in format MM/DD/YYYY")
    # date = "08/27/2021"

    print("What time would you like to book your tee time for?")
    time = input("Please enter time in format 12:30am or 4:00pm")
    # time = "5:00pm"

    print("How many people will be in your group?")
    size = input("Please enter number of people")
    # size = "1"

    # cart = True
    cart = input("Are you walking or riding?")
    if cart.lower() == 'walking':
        cart = False
    else:
        cart = True

    return date, time, size, cart

def return_difference_in_time(requested_time, possible_time):
    """ Will return the decimal absValue difference between requested time and possible time."""
    # ex req. time = 3:30pm
    # convert requested time to decimal
    if requested_time[-2:] == "pm":
        # comparison code
        hours = int(requested_time[:-5])
        hours += 12  # find the hours
        # hours = 15
        minutes = requested_time[-4:-2]
        minutes = int(minutes)
        min_as_hours = minutes / 60.0  # find the decimal representation of minutes
        # min as hours = .5
    # 3:30pm now = 15.5
    else:  # "am"
        # comparison code
        hours = int(requested_time[:-5])
        minutes = requested_time[-4:-2]
        minutes = int(minutes)
        min_as_hours = minutes / 60.0
        print(min_as_hours)
    decimal_requested_time = hours + min_as_hours  # combine them


    # convert possible time to decimal
    if possible_time[-2:] == "pm":
        # comparison code
        hours = int(possible_time[:-5])
        hours += 12  # find the hours
        minutes = int(possible_time[-4:-2])
        min_as_hours = minutes / 60.0  # find the decimal representation of minutes
        # 3:30pm now = 15.5
    else:  # "am"
        # comparison code
        hours = int(possible_time[:-5])
        minutes = possible_time[-4:-2]
        minutes = int(minutes)
        min_as_hours = minutes / 60.0

    decimal_possible_time = hours + min_as_hours  # combine them
    difference = abs(decimal_possible_time - decimal_requested_time)
    return difference



target_date, target_time, group_size, want_cart = get_user_info()


# click on resident member
driver.find_element_by_xpath('//*[@id="content"]/div/button[1]').click()
driver.implicitly_wait(10)

# click on Log in
driver.find_element_by_xpath('//*[@id="teetime-login"]/div/p[1]/button').click()

# Enter email
driver.find_element_by_xpath('//*[@id="login_email"]').send_keys(username)

# Enter PW
driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(password)

# press login
driver.find_element_by_xpath('//*[@id="login"]/div/div[3]/div/button[1]').click()
# driver.implicitly_wait(10)

# click my reservations
driver.find_element_by_xpath('//*[@id="reservations-tab"]').click()

# click on reserve a time now
driver.find_element_by_xpath('//*[@id="profile-main"]/div/ul/li/a').click()
driver.implicitly_wait(10)

# date field clearing and entering target date
driver.find_element_by_xpath('//*[@id="date-field"]').send_keys(Keys.CONTROL, "a", Keys.DELETE)
driver.find_element_by_xpath('//*[@id="date-field"]').send_keys(target_date)
driver.find_element_by_xpath('//*[@id="date-field"]').send_keys(Keys.ENTER)

time.sleep(2)  # sleep for 2 seconds to wait for the elements refresh after date entry

find_tee_time(target_time, group_size)
driver.implicitly_wait(10)

if int(group_size) == 1:
    driver.find_element_by_xpath('// *[ @ id = "book_time"] / div / div[2] / div[5] / div[1] / div / a[1]').click()


elif int(group_size) == 2:
    driver.find_element_by_xpath('// *[ @ id = "book_time"] / div / div[2] / div[5] / div[1] / div / a[2]').click()


elif int(group_size) == 3:
    driver.find_element_by_xpath('// *[ @ id = "book_time"] / div / div[2] / div[5] / div[1] / div / a[3]').click()
else:
    pass
    # 4 is default

# cart?
if want_cart:
    driver.find_element_by_xpath('// *[ @ id = "book_time"] / div / div[2] / div[5] / div[2] / div / a[2]').click()








# now we need to get a list of all the different tee times available

# tee_times = driver.find_elements_by_class_name('start')
#
# for tee_time in tee_times:
#     if tee_time.text == target_time:
#         print(tee_time.text)
#         tee_time.click()


# book time xpath
# //*[@id="book_time"]/div/div[3]/button[1]
# driver.find_element_by_xpath('//*[@id="book_time"]/div/div[3]/button[1]').click()


