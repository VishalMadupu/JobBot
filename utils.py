# import math,constants,config,time
# from typing import List

# from selenium import webdriver

# def chromeBrowserOptions():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--no-sandbox')
#     options.add_argument("--ignore-certificate-errors")
#     options.add_argument("--disable-extensions")
#     options.add_argument('--disable-gpu')
#     options.add_argument('--disable-dev-shm-usage')
#     if(config.headless):
#         options.add_argument("--headless")
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-blink-features")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     if(len(config.chromeProfilePath)>0):
#         initialPath = config.chromeProfilePath[0:config.chromeProfilePath.rfind("/")]
#         profileDir = config.chromeProfilePath[config.chromeProfilePath.rfind("/")+1:]
#         options.add_argument('--user-data-dir=' +initialPath)
#         options.add_argument("--profile-directory=" +profileDir)
#     else:
#         options.add_argument("--incognito")
#     return options

# def prRed(prt):
#     print(f"\033[91m{prt}\033[00m")

# def prGreen(prt):
#     print(f"\033[92m{prt}\033[00m")

# def prYellow(prt):
#     print(f"\033[93m{prt}\033[00m")

# def getUrlDataFile():
#     urlData = ""
#     try:
#         file = open('data/urlData.txt', 'r')
#         urlData = file.readlines()
#     except FileNotFoundError:
#         text = "FileNotFound:urlData.txt file is not found. Please run ./data folder exists and check config.py values of yours. Then run the bot again"
#         prRed(text)
#     return urlData

# def jobsToPages(numOfJobs: str) -> int:
#   number_of_pages = 1

#   if (' ' in numOfJobs):
#     spaceIndex = numOfJobs.index(' ')
#     totalJobs = (numOfJobs[0:spaceIndex])
#     totalJobs_int = int(totalJobs.replace(',', ''))
#     number_of_pages = math.ceil(totalJobs_int/constants.jobsPerPage)
#     if (number_of_pages > 40 ): number_of_pages = 40

#   else:
#       number_of_pages = int(numOfJobs)

#   return number_of_pages

# def urlToKeywords(url: str) -> List[str]:
#     keywordUrl = url[url.index("keywords=")+9:]
#     keyword = keywordUrl[0:keywordUrl.index("&") ] 
#     locationUrl =  url[url.index("location=")+9:]
#     location = locationUrl[0:locationUrl.index("&") ] 
#     return [keyword,location]

# def writeResults(text: str):
#     timeStr = time.strftime("%Y%m%d")
#     fileName = "Applied Jobs DATA - " +timeStr + ".txt"
#     try:
#         with open("data/" +fileName, encoding="utf-8" ) as file:
#             lines = []
#             for line in file:
#                 if "----" not in line:
#                     lines.append(line)
                
#         with open("data/" +fileName, 'w' ,encoding="utf-8") as f:
#             f.write("---- Applied Jobs Data ---- created at: " +timeStr+ "\n" )
#             f.write("---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result "   +"\n" )
#             for line in lines: 
#                 f.write(line)
#             f.write(text+ "\n")
            
#     except:
#         with open("data/" +fileName, 'w', encoding="utf-8") as f:
#             f.write("---- Applied Jobs Data ---- created at: " +timeStr+ "\n" )
#             f.write("---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result "   +"\n" )

#             f.write(text+ "\n")

# def printInfoMes(bot:str):
#     prYellow("ℹ️ " +bot+ " is starting soon... ")

# def donate(self):
#     prYellow('If you like the project, please support me so that i can make more such projects, thanks!')
#     try:
#         self.driver.get('https://www.automated-bots.com/')
#     except Exception as e:
#         prRed("Error in donate: " +str(e))

# class LinkedinUrlGenerate:
#     def generateUrlLinks(self):
#         path = []
#         for location in config.location:
#             for keyword in config.keywords:
#                     url = constants.linkJobUrl + "?f_AL=true&keywords=" +keyword+self.jobType()+self.remote()+self.checkJobLocation(location)+self.jobExp()+self.datePosted()+self.salary()+self.sortBy()
#                     path.append(url)
#         return path

#     def checkJobLocation(self,job):
#         jobLoc = "&location=" +job
#         match job.casefold():
#             case "asia":
#                 jobLoc += "&geoId=102393603"
#             case "europe":
#                 jobLoc += "&geoId=100506914"
#             case "northamerica":
#                 jobLoc += "&geoId=102221843&"
#             case "southamerica":
#                 jobLoc +=  "&geoId=104514572"
#             case "australia":
#                 jobLoc +=  "&geoId=101452733"
#             case "africa":
#                 jobLoc += "&geoId=103537801"

#         return jobLoc

