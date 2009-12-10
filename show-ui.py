import pygtk
pygtk.require('2.0')
import gtk

def main():
    gui = gtk.Builder()
    gui.add_from_file('data/gtk-youtube-dl.ui')
    win_youtubedl = gui.get_object('win_youtubedl')
    win_youtubedl.show_all()
    gtk.main()

if __name__ == '__main__':
    main()
