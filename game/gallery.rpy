init python:
    g = Gallery()
    g.transitions = dissolve
screen gallery:
    #tag menu

    #window:
    #    add "images/gallery/gallerybg.png"
    #    yalign .0

    #vbox:
    #    style_prefix "navigation"

    #    xpos 0.824
    #    yalign 0.283

    #    spacing 15
    #    imagebutton auto "images/knopki/button12_%s.png" action ShowMenu("characters")
    #    imagebutton auto "images/knopki/button10_%s.png" action ShowMenu("main_menu")
#screen characters:
    tag menu
    add "images/gallery/gallerybg1.png"
    image "images/knopki/button12_idle.png" xalign 0.976 yalign 0.2
    imagebutton auto "images/knopki/button14_%s.png" xalign 0.976 yalign 0.3 action ShowMenu("chapters")
    imagebutton auto "images/knopki/button15_%s.png" xalign 0.976 yalign 0.4 action ShowMenu("end")
    imagebutton auto "images/knopki/button10_%s.png" xalign 0.976 yalign 0.5 action ShowMenu("main_menu")
    imagebutton auto "images/gallery/arrow_%s.png" xpos 1300 ypos 960 action ShowMenu("characters2")
    image "images/gallery/arrowleft_idle.png" xpos 240 ypos 960
    text "1/2":
        xpos 80
        ypos 957
        size 60
    python:
        g.button("firedigger")
        if persistent.firedigger=="yes":
            if persistent.firedigger_ability=="yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/firedigger_ability.png")
                if persistent.end == "yes":
                    g.image("images/gallery/black.jpg", "images/gallery/characters/firedigger1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/firedigger.png")
        g.button("monstrata")
        if persistent.monstrata=="yes":
            if persistent.monstrata_ability=="yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/monstrata_ability.png")
                if persistent.end == "yes":
                    g.image("images/gallery/black.jpg", "images/gallery/characters/monstrata1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/monstrata.png")
        g.button("dizick")
        if persistent.dizick=="yes":
            if persistent.dizick_ability=="yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/dizick_ability.png")
                if persistent.end == "yes":
                    g.image("images/gallery/black.jpg", "images/gallery/characters/dizick1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/dizick.png")
        g.button("sotarks")
        if persistent.sotarks=="yes":
            if persistent.sotarks_ability == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/sotarks_ability.png")
                if persistent.end =="yes":
                    g.image("images/gallery/black.jpg", "images/gallery/characters/sotarks1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/sotarks.png")
        g.button("Talala")
        if persistent.talala == "yes":
            if persistent.talala_ability == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/talala_ability.png")
                if persistent.end == "yes":
                    g.image("images/gallery/black.jpg", "images/gallery/characters/talala1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/talala.png")
        g.button("ppy")
        if persistent.ppy=="yes":
            if persistent.ppy_ability == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/ppy_ability.png")
                if persistent.end == "yes":
                    g.image("images/gallery/black.jpg", "images/gallery/characters/ppy1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/ppy.png")
        g.button("alumetri")
        if persistent.alumetri == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/alumetri.png")
            if persistent.end == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/alumetri1.png")
        g.button("rafis")
        if persistent.rafis == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/rafis.png")
            if persistent.end == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/rafis1.png")
        g.button("bmc")
        if persistent.bmc == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/bmc.png")
            if persistent.end == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/bmc1.png")
        g.button("cookiezi")
        if persistent.cookiezi == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/cookiezi.png")
            if persistent.end == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/cookiezi1.png")

    add g.make_button("firedigger", "images/gallery/characters_icon/firedigger.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=10)
    add g.make_button("monstrata", "images/gallery/characters_icon/monstrata.png", locked="images/gallery/characters_icon/black.jpg", xpos=335, ypos=10)
    add g.make_button("dizick", "images/gallery/characters_icon/dizick.png", locked="images/gallery/characters_icon/black.jpg", xpos=640, ypos=10)
    add g.make_button("sotarks", "images/gallery/characters_icon/sotarks.png", locked="images/gallery/characters_icon/black.jpg", xpos=950, ypos=10)
    add g.make_button("Talala", "images/gallery/characters_icon/talala.png", locked="images/gallery/characters_icon/black.jpg", xpos=1260, ypos=10)
    add g.make_button("ppy", "images/gallery/characters_icon/ppy.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=490)
    add g.make_button("alumetri", "images/gallery/characters_icon/alumetri.png", locked="images/gallery/characters_icon/black.jpg", xpos=335, ypos=490)
    add g.make_button("rafis", "images/gallery/characters_icon/rafis.png", locked="images/gallery/characters_icon/black.jpg", xpos=640, ypos=490)
    add g.make_button("bmc", "images/gallery/characters_icon/bmc.png", locked="images/gallery/characters_icon/black.jpg", xpos=950, ypos=490)
    add g.make_button("cookiezi", "images/gallery/characters_icon/cookiezi.png", locked="images/gallery/characters_icon/black.jpg", xpos=1260, ypos=490)
screen characters2:
    tag menu
    add "images/gallery/gallerybg1.png"
    image "images/knopki/button12_idle.png" xalign 0.976 yalign 0.2
    imagebutton auto "images/knopki/button14_%s.png" xalign 0.976 yalign 0.3 action ShowMenu("chapters")
    imagebutton auto "images/knopki/button15_%s.png" xalign 0.976 yalign 0.4 action ShowMenu("end")
    imagebutton auto "images/knopki/button10_%s.png" xalign 0.976 yalign 0.5 action ShowMenu("main_menu")
    image "images/gallery/arrow_idle.png" xpos 1300 ypos 960
    imagebutton auto "images/gallery/arrowleft_%s.png" xpos 240 ypos 960 action ShowMenu("gallery")
    text "2/2":
        xpos 80
        ypos 957
        size 60
    python:
        g.button("bogdan")
        if persistent.bogdan == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/bogdan.png")
        g.button("xdem")
        if persistent.xdem == "yes":
            if persistent.end == "yes":
                g.image("images/gallery/black.jpg", "images/gallery/characters/xdem1.png")
            else:
                g.image("images/gallery/black.jpg", "images/gallery/characters/xdem.png")
        g.button("vayfochka")
        if persistent.vayfochka == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/vayfochka.png")
        g.button("chika")
        if persistent.chika == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/chika.png")
        g.button("dez")
        if persistent.dez == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/dezodor.png")
        g.button("index")
        if persistent.index == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/characters/index.png")

    add g.make_button("bogdan", "images/gallery/characters_icon/bogdik.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=10)
    add g.make_button("xdem", "images/gallery/characters_icon/xdem.png", locked="images/gallery/characters_icon/black.jpg", xpos=335, ypos=10)
    add g.make_button("vayfochka", "images/gallery/characters_icon/vayfochka.png", locked="images/gallery/characters_icon/black.jpg", xpos=640, ypos=10)
    add g.make_button("chika", "images/gallery/characters_icon/chika.png", locked="images/gallery/characters_icon/black.jpg", xpos=950, ypos=10)
    add g.make_button("dez", "images/gallery/characters_icon/dez.png", locked="images/gallery/characters_icon/black.jpg", xpos=1260, ypos=10)
    add g.make_button("index", "images/gallery/characters_icon/index.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=490)

screen chapters:
    tag menu
    add "images/gallery/gallerybg1.png"
    imagebutton auto "images/knopki/button12_%s.png" xalign 0.976 yalign 0.2 action ShowMenu("gallery")
    image "images/knopki/button14_idle.png" xalign 0.976 yalign 0.3
    imagebutton auto "images/knopki/button15_%s.png" xalign 0.976 yalign 0.4 action ShowMenu("end")
    imagebutton auto "images/knopki/button10_%s.png" xalign 0.976 yalign 0.5 action ShowMenu("main_menu")
    image "images/gallery/arrow_idle.png" xpos 1300 ypos 960
    image "images/gallery/arrowleft_idle.png" xpos 240 ypos 960
    text "1/1":
        xpos 80
        ypos 957
        size 60
    python:
        g.button("ch1")
        if persistent.ch1 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter1.png")
        g.button("ch2")
        if persistent.ch2 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter2.png")
        g.button("ch3")
        if persistent.ch3 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter3.png")
        g.button("ch4")
        if persistent.ch4 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter4_1.png")
            g.image("images/gallery/black.jpg", "images/chapter/Chapter4_2.png")
        g.button("ch5")
        if persistent.ch5 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter5.png")
        g.button("ch6")
        if persistent.ch6 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter6.png")
        g.button("ch7")
        if persistent.ch7 == "yes":
            g.image("images/gallery/black.jpg", "images/chapter/Chapter7.png")

    add g.make_button("ch1", "images/gallery/chapter_icon/1.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=10)
    add g.make_button("ch2", "images/gallery/chapter_icon/2.png", locked="images/gallery/characters_icon/black.jpg", xpos=335, ypos=10)
    add g.make_button("ch3", "images/gallery/chapter_icon/3.png", locked="images/gallery/characters_icon/black.jpg", xpos=640, ypos=10)
    add g.make_button("ch4", "images/gallery/chapter_icon/4.png", locked="images/gallery/characters_icon/black.jpg", xpos=950, ypos=10)
    add g.make_button("ch5", "images/gallery/chapter_icon/5.png", locked="images/gallery/characters_icon/black.jpg", xpos=1260, ypos=10)
    add g.make_button("ch6", "images/gallery/chapter_icon/6.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=490)
    add g.make_button("ch7", "images/gallery/chapter_icon/7.png", locked="images/gallery/characters_icon/black.jpg", xpos=335, ypos=490)

screen end:
    tag menu
    add "images/gallery/gallerybg1.png"
    imagebutton auto "images/knopki/button12_%s.png" xalign 0.976 yalign 0.2 action ShowMenu("gallery")
    imagebutton auto "images/knopki/button14_%s.png" xalign 0.976 yalign 0.3 action ShowMenu("chapters")
    image "images/knopki/button15_idle.png" xalign 0.976 yalign 0.4
    imagebutton auto "images/knopki/button10_%s.png" xalign 0.976 yalign 0.5 action ShowMenu("main_menu")
    image "images/gallery/arrow_idle.png" xpos 1300 ypos 960
    image "images/gallery/arrowleft_idle.png" xpos 240 ypos 960
    text "1/1":
        xpos 80
        ypos 957
        size 60
    python:
        g.button("end1")
        if persistent.end1 == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/end/1.png")
        g.button("end2")
        if persistent.end2 == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/end/2.png")
        g.button("end3")
        if persistent.end3 == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/end/3.png")
        g.button("end4")
        if persistent.end4 == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/end/4.png")
        g.button("end5")
        if persistent.end5 == "yes":
            g.image("images/gallery/black.jpg", "images/gallery/end/5.png")

    add g.make_button("end1", "images/gallery/chapter_icon/1.png", locked="images/gallery/characters_icon/black.jpg", xpos=20, ypos=10)
    add g.make_button("end2", "images/gallery/chapter_icon/2.png", locked="images/gallery/characters_icon/black.jpg", xpos=335, ypos=10)
    add g.make_button("end3", "images/gallery/chapter_icon/3.png", locked="images/gallery/characters_icon/black.jpg", xpos=640, ypos=10)
    add g.make_button("end4", "images/gallery/chapter_icon/4.png", locked="images/gallery/characters_icon/black.jpg", xpos=950, ypos=10)
    add g.make_button("end5", "images/gallery/chapter_icon/5.png", locked="images/gallery/characters_icon/black.jpg", xpos=1260, ypos=10)
