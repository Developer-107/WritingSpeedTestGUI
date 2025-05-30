from tkinter import *
import ctypes
import random
import tkinter


# For a sharper window
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# TkSetup
root = Tk()
root.title('Type Speed Test')

# Setting the starting window dimensions
root.geometry('700x700')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")

def resetWritingLabels():
    # Text List
    possibleTexts = ["Its had resolving otherwise she contented therefore. Afford relied warmth out sir hearts sister "
                     "use garden. Men day warmth formed admire former simple. Humanity declared vicinity continue "
                     "supplied no an. He hastened am no property exercise of. Dissimilar comparison no terminated "
                     "devonshire no literature on. Say most yet head room such just easy.", "In by an appetite no "
                     "humoured returned informed. Possession so comparison inquietude he he conviction no decisively."
                     "Marianne jointure attended she hastened surprise but she. Ever lady son yet you very paid form "
                     "away. He advantage of exquisite resolving if on tolerably. Become sister on in garden it barton"
                     " waited on.", "Am terminated it excellence invitation projection as. She graceful shy believed "
                     "distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough "
                     "income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. "
                     "Design for are edward regret met lovers. This are calm case roof and." , "Throwing consider "
                     "dwelling bachelor joy her proposal laughter. Raptures returned disposed one entirely her men ham."
                     " By to admire vanity county an mutual as roused. Of an thrown am warmly merely result depart "
                     "supply. Required honoured trifling eat pleasure man relation. Assurance yet bed was improving "
                     "furniture man. Distrusts delighted she listening mrs extensive admitting far."
    ]
    # Choosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()


    # defining where the text is split
    splitPoint = 0

    # This is where the text is that is already written
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Here is the text which will be written
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # this label shows the user how much time has gone by
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amountWords = len(labelLeft.cget('text').split(' '))

    # Destroy all unwanted widgets.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    # Destroy result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

    # re-setup writing labels.
    resetWritingLabels()


def addSecond():
    # Add a second to the counter.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        root.after(1000, addSecond)


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #set the next Letter Label
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass

# This will start the Test
resetWritingLabels()

# Start the mainloop
root.mainloop()







