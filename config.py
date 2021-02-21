#remote directory access config

#set your access port
port = 14389 

#all directory and files to be accessed remotely
#if you add files please notice file extension is needed (eg. .pdf .jpg)

accessible_directories = {"public":#public category
                              ["D:\yts\Pictures\Video Projects",
                               "D:\of mice and men.pdf"]
                        , "protected":#protected category
                              {"readonly":["D:\星战"],
                               "useraccess":[["D:\Heaton","sheep"],            #first parameter is path      
                                             ["D:\Heaton Application","sheep"]]#user access should specify user for each(second parameter)
                               }
                          } #public can be accessed by anyone, protected means read only or accessed with specific username



#users specify username and password
users = {"sheep":"123"}
