"""
File: sql_attacks.py
Authors: CSE453 Group 4
Purpose: To demonstrate the ability to harden code against SQL attacks.
"""

# Write a function to accept two strings (username and a password) and return 
# a single string (SQL)
def query(username, password):
    """
    This function accepts two parameters, a username and a password. It takes these,
    forms an SQL query with it, and returns it as a string.
    Parameters: username - string containing a username
                password - string containing a password
    Return:     SQL response - string containing the SQL query
    """
    return f"""
        SELECT authenticate 
        FROM passwordlist 
        WHERE name='{username}' 
        and passwd='{password}';
    """


# Generate a set of cases (one for each member of your team) that represent 
# valid input where the username and the password consist of letters, numbers, 
# and underscores. This function will return member valid test cases.
def valid_tests():
    """
    This function accepts no parameters, but returns a list of valid usernames
    and passwords.
    Parameters: none
    Return:     valid_test_cases - list of valid usernames and passwords
    """    
    # left string in each list is the username, right is password
    valid_test_cases = [
        ["First_User_2day", "On3_S3cr3t_P4sswd"],
        ["2nd_User_2morow", "Th!sIs@S3creT"],
        ["Third_User,2uesday", "My_sup3r_SeCr3t_P455W0rd"],
        ["", ""],
        ["", ""],
        ["", ""]
    ]
    return valid_test_cases


# Create a function that feeds these test cases through the query function 
# and displays the resulting query
def test_valid(valid_tests):
    """
    This function accepts one parameter, a list containing valid usernames
    and passwords. It then loops through the test cases, calls the query
    function with each test case set of username and password, and displays 
    the query response.
    Parameters: valid_tests - list containing test cases of valid usernames
                              and passwords
    Returns:    nothing
    """
    # display type tests being run
    print(f"\n\033[1;31m{'Running valid test cases'}\033[00m")

    # loop through valid test cases, print output
    for test in valid_tests:

        # break test list down for clarity
        username = test[0]
        password = test[1]

        # print arguments passed to query
        print(f"Query arguments - Username: {username}, Password: {password}")
        
        # print query response
        print(f"SQL query: {query(username, password)}")


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a tautology attack. This function will return member valid 
# test cases.
def tautology_tests():
    """
    This function accepts no parameters, but returns a list of valid usernames
    and malformed passwords for a tautology attack.
    Parameters: none
    Return:     tautology_test_cases - list of usernames and tautology passwords
    """
    # left string in each list is the username, right is password
    tautology_test_cases = [
        ["User_Listed2", "nope' OR 'z' = 'z'"],
        ["Number1User!", "Nada' OR 'a' = 'a'"],
        ["Usuh_numba3", "Zilch OR 'b' = 'b'"],
        ["", ""],
        ["", ""],
        ["", ""]
    ]
    return tautology_test_cases


# Create a function that feeds these tautology test cases through the query 
# function and displays the output.
def test_tautology(tautology_tests, title):
    """
    This function accepts two parameters, a list containing test cases potentially
    designed for a tautology attack using malformed usernames and passwords, and 
    a title for the tests being run. It will display the test type title, loop 
    through the set of test cases, call the query function for each set of username
    password, and display the query response.
    Parameters: tautology_tests - list of potentially malformed usernames and passwords
    Return:     nothing 
    """
    # display type tests being run
    print(f"\n\033[1;31m{title}\033[00m")

    # loop through valid test cases, print output
    for test in valid_tests:

        # break test list down for clarity
        username = test[0]
        password = test[1]

        # print arguments passed to query
        print(f"Query arguments - Username: {username}, Password: {password}")
        
        # print query response
        print(f"SQL query: {query(username, password)}")


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a union query attack. This function will return member union 
# attack test cases.
def union_tests():
    """
    This function accepts no parameters, but returns a list of valid usernames
    and malformed passwords for a union attack.
    Parameters: none
    Return:     union_test_cases - list of usernames and union attack passwords
    """
    # left string in each list is the username, right is password
    union_test_cases = [
        ["User_3_Listed", "nope' UNION SELECT authenticate FROM passwordlist"],
        ["ImAnother_user", "nothin' UNION SELECT authenticate FROM passwordlist"],
        ["Whitelisted_user" "negative' UNION SELECT authenticate FROM passwordlist "],
        ["", ""],
        ["", ""],
        ["", ""]
    ] 
    return union_test_cases


# Create a function that feeds these union query test cases through the query 
# function and displays the output 
def test_union(union_tests, title):
    """
    This function accepts two parameters, a list containing test cases potentially
    designed for a union attack using malformed usernames and passwords, and 
    a title for the tests being run. It will display the test type title, loop 
    through the set of test cases, call the query function for each set of username
    password, and display the query response.
    Parameters: union_tests - list of potentially malformed usernames and passwords
    Return:     nothing 
    """
    # display type tests being run
    """print(f"\n\033[1;31m{title}\033[00m")"""

    # loop through union test cases, run_query, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate an additional statement attack. This function will return 
