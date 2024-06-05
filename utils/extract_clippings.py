from collections import defaultdict
import json


def _extract_clippings_from_raw(raw_clippings_lines: list) -> dict:
    """
    Converts the string data embedded in `raw_clippings_lines` into a dictionary whose each key is a unique book

    Args:
        raw_clippings_lines (list): _description_

    Returns:
        dict: a dict of books with each key being a list of dictionaries which stores a highlight/note along with its other data
    """
    # creating a dictionary for books whose default data type for the values is dict
    books = defaultdict(list)

    # some internal flags used to fill the books dict (empty ones will be automatically filled)
    _info_type_in_next_line = "new book"
    _current_book = ""
    _clipping_type = ""

    for i, raw_line in enumerate(raw_clippings_lines):
        # removing the encodings
        raw_line = raw_line.strip()

        if raw_line != "":
            if "==========" in raw_line.strip():  # this marks a separator
                _info_type_in_next_line = "new book"
            elif _info_type_in_next_line == "new book":
                _book_title = raw_line
                _author = ""

                if "(" in raw_line and ")" in raw_line:
                    _index_of_left_bracket = raw_line.index("(")
                    # the string is reversed for the following
                    _index_of_right_bracket = (
                        len(raw_line) - 1 - raw_line[::-1].index(")")
                    )

                    _book_title = raw_line[:_index_of_left_bracket].strip()
                    _author = raw_line[
                        _index_of_left_bracket + 1 : _index_of_right_bracket
                    ].strip()
                else:
                    pass

                _current_book = _book_title
                _info_type_in_next_line = "clipping metadata"
                # let's jump to the next line to find the clipping_type
                _clipping_type = (
                    raw_clippings_lines[i + 1].strip().split(" ")[2].lower()
                )

                if _clipping_type == "note" and len(books[_current_book]) > 0:
                    # this is because we wanna pair up a note and a highlight
                    pass
                else:
                    books[_current_book].append({"author": _author})

                # adding empty strings for highlights and notes (as placeholders)
                # this even allows us to allow multi-line highlights to be synced
                books[_current_book][-1][_clipping_type] = ""
                books[_current_book][-1][
                    "note"
                ] = ""  # to make sure there's always a note property!
            elif _info_type_in_next_line == "clipping metadata":
                _split_raw_line = raw_line.split(" ")
                _current_clipping_data = books[_current_book][-1]

                # adding the page number
                try:
                    _page_word_index = _split_raw_line.index("page")
                    _page_num = _split_raw_line[_page_word_index + 1]
                    _current_clipping_data["page"] = _page_num
                except:
                    # in case the page number didn't exist
                    pass

                # adding the time + date (this exists for sure)
                _datetime_starting_index = _split_raw_line.index("Added")
                _current_clipping_data["added_datetime"] = "".join(
                    f"{str(e)} " for e in _split_raw_line[_datetime_starting_index:]
                ).strip()

                # emptying the into_typ_in_next_line so that it reaches the else block!
                _info_type_in_next_line = ""
            else:
                # mostly highlights and notes reach this else block!
                _clipping = books[_current_book][-1][_clipping_type]
                if _clipping == "":
                    books[_current_book][-1][_clipping_type] += raw_line.strip()
                else:
                    # adding a line break
                    books[_current_book][-1][_clipping_type] += f"\n{raw_line.strip()}"
        else:
            continue

    return books


def extractor(path_to_clippings_txt: str) -> dict:
    """
    Extracts the highlights from My Clippings.txt and arranges each clipping under book name

    Args:
        path_to_clippings_txt (str): path to My Clippings.txt

    Returns:
        dict: a dict with the key being the book name and the values being a list of clippings (where each clipping is a dictionary!)
    """
    # Retrieving from my clippings
    with open(path_to_clippings_txt, "r", encoding="utf8") as f:
        raw_clippings_lines = f.readlines()

    books = _extract_clippings_from_raw(raw_clippings_lines)

    return books
