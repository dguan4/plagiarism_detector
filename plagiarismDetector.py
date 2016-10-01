import sys


def help_usage():
    print("Usage is as follows: "
          "\n python3 plagiarismDetector.py [synonyms file] [first file] [second file] [optional tuple input]")


def detect(synonym, file1, file2, num_tuple):
    print(synonym, file1, file2, num_tuple)


if __name__ == "__main__" :
    if len(sys.argv) == 5:
        detect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 4:
        detect(sys.argv[1], sys.argv[2], sys.argv[3], 3)
    else:
        help_usage()
