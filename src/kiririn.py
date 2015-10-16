from grabber.ui.view import KiririnView
from grabber.ui.model import KiririnModel
from grabber.ui.ctrl import KiririnCtrl


class KiririnProg(object):
    view = KiririnView()
    model = KiririnModel(view)
    ctrl = KiririnCtrl(view, model)

if __name__ == '__main__':
    prog = KiririnProg()
