def format_latin_text(unformatted_latin_text):
    """
    Accepts a string of Latin text and upper-cases all of its alphabetic characters, replacing all 'U' characters with
    'V'.
    :param unformatted_latin_text: A string containing Latin text
    :return: A string containing properly formatted Latin
    """
    pass


def get_unformatted_text(file_path):
    """
    Reads a txt file and returns a list whose every element is each of the lines in the original text file.

    :param file_path: A string representing the name and path of the txt file
    :return: A list of strings
    """
    pass


def write_formatted_latin_file(input_file_path, output_file_path="output.txt"):
    """
    Creates a txt file (output_file_path) containing the formatted Latin contents of the file input_file_path.

    :param input_file_path: A string containing the name and path of the original txt file.
    :param output_file_path: A string containing the name and path of the formatted txt file to be created.
    :return:
    """
    pass


def main():
    """
    Just some sample behavior based on the README. Feel free to add tests for the other functions!
    """
    write_formatted_latin_file(input_file_path="imperatoria_verba.txt", output_file_path="formatted_text.txt")

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
