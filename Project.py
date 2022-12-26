name=['Krishna','Payal','Abdul','Pranita','Anya','Priyanshu','Harsh','Aditya','Rahul','Shiva']
marks=[68,64,91,74,80,87,80,95,76,94]
print()
print()
print("Enter the Updates in marks, positive for increment and negative in decrement")
print()
print()
#Giving Even Spaces to names in list
name1=[]
for i in name:
    name1.append(i.center(10))
c=dict(zip(name1,marks))

#Sorting Dictionary with marks
sor_vals=sorted(c.values())
sor_dict={}

for i in sor_vals:
    for j in c.keys():
        if c[j]==i:
            sor_dict[j]=c[j]
ranked=dict(reversed(list(sor_dict.items())))

#Taking updates as input
print("  Name          Marks     Rank      Updates")
print()
it=1
updates=[]
ranked_list=[]
rank_dict={}
for i in ranked:
    print(i,"     ",ranked[i],"      ",f"{it:02}","     ",end="")
    ranked_list.append(it)
    it+=1
    up=int(input("    "))
    updates.append(up)
    rank_dict[i]=it

#creating dictionaries for different values
name_prerank=ranked.keys()
rank_dict=dict(zip(name_prerank,ranked_list))
updates_dict=dict(zip(name_prerank,updates))

#adding updates
new_dict={}
for i in ranked:
    new_dict[i]=ranked[i]+updates_dict[i]

#New Ranked dictionary with new marks
new_mar_vals=sorted(new_dict.values())
new_marks={}
for i in new_mar_vals:
    for j in new_dict.keys():
        if new_dict[j]==i:
            new_marks[j]=new_dict[j]
new_marks=dict(reversed(list(new_marks.items())))
#assigning new rank to a dictionary
new_rank={}
c_i=1
for i in new_marks:
    new_rank[i]=c_i
    c_i+=1
#Name, Previous Rank, New Rank, Jump in Rank, Marks
print()
print()
print("                              UPDATED MARKS AND RANKS")
print()
print()
print("  Name           New Rank         Previous Rank        Jump in Rank            Marks")
for i in new_rank:
    print(i,"        ",f"{new_rank[i]:02}","                ",f"{rank_dict[i]:02}","                ",f"{rank_dict[i]-new_rank[i]:02}","                ",new_marks[i])
print()
name_list=list(new_marks.keys())
marks_list=list(new_marks.values())
print("The Student With Maximum Marks is",name_list[0],"with",marks_list[0],"marks")