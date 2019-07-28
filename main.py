import slide_show

if __name__ == '__main__':
    print('This is the init for the main.')
        

slideShow = slide_show.Start()
slideShow.bind("<Escape>", lambda e: slideShow.destroy())  # exit on esc
slideShow.mainloop()