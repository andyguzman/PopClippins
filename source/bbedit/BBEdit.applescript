tell application "BBEdit"
	activate
	set txt to contents of "{popclip text}"
	set doc to make new document with properties {contents:txt}
end tell