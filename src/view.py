class View:
    # banner
    @staticmethod
    def banner():
        View.new_line()
        print '[+] WP feautured image poster'
        View.new_line()
    # prints a message
    @staticmethod
    def normal(msg):
        print '[+] {}'.format(msg)
    # prints a warning
    @staticmethod
    def warning(warning):
        print '[-] {}'.format(warning)
    # prints an error
    @staticmethod
    def error(error):
        print '[!] Error: {}'.format(error)
    # ctrl+c key combination was pressed
    @staticmethod
    def ctrl_c_pressed():
        View.warning('CTRL+C was pressed, stopping')
    # prints a line with dashes
    @staticmethod
    def new_line():
        print '----------------------------------------------------------------'
