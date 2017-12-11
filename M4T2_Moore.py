# CTI-110
# M4T2 - Python Exercise
# Andrew Moore
# 10/01

# Simple program to display example of use of select user input strings

# Ask user to input string

htmlString = input("Enter html string: ")

# Display example of use for input string

if htmlString == "p":
    print ("The HTML <p> element defines a paragraph. <p>text</p>")
elif htmlString == "h1":
    print ("The HTML <h1> element defines main headings. <h1>text</h1>")
elif htmlString == "b":
    print ("The HTML <b> element defines bold font. <b>text<b>")
elif htmlString == "div":
    print ("The HTML <div> element defines a division in an HTML document.")
else:
    print ("Tag not found.")
    
    
  
