import datetime
import csv


class CreateNotes():

    def create():
        title = input("Напишите название заметки ")
        note = input("Напишите заметку ")
        dt_now = datetime.datetime.today()
        thisData = [title, note, dt_now]
        return thisData
        #listOfNotes.addNote(note)

class RewriteNotes():

    def rewrite(self, lstOfNotes):
        index = 1
        for i in lstOfNotes:    
            print(str(index) + " " + i[0])
            index += 1
        
        choose = int(input("Выберите номер заметки для редактирования ")) - 1
        thisNote = lstOfNotes[choose][1]
        newNote = input("Первоначальный вариант: " + thisNote + "\nВведите новый вариант:  ")
        lstOfNotes[choose][1] = newNote
        return lstOfNotes


class DeleteNotes():
    def delete(self, lstOfNotes):
        index = 1
        for i in lstOfNotes:    
            print(str(index) + " " + i[0])
            index += 1

        choose = int(input("Выберите номер заметки для удаления ")) - 1
        lstOfNotes.pop(choose)
        return lstOfNotes


class SaveData():

    def save(self, data):
        with open('file.csv', 'w', encoding='utf-8', newline="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=";")
            csvwriter.writerows(data)
        print("Удачно сохранено \n")


class LoadData():
    def load(self):
        lst = []
        try:
            with open('file.csv', 'r', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=";")
                for row in csvreader:
                    lst.append(row)
        except:
            print("Нечего загружать или файла не существует")

        return lst

class ListOfNotes():
    lst = []

    createNotes = CreateNotes()
    rewriteNotes = RewriteNotes()
    deleteNotes = DeleteNotes()
    saveNotes = SaveData()

    

    def doNote(self, object):
        self.lst = loadData.load()
        while (True):
            choose = input("create - создать заметку, \nedit - редактировать заметку, \nshowtitles - показать список заметок, "
                           + "\ndelete - удалить заметку, \nsave - сохранить заметки, \nexit - выход \n")
            choose = choose.lower()
            if (choose == "create"):
                self.lst.append(CreateNotes.create())
                object.printTitlesOfList()
            elif (choose == "edit"):
                self.lst = self.rewriteNotes.rewrite(self.lst)
                object.printTitlesOfList()
            elif (choose == "showtitles"):
                object.printTitlesOfList()
                if (len(self.lst) > 0):
                    noteChoose = int(input("Выберите заметку по номеру ")) - 1
                    object.printNote(noteChoose)
                else:
                    print("У вас нет заметок")
            elif (choose == "delete"):
                self.lst = self.deleteNotes.delete(self.lst)
            elif (choose == "save"):
                
                self.saveNotes.save(self.lst)

            elif (choose == "exit"):
                print("До свидания")
                break
            else:
                print("Что-то не так")

    def addNote(self, note):
        self.lst.append(note)

    def printTitlesOfList(self):
        index = 1
        for i in self.lst:
            print(str(index) + ". " +  i[0] + " (" + str(i[2]) + ") ")
            index += 1
        print()

    def printNote(self, index):
        print("----------------------------------")
        print("\t\t\t\t " + self.lst[index][0])
        print(self.lst[index][1])
        print("Дата создания: " + str(self.lst[index][2]))
        print("----------------------------------", end = "\n")

loadData = LoadData()
loadData.load()
cr = ListOfNotes()
cr.doNote(cr)
