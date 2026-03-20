userSentence = input("Type your sentence! ").lower()

def countVowels(sentence):
    vowelCount = [x for x in sentence if x in ("a", "e", "i", "o", "u")]
    print(f"You have {len(vowelCount)} vowels in your sentence.")

countVowels(userSentence)

