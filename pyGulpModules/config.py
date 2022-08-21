import os
#path to proj
pathToProj = os.path.dirname(os.path.dirname(__file__))


#### SRC
#path to html
pathToHTML = os.path.join(pathToProj, 'src')
#path to less
pathToLess = os.path.join(pathToProj, 'src', 'less')
#path to html templates
pathToHtmlTemplates = os.path.join(pathToProj, 'src', 'templates')
#path to js files
pathToJsFiles = os.path.join(pathToProj, 'src', 'js')

#### DIST
#path to dist
pathToDist = os.path.join(pathToProj, 'dist')
#path to css
pathToDistCss = os.path.join(pathToProj, 'dist', 'css')
#path to js
pathToJsFiles = os.path.join(pathToProj, 'src', 'js')