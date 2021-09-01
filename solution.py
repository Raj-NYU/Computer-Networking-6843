# welcome_assignment_answers
# Input - All eight questions given in the assignment.
# Output - The right answer for the specific question.
# Raj Shah - Computer Networking - NYU.

answer = "answer"


def welcome_assignment_answers(question):
    # The student doesn't have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.
    global answer
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No, encoding is using code such as ASCII and encryption requires a secret key."

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No key is needed."

    # Complete all the questions.
    elif question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "mTLS"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes such as ASCII."

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No, it is used to hide information."

    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "MD5 is not the most secured hashing algorithm compared to SHA-256 and 512."

    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = "Application Layer."

    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = "Transport Layer."

    return answer


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    # debug_question = "Are encoding and encryption the same? - Yes/No"
    # debug_question = "Is it possible to decrypt a message without a key? - Yes/No"
    # debug_question = "In Slack, what is the secret passphrase posted in the cyberfellows-computernetworking-fall2021 channel posted by a TA?"
    # debug_question = "Is it possible to decode a message without a key? - Yes/No"
    # debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No"
    # debug_question = "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
    # debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    # debug_question = "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
    debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"

    print(welcome_assignment_answers(debug_question))
