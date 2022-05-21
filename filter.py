from panflute import *
import sys

all_headers = {}


def action(line, doc):
    if type(line) == Header:
        if stringify(line) in all_headers.keys():
            if all_headers.get(stringify(line)) == line.level:
                sys.stderr.write("Repeated headers. Level: " + str(line.level) + ", text: " + stringify(line))
        else:
            all_headers[stringify(line)] = line.level

    if type(line) == Header:
        if line.level <= 3:
            title = [Str(stringify(line).upper())]
            return Header(*title, level=line.level)

    if type(line) == Str:
        if str(line.text).lower() == "bold":
            title = [Str(line.text)]
            return Strong(*title)


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
