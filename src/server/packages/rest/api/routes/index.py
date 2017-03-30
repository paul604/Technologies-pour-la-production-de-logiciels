from ...lib.bottle import route, static_file
from config import WELCOMING_PAGE_PATH, WELCOMING_PAGE_NAME, CSS_PAGE_PATH, CSS_PAGE_NAME, JS_PAGE_PATH, JS_PAGE_NAME



# -------------------------------------------------------- index
@route('/')
def index_route():
    '''
    retourn le fichier index.html
    '''
    return static_file(WELCOMING_PAGE_NAME, root=WELCOMING_PAGE_PATH)




# -------------------------------------------------------- css
@route('/css')
def css_route():
    '''
    retourn le fichier main.css
    '''
    return static_file(CSS_PAGE_NAME, root=CSS_PAGE_PATH)




# -------------------------------------------------------- js
@route('/js')
def js_route():
    '''
    retourn le fichier main.js
    '''
    return static_file(JS_PAGE_NAME, root=JS_PAGE_PATH)
