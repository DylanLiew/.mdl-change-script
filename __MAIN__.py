#this python function aims to write the models' BSIM4 parameters into the .mdl file

TXT_file_path = ''  #the path of your BSIM parameters' storage file
mdl_path = ''#the .mdl file's path
write_path = ''#the output path



words = ""
newlist = ""

dict_find = {}



####    this step aims to read the whole txt document ###
print('Reading file {}...'.format(TXT_file_path))
with open(TXT_file_path,"r") as file:
    words = file.read()
    # print(words)
#############################################################



####    this step aims to split all characters then store them into the list    ###
list_txt = words.split()
for x in list_txt:
    
    
    if x.find("=") != -1:######
        reg = x.split('=')
        # print(reg[0].lower())
        dict_find.update({reg[0].lower():reg[1]})
        

######## NOW THE DICTIONARY WRITTING FINISHED ###########
#############################################################


##### WRITE .mdl FILE#####
# with open(mdl_path,r) as file:
#     for line in file:
#         if line[0] == "+":
#             line



#         else:
#             with open(write_path,"a") as z:
#                 z.write(line)


with open(mdl_path,"r") as file:
    for line in file:
        if line[0] == "+":#if the first component of the line is "+", that means this line consist the variables need to change
            with open (write_path, "a") as z:#firstly we need to write "+", because when we deal with this line, we must delete "+", then in the output stage, the output of "+" will be missing
                z.write("+")
            line_diffplus = line[1:]#dismiss "+"
            line_diffplus = line_diffplus.replace('=',' = ')
            list = line_diffplus.split()
            print(list)
            for i, value in enumerate(list):
                if list[i] == "=":
                    reg1 = list[i-1]
                    # print(list[i-1])
                    reg2 = dict_find.get(reg1)
                    # print(reg2)
                    if reg2 == None:#it is normal that some parameters will be missing
                        reg2 = list [i+1]
                        # print(list[i+1])
                    with open(write_path, "a") as z:
                        z.write(reg1 + " = " + reg2 + "\t\t")
            with open(write_path, "a") as z:
                z.write("\n")


                    


            # with open(write_path,"a") as z:
            #     z.write(line[1:])
        else:
            with open(write_path,"a") as z:
                z.write(line)