# member additional statement attack test cases.
def additional_statement_tests():
    """
    This function accepts no parameters, but returns a list of valid usernames
    and malformed passwords for an additional statement attack.
    Parameters: none
    Return:     additional_statement_test_cases - list of usernames and additional 
                                                  statement attack passwords
    """
    # left string in each list is the username, right is password
    additional_statement_test_cases = [
        ["One_4_User", "none' ; ALTER TABLE passwordlist DROP COLUMN name"],
        ["additional_user", "nope' ; ALTER TABLE passwordlist DROP COLUMN passwordlist"],
        ["This_user_awesome", "zero' ; ALTER TABLE passwordlist DROP COLUMN keyword"],
        ["", ""],
        ["", ""],
        ["", ""]
    ] 
    return additional_statement_test_cases


# Create a function that feeds these additional statement query test cases 
# through the additional statement function and displays the output 
def test_additional_statement(additional_statement_tests, title):
    """
    This function accepts two parameters, a list containing test cases potentially
    designed for an additional statement attack using malformed usernames and passwords, 
    and a title for the tests being run. It will display the test type title, loop 
    through the set of test cases, call the query function for each set of username
    password, and display the query response.
    Parameters: additional_statement_tests - list of potentially malformed usernames 
                                             and passwords
    Return:     nothing 
    """
    # display type tests being run
    """print(f"\n\033[1;31m{title}\033[00m")"""
    
    # loop through additional statement test cases, run query, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a comment attack. This function will return member comment
# attack test cases.
def comment_tests():
    """
    This function accepts no parameters, but returns a list of corrupt usernames
    and valid passwords for a comment attack.
    Parameters: none
    Return:     comment_test_cases - list of comment usernames and valid passwords
    """
    # left string in each list is the username, right is password
    comment_test_cases = [
        ["Admin'; -- and passwd='DoesNotMatter';", "On3_53cr3t_P455w0rd"],
        ["Admin'; -- and passwd='NotRequired';", "V3rySecr3tStuff!"],
        ["Admin'; -- and passwd='Undisclosed';", "My_sup3r_SeCr3t_K3yW0rD"],
        ["", ""],
        ["", ""],
        ["", ""]
    ] 
    return comment_test_cases 


# Create a function that feeds these comment test cases through the query 
# function and displays the output 
def test_comment(comment_tests, title):
    """
    This function accepts two parameters, a list containing test cases potentially
    designed for a comment attack using malformed usernames and passwords, and 
    a title for the tests being run. It will display the test type title, loop 
    through the set of test cases, call the query function for each set of username
    password, and display the query response.
    Parameters: comment_tests - list of potentially malformed usernames and passwords
    Return:     nothing 
    """
    # display type tests being run
    """print(f"\n\033[1;31m{title}\033[00m")"""
    
    # loop through comment test cases, print output
    pass


# Create a function to provide a weak mitigation against all four attacks. 
# This function accepts the input as a parameter (or two!) and returns the 
# sanitized input.
def weak_mitigation(test_cases):
    """
    This function accepts a set of test cases (list of usernames and passwords)
    as a parameter which may be malformed. It then uses weak mitigation strategy 
    to sanitize them. Finally, it returns the sanitized list of test cases.
    Parameters: test_cases - list of possibly malformed usernames and passwords
    Return:     sanitized_tests - list of weakly sanitized usernames and passwords
    """
    # create list to hold the lists of sanitized usernames and passwords
    sanitized_tests = []    
    
    # loop through each test case in test cases list
    for case in test_cases:

        # create new list to hold sanitized case username and password
        sanitized_list = []
        
        # separate out username and password
        test_username = case[0]
        test_password = case[1]
    
        # call weakly_sanitized on username and password lists and append to 
        # the sanitized list for each test case
        sanitized_list.append(weakly_sanitized(list(test_username)))
        sanitized_list.append(weakly_sanitized(list(test_password)))

        # build new sanitized tests list
        sanitized_tests.append(sanitized_list)
     
    # return weak mitigation sanitized test cases
    return sanitized_tests


# function to strip blacklisted characters from inputs and not duplicate code in 
# weak_mitigation function
def weakly_sanitized(corrupt_data):
    """
    This is a helper function for the weak_mitigation function. It serves to prevent 
    duplication of code and provide functionality for stripping out forbidden 
    characters from the corrupt_data string parameter. It returns the sanitized
    string.
    Parameters: corrupt_data - string containing potentially corrupting characters
    Return:     sanitized_string - string stripped of corrupting characters
    """    
    # set defaults for new sanitized string and corrected list
    sanitized_string = ""
    corrected_list = list(corrupt_data)

    # loop through each element in corrupt data list
    for character in corrupt_data:

        # if forbidden char is found, delete it from the username list
        if character == '\'' or character == ";" or character == "--" or character == "\"":
            index = corrected_list.index(character)
            corrected_list.pop(index)

    # build the sanitized username string and append it to the sanitized list for return
    for element in corrected_list:        
        sanitized_string += element
    
    # return the sanitized string
    return sanitized_string

        
