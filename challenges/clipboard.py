# A text editor is a type of computer program that edits plain text. It consists of a string with a cursor. In the initial state, the string is empty with the cursor at the beginning of the string. Some modern text editors have a clipboard manager - they save a history of copied text.
#
# Your task is to simulate the working process of a text editor with a simple clipboard manager which can handle six types of operations:
#
# TYPE <text> - insert <text> after the current position of the cursor, where <text> consists of at most 50 characters including English letters, digits, whitespaces, and symbols .,?!-. The cursor moves to the end of the inserted text.
# SELECT <start_index> <end_index> - select the substring of the current text [text[start_index] ... text[end_index]] (inclusive indices, 0-based) of length end_index - start_index + 1. It is guaranteed that the indices are valid. The cursor changes its position to the end of the selected area.
# MOVE_CURSOR <offset> - change the cursor's current position. The <offset> specifies the direction and the value change - if it is negative the cursor moves to the left, and if it's positive the cursor moves to the right. At all times, the cursor is either located at the beginning of the string (before the first character), between two characters, or at the end of the string (after the last character) - the cursor should always be within the text bounds. If the <offset> is larger than the cursor can move, the cursor will move in that direction as much as it can. If there is a selected area, it should be cleared after this operation.
# COPY - add the text from the selected area to the clipboard. If there is no selected area then do nothing.
# PASTE <steps_back> - insert the copied text from the clipboard manager. The number <steps_back> specifies which of the stored copied texts to insert. If <steps_back> is 1 then insert the last copied text, if it is 2 then insert the text copied before the last, and so on. It <steps_back> is greater than the clipboard history size then ignore this operation. The cursor moves to the end of the inserted text.
# PASTE - do the same as if the operation is PASTE 1.
# Note: If a selected area is not empty and the next operaion is either TYPE or PASTE then the following updating process is expected during the TYPE or PASTE operation:
#
# Delete the selected text.
# Insert the new text in the place of the deleted text.
# The cursor position should move to the end of the new text.
# You are given operations, an array of strings where each is an operation of one of the six types above. Your task is to find the resulting text after performing the given operations.
#
# Example
#
# For operations = ["TYPE Great Britain is the capital of London", "SELECT 0 12", "COPY", "SELECT 32 37", "COPY", "PASTE 2", "SELECT 0 12", "PASTE", "MOVE_CURSOR 32", "TYPE !"], the output should be solution(operations) = "London is the capital of Great Britain!".
#
# Initially the text is empty,
# After the "TYPE Great Britain is the capital of London" operation, the text is "Great Britain is the capital of London|" (where the | symbol represents the cursor position),
# After the "SELECT 0 12" operation, the selected text is "Great Britain", the cursor is moved to the end of the selected area "Great Britain| is the capital of London",
# After the "COPY" operation, the clipboard is ["Great Britain"], the cursor doesn't move, and the selected area stays the same,
# After the "SELECT 32 37" operation, the selected text is "London", the cursor is moved to the end of the selected area "Great Britain is the capital of London|",
# After the "COPY" operation, the clipboard is ["Great Britain", "London"], the cursor doesn't move, and the selected area stays the same,
# After the "PASTE 2" operation, since there is a selected text, it is deleted and replaced with the text "Great Britain" because it is 2 positions back in the clipboard, the cursor stays after the inserted text, so the text is "Great Britain is the capital of Great Britain|",
# After the "SELECT 0 12" operation, the selected text is "Great Britain", the cursor is moved to the end of the selected area "Great Britain| is the capital of Great Britain",
# After the "PASTE" operation, since there is a selected text, it is deleted and replaced with the text "London" because it is the last copied text in the clipboard, the cursor stays after the inserted text, so the text is "London| is the capital of Great Britain",
# After the "MOVE_CURSOR 32", the cursor moves 32 symbols forward, so the text is "London is the capital of Great Britain|",
# After the "TYPE !" operation, the text is "London is the capital of Great Britain!|",
# So the final string is "London is the capital of Great Britain!".
def solution(operations):
    clipboard = []
    text = ""
    start_point = 0
    selected = [0, 0]

    for i in operations:
        sentence = i.split(" ")
        op = sentence[0]
        if op == "TYPE":
            text = text[:start_point] + ' '.join(sentence[x] for x in range(1, len(sentence))) + text[start_point:]
            start_point = len(text)
        elif op == "MOVE_CURSOR":
            start_point = int(sentence[1])
        elif op == "SELECT":
            selected = [int(sentence[1]), int(sentence[2])]
        elif op == "COPY":
            clipboard.append(text[selected[0]:selected[1]])
        # print(selected)
        # elif op == "PASTE":
        #     if clipboard:
        #         text = text[selected[0]:] + clipboard[-1] + text[:selected[1]]
        #         start_point = len(text)

    return text