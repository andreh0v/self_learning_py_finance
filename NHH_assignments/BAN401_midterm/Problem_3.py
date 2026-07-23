# Problem 3 a list of usernams to be cleaned

raw_usernames = [' Alice ', 'bob', 'ALICE', '', ' Charlie ']
result = []
def problem_3():
    for username in raw_usernames:
        no_whitespace = username.strip()
        lowercase_let = no_whitespace.lower()
        if lowercase_let != "" and lowercase_let not in result:
            result.append(lowercase_let)

    print("-" * 25)
    print(f"Cleaned list: {result}")
    print("-" * 25)
problem_3()