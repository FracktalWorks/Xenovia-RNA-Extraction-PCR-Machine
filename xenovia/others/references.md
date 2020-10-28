Xenovia Application Auto Startup References

Ankit Bhatnagar
ankit.bhatnagarindia@gmail.com

July 2020
--------------------------------------------

X Server + Xenovia Application Autostart
------------------------------------------
(1) https://www.raspberrypi.org/forums/viewtopic.php?t=42888
(2) websences.com/dpkg-reconfigure-x11-common/
(3) https://github.com/raspberrypi/linux/issues/2517#issuecomment-387867933

(2) global xinitrc file : /etc/X11/xinit/xinitrc (set permissin a+x)
(2) pi user .xinitrc file : /home/pi/.xinitrc (set permission a+x)
(3) global rc.local file : /etc/rc.local (set permission a+x)


Removing Logo And Initial Boot Stuff
----------------------------------------
(1) https://www.raspberrypi.org/forums/viewtopic.php?t=189666
(2) https://www.raspberrypi.org/forums/viewtopic.php?t=236647
(3) https://www.thedigitalpictureframe.com/customize-your-raspberry-pi-splash-screen-raspbian-stretch-april-2019-version/
(4) https://github.com/raspberrypi/linux/issues/2517#issuecomment-387867933

Execution Flow
---------------
rc.local ---> startx ---> global .xinitrc ---> pi user .xinitrc ---> xenovia program
