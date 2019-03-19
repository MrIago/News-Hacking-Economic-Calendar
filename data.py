import functions

headers_file = "post_header.txt"
form_file = "post_form.txt"

class user:

    def __init__(self):
        self.headers = {}
        self.headers = functions.sep_items(self.headers, headers_file, ':')
        #functions.print_dict(self.headers)
        self.form = {}
        self.form = functions.sep_items(self.form, form_file, ':')
        #functions.print_dict(self.form)
