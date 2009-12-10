import pygtk
pygtk.require('2.0')
import gtk
import popen2

class GtkYouTube:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file('data/gtk-youtube-dl.ui')
        self.win_youtubedl = builder.get_object('win_youtubedl')
        self.txt_url = builder.get_object('txt_url')
        builder.connect_signals(self)

    def show(self):
        self.win_youtubedl.show()

    def on_btn_exit_clicked(self, widget):
        gtk.main_quit()

    def on_btn_download_clicked(self, widget):
        url = self.txt_url.get_text()
        cmd = 'youtube-dl %s' % url
        popen2.popen2(cmd)

    def on_btn_save_clicked(self, widget):
        cmd = 'mplayer -dumpaudio -dumpfile %s %s' % (mp3file, flvfile)
        popen2.popen2(cmd)

if __name__ == '__main__':
    gui = GtkYouTube()
    gui.show()
    gtk.main()