# Create a function to provide a strong mitigation against all command 
# injection attacks. This function accepts the input as a parameter (or two!) 
# and returns the sanitized input.
def strong_mitigation(test_cases):
    """
    This function accepts a list of potentially malformed usernames and passwords, uses
    strong mitigation strategy to prevent access to the interpreter of the corrupt data,
    and returns a list of sanitized usernames and passwords.
    Parameters: test_cases - list of potentially malformed usernames and passwords
    Return:     sanitized_tests - list of sanitized usernames and passwords
    """
    # create list to hold the lists of sanitized usernames and passwords
    sanitized_tests = []    
    
    # loop through each test case in test cases list
    for case in test_cases:

        # create new list to hold sanitized case username and password
        sanitized_list = []
        
        # separate out username and password
        test_username = case[0]
        test_password = case[1]
    
        sanitized_list.append(strongly_sanitized(test_username))
        sanitized_list.append(strongly_sanitized(test_password))

        # build new sanitized tests list
        sanitized_tests.append(sanitized_list)

    # return the strong sanitized test cases     
    return 


# function to keep from duplicating code in strong_mitigation function    
def strongly_sanitized(test_string):
    """
    This is a helper function for the strong_mitigation function. It serves to prevent 
    duplication of code and provide functionality for providing valid input to the
    interpreter by sanitizing the test_string string parameter using strong mitigation
    strategy. It then returns the sanitized string.
    Parameters: test_string - string containing potentially malicious username or password
    Return:     sanitized_string - string cleansed and made a valid input for interpreter
    """
    # split test string into list elements by spaces
    test_list = test_string.split()

    # set defaults for the return sanitized string and a work string
    sanitized_string = ""
    corrected_list = []
    
    # create list of forbidden characters to check against
    forbidden_characters = ["\'", "\'", ";", "--"]

    # if test list is more than one element, corrected list becomes test_list[0]
    if len(test_list) > 1:
        corrected_list = list(test_list[0])

    # otherwise, corrected list become equal to the test_list    
    else:
        corrected_list = list(test_list)    
    
    # check for forbidden characters in the corrected list
    for character in forbidden_characters:
        if character in corrected_list:
            index = corrected_list.index(character)
            corrected_list.pop(index)

    # build the sanitized string from the corrected list elements
    for element in corrected_list:        
        sanitized_string += element

    # return the sanitized string
    return sanitized_string


# main function
def main():
    """
    This is the main function which drives the program. All functions as
    defined by the assignment are first called directly with the associated
    test cases, next called using the weak mitigation function, and finally
    called using the strong mitigation function. It accepts no parameters and
    returns nothing.
    Parameters: none
    Return:     nothing
    """
    # run valid test cases
    test_valid(valid_tests())

    # run tautology test cases
    test_tautology(tautology_tests(), "Running tautology test cases")

    # run union test cases
    test_union(union_tests(), "Running union test cases")

    # run additional statement test cases
    test_additional_statement(additional_statement_tests(), \
                              "Running additional statement test cases")

    # run comment test cases
    test_comment(comment_tests(), "Running comment test cases")

    # run tautology tests using weak mediation
    test_tautology(weak_mitigation(tautology_tests()), \
                   "Running tautology test cases with weak mitigation")

    # run union tests using weak mediation
    test_union(weak_mitigation(union_tests()), \
                   "Running union test cases with weak mitigation")

    # run additional statement tests using weak mediation
    test_additional_statement(weak_mitigation(additional_statement_tests()), \
                   "Running additional statement test cases with weak mitigation")

    # run comment tests using weak mediation
    test_comment(weak_mitigation(comment_tests()), \
                   "Running comment test cases with weak mitigation")  

    # run tautology tests using strong mediation
    test_tautology(strong_mitigation(tautology_tests()), \
                   "Running tautology test cases with strong mitigation")

    # run union tests using strong mediation
    test_union(strong_mitigation(union_tests()), \
                   "Running union test cases with strong mitigation")

    # run additional statement tests using strong mediation
    test_additional_statement(strong_mitigation(additional_statement_tests()), \
                   "Running additional statement test cases with strong mitigation")

    # run comment tests using strong mediation
    test_comment(strong_mitigation(comment_tests()), \
                   "Running comment test cases with strong mitigation")
 

# if run directly, run main function
if __name__ == "__main__":
    main()