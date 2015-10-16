import tkinter.ttk

class KiririnView(object):
    __root = None

    # ui widgets
    buttons = {}
    checkboxes = {}

    booru_var = None
    tags_var = None

    __select_booru_combobox = None

    # callbacks for menu commands
    # "great" thanks to Tk developers
    newJobCallback = None
    loadJobCallback = None
    saveCurrentJobCallback = None
    howtoCallback = None
    aboutCallback = None

    def setCallbacks(self, newJ, loadJ, saveJ, howto, about):
        self.newJobCallback = newJ
        self.loadJobCallback = loadJ
        self.saveCurrentJobCallback = saveJ
        self.howtoCallback = howto
        self.aboutCallback = about

    # OMG, square-wheeled bicycle
    def menu_new(self):
        self.newJobCallback()

    def menu_load(self):
        self.loadJobCallback()

    def menu_save_curr(self):
        self.saveCurrentJobCallback()

    def menu_about(self):
        self.aboutCallback()

    def menu_howto(self):
        self.howtoCallback()

    def __init__(self):
        self.__root = None

        self.__create_ui()

        self.__default()

    @property
    def root(self):
        return self.__root

    def set_booru_list(self, lst):
        self.__select_booru_combobox['values'] = lst

    def __default(self):
        self.checkboxes['rating_safe'].set(1)
        self.checkboxes['rating_questionable'].set(1)

        self.checkboxes['size_original'].set(1)
        self.checkboxes['size_resized'].set(1)

    def __create_ui(self):
        self.__root = tkinter.Tk()

        self.__root.title('Kiririn Booru Grabber')

        x, y, w, h = 0, 0, 500, 400
        self.__root.geometry('%sx%s+%s+%s' % (w, h, x, y))

        menubar = tkinter.Menu(self.__root)

        job_menu = tkinter.Menu(menubar, tearoff=0)
        job_menu.add_command(label='Save current Job',
                             command=self.menu_save_curr)
        job_menu.add_separator()
        job_menu.add_command(label='New Job', command=self.menu_new)
        job_menu.add_command(label='Load Job', command=self.menu_load)
        menubar.add_cascade(label='Job', menu=job_menu)

        help_menu = tkinter.Menu(menubar, tearoff=0)

        m1 = tkinter.Menu(help_menu)
        # help_menu.add_cascade(label='hhhhhh', menu=m1)
        # m1 = tkinter.Menubutton(help_menu, text='ONE')
        # m2 = tkinter.Menubutton(help_menu, text='TWO')
        help_menu.add_command(label='How to', command=self.menu_howto)
        help_menu.add_command(label='About', command=self.menu_about)
        menubar.add_cascade(label='Help', menu=help_menu)

        self.__root.config(menu=menubar)

        main_frame = tkinter.ttk.Frame(self.__root)
        main_frame['padding'] = (5, 5)
        main_frame.pack(side='top', fill='both', expand=True)

        upper_frame = tkinter.ttk.Frame(main_frame)
        upper_frame.pack(side='top', fill='x', expand=False)
        # ---------------------------------------------------------------------
        select_frame = tkinter.ttk.Frame(upper_frame)
        select_frame.pack(side='left', fill='x', expand=True)
        select_frame['padding'] = (5, 5)

        select_booru_label = tkinter.ttk.Label(select_frame,
                                               text='Select Booru:')
        select_booru_label.pack(side='top', fill='x')

        self.booru_var = tkinter.StringVar()
        self.__select_booru_combobox = tkinter.ttk.Combobox(select_frame)
        self.__select_booru_combobox.pack(side='top', fill='x')

        tags_label = tkinter.ttk.Label(select_frame, text='Enter Tags:')
        tags_label.pack(side='top', fill='x')

        self.tags_var = tkinter.StringVar()
        tags_edit = tkinter.ttk.Entry(select_frame, textvariable=self.tags_var)
        tags_edit.pack(side='top', fill='x')

        save_label = tkinter.ttk.Label(select_frame, text='Save Path:')
        save_label.pack(side='top', fill='x')

        self.save_var = tkinter.StringVar()
        save_edit = tkinter.ttk.Entry(select_frame, textvariable=self.save_var)
        save_edit.pack(side='top', fill='x')

        # ---------------------------------------------------------------------
        options_frame = tkinter.ttk.LabelFrame(upper_frame, text='Options')
        options_frame.pack(side='left', fill='both', expand=False)

        rating_frame = tkinter.ttk.Frame(options_frame)
        rating_frame.pack(side='left', fill='both', expand=False)

        rating_label = tkinter.ttk.Label(rating_frame, text='Rating:')
        rating_label.pack(side='top', fill='x', anchor='nw')

        self.checkboxes['rating_safe'] = tkinter.IntVar()
        rating_safe_checkbox = tkinter.ttk.Checkbutton(rating_frame, text='Safe',
                                variable=self.checkboxes['rating_safe'])
        rating_safe_checkbox.pack(side='top', fill='none', anchor='nw')

        self.checkboxes['rating_questionable'] = tkinter.IntVar()
        rating_questionable_checkbox = tkinter.ttk.Checkbutton(rating_frame,
                                                           text='Questionable',
                                variable=self.checkboxes['rating_questionable'])
        rating_questionable_checkbox.pack(side='top', fill='none', anchor='nw')

        self.checkboxes['rating_explicit'] = tkinter.IntVar()
        rating_explicit_checkbox = tkinter.ttk.Checkbutton(rating_frame,
                                                       text='Explicit',
                                variable=self.checkboxes['rating_explicit'])
        rating_explicit_checkbox.pack(side='top', fill='none', anchor='nw')

        size_frame = tkinter.ttk.Frame(options_frame)
        size_frame.pack(side='left', fill='both', expand=False)

        size_label = tkinter.ttk.Label(size_frame, text='Size:')
        size_label.pack(side='top', fill='none', anchor='nw')

        self.checkboxes['size_original'] = tkinter.IntVar()
        size_original_checkbox = tkinter.ttk.Checkbutton(size_frame,
                                                     text='Original',
                                variable=self.checkboxes['size_original'])
        size_original_checkbox.pack(side='top', fill='none', anchor='nw')

        self.checkboxes['size_resized'] = tkinter.IntVar()
        size_resized_checkbox = tkinter.ttk.Checkbutton(size_frame, text='Resized',
                                variable=self.checkboxes['size_resized'])
        size_resized_checkbox.pack(side='top', fill='none', anchor='nw')
        # --------------------------------------------------------------------------

        actions_frame = tkinter.ttk.LabelFrame(upper_frame, text='Actions')
        actions_frame.pack(side='right', fill='both', expand=False)
        actions_frame['padding'] = (5, 5)

        self.buttons['start'] = tkinter.ttk.Button(actions_frame, text='START')
        self.buttons['start'].pack(side='top', fill='x')

        self.buttons['pause'] = tkinter.ttk.Button(actions_frame, text='PAUSE')
        self.buttons['pause'].pack(side='top', fill='x')

        self.buttons['stop'] = tkinter.ttk.Button(actions_frame, text='STOP')
        self.buttons['stop'].pack(side='top', fill='x')

        # ====================================================================

        # tags_frame = tkinter.ttk.Frame(main_frame)
        # tags_frame.pack(side='top', fill='x', expand=False)
        # tags_frame['padding'] = (5, 5)

        # progress frame

        progress_frame = tkinter.ttk.Frame(main_frame)
        progress_frame.pack(side='top', fill='x', expand=False)
        progress_frame['padding'] = (5, 5)

        progress_label = tkinter.ttk.Label(progress_frame, text='STAGE 1 of 3')
        progress_label.pack(side='left', fill='x')

        grab_progress = tkinter.ttk.Progressbar(progress_frame)
        grab_progress.pack(side='left', fill='x', expand=True)

        log_text = tkinter.Text(main_frame)
        log_text.pack(side='top', fill='both', expand=True)

    def close(self):
        self.__root.destroy()
        self.__root.quit()