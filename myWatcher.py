import os, time
import pyGulpModules.htmlTemplates as htmlTemplates
import pyGulpModules.config as config
FILES = {

}
def main():
##    myStr = "@template('templates/header.html')@template('templates/header123.html')"
##    myStr = '<html>'
##
##    myStr = processTemplates(myStr, templates)
##    print(myStr)
    #myStr = 'templates/header.html'
    #print(readTemplate(myStr))
    #htmlTemplates.processTemplates(r"C:\Users\Alexander\Desktop\pyGulp\src\index.html")

    while True:
        flag = False
        for root, dirnames, files in os.walk(config.pathToHTML):
            for filename in files:
                fullname = os.path.join(root, filename)
                tModif = os.path.getmtime(fullname)
                if filename.endswith('.html'):
                    if not fullname in FILES or FILES[fullname] != tModif:
                        FILES[fullname] = tModif
                        flag = True
        if flag:
            for root, dirnames, files in os.walk(config.pathToHTML):
                for filename in files:
                    fullname = os.path.join(root, filename)
                    if filename.endswith('.html') and fullname.find(config.pathToHtmlTemplates) == -1:
                        htmlTemplates.processTemplates(fullname)
                        print(filename, 'updated')
        time.sleep(1)

if __name__ == "__main__":
    main()