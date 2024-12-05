import random

prompt = "How do you do. Please tell me your problem (or 'q' to quit): "

positive_keywords = ["happy", "wonderful", "joy", "joyful", "love", "excited"]
negative_verb_keywords = ["avoid", "worry", "fear"]
negative_adjective_keywords = ["sad", "upset", "depressed", "unhappy", "tired"]
negative_noun_keywords = ["problem", "issue"]
neutral_keywords = ["feel", "think"]
family_keywords = ["mother", "father", "sister", "brother", "family"]
crime_keywords = ["crime", "mystery", "murder", "case"] # it's all about the reply:)

positive_replies = [
    "Oh, that sounds nice!",
    "That's great!",
    "I'm happy to hear that!",
    "That must be wonderful!"
]

negative_adjective_replies = [
    "Why are you {word}",
    "Why do you feel {word}?",
]

negative_noun_replies = [
    "What makes you think of {word}",
    "Tell me more about this {word}?",
]


family_replies = [
    "Tell me more about your {word}",
    "What's your relationship with your {word}"
]


no_response_replies = [
    "I see.",
    "Please go on.",
    "Can you elaborate on that?",
]

def swap_pronouns(phrase):
    phrase = phrase.replace(" I ", " __you__ ")
    phrase = phrase.replace(" you ", " __i__ ")
    phrase = phrase.replace(" me ", " __you__ ")
    phrase = phrase.replace(" my ", " __your__ ")
    phrase = phrase.replace(" your ", " __my__ ")
    phrase = phrase.replace(" am ", " __are__ ")

    phrase = phrase.replace("__you__", "you")
    phrase = phrase.replace("__i__", "I")
    phrase = phrase.replace("__your__", "your")
    phrase = phrase.replace("__my__", "my")
    phrase = phrase.replace("__are__", "are")

    return phrase


while True:

    problem = input(prompt)

    if problem.lower() == "q":
        print("Goodbye! Take care.")
        break


    words = problem.split()

    response_found = False

    for word in words:
        if word in positive_keywords:
            reply = random.choice(positive_replies).format(word=word)
            print(reply)
            response_found = True
            break

        elif word in negative_verb_keywords:
            start = problem.find(word)
            end = problem.find(".", start)
            if end == -1:
                end = len(problem)
            partial_response = problem[start:end]
            print(f"Why do you {partial_response}?")
            break

        elif word in negative_adjective_keywords:
            reply = random.choice(negative_adjective_replies).format(word=word)
            print(reply)
            response_found = True
            break

        elif word in negative_noun_keywords:
            reply = random.choice(negative_noun_replies).format(word=word)
            print(reply)
            response_found = True
            break

        elif word in family_keywords:
            reply = random.choice(family_replies).format(word=word)
            print(reply)
            response_found = True
            break

        elif word in crime_keywords:
            print("It was the gardener, wasn't it?") #yeahh
            response_found = True
            break


    if not response_found:
        print(random.choice(no_response_replies))