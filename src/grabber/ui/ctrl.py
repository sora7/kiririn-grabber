class KiririnCtrl(object):
    __view = None
    __model = None

    def __init__(self, view, model):
        self.__view = view

        self.__view.setCallbacks(self.new_menu_handler,
                                 self.load_menu_handler,
                                 self.save_menu_handler,
                                 self.howto_menu_handler,
                                 self.about_menu_handler)
        self.__model = model

        self.__bind_handlers()

        self.__view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
        self.__view.root.mainloop()

    def __bind_handlers(self):
        self.__view.buttons['start'].bind("<Button-1>", self.start_handler)
        self.__view.buttons['stop'].bind("<Button-1>", self.stop_handler)

    def start_handler(self, event):
        self.__model.start()

    def stop_handler(self, event):
        self.__model.stop()

    # the fun must go on!
    def new_menu_handler(self):
        print('NEW')

    def load_menu_handler(self):
        print('LOAD')

    def save_menu_handler(self):
        print('SAVE')

    def howto_menu_handler(self):
        print('HOW TO BE A RETARD')

    def about_menu_handler(self):
        print('ABOUT')

    def close_handler(self):
        self.__view.close()