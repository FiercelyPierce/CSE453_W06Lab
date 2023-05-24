"""
File: sql_attacks.py
Authors: CSE453 Group 4
Purpose: To demonstrate the ability to harden code against SQL attacks.
"""

# Write a function to accept two strings (username and a password) and return 
# a single string (SQL)
def query(username, password):
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
    
    # left string in each list is the username, right is password
    valid_test_cases = [
        ["First_User_2day", "On3_S3cr3t_P4sswd"],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""]
    ]
    return valid_test_cases


# Create a function that feeds these test cases through the query function 
# and displays the resulting query
def test_valid(valid_tests):

    # loop through valid test cases, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a tautology attack. This function will return member valid 
# test cases.
def tautology_tests():
    
    # left string in each list is the username, right is password
    tautology_test_cases = [
        ["User_Listed2", "nope' OR 'z' = 'z'"],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""]
    ]
    return tautology_test_cases


# Create a function that feeds these tautology test cases through the query 
# function and displays the output.
def test_tautology(tautology_tests):

    # loop through tautology test cases, run query, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a union query attack. This function will return member union 
# attack test cases.
def union_tests():
    
    # left string in each list is the username, right is password
    union_test_cases = [
        ["User_3_Listed", "nope' UNION SELECT validate FROM userPasswords"],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""]
    ] 
    return union_test_cases


# Create a function that feeds these union query test cases through the query 
# function and displays the output 
def test_union(union_tests):

    # loop through union test cases, run_query, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate an additional statement attack. This function will return 
# member additional statement attack test cases.
def additional_statement_tests():
    
    # left string in each list is the username, right is password
    additional_statement_test_cases = [
        ["On3_User", "none' ; ALTER TABLE passwordList DROP COLUMN name"],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""]
    ] 
    return additional_statement_test_cases


# Create a function that feeds these additional statement query test cases 
# through the additional statement function and displays the output 
def test_additional_statement(additional_statement_tests):

    # loop through additional statement test cases, run query, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a comment attack. This function will return member comment
# attack test cases.
def comment_tests():
    
    # left string in each list is the username, right is password
    comment_test_cases = [
        ["Admin'; -- and passwd='DoesNotMatter';", "On3_53cr3t_P455w0rd"],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""],
        ["", ""]
    ] 
    return comment_test_cases 


# Create a function that feeds these comment test cases through the query 
# function and displays the output 
def test_comment(comment_tests):

    # loop through comment test cases, print output
    pass


# Create a function to provide a weak mitigation against all four attacks. 
# This function accepts the input as a parameter (or two!) and returns the 
# sanitized input.
def weak_mitigation(test_cases):

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
     
    """
    Test code
    # print output for now
    for number in range(len(sanitized_tests)):
        print(f"Original: Username - {test_cases[number][0]}, Password - {test_cases[number][1]}")
        print(f"Weak mitigation: Username - {sanitized_tests[number][0]}, Password - {sanitized_tests[number][1]}")
    """

    # return weak mitigation sanitized test cases
    return sanitized_tests


# function to strip blacklisted characters from inputs and not duplicate code in weak_mitigation function
def weakly_sanitized(corrupt_data):
    
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

    """
    Test code
    # print output for now
    for number in range(len(sanitized_tests)):
        print(f"Original: Username - {test_cases[number][0]}, Password - {test_cases[number][1]}")
        print(f"Strong mitigation: Username - {sanitized_tests[number][0]}, Password - {sanitized_tests[number][1]}")
    """
    
    # return the strong sanitized test cases     
    return 


# function to keep from duplicating code in strong_mitigation function    
def strongly_sanitized(test_string):

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
    
    # run valid test cases
    # test_valid(valid_test())

    # run tautology test cases
    # test_tautology(tautology_tests())

    # run union test cases
    # test_union(union_tests())

    # run additional statement test cases
    # test_additional_statement(additional_statement_tests())

    # run comment test cases
    # test_comment(comment_tests())

    # run tautology tests using weak mediation
    # test_tautology(weak_mitigation(tautology_tests()))

    """
    WM test code 
    print("\nTautology")
    weak_mitigation(tautology_tests()) # testing weak mitigation with tautology test lists
    """

    # run union tests using weak mediation
    # test_union(weak_mitigation(union_tests()))

    """
    WM test code
    print("\nUnion")
    weak_mitigation(union_tests()) # testing weak mitigation with union tests
    """

    # run additional statement tests using weak mediation
    # test_additional_statement(weak_mitigation(additional_statement_tests()))

    """
    WM test code
    print("\nAdditional Statements")
    weak_mitigation(additional_statement_tests()) # testing weak mitigation with additional statement tests
    """

    # run comment tests using weak mediation
    # test_comment(weak_mitigation(comment_tests()))  

    """
    WM test code
    print("\nComment")
    weak_mitigation(comment_tests()) # testing weak mitigation with comment tests
    print()
    """

    # run tautology tests using strong mediation
    # test_tautology(strong_mitigation(tautology_tests()))

    """
    SM test code
    print("\nTautology")
    strong_mitigation(tautology_tests())
    """

    # run union tests using strong mediation
    # test_union(strong_mitigation(union_tests()))

    """
    SM test code
    print("\nUnion")
    strong_mitigation(union_tests())
    """

    # run additional statement tests using strong mediation
    # test_additional_statement(strong_mitigation(additional_statement_tests()))

    """
    SM test code
    print("\nAdditional Statement")
    strong_mitigation(additional_statement_tests())
    """

    # run comment tests using strong mediation
    # test_comment(strong_mitigation(comment_tests()))

    """
    SM test code
    print("\nComment")
    strong_mitigation(comment_tests())
    print() 
    """ 
    
 

# if run directly, run main function
if __name__ == "__main__":
    main()
