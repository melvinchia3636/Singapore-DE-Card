from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('1920x858+0+0')
root.config(bg='white')
root.title('Singepore DE-Card')
root.resizable(False, False)

pfont = Font(size=14)
pfont2 = Font(size=13, family='Arial Black')
pfont3 = Font(size=14, family='Arial Black')
entryfont = Font(size=20, family='Bahnschrift')

bc = PhotoImage(file='bc.png')
bc2 = PhotoImage(file='bc2.png')
imm = PhotoImage(file='imm27a.png')

canvas = Canvas(root, bg='white', highlightthickness=0)
canvas.place(x=0, y=0, width=1920, height=858)
canvas.create_line(6, 33, 45, 33, width=3)
canvas.create_line(27, 45, 55, 45, width=2)
canvas.create_line(27, 44, 27, 75, width=2)
canvas.create_line(1860, 17, 1898, 17, width=3)
canvas.create_line(1898, 17, 1898, 65, width=3)
canvas.create_line(1900, 20, 1900, 848, width=2)
canvas.create_line(10, 823, 10, 850 , width=1.5)
canvas.create_line(625, 795, 625, 825, width=2)
canvas.create_line(597, 824, 625, 824, width=2)
canvas.create_line(1213, 492, 1240, 492, width=2)
canvas.create_line(1240, 461, 1240, 493, width=2)
canvas.create_line(1200, 820, 1230, 820, width=2)
canvas.create_line(1230, 790, 1230, 821, width=2)
canvas.create_line(1285, 625, 1315, 625, width=2)
canvas.create_line(1285, 624, 1285, 655, width=2)
canvas.create_line(1875, 815, 1845, 815, width=2)
canvas.create_line(1875, 816, 1875, 785, width=2)
canvas.create_line(6, 100, 1820, 100, width=2, fill='#FC3D39')
canvas.create_line(635, 25, 635, 854, width=2, fill='#FC3D39')
canvas.create_line(1265, 25, 1265, 850, width=2, fill='#FC3D39')
canvas.create_line(1820, 100, 1820, 850, width=2, fill='#FC3D39')
canvas.create_line(6, 305, 635, 305, width=2, fill='#FC3D39')
canvas.create_line(6, 385, 635, 385, width=2, fill='#FC3D39')
canvas.create_line(6, 465, 635, 465, width=2, fill='#FC3D39')
canvas.create_line(6, 545, 635, 545, width=2, fill='#FC3D39')
canvas.create_line(6, 720, 635, 720, width=2, fill='#FC3D39')
canvas.create_line(520, 185, 1265, 185, width=2, fill='#FC3D39')
canvas.create_line(520, 185, 520, 305, width=2, fill='#FC3D39')
canvas.create_line(200, 385, 200, 465, width=2, fill='#FC3D39')
canvas.create_line(405, 385, 405, 465, width=2, fill='#FC3D39')
canvas.create_line(395, 720, 395, 850, width=2, fill='#FC3D39')
canvas.create_line(635, 133, 1265, 133, width=2, fill='#FC3D39')
canvas.create_line(825, 133, 825, 185, width=2, fill='#FC3D39')
canvas.create_line(1000, 133, 1000, 185, width=2, fill='#FC3D39')
canvas.create_line(635, 345, 1265, 345, width=2, fill='#FC3D39')
canvas.create_line(635, 497, 1265, 497, width=2, fill='#FC3D39')
canvas.create_line(635, 600, 1820, 600, width=2, fill='#FC3D39')
canvas.create_line(635, 733, 1265, 733, width=2, fill='#FC3D39')
canvas.create_line(945, 600, 945, 850, width=2, fill='#FC3D39')
canvas.create_line(1265, 284, 1820, 284, width=2, fill='#FC3D39')
canvas.create_line(1265, 422, 1820, 422, width=2, fill='#FC3D39')
canvas.create_line(1265, 422, 1820, 422, width=2, fill='#FC3D39')
canvas.create_line(1005, 345, 1005, 497, width=2, fill='#FC3D39')

imm27a = Label(root, image=imm, bg='white')
imm27a2 = Label(root, image=imm, bg='white')
imm27a3 = Label(root, image=imm, bg='white')
barcode1 = Label(root, image=bc, bg='white')
barcode2 = Label(root, image=bc, bg='white')
barcode3 = Label(root, image=bc2, bg='white')

p1 = Label(root, text='Full Name as it appears in passport/travel document (BLOCK LETTERS)', bg='white', fg='#FC3D39', font=pfont)
p2 = Label(root, text='Sex*', bg='white', fg='#FC3D39', font=pfont)

tbf1 = Frame(root, bg='#FF8B94')
tickbox1 = Button(root, font=pfont, bg='white', relief=FLAT)
tbf2 = Frame(root, bg='#FF8B94')
tickbox2 = Button(root, font=pfont, bg='white', relief=FLAT)

