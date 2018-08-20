import textwrap
def wrap(string, max_width):
    textwrap.wrap(string,max_width)
    return textwrap.fill(string,max_width)
print(wrap("hello guys, how are you",8))