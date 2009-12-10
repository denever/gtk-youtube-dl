import pygtk
pygtk.require('2.0')
import gtk
import popen2

class GtkYouTube:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file('data/gtk-youtube-dl.ui')
        self.win_youtubedl = builder.get_object('win_youtubedl')
        builder.connect_signals(self)

    def show(self):
        self.win_youtubedl.show()

    def on_btn_exit_clicked(self, widget):
        gtk.main_quit()

    def on_btn_download_clicked(self, widget):
        pass

    def on_btn_save_clicked(self, widget):
        pass

if __name__ == '__main__':
    gui = GtkYouTube()
    gui.show()
    gtk.main()
