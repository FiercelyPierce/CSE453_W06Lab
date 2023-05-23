"""
File: sql_attacks.py
Authors: CSE453 Group 4
Purpose: To demonstrate the ability to harden code against attacks.
"""
import string

# Write a function to accept two strings (username and a password) and return 
# a single string (SQL)
def query(username, password):
    pass

# Generate a set of cases (one for each member of your team) that represent 
# valid input where the username and the password consist of letters, numbers, 
# and underscores. This function will return member valid test cases.
def valid_tests():
    pass

# Create a function that feeds these test cases through the query function 
# and displays the resulting query
def test_valid(valid_tests):

    # loop through valid test cases, print output
    pass

# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a tautology attack. This function will return member valid 
# test cases.
def tautology_tests():
    pass

# Create a function that feeds these tautology test cases through the query 
# function and displays the output.
def test_tautology(tautology_tests):

    # loop through tautology test cases, run query, print output
    pass

# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a union query attack. This function will return member union 
# attack test cases.
def union_tests():
    pass 

# Create a function that feeds these union query test cases through the query 
# function and displays the output 
def test_union(union_tests):

    # loop through union test cases, run_query, print output
    pass

# Generate test cases (again, each team member should generate one test case) 
# that demonstrate an additional statement attack. This function will return 
# member additional statement attack test cases.
def additional_statement_tests():
    pass 

# Create a function that feeds these additional statement query test cases 
# through the additional statement function and displays the output 
def test_additional_statement(additional_statement_test):

    # loop through additional statement test cases, run query, print output
    pass

# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a comment attack. This function will return member comment
# attack test cases.
def comment_tests():
    pass 

# Create a function that feeds these comment test cases through the query 
# function and displays the output 
def test_comment(comment_test):

    # loop through comment test cases, print output
    pass

# Create a function to provide a weak mitigation against all four attacks. 
# This function accepts the input as a parameter (or two!) and returns the 
# sanitized input.
def weak_mitigation(test_cases):
    
    # set default for weak mitigation sanatized test cases
    new_test_cases = []

    # loop through each test case in test cases list
    for case in test_cases:

        # set default for new test case
        new_test_case = ""

        # case test case to a list for sanitizing
        new_case = list(case)

        # loop through each element in current test case
        for letter in case:

            # if forbidden char is found, delete it from the new test case list
            if letter == '\'' or letter == ";":
                index = new_case.index(letter)
                new_case.pop(index)

        # build the cleansed test case and append it to the new test cases list for return
        for element in new_case:        
            new_test_case += element
        new_test_cases.append(new_test_case)
     
    # return weak mitigation sanitized test cases
    return new_test_cases

        
# Create a function to provide a strong mitigation against all command 
# injection attacks. This function accepts the input as a parameter (or two!) 
# and returns the sanitized input.
def strong_mitigation(test_cases):
    
    # set defaults for new test case string and new test cases list
    new_test_case = ""
    new_test_cases = []

    # loop through test cases parameter to validate test cases
    for test_case in test_cases:

        # split each test case by spaces to check for multiple entries
        test_case_list = test_case.split()

        # if the test case has more than one element, use strong mitigation
        # by not allowing the input to reach the sql query command line through
        # removing all inputs
        if len(test_case_list) > 1:
            new_test_case = " "
        
        # if forbidden characters are in the test case, use strong mitigation by
        # not allowing any input to the sql query command line through blanks
        elif "\'" in test_case or ";" in test_case:
            new_test_case = " "
        
        # otherwise, pass the valid test case through the strong mitigation function
        else:
            new_test_case = test_case

        # apppend the sanitized test case to the new test cases list    
        new_test_cases.append(new_test_case)

    # return the strong sanitized test cases     
    return new_test_cases
    


# main function
def main():
    
    # call test_valid(valid_test())

    # call test_tautology(tautology_tests())

    # call test_union(union_tests())

    # call test_additional_statement(additional_statement_tests())

    # call test_comment(comment_tests())

    # call test_tautology(weak_mitigation(tautology_tests()))

    # call test_union(weak_mitigation(union_tests()))

    # call test_additional_statement(weak_mitigation(additional_statement_tests()))

    # call test_comment(weak_mitigation(comment_tests()))  

    # call test_tautology(strong_mitigation(tautology_tests()))

    # call test_union(strong_mitigation(union_tests()))

    # call test_additional_statement(strong_mitigation(additional_statement_tests()))

    # call test_comment(strong_mitigation(comment_tests()))  
    
    pass

# if run directly, run main function
if __name__ == "__main__":
    main()
