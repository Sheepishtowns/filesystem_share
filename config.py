#remote directory access config
port = 14389  #if invalid auto changes

#all directory and files to be accessed remotely
#if you add files please notice file extension is needed (eg. .pdf .jpg)
accessible_directories = {"public":
                              ["D:\yts\Pictures\Video Projects",
                               "D:\of mice and men.pdf"]
                        , "private":
                              ["D:\sheep"]
                        , "protected":
                              {"readonly":["D:\星战"],
                               "useraccess":[["D:\Heaton","sheep"],#third parameter for readonly
                                             ["D:\Heaton Application","sheep",True]]#user access should specify user for each
                               }
                          } #public can be accessed by anyone, private can only be accessed with a password, protected means read only or accessed with specific username

#password for private stuff (admin tools)
key = "abcd"

#black list ip(whole system)
black_ip = []

#white list ip(whole system)
white_ip = []

#users specify username and password
users = {"sheep":"123"}