p3 = Label(root, text='Male', bg='white', fg='#FC3D39', font=pfont)
p4 = Label(root, text='Female', bg='white', fg='#FC3D39', font=pfont)

p5 = Label(root, text='Passport Number', bg='white', fg='#FC3D39', font=pfont)
p6 = Label(root, text='Place Of Issue', bg='white', fg='#FC3D39', font=pfont)
p7 = Label(root, text='Date of Expiry', bg='white', fg='#FC3D39', font=pfont)
p8 = Label(root, text='Country Of Birth', bg='white', fg='#FC3D39', font=pfont)
p9 = Label(root, text='Date of Birth (DD-MM-YYYY)', bg='white', fg='#FC3D39', font=pfont)
p10 = Label(root, text='Nationality', bg='white', fg='#FC3D39', font=pfont)
p11 = Label(root, text='Identity Card Number (for Malaysian Only)', bg='white', fg='#FC3D39', font=pfont)
p12 = Label(root, text='Flight No/Vessel Name/Vehicle No', bg='white', fg='#FC3D39', font=pfont)
p13 = Label(root, text='FOR OFFICE USE ONLY', bg='white', fg='#FC3D39', font=pfont2)

num4 = Label(root, text='(4)', bg='white', fg='#FC3D39', font=pfont)

p14 = Label(root, text='Place of Residence', bg='white', fg='#FC3D39', font=pfont)
p15 = Label(root, text='City', bg='white', fg='#FC3D39', font=pfont)
p16 = Label(root, text='State', bg='white', fg='#FC3D39', font=pfont)
p17 = Label(root, text='Country', bg='white', fg='#FC3D39', font=pfont)

p18 = Label(root, text='Last City / Port of Embarkation Before Singapore', bg='white', fg='#FC3D39', font=pfont)
p19 = Label(root, text='Next City /  Port of Disembarkation After Singapore', bg='white', fg='#FC3D39', font=pfont)

p20 = Label(root, text='Address In Singapore', bg='white', fg='#FC3D39', font=pfont)
p21 = Label(root, text='Length of Stay', bg='white', fg='#FC3D39', font=pfont)

p22 = Label(root, text='Have you ever been to Africa or South America during the last 6 days?*', bg='white', fg='#FC3D39', font=pfont)

p23 = Label(root, justify=LEFT, text='Have you ever\nused a passport\nunder different\nname to enter\nSingapore?*', bg='white', fg='#FC3D39', font=pfont)
p24 = Label(root, justify=LEFT, text='Have you ever\nbeen prohibited\nfrom entering\nSingapore?*', bg='white', fg='#FC3D39', font=pfont)

p25 = Label(root, justify=LEFT, text='If \"Yes\" state name(s) different\nfrom current passport', bg='white', fg='#FC3D39', font=pfont)
p26 = Label(root, justify=LEFT, text='*Please tick (\u2713) appropriate box', bg='white', fg='#FC3D39', font=pfont)

p27 = Label(root, justify=LEFT, text='Signature', bg='white', fg='#FC3D39', font=pfont)

num5 = Label(root, text='(5)', bg='white', fg='#FC3D39', font=pfont)

p28 = Label(root, justify=LEFT, text='Full Name as it appears in passport/travel document\n(BLOCK LETTERS)', bg='white', fg='#FC3D39', font=pfont)

p29 = Label(root, justify=LEFT, text='Nationality', bg='white', fg='#FC3D39', font=pfont)

p30 = Label(root, text='Identity Card Number (for Malaysian Only)', bg='white', fg='#FC3D39', font=pfont)

p31 = Label(root, text='OFFICE USE ONLY', bg='white', fg='#FC3D39', font=pfont3)

num6 = Label(root, text='(6)', bg='white', fg='#FC3D39', font=pfont)

canvas.create_rectangle(15, 135, 625, 178, fill='#FF8B94', outline='#FF8B94')
canvas.create_rectangle(15, 195, 502, 238, fill='#FF8B94', outline='#FF8B94')
canvas.create_rectangle(15, 255, 502, 298, fill='#FF8B94', outline='#FF8B94')

canvas.create_rectangle(15, 335, 625, 378, fill='#FF8B94', outline='#FF8B94')

canvas.create_rectangle(15, 494, 92, 537, fill='#FF8B94', outline='#FF8B94')
canvas.create_line(92, 516, 110, 516, fill='#FF8B94')
canvas.create_rectangle(110, 494, 187, 537, fill='#FF8B94', outline='#FF8B94')
canvas.create_line(187, 516, 205, 516, fill='#FF8B94')
canvas.create_rectangle(205, 494, 364, 537, fill='#FF8B94', outline='#FF8B94')

