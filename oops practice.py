#TASK-1#

class CashRegister:
    def __init__(self, pur_items, items, discount):                    #Instantiating Cash Register#
        self.purchased_items = pur_items
        self.total_items = items
        self.discount = discount

    def add_item(self, new_item):                                     #Method to add new item#
        self.new_item = new_item
        self.purchased_items.update(new_item)
        self.total_items = self.total_items + 1
        print("AFTER ADDING  NEW ITEM")
        print("Total items after adding is "+str(self.total_items))
        print(self.purchased_items)

    def remove_item(self, item):                                       #Method to remove item#
        self.item=item
        self.purchased_items.pop(item)
        self.total_items=self.total_items-1
        print("AFTER REMOVING SELECTED ITEM")
        print("Total items after removing is "+str(self.total_items))
        print(self.purchased_items)

    def apply_discount(self):                                          #method to apply discount#
        d={}
        items=a.purchased_items.keys()
        for i in items:                                                #looping over price of each item to apply discount#
            values=(a.purchased_items.get(i))*self.discount
            d.update({i:values})                                       #pushing updated items with prices to a dictionary #
        print("ITEMS LIST AFTER APPLYING DISCOUNT")
        print(d)
    def get_total(self):                                               #method to print total of prices of purchased items#
        prices = self.purchased_items.values()
        sum=0
        for i in prices:
            sum=sum+i
        print("TOTAL VALUE OF PRICES OF ALL ITEMS")
        print(sum)
    def show_items(self):                                             #method to show list of items#
        print("LIST OF ITEMS IN CASH REGISTER")
        print(a.purchased_items)

    def reset_register(self):                                         #method to reset cash register items#
        a.purchased_items.clear()
        print("RESET REGISTER")
        print(a.purchased_items)

    ##To reset whole class of CashRegister we can simply deallocated memory to CashRegister object##
    ##def reset_whole(self):
      ##  del a
        ##print("RESET WHOLE CASH REGISTER")
        #print(a)


a = CashRegister({"pen": 10, "pencil": 15, "book": 20, "bottle": 25}, 4, 0.2)              #CashRegister object#

a.add_item({"key": 5})                                                                  #calling add_item method
a.remove_item("pen")                                                                    #calling remove item method
a.apply_discount()                                                                      #calling discount method
a.get_total()                                                                           #calling get total method
a.show_items()                                                                          #calling show items method
a.reset_register()                                                                      #calling reset register method

#a.reset_whole()                                                                        #Resetting whole object#

print("TASK-2 \n")
#TASK-2


class Student:

    def __init__(self, name, age, id, subjects):
        self.name = name
        self.age = age
        self.id = id
        self.subjects =subjects

class Special_Student(Student):                #class inheriting student for specialization#

     def __init__(self,spec_name):             #instantiating class#
        self.spec_name=spec_name
        print("specialization "+str(spec_name))

     def new(self, new_subject):               #method to add new subject#
         self.new_subject=new_subject
         ob.subjects.update(new_subject)
         print("LIST OF SUBJECTS AFTER ADDING")
         print(ob.subjects)

     def delete(self, old_subject):              #method to deleted selected  subject#
         self.old_subject = old_subject
         ob.subjects.pop(old_subject)
         print("LIST OF SUBJECTS AFTER REMOVING")
         print(ob.subjects)

     def subjects(self):                          #method to print all subjects#
         ob.subjects.update({"java":89})     #since the object has a subject deleted, updating with the deleted subject#
         subjects=ob.subjects.keys()
         print("subjects taken by student "+(str(subjects)[9:42]))      #converting dict into string and printing#

     def overall_mark(self):                          #method to find average#

        sum=0
        avg=0                                # initializing new variable to store result avg#
        length=len(ob.subjects)
        for i in ob.subjects.values():
            sum=sum+i
        avg=sum/length                          # Storing result in newly created result variable#
        print("avg of marks "+str(avg))


ob=Student("pinky",23,1,{"math":100,"python":90, "java":89 })          #passing object to parent 'Student' class#
oa=Special_Student("software")                                          # passing object to child Specialization class#
oa.new({"c":76})                                                   #calling add_item method#
oa.delete("java")                                               # calling remove subject method#
oa.subjects()                                                    # calling subjects method fo list of subjects#
oa.overall_mark()                                                #calling overall_mark method to find average#

