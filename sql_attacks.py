"""
File: sql_attacks.py
Authors: CSE453 Group 4
Purpose: To demonstrate the ability to harden code against attacks.
"""

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
    pass

# Create a function to provide a strong mitigation against all command 
# injection attacks. This function accepts the input as a parameter (or two!) 
# and returns the sanitized input.
def strong_mitigation(test_cases):
    pass

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
