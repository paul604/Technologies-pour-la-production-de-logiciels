from ...lib.bottle import route, static_file
from config import WELCOMING_PAGE_PATH, WELCOMING_PAGE_NAME



# -------------------------------------------------------- index
@route('/')
def e_route():
    '''
    Liste les équipements où l'on peut pratiquer l'activité dont le nom exact (`request.query.activite`) est passé en GET
    '''
    return static_file(WELCOMING_PAGE_NAME, root=WELCOMING_PAGE_PATH)
