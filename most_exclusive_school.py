def get_most_exclusive_school(file_path):
    """
    Returns the most exclusive state school in the list of school provided in the file denoted by file_path.
    Exclusivity is determined by SAT score (that is, the highest the SAT score, the more exclusive).

    :param file_path: The name and path of the file containing the schools' information
    :return: A string containing the name of the most exclusive state school
    """
    pass


def main():
    """
    Just some sample behavior based on the README.
    """
    school_name = get_most_exclusive_school("schools.csv")
    print(school_name)

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
