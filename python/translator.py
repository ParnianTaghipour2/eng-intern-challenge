import sys

# Mapping dictionaries for English to Braille and vice versa
# not adding <> because I had to add another dictionary for that and it was not in the requirement!
MAPPING = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", ".": "..OO.O", ",": "..O...", "?": "..O.OO",
    "!": "..OOO.", ":": "..OO..", ";": "..0.0.", "-": "....OO", "/": ".O..O.",
    "(": "O.O..O", ")": ".O.OO.", "capitalNext": ".....O", "decimalNext": ".O...O", "numberNext": ".O.OOO"
}
# Seprating Numbers because of the mutual codes
digitToBraille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

brailleToDigit = {v: k for k, v in digitToBraille.items()}
brailleMapping = {v: k for k, v in MAPPING.items()}

def isBraille(s):
    return set(s) <= {"O", "."} and len(s) % 6 == 0 # Braille property is it should have 6 letter

def brailleToText(braille):
    words = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    text, numberMode, capitalNext = [], False, False

    for word in words:
        if word == MAPPING["capitalNext"]:
            capitalNext = True
        elif word == MAPPING["decimalNext"]:
            text.append(".")
        elif word == MAPPING["numberNext"]:
            numberMode = True
        else:
            if numberMode and word != MAPPING[" "]:
                char = brailleToDigit.get(word, " ")
            else:
                char = brailleMapping.get(word, " ")
                numberMode = False
                if capitalNext:
                    char = char.upper()
                    capitalNext = False
            text.append(char)
    return "".join(text)

def textToBraille(text):
    braille = []
    for char in text:
        if char.isupper():
            braille.append(MAPPING["capitalNext"])
            braille.append(MAPPING[char.lower()])
        elif char.isdigit():
            if not braille or braille[-1] != MAPPING["numberNext"]:
                braille.append(MAPPING["numberNext"])
            braille.append(digitToBraille[char])
        elif char == ".":
            braille.append(MAPPING["decimalNext"])
        else:
            braille.append(MAPPING.get(char, "......"))
    return "".join(braille)

def main():
    if len(sys.argv) >= 2:
        inputStr = " ".join(sys.argv[1:])
        result = brailleToText(inputStr) if isBraille(inputStr) else textToBraille(inputStr)
        print(result)
    else:
        print("Please provide the Input. Run the code using Python3 translator.py")

if __name__ == "__main__":

    main()
