import glob, os, time, datetime, shutil

#MyBackup

#get the lsit of all the files in the directory into myfiles
myfiles=glob.glob("C:/Users/Veera/Desktop/A/*.*")
#print myfiles

#get modification info of the files in the list
for i in myfiles:
    statinfo = os.stat(i)
    j=time.localtime(statinfo.st_mtime)
    m_year=j.tm_year
    m_mon=j.tm_mon
    m_day=j.tm_mday
    m_hour=j.tm_hour
    
    #pulling todays information.
    today =datetime.date.today()
    t_year=today.year
    t_mon=today.month
    t_day=today.day

    #compare the modification date with today's date.
    if (m_year == t_year) and (m_mon == t_mon) and (m_day == t_day) and (m_hour <=24):
        print "Files generated within 24hrs and will be copied", "[",i,"]"



        #source_folder_file ="'"+i+"'"
        source_folder_file = i
        x=source_folder_file.replace("\\" , "/" )
        print x#source_folder_file slashes corrected

        Destination_folder = 'C:/Users/Veera/Desktop/B'
        shutil.copy(x,Destination_folder)

        
    
