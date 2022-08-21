#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alexander
#
# Created:     21.08.2022
# Copyright:   (c) Alexander 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import config
def main():
    pass

def readHTML(filename):
    '''
    Читает html файл. Возвращает строку с содержимым
    '''
    try:
        htmlContent = ''
        with open(filename, 'rb') as fh:
            htmlContent = fh.read(os.path.getsize(filename)).decode("UTF-8").replace('\r', '')#.replace('\n', '_####_')
    except Exception as err:
        print('readHTML:', err)
    finally:
        return htmlContent
def readTemplate(templatePath:str):
    '''
    Читаю шаблон html. На вход путь к шаблону
    На выходе строка с html шаблоном или пустой строкой, если прочесть не получилось
    '''
    try:
        templateContent = ''
        templatePath = templatePath.replace('/', "\\")
        templatePath = os.path.join(config.pathToHTML, templatePath)
        if not os.path.isfile(templatePath):
            templatePath += ".html"
        with open(templatePath, 'rb') as fh:
            templateContent = fh.read(os.path.getsize(templatePath)).decode("UTF-8")
    except Exception as err:
        print('readTemplate:', err)
    finally:
        return templateContent

def writeHTML(htmlFilename, fullHTML):
    '''
    Запись htmlFilename
    Записываю fullHTML
    '''
    try:
        distFilename = htmlFilename.replace(config.pathToHTML, config.pathToDist)

        with open(distFilename, 'w', encoding="UTF-8") as wh:
            wh.write(fullHTML)#.replace('_####_', '\n')
    except Exception as err:
        print('writeHTML', err)

def processTemplates(htmlFilename):
    fullHTML = readHTML(htmlFilename)
    templates = templatePathGetter(fullHTML)
    for curTemplate in templates:
        templateHTML = readTemplate(curTemplate)
        if templateHTML.strip() != '':
            fullHTML = fullHTML.replace("@include('"+curTemplate+"')", templateHTML)
    writeHTML(htmlFilename, fullHTML)
def templatePathGetter(testString:str):
    try:
        result = []
        indAt = testString.index('@')
        while True:
            frmPath = testString.index("'", indAt)+1
            toPath = testString.index("'", frmPath)
            result.append(testString[frmPath:toPath])
            indAt = testString.index('@', toPath+1)
    except Exception as err:
        pass
    finally:
        return result
if __name__ == '__main__':
    main()
