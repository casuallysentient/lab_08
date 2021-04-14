def get_school_list(file_path):
    try:
        file = open(file_path, "r")
        temp = file.readlines()
        schools = [s.strip() for s in temp]
        schools.pop(0)
        file.close()
        return schools
    except FileNotFoundError:
        return ""


def get_most_exclusive_school(file_path):
    """
    Returns the most exclusive state school in the list of school provided in the file denoted by file_path.
    Exclusivity is determined by SAT score (that is, the highest the SAT score, the more exclusive).

    :param file_path: The name and path of the file containing the schools' information
    :return: A string containing the name of the most exclusive state school
    """
    schools = get_school_list(file_path)
    high_score = 0
    best_school = ""
    for stats in schools:
        stats = stats.split(",")
        is_state_school = stats[7]
        if stats[4] != "Null" and stats[5] != "Null":
            avg_score = int(stats[4]) + int(stats[5])
            if is_state_school == "True" and high_score <= avg_score < 1800:
                high_score = avg_score
                best_school = stats[0]
    return best_school


def main():
    """
    Just some sample behavior based on the README.
    """
    school_name = get_most_exclusive_school("schools.csv")
    print(school_name)

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
