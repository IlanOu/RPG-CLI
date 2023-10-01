import curses

# define the menu function
def menu(title, classes, color='white'):
  # define the curses wrapper
  def character(stdscr,):
    attributes = {}
    # stuff i copied from the internet that i'll put in the right format later
    icol = {
      1:'blue',
      2:'green',
      3:'cyan',
      4:'brown',
      5:'magenta',
      6:'yellow',
      7:'white'
    }
    # put the stuff in the right format
    col = {v: k for k, v in icol.items()}

    # declare the background color

    bc = curses.COLOR_BLACK

    # make the 'normal' format
    curses.init_pair(1, 7, bc)
    attributes['normal'] = curses.color_pair(1)


    # make the 'highlighted' format
    try:
        curses.init_pair(2, col[color], bc)
    except:
        print("Error: '", color, "' does not exist in current colors." )
        return "Error: '", color, "' does not exist in current colors"
        
    attributes['highlighted'] = curses.color_pair(2)


    # handle the menu
    c = 0
    option = 0
    while c != 10:

        stdscr.erase() # clear the screen (you can erase this if you want)

        # add the title
        stdscr.addstr(f"{title}\n", curses.color_pair(1))

        # add the options
        for i in range(len(classes)):
            # handle the colors
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            
            # actually add the options

            stdscr.addstr(f'> ', attr)
            stdscr.addstr(f'{classes[i]}' + '\n', attr)
        c = stdscr.getch()

        # handle the arrow keys
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1
    return option
  return curses.wrapper(character)




print(f"output:", 
      menu('TEST', 
           ['this will return 0',
            'this will return 1', 
            'this is just to show that you can do more options then just two'], 
           'magenta'))
