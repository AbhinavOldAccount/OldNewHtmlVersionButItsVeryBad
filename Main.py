import New

def Read(Text):
    Position = -1
    CurrentCharacter = None
    TagContent = ""
    TagStarted = False
    TagType = ""
    Output = "<!DOCTYPE html><html><body>"
    while Position < len(Text) - 1:
        Position += 1
        CurrentCharacter = Text[Position]

        if CurrentCharacter in " \n" and not TagStarted: continue
        if TagStarted and CurrentCharacter != "|":
            TagContent += CurrentCharacter
        elif CurrentCharacter == "[":
            Position += 1
            CurrentCharacter = Text[Position]
            if CurrentCharacter == "P":
                TagType = "p"
                Position += 1
            elif CurrentCharacter == "H":
                Position += 7
                CurrentCharacter = Text[Position]
                TagType = f"h{CurrentCharacter}"
        elif CurrentCharacter == "]": TagStarted = True
        elif CurrentCharacter == "|":
            TagStarted = False
            Output += f"<{TagType}>" + TagContent + f"</{TagType}>"
            TagContent = ""
        elif CurrentCharacter == "&": Output += "<br>"
        elif CurrentCharacter == "I":
            Position += 1
            CurrentCharacter = Text[Position]
            if CurrentCharacter == "|":
                Content = ""
                Position += 1
                CurrentCharacter = Text[Position]
                N = False
                while CurrentCharacter != "|":
                    if N:
                        Position += 1
                    else: N = True
                    CurrentCharacter = Text[Position]
                    if CurrentCharacter != "|":
                        Content += CurrentCharacter
                Output += f"<label>{Content}</label>"
            Output += '<input type="text">'

    Output += "</body></html>"
    return Output

TextFile = "C:/Users/Abhinav/OneDrive/Desktop/CodeAbhinav/Python/NewHtml/Demo.nh"
FileA = open(TextFile, "r")
ContentA = FileA.read()
Result = "C:/Users/Abhinav/OneDrive/Desktop/CodeAbhinav/Python/NewHtml/Result.html"
FileB = open(Result, "w")
FileB.write(New.New(ContentA))