canvas.create_rectangle(15, 580, 625, 623, fill='#FF8B94', outline='#FF8B94')
canvas.create_rectangle(15, 665, 502, 708, fill='#FF8B94', outline='#FF8B94')
p32 = Label(root, justify=LEFT, text='Tick if\nMalaysian', bg='white', fg='#FC3D39', font=pfont)
tbf3 = Frame(root, bg='#FF8B94')
tickbox3 = Button(root, font=pfont, bg='white', relief=FLAT)

tbf4 = Frame(root, bg='#FF8B94')
tickbox4 = Button(root, font=pfont, bg='white', relief=FLAT)
tbf5 = Frame(root, bg='#FF8B94')
tickbox5 = Button(root, font=pfont, bg='white', relief=FLAT)

num14 = Label(root, text='14', bg='white', fg='#FC3D39', font=pfont2)
num30 = Label(root, text='30', bg='white', fg='#FC3D39', font=pfont2)
p33 = Label(root, text='Others', bg='white', fg='#FC3D39', font=pfont2)

canvas.create_rectangle(496, 765, 573, 808, fill='#FF8B94', outline='#FF8B94')

canvas.create_rectangle(645, 218, 1255, 261, fill='#FF8B94', outline='#FF8B94')
canvas.create_rectangle(645, 292, 1255, 335, fill='#FF8B94', outline='#FF8B94')

canvas.create_rectangle(1075, 406, 1152, 449, fill='#FF8B94', outline='#FF8B94')
p34 = Label(root, text='Days', bg='white', fg='#FC3D39', font=pfont)

tbf6 = Frame(root, bg='#FF8B94')
tickbox6 = Button(root, font=pfont, bg='white', relief=FLAT)
p35 = Label(root, text='Yes', bg='white', fg='#FC3D39', font=pfont)
tbf7 = Frame(root, bg='#FF8B94')
tickbox7 = Button(root, font=pfont, bg='white', relief=FLAT)
p36 = Label(root, text='No', bg='white', fg='#FC3D39', font=pfont)

tbf8 = Frame(root, bg='#FF8B94')
tickbox8 = Button(root, font=pfont, bg='white', relief=FLAT)
p37 = Label(root, text='Yes', bg='white', fg='#FC3D39', font=pfont)
tbf9 = Frame(root, bg='#FF8B94')
tickbox9 = Button(root, font=pfont, bg='white', relief=FLAT)
p38 = Label(root, text='No', bg='white', fg='#FC3D39', font=pfont)

tbf10 = Frame(root, bg='#FF8B94')
tickbox10 = Button(root, font=pfont, bg='white', relief=FLAT)
p39 = Label(root, text='Yes', bg='white', fg='#FC3D39', font=pfont)
tbf11 = Frame(root, bg='#FF8B94')
tickbox11 = Button(root, font=pfont, bg='white', relief=FLAT)
p40 = Label(root, text='No', bg='white', fg='#FC3D39', font=pfont)

canvas.create_rectangle(1300, 465, 1787, 508, fill='#FF8B94', outline='#FF8B94')

canvas.create_rectangle(1330, 700, 1366, 743, fill='#FF8B94', outline='#FF8B94')
canvas.create_rectangle(1414, 700, 1696, 743, fill='#FF8B94', outline='#FF8B94')
canvas.create_rectangle(1744, 700, 1780, 743, fill='#FF8B94', outline='#FF8B94')

canvas.create_line(1366, 721.5, 1414, 721.5, fill='#FF8B94')
canvas.create_line(1696, 721.5, 1744, 721.5, fill='#FF8B94')

name=[]
passport=[]
nationality=[]
malaysiaic=[]
DD = []
MM = []
YYYY = []
others = []
lastcity = []
nextcity = []
days = []
malaysiaic2=[]
officeonly = []

for i in range(39):
    name.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(15):
    passport.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(12):
    malaysiaic.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))
    
for i in range(15):
    nationality.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(2):
    DD.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))
    
for i in range(2):
    MM.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(4):
    YYYY.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(2):
    others.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(15):
    lastcity.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))
for i in range(15):
    nextcity.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(2):
    days.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(12):
    malaysiaic2.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

for i in range(9):
    officeonly.append(Entry(root, relief=FLAT, justify=CENTER, font=entryfont))

imm27a.place(x=515, y=30)
imm27a2.place(x=1145, y=30)
imm27a3.place(x=1770, y=30)
barcode1.place(x=100, y=22)
barcode2.place(x=740, y=22)
barcode3.place(x=1822, y=92)

p1.place(x=12, y=101)
p2.place(x=525, y=187)

