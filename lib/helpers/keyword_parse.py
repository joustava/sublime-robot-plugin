
def get_keyword_at_pos(line, col):
    length = len(line)

    if length == 0:
        return None

    # between spaces
    if ((col >= length or line[col] == ' ' or line[col] == "\t")
    and (col == 0 or line[col-1] == ' ' or line[col-1] == "\t")):
        return None

    # first look back until we find 2 spaces in a row, or reach the beginning
    i = col - 1
    while i >= 0:
        if line[i] == "\t" or ((line[i - 1] == ' ' or line[i - 1] == '|') and line[i] == ' '):
            break
        i -= 1
    begin = i + 1

    # now look forward or until the end
    i = col # previous included line[col]
    while i < length:
        if line[i] == "\t" or (line[i] == " " and len(line) > i and (line[i + 1] == " " or line[i + 1] == '|')):
            break
        i += 1
    end = i

    keyword = line[begin:end]

    return line[begin:end]