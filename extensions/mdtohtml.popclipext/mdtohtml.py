import os
import markdown

input = os.environ['POPCLIP_TEXT']
text = unicode(input, "utf-8")
output = markdown.markdown(text)
print output

# Markdown Mark by [Dustin Curtis](https://github.com/dcurtis/markdown-mark)