tbf1.place(x=529, y=224, width=27, height=27)
tickbox1.place(x=530, y=225, width=25, height=25)
tbf2.place(x=529, y=275, width=27, height=27)
tickbox2.place(x=530, y=276, width=25, height=25)

p3.place(x=560, y=225)
p4.place(x=560, y=276)

p5.place(x=12, y=306)

p6.place(x=12, y=386)
p7.place(x=205, y=386)
p8.place(x=410, y=386)

p9.place(x=12, y=466)

p10.place(x=12, y=546)
p11.place(x=12, y=630)

p12.place(x=12, y=725)

p13.place(x=405, y=725)

num4.place(x=595, y=795)

p14.place(x=645, y=102.5)
p15.place(x=645, y=134)
p16.place(x=835, y=134)
p17.place(x=1010, y=134)

p18.place(x=642, y=186)
p19.place(x=642, y=262)

p20.place(x=645, y=346)
p21.place(x=1016, y=346)

p22.place(x=645, y=498)

p23.place(x=645, y=601)
p24.place(x=960, y=601)

p25.place(x=645, y=734)
p26.place(x=645, y=820)

p27.place(x=960, y=734)
num5.place(x=1200, y=791)

p28.place(x=1270, y=101)

p29.place(x=1270, y=285)

p30.place(x=1270, y=423)

p31.place(x=1450, y=635)

num6.place(x=1845, y=786)

x=16
for i in range(15):
    name[i].place(x=x, y=136, height=42, width=35)
    x+=41

x=16
for i in range(15, 27):
    name[i].place(x=x, y=196, height=42, width=35)
    x+=41

x=16
for i in range(27, 39):
    name[i].place(x=x, y=256, height=42, width=35)
    x+=41

x=16
for i in range(15):
    passport[i].place(x=x, y=336, height=42, width=35)
    x+=41

x=16
for i in range(15):
    nationality[i].place(x=x, y=581, height=42, width=35)
    x+=41

x=16
for i in range(12):
    malaysiaic[i].place(x=x, y=666, height=42, width=35)
    x+=41

p32.place(x=540, y=627)
tbf3.place(x=565, y=682, width=27, height=27)
tickbox3.place(x=566, y=683, width=25, height=25)


x=16
for i in range(2):
    DD[i].place(x=x, y=495, height=42, width=35)
    x+=41

x=111
for i in range(2):
    MM[i].place(x=x, y=495, height=42, width=35)
    x+=41

x=206
for i in range(4):
    YYYY[i].place(x=x, y=495, height=42, width=35)
    x+=41

tbf4.place(x=410, y=780, width=27, height=27)
tbf5.place(x=453, y=780, width=27, height=27)
tickbox4.place(x=411, y=781, width=25, height=25)
tickbox5.place(x=454, y=781, width=25, height=25)
num14.place(x=408, y=807)
num30.place(x=452, y=807)
p33.place(x=500, y=812, height=16)

x=497
for i in range(2):
    others[i].place(x=x, y=766, height=42, width=35)
    x+=41

x=646
for i in range(15):
    lastcity[i].place(x=x, y=219, height=42, width=35)
    x+=41

x=646
for i in range(15):
    nextcity[i].place(x=x, y=293, height=42, width=35)
    x+=41
    
x=1076
for i in range(2):
    days[i].place(x=x, y=407, height=42, width=35)
    x+=41

p34.place(x=1160, y=415)

tbf6.place(x=715, y=550, width=27, height=27)
tickbox6.place(x=716, y=551, width=25, height=25)
tbf7.place(x=810, y=550, width=27, height=27)
tickbox7.place(x=811, y=551, width=25, height=25)
p35.place(x=712, y=580, height=16)
p36.place(x=809, y=580, height=16)

tbf8.place(x=810, y=670, width=27, height=27)
tickbox8.place(x=811, y=671, width=25, height=25)
tbf9.place(x=900, y=670, width=27, height=27)
tickbox9.place(x=901, y=671, width=25, height=25)
p37.place(x=807, y=700, height=16)
p38.place(x=898, y=700, height=16)

tbf10.place(x=1130, y=670, width=27, height=27)
tickbox10.place(x=1131, y=671, width=25, height=25)
tbf11.place(x=1220, y=670, width=27, height=27)
tickbox11.place(x=1221, y=671, width=25, height=25)
p39.place(x=1127, y=700, height=16)
p40.place(x=1218, y=700, height=16)

x=1301
for i in range(12):
    malaysiaic2[i].place(x=x, y=466, height=42, width=35)
    x+=41

officeonly[0].place(x=1331, y=701, height=42, width=35)
x=1415
for i in range(1, 8):
    officeonly[i].place(x=x, y=701, height=42, width=35)
    x+=41
officeonly[8].place(x=1745, y=701, height=42, width=35)
    
root = mainloop()
