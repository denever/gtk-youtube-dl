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
        self.btn_download = builder.get_object('btn_download')
        self.btn_save = builder.get_object('btn_save')
        self.chs_fileflv = builder.get_object('chs_fileflv')
        self.chs_filemp3 = builder.get_object('chs_filemp3')
        builder.connect_signals(self)

    def show(self):
        self.win_youtubedl.show()

    def on_btn_exit_clicked(self, widget):
        gtk.main_quit()

    def on_btn_download_clicked(self, widget):
        url = self.txt_url.get_text()
        flv = self.chs_fileflv.get_filename()
        cmd = 'youtube-dl -q -o %s  "%s"' % (flv, url)
        stdin, stdout = popen2.popen2(cmd)

    def on_btn_save_clicked(self, widget):
        mp3file = self.chs_filemp3.get_filename()
        print mp3file
        cmd = 'mplayer -dumpaudio -dumpfile %s %s' % (mp3file, flvfile)
        popen2.popen2(cmd)
        
    def on_txt_url_changed(self, widget):
        self.btn_download.set_sensitive(True)

    def on_chs_filemp3_changed(self, widget):
        self.btn_save.set_sensitive(True)
    

if __name__ == '__main__':
    gui = GtkYouTube()
    gui.show()
    gtk.main()
