#remote directory access config

#set your access port
port = 14389 

#all directory and files to be accessed remotely
#if you add files please notice file extension is needed (eg. .pdf .jpg)
#Add anything

accessible_directories = {"public":#public category
                              [#Add in here --> "/path/to/anything","/path/to/anything"
                                
                              ]  
                        , "protected":#protected category
                               "useraccess":[
                                  #add in here --> ["path/to/anything", "user"],["path/to/anything", "user2"]
                               ]                                               #first parameter is path
                                                                               #user access should specify user for each(second parameter)
                                                                               #user config down below
                          } #public can be accessed by anyone, protected can be accessed with specific username



#users specify username and password
#for access protected ones
users = {"sheep":"123"}
