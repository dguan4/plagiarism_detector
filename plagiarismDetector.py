import sys
from os.path import isfile


def help_usage():
    """
    Simple function to print usage of this file
    :return:
    """
    print("Usage is as follows: "
          "\n python3 [fileName] [synonyms file] [first file] [second file] [optional tuple input]")


def set_tuples(line, num_tuple):
    """
    Sets the tuples from the line and N tuple given
    Adds these all to a list
    This assumes that the last tuple is from the length-num_tuple to the length
    :param line: line of words to create tuples
    :param num_tuple: the N tuple we're creating
    :return: the list of tuples
    """
    file_line = line.strip().split()
    file_list = []
    for i in range(0, len(file_line)-num_tuple+1):
        file_list.append(tuple(file_line[i:i+num_tuple]))
    return file_list


def compare_tuples(first, second, synonyms):
    """
    Simple comparison of tuples
    Without synonyms I could simply check equality (i.e. tuple1 == tuple2)
    This assumes that order matters and that sentences reordered aren't the same
    This also assumes that both tuples are of the same length
    :param first: first tuple to compare
    :param second: second tuple to compare
    :param synonyms: the dictionary of synonyms
    :return: true of false based on whether the tuples are the same/similar or not
    """
    if first is None or second is None:
        return False
    for i in range(len(first)):
        if first[i] != second[i]:
            if second[i] in synonyms:
                if first[i] not in synonyms[second[i]]:
                    return False
            else:
                return False
    return True


def detect(synonym, file1, file2, num_tuple):
    """
    Function that takes in the required arguments and a tuple argument.
    We first create two lists of N tuples and then run through both lists, comparing and looking for similar tuples
    This assumes that any tuple match within two files would be considered plagiarized regardless of where it appears
    And also assumes that we're looking at the match from the biggest file i.e. (match/biggest file length) %
    We also assume that we won't ever get lines that are smaller than our N tuple
    :param synonym: synonym file
    :param file1: first file to open
    :param file2: second file to open
    :param num_tuple: the N tuple, default is 3
    :return: prints the percentage match between both files
    """
    if not isfile(file1) or not isfile(file2) or not isfile(synonym):
        print("Invalid file name, please try again")
        return
    file1 = open(file1)
    file2 = open(file2)
    file1_list = []
    file2_list = []
    match = 0
    synonyms = {}
    with open(synonym) as synonym:
        for line in synonym:
            syn_line = line.strip().split()
            for words in syn_line:
                synonyms[words] = syn_line
    for line in file1:
        file1_list += set_tuples(line, num_tuple)
    for line in file2:
        file2_list += set_tuples(line, num_tuple)
    for tuple1 in file1_list:
        for tuple2 in file2_list:
            if compare_tuples(tuple1, tuple2, synonyms):
                match += 1
                break
    print("{0:.2f}%".format(match/(max(len(file1_list), len(file2_list))) * 100))


if __name__ == "__main__":
    if len(sys.argv) == 5:
        detect(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
    elif len(sys.argv) == 4:
        detect(sys.argv[1], sys.argv[2], sys.argv[3], 3)
    else:
        help_usage()
