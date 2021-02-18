import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^\w\.-]', '', new_id)
    new_id = re.sub('\.{2,}', '.', new_id)
    new_id = new_id.strip(".")
    new_id = "a" if new_id == "" else new_id
    new_id = new_id[:15] if len(new_id) > 15 else new_id
    new_id = new_id.rstrip(".")
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