#     def jobExp(self):
#         jobtExpArray = config.experienceLevels
#         firstJobExp = jobtExpArray[0]
#         jobExp = ""
#         match firstJobExp:
#             case "Internship":
#                 jobExp = "&f_E=1"
#             case "Entry level":
#                 jobExp = "&f_E=2"
#             case "Associate":
#                 jobExp = "&f_E=3"
#             case "Mid-Senior level":
#                 jobExp = "&f_E=4"
#             case "Director":
#                 jobExp = "&f_E=5"
#             case "Executive":
#                 jobExp = "&f_E=6"
#         for index in range (1,len(jobtExpArray)):
#             match jobtExpArray[index]:
#                 case "Internship":
#                     jobExp += "%2C1"
#                 case "Entry level":
#                     jobExp +="%2C2"
#                 case "Associate":
#                     jobExp +="%2C3"
#                 case "Mid-Senior level":
#                     jobExp += "%2C4"
#                 case "Director":
#                     jobExp += "%2C5"
#                 case "Executive":
#                     jobExp  +="%2C6"

#         return jobExp

#     def datePosted(self):
#         datePosted = ""
#         match config.datePosted[0]:
#             case "Any Time":
#                 datePosted = ""
#             case "Past Month":
#                 datePosted = "&f_TPR=r2592000&"
#             case "Past Week":
#                 datePosted = "&f_TPR=r604800&"
#             case "Past 24 hours":
#                 datePosted = "&f_TPR=r86400&"
#         return datePosted

#     def jobType(self):
#         jobTypeArray = config.jobType
#         firstjobType = jobTypeArray[0]
#         jobType = ""
#         match firstjobType:
#             case "Full-time":
#                 jobType = "&f_JT=F"
#             case "Part-time":
#                 jobType = "&f_JT=P"
#             case "Contract":
#                 jobType = "&f_JT=C"
#             case "Temporary":
#                 jobType = "&f_JT=T"
#             case "Volunteer":
#                 jobType = "&f_JT=V"
#             case "Intership":
#                 jobType = "&f_JT=I"
#             case "Other":
#                 jobType = "&f_JT=O"
#         for index in range (1,len(jobTypeArray)):
#             match jobTypeArray[index]:
#                 case "Full-time":
#                     jobType += "%2CF"
#                 case "Part-time":
#                     jobType +="%2CP"
#                 case "Contract":
#                     jobType +="%2CC"
#                 case "Temporary":
#                     jobType += "%2CT"
#                 case "Volunteer":
#                     jobType += "%2CV"
#                 case "Intership":
#                     jobType  +="%2CI"
#                 case "Other":
#                     jobType  +="%2CO"
#         jobType += "&"
#         return jobType

#     def remote(self):
#         remoteArray = config.remote
#         firstJobRemote = remoteArray[0]
#         jobRemote = ""
#         match firstJobRemote:
#             case "On-site":
#                 jobRemote = "f_WT=1"
#             case "Remote":
#                 jobRemote = "f_WT=2"
#             case "Hybrid":
#                 jobRemote = "f_WT=3"
#         for index in range (1,len(remoteArray)):
#             match remoteArray[index]:
#                 case "On-site":
#                     jobRemote += "%2C1"
#                 case "Remote":
#                     jobRemote += "%2C2"
#                 case "Hybrid":
#                     jobRemote += "%2C3"

#         return jobRemote

#     def salary(self):
#         salary = ""
#         match config.salary[0]:
#             case "$40,000+":
#                 salary = "f_SB2=1&"
#             case "$60,000+":
#                 salary = "f_SB2=2&"
#             case "$80,000+":
#                 salary = "f_SB2=3&"
#             case "$100,000+":
#                 salary = "f_SB2=4&"
#             case "$120,000+":
#                 salary = "f_SB2=5&"
#             case "$140,000+":
#                 salary = "f_SB2=6&"
#             case "$160,000+":
#                 salary = "f_SB2=7&"    
#             case "$180,000+":
#                 salary = "f_SB2=8&"    
#             case "$200,000+":
#                 salary = "f_SB2=9&"                  
#         return salary

#     def sortBy(self):
#         sortBy = ""
#         match config.sort[0]:
#             case "Recent":
#                 sortBy = "sortBy=DD"
#             case "Relevent":
#                 sortBy = "sortBy=R"                
#         return sortBy


# utils.py
import math, constants, config, time, tempfile, os
from typing import List
from selenium import webdriver

def chromeBrowserOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    if config.headless:
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    if len(config.chromeProfilePath) > 0:
        # generate a brand-new profile directory each run
        temp_profile = tempfile.mkdtemp(prefix="chrome-profile-")
        options.add_argument(f"--user-data-dir={temp_profile}")
        # preserve the sub-directory name if needed
        profileDir = config.chromeProfilePath.split("/")[-1]
        options.add_argument(f"--profile-directory={profileDir}")
    else:
        options.add_argument("--incognito")

    return options

def prRed(prt):
    print(f"\033[91m{prt}\033[00m")

