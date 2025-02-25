from translate import Translator

def translate_the_text(text, target_language):
    try:
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return f"Translation Error: {str(e)}"

# Define the target languages and their codes
indian_languages = {
    '1': ('hi', 'Hindi'),
    '2': ('te', 'Telugu'),
    '3': ('kn', 'Kannada'),
    '4': ('ta', 'Tamil'),
    '5': ('ml', 'Malayalam'),
    '6': ('mr', 'Marathi'),
    '7': ('gu', 'Gujarati'),
    '8': ('pa', 'Punjabi'),
    '9': ('bn', 'Bengali'),
    '10': ('or', 'Odia'),
    '11': ('as', 'Assamese'),  # Assamese
    '12': ('ur', 'Urdu'),  # Urdu
    '13': ('mrj', 'Marwari'),  # Marwari
    '14': ('mai', 'Maithili'),
    '15': ('sa', 'Sanskrit '),
    '16': ('sd', 'Sindhi'),
    '17': ('mni', 'Manipuri'),
    # Add more Indian languages and their codes as needed
}

while True:
    # Input text to be translated
    english_text = input("Enter the English text to translate: ")

    # Display available languages for selection
    print("Select a target Indian language:")
    for index, (_, language_name) in indian_languages.items():
        print(f"{index}. {language_name}")

    # Get user's language choice
    choice = input("Enter the number of the target language: ")

    # Check if the choice is valid
    if choice in indian_languages:
        target_language_code, target_language_name = indian_languages[choice]
        translated_text = translate_the_text(english_text, target_language_code)
        print(f"Translated text to {target_language_name}:\n{translated_text}")
    else:
        print("Invalid language choice. Please enter a valid number from the list.")

    # Ask the user if they want to translate more text
    another_translation = input("Do you have more text to translate? (yes/no): ").lower()
    if another_translation != "yes":
        break
