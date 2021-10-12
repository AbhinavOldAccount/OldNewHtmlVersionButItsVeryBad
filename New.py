Position = -1
CurrentCharacter = None

Text = ""

def Advance():
    global Position, CurrentCharacter
    Position += 1
    CurrentCharacter = Text[Position]

def GetContent():
    FirstRun = True
    Content = ""
    while True:
        Advance()
        if not FirstRun:
            Advance()
        if CurrentCharacter != "]":
            Content += CurrentCharacter
        else: break
    return Content

def Run():
    Title = ""
    BackgroundColor = "rgb(255, 255, 255)"
    Output = "<!DOCTYPE html><html><body>"
    while Position < len(Text) - 1:
        Advance()
        if CurrentCharacter == "P":
            Advance()
            Style = ""
            if CurrentCharacter == "^":
                while True:
                    Advance()
                    if CurrentCharacter == "[": break
                    Style += CurrentCharacter
                if Style == "*": Output += f"<p><b>{GetContent()}</b></p>"
                elif Style == "**": Output += f"<p><i>{GetContent()}</i></p>"
                elif Style == "***": Output += f"<p><b><i>{GetContent()}</i></b></p>"
            else: Output += f"<p>{GetContent()}</p>"
        elif CurrentCharacter == "H":
            Advance()
            Level = CurrentCharacter
            Advance()
            Output += f"<h{Level}>{GetContent()}</h{Level}>"
        elif CurrentCharacter == "A":
            Advance()
            Link = ""
            if CurrentCharacter == "^":
                while True:
                    Advance()
                    if CurrentCharacter == "[": break
                    Link += CurrentCharacter
            Output += f"<a href='{Link}'>{GetContent()}</a>"
        elif CurrentCharacter == "I":
            Advance()
            if CurrentCharacter == "[":
                Output += f'<label>{GetContent()}</label><input type="text">'
            else: Output += f'<input type="text">'
        elif CurrentCharacter == "B" and Text[Position + 1] == "G":
            Advance()
            Advance()
            BackgroundColor = f'rgb({GetContent()})'
        elif CurrentCharacter == "B":
            Advance()
            Output += f"<button>{GetContent()}</button>"
        elif CurrentCharacter == "T":
            Advance()
            Title = GetContent()
        elif CurrentCharacter == "&":
            Output += "<br>"
            Advance()
    return Output + f'</body><head><link href="https://fonts.googleapis.com/css?family=Fredoka One" rel="stylesheet"><title>{Title}</title><style>body' + "{" + f'background-color:{BackgroundColor};' + '}' + '* {font-family:"Fredoka One"; font-size: 105%;' + '}</style></head></html>'

TextFile = "C:/Users/Abhinav/OneDrive/Documents/CodeAbhinav/Python/NewHtml/Demo.nh"
FileA = open(TextFile, "r")
ContentA = FileA.read()
Result = "C:/Users/Abhinav/OneDrive/Documents/CodeAbhinav/Python/NewHtml/Result.html"
FileB = open(Result, "w")
Text = ContentA
FileB.write(Run())