def prGreen(prt):
    print(f"\033[92m{prt}\033[00m")

def prYellow(prt):
    print(f"\033[93m{prt}\033[00m")

def getUrlDataFile():
    try:
        with open('data/urlData.txt', 'r', encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        text = ("FileNotFound: urlData.txt file is not found. "
                "Please ensure the data folder exists and check config.py values. "
                "Then run the bot again.")
        prRed(text)
        return []

def jobsToPages(numOfJobs: str) -> int:
    if ' ' in numOfJobs:
        totalJobs = int(numOfJobs.split(' ')[0].replace(',', ''))
        pages = math.ceil(totalJobs / constants.jobsPerPage)
        return min(pages, 40)
    else:
        return int(numOfJobs)

def urlToKeywords(url: str) -> List[str]:
    keyword = url.split("keywords=")[1].split("&")[0]
    location = url.split("location=")[1].split("&")[0]
    return [keyword, location]

def writeResults(text: str):
    timeStr = time.strftime("%Y%m%d")
    fileName = f"Applied Jobs DATA - {timeStr}.txt"
    header = (
        f"---- Applied Jobs Data ---- created at: {timeStr}\n"
        "---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result \n"
    )
    data_path = os.path.join('data', fileName)

    # read existing (non-header) lines
    try:
        with open(data_path, 'r', encoding="utf-8") as f:
            lines = [l for l in f if not l.startswith("----")]
    except FileNotFoundError:
        lines = []

    # rewrite with header + old lines + new entry
    with open(data_path, 'w', encoding="utf-8") as f:
        f.write(header)
        for line in lines:
            f.write(line)
        f.write(text + "\n")

def printInfoMes(bot: str):
    prYellow("ℹ️ " + bot + " is starting soon...")

def donate(self):
    prYellow('If you like the project, please support me so that I can make more such projects, thanks!')
    try:
        self.driver.get('https://www.automated-bots.com/')
    except Exception as e:
        prRed("Error in donate: " + str(e))

class LinkedinUrlGenerate:
    def generateUrlLinks(self):
        path = []
        for location in config.location:
            for keyword in config.keywords:
                url = (
                    constants.linkJobUrl
                    + f"?f_AL=true&keywords={keyword}"
                    + self.jobType()
                    + self.remote()
                    + self.checkJobLocation(location)
                    + self.jobExp()
                    + self.datePosted()
                    + self.salary()
                    + self.sortBy()
                )
                path.append(url)
        return path

    def checkJobLocation(self, job):
        jobLoc = "&location=" + job
        match job.casefold():
            case "asia":
                jobLoc += "&geoId=102393603"
            case "europe":
                jobLoc += "&geoId=100506914"
            case "northamerica":
                jobLoc += "&geoId=102221843"
            case "southamerica":
                jobLoc += "&geoId=104514572"
            case "australia":
                jobLoc += "&geoId=101452733"
            case "africa":
                jobLoc += "&geoId=103537801"
        return jobLoc

    def jobExp(self):
        arr = config.experienceLevels
        mapping = {
            "Internship": "1",
            "Entry level": "2",
            "Associate": "3",
            "Mid-Senior level": "4",
            "Director": "5",
            "Executive": "6"
        }
        codes = [mapping[arr[0]]]
        for lvl in arr[1:]:
            codes.append(mapping[lvl])
        return "&f_E=" + "%2C".join(codes)

    def datePosted(self):
        match config.datePosted[0]:
            case "Any Time":       return ""
            case "Past Month":     return "&f_TPR=r2592000"
            case "Past Week":      return "&f_TPR=r604800"
            case "Past 24 hours":  return "&f_TPR=r86400"
        return ""

    def jobType(self):
        arr = config.jobType
        mapping = {
            "Full-time": "F", "Part-time": "P",
            "Contract": "C", "Temporary": "T",
            "Volunteer": "V", "Intership": "I", "Other": "O"
        }
        codes = [mapping[arr[0]]]
        for t in arr[1:]:
            codes.append(mapping[t])
        return "&f_JT=" + "%2C".join(codes)

    def remote(self):
        arr = config.remote
        mapping = {"On-site": "1", "Remote": "2", "Hybrid": "3"}
        codes = [mapping[arr[0]]]
        for r in arr[1:]:
            codes.append(mapping[r])
        return "f_WT=" + "%2C".join(codes)

    def salary(self):
        mapping = {
            "$40,000+": "2", "$60,000+": "3", "$80,000+": "4",
            "$100,000+": "5", "$120,000+": "6", "$140,000+": "7",
            "$160,000+": "8", "$180,000+": "9", "$200,000+": "10"
        }
        return "f_SB2=" + mapping[config.salary[0]]

    def sortBy(self):
        return "sortBy=" + ("DD" if config.sort[0] == "Recent" else "R")
