from typing import Optional
from collections import deque

### Constants
PALINDROME_EXAMPLES = [
    # even number of letters:
    "noon", "boob",
    # odd number of letters:
    "level", "refer", "racecar", "deified", "rotator", 
    # punctuation, spaces, and case
    "A man, a plan, a canal: Panama", "Was it a car or a cat I saw", 
    "Never odd or even", "No lemon, no melon",
    "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod", 
    # alpha-numberic characters, punctuation
    "A code: 12321E-DOC_A",
    # numeric
    "1234321", "000-000", 
    # one character
    "a", "y",
    # no-alpha-numberic characters only
    "", "<>"
]
NOT_PALINDROME_EXAMPLES = ["car", "Stop", "russia is a terrorist state!"]
OUTPUT_TABLE_BORDER = "-" * 70

### Functions
def parse_text_to_dqueue(text: str = None) -> Optional[deque]:
    """
    Parse text to doubly queue ignoring register and characters.
    Raise Error is `text` parameter is `None`.
    """
    if text is None:
        raise ValueError("Input text cannot be None.")
    return deque([char.lower() for char in text if char.isalnum()])


def palindrome_validation(deque_text: Optional[deque]) -> bool:
    """
    Check if provided text is a palindrome. 
    Following the core palindrom rules, along with rules to ignore space, punctuation, and case. 
    """
    if deque_text is None:
        return False
    deque_length = len(deque_text)
    # If number of elements of `dqueue` objects is 0 or 1 -> it also considered as a palindrome.
    if deque_length < 2:
        return True
    # Since one charactrer is considering as a palindrome, than we could ignore it in the middle of the odd number of characters words
    number_of_comparison = deque_length // 2   
    for _ in range(number_of_comparison):
        if deque_text.pop() != deque_text.popleft():
            return False
    return True

def run_examples(examples_list: list[str]) -> None:
    """
    Print the running examples results. 
    """
    if not examples_list:
        return
    print(OUTPUT_TABLE_BORDER)
    print(f"{'Is palindrome?':<14} | Text")
    print(OUTPUT_TABLE_BORDER)
    for example in examples_list:
        text_to_deque = parse_text_to_dqueue(example)
        is_palindrome = "[YES]" if palindrome_validation(text_to_deque) else "[NO]"
        print(f"{is_palindrome:>14} | \"{example}\"")
    print(OUTPUT_TABLE_BORDER)


if __name__ == "__main__":
    print("~ IS PROVIDED TEXT IS A PALINDROME? ~", "\n")
    run_examples(PALINDROME_EXAMPLES)
    print("\n")
    run_examples(NOT_PALINDROME_EXAMPLES)