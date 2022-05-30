# zx81pi

A ZX81 built from a Raspberry Pi, Arduino and a ZX81 keyboard.

## The keyboard

This was made using a ZX81 keyboard membrane purchased from RWAP software. The keyboard was stuck to to the outside of a project box and connected to an Arduino Pro Micro.
Code has been written derived from code written by and copyright Dave Curran of Tynemouth Software (http://blog.tynemouthsoftware.co.uk/2012/02/arduino-based-zx81-usb-keyboard.html)
The keyboard can talk directly to an emulator on a Raspberry Pi, enabling the keyword shortcut system of the ZX81 keyboard to be used.

TODO - Arduino Schematic, photos

## The Raspberry Pi

The raspberry pi runs the sz81 emulator

http://sz81.sourceforge.net/

#### Build the emulator (Stock Raspbian)
    wget http://sourceforge.net/projects/sz81/files/sz81/2.1.7/sz81-2.1.7-source.tar.gz/download
    tar -xvf download
Go to the source directory 
    cd sz81-2.1.7
Edit the makefile, make sure the system wide installation lines are uncommented:

    # Comment/uncomment these to choose an installation destination
    # System wide installation
    PREFIX?=/usr/local
    BINDIR?=$(PREFIX)/bin
    DOCDIR?=$(PREFIX)/share/doc/$(TARGET)
    PACKAGE_DATA_DIR?=$(PREFIX)/share/$(TARGET)
    
    # Local installation within your home folder
    #PREFIX?=$(HOME)/Games/$(TARGET)
    #BINDIR?=$(PREFIX)
    #DOCDIR?=$(PREFIX)/doc
    #PACKAGE_DATA_DIR?=$(PREFIX)/data

    # Run from current folder i.e. no installation
    #PREFIX?=.
    #BINDIR?=$(PREFIX)
    #DOCDIR?=$(PREFIX)
    #PACKAGE_DATA_DIR?=$(PREFIX)/data
    
May need to install libsdl:

    sudo apt-get install libsdl1.2-dev

Run:

    make
    sudo make install

Test that the emulator runs by typing sz81 at the command prompt

Ansible Script
ansible-playbook -i hosts playbook.yml
