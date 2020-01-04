label free_time1:
    if free_time < ft_max:
        call screen imagemap2
        $ result = _return
        if result == "dinning":
            scene bg ronpa_dininghall with dissolve
            show sprite_b bmc with dissolve
            "Этот тип похоже из столовой вообще не выбирается."
            menu:
                "Провести время с Бистролом.":
                    if bmcr == 0:
                        jump bmc1
                    if bmcr == 1:
                        jump bmc2
                    if bmcr > 1:
                        ob "Вы уже прокачали отношения с Бистролом на максимум, найдите себе другого собеседника."
                        scene bg koridor1 with dissolve
                        jump free_time1
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor1 with dissolve
                    jump free_time1
        if result == "dRoom":
            "Мне нечего делать в своей комнате."
            jump free_time1
        if result == "rRoom":
            "Я постучал в дверь."
            "..."
            "Нет ответа. Похоже Рафиса нет в своей комнате."
            jump free_time1
        if result == "sRoom":
            "Стук в дверь."
            "Щелчок."
            scene bg ronpa_sroom with dissolve
            show sprite_s sotarks with dissolve
            st "Привет."
            st "Ты что-то хотел?"
            menu:
                "Провести время с Сотарксом.":
                    if sotarksr == 0:
                        jump sotarks1
                    if sotarksr == 1:
                        jump sotarks2
                    if sotarksr > 1:
                        ob "Вы уже прокачали отношения с Сотарксом на максимум, найдите себе другого собеседника."
                        scene bg koridor1 with dissolve
                        jump free_time1
                "Найти собеседника получше.":
                    "Ой, извини дверью ошибся."
                    scene koridor1 with dissolve
                    jump free_time1
        if result == "cRoom":
            "Тук-тук."
            "Нет ответа. Неудивительно."
            jump free_time1
        if result == "aRoom":
            if ft_number != 2:
                "Тук-тук."
                scene bg ronpa_aroom with dissolve
                show sprite_a alumetri with dissolve
                al "Здравствуй, Диггер."
                al "Чем могу помочь?"
                menu:
                    "Провести время с Алюметри.":
                        if alumetrir == 0:
                            jump alumetri1
                        if alumetrir == 1:
                            jump alumetri2
                        if alumetrir > 1:
                            ob "Вы уже прокачали отношения с Алюметри на максимум, найдите себе другого собеседника."
                            scene bg koridor1 with dissolve
                            jump free_time1
                    "Найти собеседника получше.":
                        dg "Извини, я дверью ошибся."
                        scene bg koridor1 with dissolve
                        jump free_time1
            else:
                "Тук-тук."
                "Никто не отвечает."
                jump free_time1
        if result == "tRoom":
            "Привет, дверь! Как твои дела?"
            "Нет ответа..."
            jump free_time1
        if result == "bRoom":
            "Тик-ток, дин-дон!"
            "Нет ответа."
            jump free_time1
        if result == "trash":
            scene bg ronpa_trash with dissolve
            "Здесь никого нет."
            "Пойду поищу в другом месте."
            scene bg koridor1 with dissolve
            jump free_time1
        if result == "storage":
            "Вряд ли там кто-то будет. Лучше выберу другое место."
            jump free_time1
        if result == "laundry":
            scene bg ronpa_laundry with dissolve
            "Никого. Пойду поищу в другом месте."
            scene bg koridor1 with dissolve
            jump free_time1
        if result == "bath":
            "Вряд ли там будет кто-нибудь."
            "Лучше выберу другое место."
            jump free_time1
        if result == "school":
            scene bg koridor2 with dissolve
            jump free_time11
    else:
        if ft_number == 1:
            jump nighttime1
        if ft_number == 2:
            jump murder1
label free_time11:
    if free_time < ft_max:
        call screen imagemap1
        $ result = _return
        if result == "dormitory":
            scene bg koridor1 with dissolve
            jump free_time1
        if result == "shop":
            scene bg ronpa_shop with dissolve
            call osu_shop from _call_osu_shop_1
            scene bg koridor2 with dissolve
            jump free_time11
        if (result == "classA") or (result == "classB") or (result == "MedLab"):
            "Закрыто!!!"
            jump free_time11
        if result == "2F":
            "На второй этаж пройти нельзя!!!"
            jump free_time11
        if result == "cinema":
            scene bg ronpa_cinema with dissolve
            "Похоже здесь никого нет."
            "Поищу в другом месте."
            scene bg koridor2 with dissolve
            jump free_time11
        if result == "lobby":
            scene bg ronpa_entrance with dissolve
            show sprite_r rafis with dissolve
            ra "О, Диггер, ты тоже решил сюда прийти?"
            menu:
                "Провести время с Рафисом":
                    if rafisr == 0:
                        jump rafis1
                    if rafisr == 1:
                        jump rafis2
                    if rafisr > 1:
                        ob "Вы уже прокачали отношения с Рафисом на максимум, найдите себе другого собеседника."
                        scene bg koridor2 with dissolve
                        jump free_time11
                "Найти собеседника получше.":
                    dg "Эм, а где здесь туалет?"
                    scene koridor2 with dissolve
                    jump free_time11
        if result == "gym":
            scene bg ronpa_pregym with dissolve
            scene bg ronpa_gym with dissolve
            show sprite_t talala:
                zoom .5
                yalign .999
                xalign .5
            with dissolve
            ta "Диггер! Привет! Рад тебя видеть."
            menu:
                "Провести время с Талалой":
                    if talalar == 0:
                        jump talala1
                    if talalar == 1:
                        jump talala2
                    if talalar > 1:
                        ob "Вы уже прокачали отношения с Талалой на максимум, найдите себе другого собеседника."
                        scene bg koridor2 with dissolve
                        jump free_time11
                "Найти собеседника получше.":
                    dg "Извини, но у меня дела."
                    dg "Пока"
                    scene bg ronpa_pregym with dissolve
                    "Я вышел из спортзала."
                    scene bg koridor2 with dissolve
                    jump free_time11
    else:
        if ft_number == 1:
            jump nighttime1
        if ft_number == 2:
            jump murder1


###ТАЛАЛА
label talala_gift:
    menu:
        "Подарить ему подарок.":
            if (talala1 >= 1) and (talala2 == 0):
                $ talala1 -= 1
                "Для Талалы у меня есть только Обувь Анжелы."
                dg "Возьми, думаю, это может тебе понравиться."
                ta "Стой... Неужели это то, что я думаю?!"
                ta "Спасибо большое! Я искал это так много времени."
                return
            if (talala2 >= 1) and (talala1 == 0):
                $ talala2 -= 1
                "Для Талалы у меня есть только Книга: как зафармить Чику."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                ta "Это что, гайд, как фкшнуть Чику?"
                ta "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (talala1 >= 1) and (talala2 >= 1):
                menu:
                    "Обувь Анжелы.":
                            $ talala1 -= 1
                            dg "Возьми, думаю, это может тебе понравиться."
                            ta "Стой... Неужели это то, что я думаю?!"
                            ta "Спасибо большое! Я искал это так много времени."
                            return
                    "Книга.":
                            $ talala2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            ta "Это что, гайд, как фкшнуть Чику?"
                            ta "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (talala1 == 0) and (talala2 == 0):
                "У меня нет подарка для Талалы."
                dg "Ладно, я пожалуй пойду. Удачи."
                ta "Пока, Диггер!"
                if glava == 5:
                    scene bg koridor2 with dissolve
                    jump free_time11
                if glava == 6:
                    scene bg koridor1 with dissolve
                    jump free_time2
                if glava == 7:
                    scene bg koridor5 with dissolve
                    jump free_time3_2
        "Уйти.":
            if glava == 5:
                scene bg koridor2 with dissolve
                jump free_time11
            if glava == 6:
                scene bg koridor1 with dissolve
                jump free_time2
            if glava == 7:
                scene bg koridor5 with dissolve
                jump free_time3_2

label talala1:
    $ free_time += 1
    ta "Что ты думаешь о том, что на банчо Пеппи двигает ноты про игрокам?"
    scene black with Dissolve(1)
    if glava == 5:
        scene bg ronpa_gym with Dissolve(1)
        show sprite_t talala:
            zoom .5
            yalign .999
            xalign .5
        with dissolve
    if glava == 6:
        scene bg ronpa_laundry with Dissolve(1)
        show sprite_t talala with dissolve
    if glava == 7:
        scene bg ronpa_izo with Dissolve(1)
        show sprite_t talala with dissolve
    ta "Возможно, в этом даже были замешаны инопланетные Гаши."
    "Я провёл некоторое время с Талалой."
    call talala_gift from _call_talala_gift
    if game_end == False:
        ta "Раз уж мы оказались здесь все вместе, то так захотел Бог - вот как я считаю."
        dg "..."
        ta "А раз Бог захотел этого, то значит это не просто так."
        ta "Мы были все брошены сюда не просто так."
        dg "Тала..."
        ta "Просто шучу! Не кипятись."
        ta "Говоря на чистоту, я уже соскучился по-настоящему миру."
        ta "Ой... Лучше не буду об этом говорить."
        ta "Здесь тоже вполне неплохо!"
        dg "Талала, меня очень волнует один вопрос."
        dg "Почему ты перестал ныть?"
        dg "Что с тобой?"
        ta "А-ха-ха-ха."
        ta "Прости Диггер, но есть вещи, о которых я не могу говорить прямо сейчас."
        ta "Давай лучше поговорим о чём-нибудь другом."
        ta "Помнишь время, когда я фкшнул одну очень сложную карту?"
        ta "Этот мой скор долгое время никто не мог побить."
        "Припоминаю что-то такое. Что же это была за карта?"
        jump t1
    else:
        return
label t1:
    menu:
        "8-bit princess":
            ta "Да, это была именно она!"
        "Cosmic cortex":
            ta "Эм... Нет."
            ta "Ладно, похоже ты не понимаешь о чём я."
            jump t1
        "Blue zenith":
            ta "Я её фкшил, однако никогда не держал на ней первое место."
            ta "Ответ неверный."
            jump t1
    ta "Так вот, я уже очень давно не топ 1 на ней."
    ta "Понимаешь, к чему я?"
    ta "Времена меняются."
    ta "Вместе с этим и люди."
    ta "Неизменными остаются лишь те, кто всем доволен или же просто глупцы."
    "Неожиданно он начал говорить логичные вещи."
    dg "Да уж..."
    ta "Думаю, теперь ты понимаешь."
    ta "Было интересно общаться с тобой."
    $ talalar += 1
    if free_time < ft_max:
        "Мы уже довольно долго общаемся с Талалой, однако прошла только половина дня."
        menu:
            "Продолжить общаться с Талалой.":
                if talalar < 2:
                    dg "Ты уже уходишь?"
                    ta "Да нет. Делать всё равно нечего."
                    ta "Просто, я подумал, что мог достать тебя."
                    dg "Нет, всё нормально. Мне тоже нечем заняться."
                    jump talala2
                else:
                    "Ты уже повысил отношения с Талалой на максимум, найди себе другого собеседника"
                    if glava == 5:
                        scene bg koridor2 with dissolve
                        jump free_time11
                    if glava == 6:
                        scene bg koridor1 with dissolve
                        jump free_time2
                    if glava == 7:
                        scene bg koridor5 with dissolve
                        jump free_time3_2
            "Пойти поговорить с кем-то ещё.":
                if glava == 5:
                    scene bg koridor2 with dissolve
                    jump free_time11
                if glava == 6:
                    scene bg koridor1 with dissolve
                    jump free_time2
                if glava == 7:
                    scene bg koridor5 with dissolve
                    jump free_time3_2
    else:
        dg "Уже достаточно поздно, пожалуй, я пойду. Пока"
        ta "Пока!"
        if glava == 5:
            scene bg koridor2 with dissolve
            jump free_time11
        if glava == 6:
            scene bg koridor1 with dissolve
            jump free_time2
        if glava == 7:
            scene bg koridor5 with dissolve
            jump free_time3_2

label talala2:
    $ free_time += 1
    scene black with Dissolve(1)
    if glava == 5:
        scene bg ronpa_gym with Dissolve(1)
        show sprite_t talala:
            zoom .5
            yalign .999
            xalign .5
        with dissolve
    if glava == 6:
        scene bg ronpa_laundry with Dissolve(1)
        show sprite_t talala with dissolve
    if glava == 7:
        scene bg ronpa_izo with Dissolve(1)
        show sprite_t talala with dissolve
    "Я провёл какое-то время с Талалой."
    ta "Ну а вообще, если забанить всех читеров, то на первом месте будет Сокиец, а на втором я."
    call talala_gift from _call_talala_gift_1
    if game_end == False:
        ta "Раз уж мы с тобой уже так близки, то я хотел бы рассказать тебе историю из моей жизни."
        "Близки?"
        ta "Однажды в детстве, когда я ещё ходил в школу, моему классу задали выучить стихотворение."
        ta "Все выходили по очереди и рассказывали - как это и должно было быть."
        ta "Я очень волновался, так как не выучил стихотворение полностью."
        ta "Передо мной должен был отвечать мой лучший друг, Рак."
        ta "Он хорошо учился, поэтому сомнений в том, что он выучил не было ни у кого."
        ta "И вот настаёт его очередь рассказывать, он выходит и говорит:"
        ta "«Села муха на варенье - вот и всё стихотворенье.»"
        dg "..."
        ta "Весь класс в шоке, не может ничего сказать."
        ta "Из-за этой выходки учителю пришлось приостановить урок, и до меня не дошла очередь."
        ta "Хотя Рак и не хочет говорить мне, но он сделал это нарочно, ради того, чтобы я не получил двойку."
        ta "После этого поступка, мы с Раком стали ещё более хорошими друзьями."
        ta "Так как друзья познаются в беде."
        ta "Поэтому Диггер, если тебе понадобится помощь, то ты всегда можешь попросить меня."
        dg "Спасибо... Наверное..."
        $ talalar += 1
        ob "Вы повысили отношения с Талалой на максимум."
        ob "Поздравляю!"
        if glava == 5:
            scene bg koridor2 with dissolve
            jump free_time11
        if glava == 6:
            scene bg koridor1 with dissolve
            jump free_time2
        if glava == 7:
            scene bg koridor5 with dissolve
            jump free_time3_2
    else:
        return
###BEASTTROLMC
label bmc_gift:
    menu:
        "Подарить ему подарок.":
            if (bmc1 >= 1) and (bmc2 == 0):
                $ bmc1 -= 1
                "Для Бистрола у меня есть только краска для волос."
                dg "Возьми, думаю, это может тебе понравиться."
                bmc "Стой... Неужели это то, что я думаю?!"
                bmc "Спасибо большое! Я давно хотел купить его."
                return
            if (bmc2 >= 1) and (bmc1 == 0):
                $ bmc2 -= 1
                "Для Бистрола у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                bmc "Какая интересная книга."
                bmc "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (bmc1 >= 1) and (bmc2 >= 1):
                menu:
                    "Краска для волос.":
                            $ bmc1 -= 1
                            dg "Возьми, думаю, это может тебе понравиться."
                            bmc "Стой... Неужели это то, что я думаю?!"
                            bmc "Спасибо большое! Я давно хотел купить его."
                            return
                    "Книга.":
                            $ bmc2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            bmc "Какая интересная книга."
                            bmc "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (bmc1 == 0) and (bmc2 == 0):
                "У меня нет подарка для Бистрола."
                dg "Ладно, я пожалуй пойду. Удачи."
                bmc "Пока, Диггер!"
                if glava == 5:
                    scene bg koridor1 with dissolve
                    jump free_time1
                if glava == 6:
                    scene bg koridor2 with dissolve
                    jump free_time2_1
        "Уйти.":
            if glava == 5:
                scene bg koridor1 with dissolve
                jump free_time11
            if glava == 6:
                scene bg koridor2 with dissolve
                jump free_time2

label bmc1:
    $ free_time += 1
    bmc "Знаешь, на самом деле я не толстый, просто у меня кость широкая."
    scene black with Dissolve(1)
    if glava == 5:
        scene bg ronpa_dininghall with Dissolve(1)
    if glava == 6:
        scene bg ronpa_medlab with Dissolve(1)
    show sprite_b bmc with dissolve
    bmc "Ну и я её зафармил."
    dg "Ясно..."
    call bmc_gift from _call_bmc_gift
    if game_end == False:
        bmc "Раньше я не был таким толстым."
        dg "Что же с тобой произошло?"
        bmc "Всё началось с того, что мой аккаунт на твиче и ютубе забанили лишь за то, что я не являлся фанатом ЛГБТ сообщества."
        bmc "После этого я впал в глубокую депрессию и начал очень много есть."
        bmc "Так, даже после разбана я не смог остановиться и пришёл к этому плачевному состоянию."
        dg "Понятно. Значит во всём виновата толерантность."
        bmc "Не подумай, я уважаю человека не за его сексуальную ориентацию."
        bmc "Уважение приходит с поступками."
        bmc "Но то, что творится сейчас, не перестаёт пугать меня."
        bmc "Стримить и снимать видео теперь могут только люди, которые относятся к каким-либо меньшинствам."
        bmc "Это абсурд."
        dg "Согласен с тобой."
        bmc "Куда катится наш мир...."
        $ bmcr += 1
        if free_time < ft_max:
            "Мы уже довольно долго общаемся с Бистролом, однако прошла только половина дня."
            menu:
                "Продолжить общаться с Бистролом.":
                    if bmcr < 2:
                        jump bmc2
                    else:
                        "Ты уже повысил отношения с Бистролом на максимум, найди себе другого собеседника"
                        if glava == 5:
                            scene bg koridor1 with dissolve
                            jump free_time11
                        if glava == 6:
                            scene bg koridor2 with dissolve
                            jump free_time2
                "Пойти поговорить с кем-то ещё.":
                    if glava == 5:
                        scene bg koridor1 with dissolve
                        jump free_time11
                    if glava == 6:
                        scene bg koridor2 with dissolve
                        jump free_time2
        else:
            dg "Уже достаточно поздно, пожалуй я пойду. Пока"
            bmc "Пока!"
            if glava == 5:
                scene bg koridor1 with dissolve
                jump free_time11
            if glava == 6:
                scene bg koridor2 with dissolve
                jump free_time2
    else:
        return
label bmc2:
    $ free_time += 1
    scene black with Dissolve(1)
    if glava == 5:
        scene bg ronpa_dininghall with Dissolve(1)
    if glava == 6:
        scene bg ronpa_medlab with Dissolve(1)
    show sprite_b bmc with dissolve
    bmc "Если честно, то я тоже пытался отсосать самому себе."
    call bmc_gift from _call_bmc_gift_1
    if game_end == False:
        bmc "Почему-то я вспомнил момент из прошлого, когда я ещё хорошо играл в осу."
        bmc "Тогда я зафармил 875пп."
        bmc "У меня ещё сердце чуть из груди не выпрыгнуло."
        bmc "Я даже пальцы контролировать не мог."
        bmc "Что же это была за карта."
        jump b1
    else:
        return
label b1:
    menu:
        "GYZE - HONESTY.":
            bmc "Нет же! Другая."
            jump b1
        "BABYMETAL - Road of Resistance.":
            bmc "Точно не она."
            jump b1
        "GALNERYUS - RAISE MY SWORD":
            bmc "Точно, она!"
    bmc "Так вот, если бы сейчас я так её сыграл, то меня бы точно в больницу увезли."
    bmc "На самом деле у меня уже было несколько сердечных приступов."
    bmc "Вот тебе и побочный эффект осу."
    bmc "Трясёт от любой ерунды."
    bmc "Однако даже осознавая это, ты не можешь прекратить играть."
    bmc "Часто у осеров нет ничего в жизни, кроме игры."
    bmc "И даже если они захотят, то не смогут бросить."
    bmc "Как наркотик прям. Ха-ха."
    dg "Сильный человек сможет!"
    bmc "Без сомнений."
    bmc "Однако много ли сильных людей ты знаешь?"
    bmc "Я - нет."
    bmc "Поэтому, когда мы выберемся отсюда, я сделаю так, чтобы как можно меньше людей начинало играть в осу."
    dg "Думаю, за такие поступки тебя больше любить никто не станет."
    bmc "Ну и пусть. Если я смогу спасти хотя бы одного человека - это будет не просто так."
    dg "В любом случае, удачи."
    bmc "Спасибо Диггер."
    $bmcr += 1
    "Вы повысили отношения с Бистролом на максимум."
    "Поздравляю!"
    if glava == 5:
        scene bg koridor1 with dissolve
        jump free_time11
    if glava == 6:
        scene bg koridor2 with dissolve
        jump free_time2

### ALUMETRI
label al_gift:
    menu:
        "Подарить ему подарок.":
            if (alumetri1 >= 1) and (alumetri2 == 0):
                $ alumetri1 -= 1
                "Для Алюметри у меня есть только хайповый шмот."
                dg "Возьми, думаю, это может тебе понравиться."
                al "Стой... Неужели это то, что я думаю?!"
                al "Спасибо большое! Я давно хотел купить это."
                return
            if (alumetri2 >= 1) and (alumetri1 == 0):
                $ alumetri2 -= 1
                "Для Алюметри у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                al "Какая интересная книга."
                al "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (alumetri1 >= 1) and (alumetri2 >= 1):
                menu:
                    "Хайповый Шмот.":
                        $ alumetri1 -= 1
                        dg "Возьми, думаю, это может тебе понравиться."
                        al "Стой... Неужели это то, что я думаю?!"
                        al "Спасибо большое! Я давно хотел купить это."
                        return
                    "Книга.":
                            $ alumetri2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            al "Какая интересная книга."
                            al "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (alumetri1 == 0) and (alumetri2 == 0):
                "У меня нет подарка для Алюметри."
                dg "Ладно, я пожалуй пойду. Удачи."
                al "Пока, Диггер!"
                scene bg koridor1 with dissolve
                jump free_time1
        "Уйти.":
            scene bg koridor1 with dissolve
            jump free_time1


label alumetri1:
    $ free_time += 1
    al "Пошлая Молли - это мировая классика."
    scene black with Dissolve(1)
    scene bg ronpa_aroom with Dissolve(1)
    show sprite_a alumetri with dissolve
    al "А вообще, дабстеп тоже бывает хорошим."
    "Я провёл время с Алюметри."
    call al_gift from _call_al_gift
    if game_end == False:
        al "Знаешь, Диггер, я считаю, что лучшего момента почувствовать себя счастливыми не существует."
        al "Если не сейчас, то когда?"
        al "Кажется, жизнь вот-вот начнется, настоящая жизнь!"
        al "Но всегда на пути существует одна проблема, одно незаконченное дело, один непогашенный долг, которые нуждаются в первостепенном решении."
        al "И вот после этого жизнь начнется."
        al "И если мы присмотримся, то увидим, что эти проблемы бесконечны. "
        al "Из них, собственно, и состоит жизнь."
        al "Это помогает нам увидеть, что пути к счастью нет, счастье – это и есть путь."
        al "Мы должны ценить каждый момент, особенно, когда делим его с кем-то дорогим, и помнить, что время не ждет никого."
        al "Счастье – это путь, а не судьба."
        al "Понимаешь что я имею в виду?"
        dg "Наверное."
        al "Я не собираюсь впадать в отчаянье только потому, что какой-то сумасшедший запер нас всех здесь."
        al "Всё это - часть моего пути."
        al "И как бы сложно не было, сколько бы проблем не встретилось на моём пути, я не дамся отчаянью так просто."
        al "Всё, что я ощущаю сейчас - это кураж."
        al "Кураж от того, что будет дальше."
        al "Я поставил себе цель - вывести всех из этой чёртовой игры."
        al "И свою цель я постараюсь выполнить."
        al "Я, как все вы, воин надежды."
        "Он говорит так уверено, что становится немного не по себе."
        "Мне понятны его слова, но одно можно сказать точно: он отличается от всех остальных здесь."
        "Он замотивирован так, как не замотивирован никто."
        "Это поможет ему выбраться отсюда, несомненно."
        "Однако я до сих пор не верю в то, что его план не потерпит крах."
        $ alumetrir += 1
        if free_time < ft_max:
            "Мы уже довольно долго общаемся с Алюметри, однако прошла только половина дня."
            menu:
                "Продолжить общаться с Алюметри.":
                    if alumetrir < 2:
                        jump alumetri2
                    else:
                        "Ты уже повысил отношения с Алюметри на максимум, найди себе другого собеседника"
                        scene bg koridor1 with dissolve
                        jump free_time1
                "Пойти поговорить с кем-то ещё.":
                    scene bg koridor1 with dissolve
                    jump free_time1
        else:
            dg "Уже достаточно поздно, пожалуй я пойду. Пока"
            al "Пока!"
            scene bg koridor1 with dissolve
            jump free_time1
    else:
        return

label alumetri2:
    $ free_time += 1
    al "Свобода - это вещь относительная."
    scene black with Dissolve(1)
    scene bg ronpa_aroom with Dissolve(1)
    show sprite_a alumetri with dissolve
    al "Комнатные политики частенько душат, правда?"
    dg "Да..."
    call al_gift from _call_al_gift_1
    if game_end == False:
        al "Знаешь Диггер, жизнь может быть тяжелой время от времени."
        al "В один момент, эмоции могут затмить разум."
        al "Бывает даже привести к мысли о самоубийстве."
        al "Может показаться, что выхода нет."
        al "Однако очень важно помнить: эти чувства пройдут..."
        al "Как бы плохо всё не было в твоей жизни, не нужно отчаиваться."
        al "Какой бы заезженной не была эта фраза - выход есть всегда."
        al "Почему-то не все об этом помнят."
        al "Как люди вообще могут совершать суицид?"
        al "Жизнь - это величайшее счастье."
        al "Ох, мне кажется я заговорился, извини."
        dg "Всё нормально..."
        "Кажется, ему нужно обратиться к психиатру."
        al "Расскажи лучше ты что-нибудь Диггер."
        dg "Нет чего-то, что я мог бы рассказать тебе."
        dg "Всё либо уже есть в сети, либо я не считаю нужным подвергать это огласке."
        al "Как скучно!"
        dg "Уж прости..."
        $alumetrir += 1
        "Вы повысили отношения с Алюметри на максимум."
        "Поздравляю!"
        scene bg koridor1 with dissolve
        jump free_time1
    else:
        return

### SOTARKS
label so_gift:
    menu:
        "Подарить ему подарок.":
            if (sotarks1 >= 1) and (sotarks2 == 0):
                $ sotarks1 -= 1
                "Для Сотаркса у меня есть только ром."
                dg "Возьми, думаю, это может тебе понравиться."
                st "Стой... Неужели это мой любимый ром?"
                st "Спасибо большое! Сегодня же его испробую!"
                return
            if (sotarks2 >= 1) and (sotarks1 == 0):
                $ sotarks2 -= 1
                "Для Сотаркса у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                st "Какая интересная книга."
                st "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (sotarks1 >= 1) and (sotarks2 >= 1):
                menu:
                    "Ром.":
                        $ sotarks1 -= 1
                        dg "Возьми, думаю, это может тебе понравиться."
                        st "Стой... Неужели это мой любимый ром?"
                        st "Спасибо большое! Сегодня же его испробую!"
                        return
                    "Книга.":
                            $ sotarks2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            st "Какая интересная книга."
                            st "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (sotarks1 == 0) and (sotarks2 == 0):
                "У меня нет подарка для Сотаркса."
                dg "Ладно, я пожалуй пойду. Удачи."
                st "Пока, Диггер!"
                scene bg koridor1 with dissolve
                jump free_time1
        "Уйти.":
            scene bg koridor1 with dissolve
            jump free_time1

label sotarks1:
    $ free_time += 1
    st "1-2 джампы лучшие."
    scene black with Dissolve(1)
    scene bg ronpa_sroom with Dissolve(1)
    show sprite_s sotarks with dissolve
    st "Ну и я рыгнул ему прямо в лицо."
    "Я провёл время с Сотарксом."
    call so_gift from _call_so_gift
    if game_end == False:
        st "Знаешь, очень долго я вёл разгульный образ жизни."
        st "Очень часто выпивал, бездельничал."
        st "В итоге это не привело ни к чему хорошему."
        st "Хотя, наверное единственное, что интересовало меня в жизни - это осу."
        st "Эта игра вдохнула в меня жизнь."
        st "В тот момент, когда я начал играть в осу, до меня дошло, что творить для людей - это моё призвание."
        st "Сначала у меня не получалось хорошо."
        st "Но я не сдался и достиг своей цели."
        st "Сейчас все в осу знают обо мне."
        st "Я признаю, что в какой-то момент делал конвейерные карты."
        st "Однако я не вижу в этом ничего плохого."
        st "Я лишь удовлетворял потребности ненасытных пп фармеров."
        st "Конечно, я мог выбрать путь техник маппинга."
        st "Но честно говоря - это не по мне."
        st "Кто бы что не говорил, я горжусь своей карьерой осера!"
        "Почему он говорит об этом?"
        st "И... Если мы все здесь погибнем, то получается, что я делал все карты зря?"
        st "Если я не смогу больше мапать, то..."
        st "Не важно."
        st "Я лишь хотел сказать, что мы все должны выбраться отсюда целыми и невредимыми."
        dg "Ты прав."
        "Хотя я и не верю в это."
        $ sotarksr += 1
        if free_time < ft_max:
            "Мы уже довольно долго общаемся с Сотарксом, однако прошла только половина дня."
            menu:
                "Продолжить общаться с Сотарксом.":
                    if sotarksr < 2:
                        jump sotarks2
                    else:
                        "Ты уже повысил отношения с Сотарксом    на максимум, найди себе другого собеседника"
                        scene bg koridor1 with dissolve
                        jump free_time1
                "Пойти поговорить с кем-то ещё.":
                    scene bg koridor1 with dissolve
                    jump free_time1
        else:
            dg "Уже достаточно поздно, пожалуй я пойду. Пока"
            st "Пока!"
            scene bg koridor1 with dissolve
            jump free_time1
    else:
        return

label sotarks2:
    $ free_time += 1
    st "думаю лучшим твоих карт, Диггер..."
    scene black with Dissolve(1)
    scene bg ronpa_sroom with Dissolve(1)
    show sprite_s sotarks with dissolve
    st "Ладно, ты прав, твои карты не такие уж и плохие..."
    "Я провёл время с Сотарксом."
    call so_gift from _call_so_gift_1
    if game_end == False:
        st "Знаешь, мне кажется, что было бы круто затусить всем вместе, когда мы выберемся отсюда."
        st "Думаю, мы могли бы здорово провести время."
        st "Мы все из одного комьюнити, нам будет о чём поговорить."
        dg "Но когда мы выберемся отсюда, то будем говорить на разных языках."
        st "Ох, не думаю, что это огромная проблема."
        st "Все здесь знают английский."
        st "Мне кажется, что мы сможем понимать друг друга."
        st "Помню, когда-то давно, на сходке осеров, даже Сокиец был."
        st "Мы хорошо проводили время."
        st "Однако сейчас он ни с кем не разговаривает."
        st "Грустно даже как-то."
        st "Надо бы узнать, что с ним случилось."
        dg "Да, ты прав. Я тоже немного беспокоюсь за него."
        st "Ну вот и договорились!"
        st "Когда мы выберемся, то соберёмся все вместе в каком-нибудь клёвом местечке."
        st "Закатим тусовку века. Если что, кое-кто нам в этом поможет."
        dg "Точно, среди нас же есть кое-кто, кто разбирается в тусовках."
        jump s1
    else:
        return

label s1:
    menu:
        "Рафис.":
            st "Нет, не он."
            dg "Точно, Рафис же {color=0a6600}Лучшая в мире модель{/color}."
            jump s1
        "Алюметри.":
            st "Точно, именно он!"
            dg "Как никак он {color=0a6600}Лучший в мире тусовщик{/color}."
        "Сокиец.":
            st "Не правильно."
            dg "Да, он же {color=0a6600}Лучший в мире Ассасин{/color}."
            jump s1
    dg "Хорошо, ты уговорил меня."
    st "Ура!"
    st "Осталось всего ничего: выбраться из этой дыры."
    $sotarksr += 1
    "Вы повысили отношения с Сотарксом на максимум."
    "Поздравляю!"
    scene bg koridor1 with dissolve
    jump free_time1

### RAFIS
label ra_gift:
    menu:
        "Подарить ему подарок.":
            if (rafis1 >= 1) and (rafis2 == 0):
                $ rafis1 -= 1
                "Для Рафиса у меня есть только Балаклава."
                dg "Возьми, думаю, это может тебе понравиться."
                ra "Стой... Неужели это балаклава?"
                ra "Спасибо большое! Сегодня же опробую!"
                return
            if (rafis2 >= 1) and (rafis1 == 0):
                $ rafis2 -= 1
                "Для Рафиса у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                ra "Какая интересная книга."
                ra "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (rafis1 >= 1) and (rafis2 >= 1):
                menu:
                    "Балаклава.":
                        $ rafis1 -= 1
                        dg "Возьми, думаю, это может тебе понравиться."
                        ra "Стой... Неужели это балаклава?"
                        ra "Спасибо большое! Сегодня же опробую!"
                        return
                    "Книга.":
                        $ rafis2 -= 1
                        dg "Держи. Мне кажется, ты заценишь данный подгон."
                        ra "Какая интересная книга."
                        ra "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                        return
            if (rafis1 == 0) and (rafis2 == 0):
                "У меня нет подарка для Рафиса."
                dg "Ладно, я пожалуй пойду. Удачи."
                ra "Пqока, Диггер!"
                if glava == 5:
                    scene bg koridor2 with dissolve
                    jump free_time1
                if glava == 6:
                    scene bg koridor4 with dissolve
                    jump free_time2_2
        "Уйти.":
            if glava == 5:
                scene bg koridor2 with dissolve
                jump free_time1
            if glava == 6:
                scene bg koridor4 with dissolve
                jump free_time2_2

label rafis1:
    $ free_time += 1
    ra "Однажды я так сильно напился..."
    scene black with Dissolve(1)
    if glava == 5:
        scene bg ronpa_entrance with Dissolve(1)
    if glava == 6:
        scene bg ronpa_prepool with Dissolve(1)
    show sprite_r rafis with dissolve
    ra "Ну а в конце я ему рожу разбил."
    dg "Ясно..."
    "Я провёл время в Рафисом."
    call ra_gift from _call_ra_gift
    if game_end == False:
        ra "Помнишь тот год, когда мы выиграли OWC ?"
        "Точно, Польша же давно побеждала OWC."
        "В каком же году это было?"
        jump r1
    else:
        return
label r1:
    menu:
        "2016":
            ra "Нет же!"
            ra "В 2016 году победила US."
            dg "Точно."
            dg "Тогда..."
            jump r1
        "2017":
            ra "Точно! Ты прав."
            dg "И что?"
        "2018":
            ra "Нет же!"
            ra "В 2016 году победила US."
            dg "Точно."
            dg "Тогда..."
            jump r1
    ra "В тот год, мы были сильны как никогда."
    ra "Однако, как ты помнишь, эта победа не далась нам легко."
    ra "В финале нам пришлось неплохо так попотеть."
    ra "Но как бы то ни было, надежда в моём сердце никогда не угасала."
    ra "Я до последнего момента верил в то, что мы победим."
    ra "Так оно и случилось."
    ra "Я просто хочу сказать, что мы должны верить в то, что можем выбраться из этой игры."
    ra "И тогда у нас точно всё получится!"
    "Каждый из них думает так, однако шанс на успех очень мал."
    "Думаю, в глубине души, они понимают это."
    "Я бы и сам не прочь поверить в то, что мы сможем выбраться все вместе."
    "Но моё сознание не даст мне обмануть самого себя."
    ra "Я догадываюсь, что ты не веришь во всё это."
    ra "Ты не такой человек, который поверит в настолько хороший исход."
    ra "И я не осуждаю тебя. Люди бывают разные."
    ra "Я просто хотел сказать, что если встанешь на пути к хорошему концу, то тобой займусь я."
    dg "..."
    ra "Ха-ха."
    ra "Просто шучу."
    "Я бы не сказал, что люди шутят с такой серьёзной интонацией."
    $ rafisr += 1
    if free_time < ft_max:
        "Мы уже довольно долго общаемся с Рафисом, однако прошла только половина дня."
        menu:
            "Продолжить общаться с Рафисом.":
                if rafisr < 2:
                    jump rafis2
                else:
                    "Ты уже повысил отношения с Рафисом на максимум, найди себе другого собеседника"
                    if glava == 5:
                        scene bg koridor1 with dissolve
                        jump free_time1
                    if glava == 6:
                        scene bg koridor4 with dissolve
                        jump free_time2_2
            "Пойти поговорить с кем-то ещё.":
                if glava == 5:
                    scene bg koridor1 with dissolve
                    jump free_time1
                if glava == 6:
                    scene bg koridor4 with dissolve
                    jump free_time2_2
    else:
        dg "Уже достаточно поздно, пожалуй я пойду. Пока"
        ra "Пока!"
        if glava == 5:
            scene bg koridor1 with dissolve
            jump free_time1
        if glava == 6:
            scene bg koridor4 with dissolve
            jump free_time2_2

label rafis2:
    $ free_time += 1
    ra "После того, как я обогнал Рохалка на балаклаве..."
    scene black with Dissolve(1)
    if glava == 5:
        scene bg ronpa_entrance with Dissolve(1)
    if glava == 6:
        scene bg ronpa_prepool with Dissolve(1)
    show sprite_r rafis with dissolve
    ra "Да, той ночью мне снился его член."
    dg "..."
    call ra_gift from _call_ra_gift_1
    if game_end == False:
        ra "Когда-то я даже был топ 1 в осу."
        ra "Мало кто помнит об этом."
        ra "Но времена меняются."
        ra "Новички заменяют старожилов."
        ra "Это неизбежно."
        ra "От этого даже грустно немного."
        ra "Не получится всю жизнь быть хорошим в чём-то."
        ra "Потому что всегда найдётся кто-то, кто будет лучше тебя."
        ra "Хотя, наверное, это подходит только к спорту."
        ra "Если бы мы говорили, например, о книгах, то сложно сказать кто лучше, а кто хуже."
        ra "У людей разные вкусы."
        ra "Думаю, если переводить на осу, то можно сравнить это с маппингом."
        ra "Кому-то нравится Сотаркс, а кто-то фанатеет от Фанжена."
        ra "Нельзя сказать кто лучше, однако можно сказать кто делал карту дольше, понимаешь?"
        "Не особо если честно..."
        ra "Я просто хотел сказать, что жизнь не заканчивается одним увлечением."
        ra "Почти всегда можно перестроиться или даже начать жизнь с чистого листа."
        ra "Однако мало людей способны пойти на это."
        ra "Их можно понять."
        ra "Что-то новое всегда пугает, и это нормально."
        ra "В общем, что-то я заговорился."
        ra "Я хочу сказать, что пробовать что-то новое - это поступок храброго человека."
        ra "Не стоит бояться последствий."
        "А вот с этим я уже совсем не согласен..."
        $rafisr += 1
        "Вы повысили отношения с Рафисом на максимум."
        "Поздравляю!"
        if glava == 5:
            scene bg koridor1 with dissolve
            jump free_time1
        if glava == 6:
            scene bg koridor4 with dissolve
            jump free_time2_2
    else:
        return

#### ФРИТАЙМ 6 ГЛАВА
label free_time2:
    if free_time < ft_max:
        call screen imagemap2
        $ result = _return
        if result == "dRoom":
            "В моей комнате вряд ли будет кто-то."
            jump free_time2
        if result == "dizRoom":
            scene bg ronpa_dizroom with dissolve
            "Я постучал в дверь."
            show sprite_d dizick with dissolve
            dz "Привет, Диггер, чем могу помочь?"
            menu:
                "Провести время с Дизиком.":
                    if dizickr == 0:
                        jump dizick1
                    if dizickr == 1:
                        jump dizick2
                    if dizickr > 1:
                        ob "Вы уже прокачали отношения с Дизиком на максимум, найдите себе другого собеседника."
                        scene bg koridor1 with dissolve
                        jump free_time2
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor1 with dissolve
                    jump free_time2
        if (result == "rRoom") or (result == "bRoom") or (result == "cRoom") or (result == "tRoom"):
            "Я постучал в дверь."
            "..."
            "Похоже в комнате никого нет."
            jump free_time2
        if (result == "trash") or (result == "storage") or (result == "bath"):
            "Вряд ли там кто-то будет."
            jump free_time2
        if result == "dinning":
            scene bg ronpa_dininghall with dissolve
            "Довольно странно, но в столовой никого не было."
            "Пойду поищу в другом месте."
            scene bg koridor1 with dissolve
            jump free_time2
        if result == "laundry":
            scene bg ronpa_laundry with dissolve
            show sprite_t talala with dissolve
            ta "О, Диггер, привет!"
            menu:
                "Провести время с Талалой.":
                    if talalar == 0:
                        jump talala1
                    if talalar == 1:
                        jump talala2
                    if talalar > 1:
                        ob "Вы уже прокачали отношения с Талалой на максимум, найдите себе другого собеседника."
                        scene bg koridor1 with dissolve
                        jump free_time2
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor1 with dissolve
                    jump free_time2
        if result == "school":
            scene bg koridor2 with dissolve
            jump free_time2_1
    else:
        if ft_number == 4:
            jump murder2
        else:
            jump banya
label free_time2_1:
    if free_time < ft_max:
        call screen imagemap1
        $ result = _return
        if (result == "classA") or (result == "classB"):
            "Как и всегда, класс закрыт."
            jump free_time2_1
        if (result == "gym") or (result == "cinema") or (result == "lobby"):
            "Вряд ли там кто-то есть."
            jump free_time2_1
        if result == "shop":
            scene bg ronpa_shop with dissolve
            call osu_shop from _call_osu_shop_2
            scene bg koridor2 with dissolve
            jump free_time2_1
        if result == "MedLab":
            scene bg ronpa_medlab with dissolve
            show sprite_b bmc with dissolve
            bmc "Привет, Диггер."
            menu:
                "Провести время с Бистролом.":
                    if bmcr == 0:
                        jump bmc1
                    if bmcr == 1:
                        jump bmc2
                    if bmcr > 1:
                        ob "Вы уже прокачали отношения с Бистролом на максимум, найдите себе другого собеседника."
                        scene bg koridor2 with dissolve
                        jump free_time2_1
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor2 with dissolve
                    jump free_time2_1
        if result == "dormitory":
            scene bg koridor1 with dissolve
            jump free_time2
        if result == "2F":
            scene bg koridor4 with dissolve
            jump free_time2_2
    else:
        if ft_number == 4:
            jump murder2
        else:
            jump banya
label free_time2_2:
    if free_time < ft_max:
        call screen imagemap3
        $ result = _return
        if (result == "ClassC") or (result == "ClassD"):
            "Мне нечего там делать."
            jump free_time2_2
        if result == "3F":
            "Проход на третий этаж перекрыт железными прутьями."
            jump free_time2_2
        if result == "Library":
            scene bg ronpa_library with dissolve
            show sprite_c cookiezi with dissolve
            co "Диггер, здравствуй."
            menu:
                "Провести время с Сокийцем.":
                    if cor == 0:
                        jump cookiezi1
                    if cor == 1:
                        jump cookiezi2
                    if cor > 1:
                        ob "Вы уже прокачали отношения с Сокийцем на максимум, найдите себе другого собеседника."
                        scene bg koridor4 with dissolve
                        jump free_time2_2
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor4 with dissolve
                    jump free_time2_2
        if result == "Pool":
            scene bg ronpa_prepool with dissolve
            show sprite_r rafis with dissolve
            ra "..."
            menu:
                "Провести время с Рафисом.":
                    if rafisr == 0:
                        jump rafis1
                    if rafisr == 1:
                        jump rafis2
                    if rafisr > 1:
                        ob "Вы уже прокачали отношения с Рафисом на максимум, найдите себе другого собеседника."
                        scene bg koridor4 with dissolve
                        jump free_time2_2
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor4 with dissolve
                    jump free_time2_2
        if result == "1F":
            scene bg koridor2 with dissolve
            jump free_time2_1
    else:
        if ft_number == 4:
            jump murder2
        else:
            jump banya


###ДИЗИК
label dz_gift:
    menu:
        "Подарить ему подарок.":
            if (dizick1 >= 1) and (dizick2 == 0):
                $ dizick1 -= 1
                "Для Дизика у меня есть только Ducky Shine 6."
                dg "Возьми, думаю, это может тебе понравиться."
                dz "Стой... Неужели это то, что я думаю?!"
                dz "Спасибо большое! Я давно хотел купить это."
                return
            if (dizick2 >= 1) and (dizick1 == 0):
                $ dizick2 -= 1
                "Для Дизика у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                dz "Какая интересная книга."
                dz "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (dizick1 >= 1) and (dizick2 >= 1):
                menu:
                    "Ducky Shine 6.":
                        $ dizick1 -= 1
                        dg "Возьми, думаю, это может тебе понравиться."
                        dz "Стой... Неужели это то, что я думаю?!"
                        dz "Спасибо большое! Я давно хотел купить это."
                        return
                    "Книга.":
                            $ dizick2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            dz "Какая интересная книга."
                            dz "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (dizick1 == 0) and (dizick2 == 0):
                "У меня нет подарка для Дизика."
                dg "Ладно, я пожалуй пойду. Удачи."
                dz "Пока, Диггер!"
                if glava == 6:
                    scene bg koridor1 with dissolve
                    jump free_time2
                if glava == 7:
                    scene bg koridor5 with dissolve
                    jump free_time3_2
        "Уйти.":
            if glava == 6:
                scene bg koridor1 with dissolve
                jump free_time2
            if glava == 7:
                scene bg koridor5 with dissolve
                jump free_time3_2
label dizick1:
    $ free_time += 1
    dz "Диггер, давай ты купишь мне квартиру, а я зафармлю 150к пп на гатари."
    scene black with Dissolve(1)
    if glava == 6:
        scene bg ronpa_dizroom with Dissolve(1)
    else:
        scene bg ronpa_gameroom with Dissolve(1)
    show sprite_d dizick with dissolve
    dz "Хорошо, я - бездарное чудище."
    call dz_gift from _call_dz_gift
    if game_end == False:
        dz "Знаешь Диггер, после того, как вы увидели отрывок моей жизни, то на меня нахлынула волна ностальгии по тем временам."
        dz "Хоть в тот день я и испытал великое отчаянье в моей жизни, это ещё ничего не значит."
        dz "Только потом я осознал, что это были лучшие дни в моей жизни."
        dz "Многие люди считают, что детство - это лучшее время."
        dz "Наверное, так и есть."
        "Уж не знаю."
        dz "Однако мы осознаём это слишком поздно."
        dz "Когда здоровье уже не то, мы вспоминаем какое оно было в годы молодости."
        dz "Однако мы сами виноваты в том, что не следили за ним тогда."
        dz "Поэтому говорить, что раньше было лучше - не самая здравая идея."
        dz "В таком случае, можно сказать, что годы, когда мы губили наше здоровье - лучшие."
        dz "Но ведь это не так."
        dz "Скорее нужно жалеть, что мы потратили эти золотые годы на всякую ерунду."
        dz "Хотя есть и такие, кто не терял время зря."
        dz "Они упорно учились и занимались собой на протяжении всей молодости."
        dz "Можно ли назвать их счастливыми?"
        dz "Наверное в перспективе можно, однако..."
        dz "В годы молодости они трудились до посинения, почти не отдыхая."
        dz "Разве это счастье?"
        dz "Думаю, у разных людей будут разные ответы на этот вопрос."
        dz "Кто-то считает, что нужно всю жизнь трудиться, и в какой-то момент это становится для него счастьем."
        dz "Другие же люди считают, что нужно жить себе в удовольствие."
        dz "Первые не могут найти общий язык со вторыми: оно и понятно."
        dz "Для человека, который живёт ради себя будет непонятно зачем так много работать."
        dz "Я вот не могу отнести себя ни к первым, ни ко вторым."
        dz "Это странно?"
        dz "Просто... Когда думаю, что всю жизнь буду отдыхать, то что-то не даёт мне покоя."
        dz "С другой стороны я согласен, что работать всю жизнь - это глупо."
        dz "Поэтому можно сказать, что я нахожусь где-то посередине этих точек зрений."
        dz "А к кому себя относишь ты, Диггер?"
        dg "Не знаю... Мне сложно так быстро ответить..."
        "Я никогда не задумывался над этим."
        dz "Это нормально."
        dz "Спасибо, что выслушал меня."
        $dizickr += 1
        if free_time < ft_max:
            "Мы уже довольно долго общаемся с Дизиком, однако прошла только половина дня."
            menu:
                "Продолжить общаться с Дизиком.":
                    if dizickr < 2:
                        jump dizick2
                    else:
                        "Ты уже повысил отношения с Дизиком на максимум, найди себе другого собеседника"
                        if glava == 6:
                            scene bg koridor1 with dissolve
                            jump free_time2
                        if glava == 7:
                            scene bg koridor5 with dissolve
                            jump free_time3_2
                "Пойти поговорить с кем-то ещё.":
                    if glava == 6:
                        scene bg koridor1 with dissolve
                        jump free_time2
                    if glava == 7:
                        scene bg koridor5 with dissolve
                        jump free_time3_2
        else:
            dg "Уже достаточно поздно, пожалуй я пойду. Пока"
            dz "Пока!"
            if glava == 6:
                scene bg koridor1 with dissolve
                jump free_time2
            if glava == 7:
                scene bg koridor5 with dissolve
                jump free_time3_2
    else:
        return

label dizick2:
    $ free_time += 1
    dz "Ты не против, если я буду звать тебя Саня?"
    scene black with Dissolve(1)
    if glava == 6:
        scene bg ronpa_dizroom with Dissolve(1)
    else:
        scene bg ronpa_gameroom with Dissolve(1)
    show sprite_d dizick with dissolve
    dz "Я понял. Мне не хватает уважения к старшим."
    call dz_gift from _call_dz_gift_1
    if game_end == False:
        dz "Диггер, не считаешь ли ты странным, что человек начинает интересоваться противоположным полом в свой самый продуктивный возраст?"
        dz "Как правило после 16 лет."
        dz "А ведь именно в этом возрасте стоило бы учиться, работать над собой."
        dz "Лично меня это всегда бесило."
        dg "Что тебе мешает совмещать девушку с учёбой?"
        dz "Это не так уж просто, знаешь ли."
        dz "Скорее, для меня это невозможно."
        dz "Я могу сфокусироваться только на одном деле."
        dz "И пока я не доведу его до конца, то вряд ли успокоюсь."
        dz "Возможно, я могу забросить что-то, но не бросить."
        dz "Не зря ведь я стал писателем."
        dz "Первую свою новеллу я писал практически 2 года, хотя она и состояла из 3 часов геймплея."
        dz "И вообще, первый раз я бросил играть в осу именно из-за девки."
        dz "Наверное, это странно."
        dz "Я давно уже запутался в том, странный я или нет."
        dz "Хотя, в детстве я всегда думал, что могу идеально оценивать свои навыки."
        dz "Конечно, это было не так. Можно сказать, что это стало причиной краха в некоторых вещах."
        dz "Как бы то ни было, каждый день я стараюсь расти и развиваться."
        dz "Возможно когда-нибудь я приду к своему идеалу."
        "Интересно, что это за идеал."
        dg "Знаешь Дизик, ты вёл себя очень странно на протяжении всего нашего общения в интернете."
        dg "Сейчас ты абсолютно другой."
        dz "Я просто боялся показаться не таким, понимаешь?"
        dz "Хотел, чтобы все думали обо мне хорошо."
        dz "Со временем понял, что это было глупо."
        dg "Ясно..."
        dg "В любом случае, я хочу чтобы ты знал: мы все выберемся отсюда живыми."
        dg "Я подозреваю, что ты замышляешь что-то."
        dg "Знай, что просто так ты не помешаешь моим планам."
        dz "Конечно, ты же Диггер."
        dz "Никому из находящихся в этой школе не сравнится с тобой."
        $dizickr += 1
        "Вы повысили отношения с Дизиком на максимум."
        "Поздравляю!"
        if glava == 6:
            scene bg koridor1 with dissolve
            jump free_time2
        if glava == 7:
            scene bg koridor5 with dissolve
            jump free_time3_2
    else:
        return

### COOKIEZI

label co_gift:
    menu:
        "Подарить ему подарок.":
            if (cookiezi1 >= 1) and (cookiezi2 == 0):
                $ cookiezi1 -= 1
                "Для Сокийца у меня есть только печенька."
                dg "Возьми, думаю, это может тебе понравиться."
                co "Стой... Неужели это то, что я думаю?!"
                co "Спасибо большое! Я давно хотел купить это."
                return
            if (cookiezi2 >= 1) and (cookiezi1 == 0):
                $ cookiezi2 -= 1
                "Для Сокийца у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                co "Какая интересная книга."
                co "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (cookiezi1 >= 1) and (cookiezi2 >= 1):
                menu:
                    "Печенька.":
                        $ cookiezi1 -= 1
                        dg "Возьми, думаю, это может тебе понравиться."
                        co "Стой... Неужели это то, что я думаю?!"
                        co "Спасибо большое! Я давно хотел купить это."
                        return
                    "Книга.":
                            $ cookiezi2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            co "Какая интересная книга."
                            co "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (cookiezi1 == 0) and (cookiezi2 == 0):
                "У меня нет подарка для Сокийца."
                dg "Ладно, я пожалуй пойду. Удачи."
                co "Пока, Диггер!"
                if glava == 6:
                    scene bg koridor4 with dissolve
                    jump free_time2_2
                if glava == 7:
                    scene bg koridor5 with dissolve
                    jump free_time3_2
        "Уйти.":
            if glava == 6:
                scene bg koridor4 with dissolve
                jump free_time2_2
            if glava == 7:
                scene bg koridor5 with dissolve
                jump free_time3_2
label cookiezi1:
    $free_time += 1
    co "..."
    scene black with Dissolve(1)
    if glava == 6:
        scene bg ronpa_library with Dissolve(1)
    else:
        scene bg ronpa_computer with Dissolve(1)
    show sprite_c cookiezi with dissolve
    dg "А ты молчаливый..."
    call co_gift from _call_co_gift
    if game_end == False:
        dg "Знаешь, меня волнует одна вещь."
        dg "Во время суда, Иксдем сказал, что Алюметри знал причину твоего молчания."
        dg "Почему же он не рассказал её нам?"
        co "Это хороший вопрос."
        co "Я не могу сказать точно, так как не понимал вас всё это время."
        co "Но по вашим рассказам, Алюметри был помешан на том, чтобы объединить всех и выбраться вместе."
        dg "Всё верно, он вечно твердил про то, что мы войны надежды."
        co "Раз так, то у меня есть одна версия."
        co "Что, если он хотел заставить вас самих подумать?"
        co "На самом деле в этом не было ничего сложного."
        co "Возможно он считал, что если вы не сможете догадаться до такого простого факта, то не заслуживаете называться воинами надежды."
        dg "Звучит леггитно."
        dg "Раз так, то я оправдал его ожидания."
        co "Хах, наверное так оно и есть."
        co "Однако, жаль что его сейчас нет с нами."
        dg "Да... Ты прав."
        co "Думаю, он наблюдает за нами в спектатор моде."
        dg "Хорошие осеры после смерти попадают на гатари..."
        co "А плохие?"
        dg "На акатсуки."
        co "Ужас."
        $cor += 1
        if free_time < ft_max:
            "Мы уже довольно долго общаемся с Сокийцем, однако прошла только половина дня."
            menu:
                "Продолжить общаться с Сокийцем.":
                    if cookiezir < 2:
                        jump cookiezi2
                    else:
                        "Ты уже повысил отношения с Сокийцем на максимум, найди себе другого собеседника"
                        if glava == 6:
                            scene bg koridor4 with dissolve
                            jump free_time2_2
                        if glava == 7:
                            scene bg koridor5 with dissolve
                            jump free_time3_2
                "Пойти поговорить с кем-то ещё.":
                    if glava == 6:
                        scene bg koridor4 with dissolve
                        jump free_time2_2
                    if glava == 7:
                        scene bg koridor5 with dissolve
                        jump free_time3_2
        else:
            dg "Уже достаточно поздно, пожалуй я пойду. Пока"
            co "Пока!"
            if glava == 6:
                scene bg koridor4 with dissolve
                jump free_time2_2
            if glava == 7:
                scene bg koridor5 with dissolve
                jump free_time3_2
    else:
        return
label cookiezi2:
    $free_time += 1
    co "На самом деле Сокиец - это не мой ник: мне придумал его брат."
    scene black with Dissolve(1)
    if glava == 6:
        scene bg ronpa_library with Dissolve(1)
    else:
        scene bg ronpa_computer with Dissolve(1)
    show sprite_c cookiezi with dissolve
    dg "Вот оно что."
    call co_gift from _call_co_gift_1
    if game_end == False:
        dg "Всегда хотел кое-что спросить у тебя, Сокиец."
        dg "Игрок под ником Legendary читер?"
        co "Эм..."
        co "Ну, честно говоря - это мой мультиакк."
        co "Так что нет. Это абсолютно леггитный чел."
        dg "..."
        co "Шучу конечно."
        co "Я не могу дать тебе ответ на этот вопрос."
        co "Не знаком с ним."
        co "Но лично я считаю, что он читер."
        co "Хотя..."
        co "Если подумать, то любой игрок, который играет намного сильнее тебя, может показаться читером."
        co "Поэтому мне сложно судить."
        co "Я бы сказал, что скорее да, чем нет."
        dg "Ясно."
        "Сокиец не был особо разговорчив."
        "Мне казалось, что ему лучше было одному."
        "Не буду доставать его."
        $cor += 1
        "Вы повысили отношения с Сокийцем на максимум."
        "Поздравляю!"
        if glava == 6:
            scene bg koridor4 with dissolve
            jump free_time2
        if glava == 7:
            scene bg koridor5 with dissolve
            jump free_time3_2
    else:
        return


#### ФРИТАЙМ ГЛАВА 7

label free_time3:
    if free_time < ft_max:
        call screen imagemap2
        $ result = _return
        if (result == "bath") or (result == "laundry") or (result == "trash") or (result == "storage"):
            "Вряд ли там кто-то будет."
            jump free_time3
        if (result == "dizRoom") or (result == "tRoom") or (result == "cRoom"):
            "Тук-тук."
            "..."
            "Похоже, внутри никого нет."
            jump free_time3
        if result == "dRoom":
            "Мне нечего делать в своей комнате."
            jump free_time3
        if result == "bogRoom":
            "Тук-тук."
            scene bg ronpa_bogRoom with dissolve
            show sprite_bb bogdik with dissolve
            bog "Привет, Диггер. Ты что-то хотел?"
            menu:
                "Провести время с Тундром.":
                    if bogdanr == 0:
                        jump bogdan1
                    if bogdanr == 1:
                        jump bogdan2
                    if bogdanr > 1:
                        ob "Вы уже прокачали отношения с Богданом на максимум, найдите себе другого собеседника."
                        scene koridor1 with dissolve
                        jump free_time1
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor1 with dissolve
                    jump free_time3
        if result == "dinning":
            scene bg ronpa_dininghall with dissolve
            "Никого."
            "С момента, когда Бистрола не стало, в столовой пусто."
            "..."
            scene koridor1 with dissolve
            jump free_time3
        if result == "school":
            scene koridor2 with dissolve
            jump free_time3_1
    else:
        jump idk
label free_time3_1:
    if free_time < ft_max:
        call screen imagemap1
        $result = _return
        if (result == "cinema") or (result == "lobby") or (result == "gym") or (result == "classA") or (result == "classB") or (result == "MedLab"):
            "Скорее всего, все тусуются на третьем этаж."
            "Здесь мне нужен максимум магазин."
            jump free_time3_1
        if result == "shop":
            scene bg ronpa_shop with dissolve
            call osu_shop from _call_osu_shop_3
            scene bg koridor2 with dissolve
            jump free_time3_1
        if result == "2F":
            scene bg koridor4 with dissolve
            "Лучше пойду сразу на третий этаж."
            scene bg koridor5 with dissolve
            jump free_time3_2
        if result == "dormitory":
            scene bg koridor1 with dissolve
            jump free_time3
    else:
        jump idk
label free_time3_2:
    if free_time < ft_max:
        call screen imagemap4
        $result = _return
        if (result == "ClassE") or (result == "ClassF"):
            "Класс закрыт."
            jump free_time3_2
        if (result == "2F"):
            scene bg koridor4 with dissolve
            scene bg koridor2 with dissolve
            jump free_time3_1
        if (result == "4F"):
            "Может, если я очень захочу, то смогу превратиться в воду и пройти сквозь решётку?"
            "..."
            "...."
            "Не работает."
            jump free_time3_2
        if result == "gRoom":
            scene bg ronpa_gameroom with dissolve
            show sprite_d dizick with dissolve
            "Дизик играл в бильярд сам с собой."
            "У него не очень получалось..."
            menu:
                "Провести время с Дизиком.":
                    if dizickr == 0:
                        jump dizick1
                    if dizickr == 1:
                        jump dizick2
                    if dizickr > 1:
                        ob "Вы уже прокачали отношения с Дизиком на максимум, найдите себе другого собеседника."
                        scene bg koridor5 with dissolve
                        jump free_time3_2
                "Найти Собеседника получше.":
                    scene bg koridor5 with dissolve
                    jump free_time3_2
        if result == "izo":
            scene bg ronpa_izo with dissolve
            show sprite_t talala with dissolve
            "Талала пытался нарисовать что-то на холсте."
            "Это был... Пудж?"
            menu:
                "Провести время с Талалой":
                    if talalar == 0:
                        jump talala1
                    if talalar == 1:
                        jump talala2
                    if talalar > 1:
                        ob "Вы уже прокачали отношения с Талалой на максимум, найдите себе другого собеседника."
                        scene bg koridor5 with dissolve
                        jump free_time3_2
                "Найти Собеседника получше.":
                    scene bg koridor5 with dissolve
                    jump free_time3_2
        if result == "computer":
            scene bg ronpa_computer with dissolve
            show sprite_c cookiezi with dissolve
            "Сокиец пытался понять как работает суперкомпьютер."
            menu:
                "Провести время с Сокийцем.":
                    if cor == 0:
                        jump cookiezi1
                    if cor == 1:
                        jump cookiezi2
                    if cor > 1:
                        ob "Вы уже прокачали отношения с Сокийцем на максимум, найдите себе другого собеседника."
                        scene bg koridor5 with dissolve
                        jump free_time3_2
                "Найти Собеседника получше.":
                    dg "Эм... Я просто дверью ошибся! Пока."
                    scene bg koridor5 with dissolve
                    jump free_time3_2
    else:
        jump idk

### BOGDAN

label bog_gift:
    menu:
        "Подарить ему подарок.":
            if (bogdan1 >= 1) and (bogdan2 == 0):
                $ bogdan1 -= 1
                "Для Богдана у меня есть только Чонгук."
                dg "Возьми, думаю, это может тебе понравиться."
                bog "Стой... Неужели это то, что я думаю?!"
                bog "Спасибо большое! Я давно хотел купить это."
                return
            if (bogdan2 >= 1) and (bogdan1 == 0):
                $ bogdan2 -= 1
                "Для Богдана у меня есть только книга."
                dg "Держи. Мне кажется, ты заценишь данный подгон."
                bog "Какая интересная книга."
                bog "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                return
            if (bogdan1 >= 1) and (bogdan2 >= 1):
                menu:
                    "Чонгук.":
                        $ bogdan1 -= 1
                        dg "Возьми, думаю, это может тебе понравиться."
                        bog "Стой... Неужели это то, что я думаю?!"
                        bog "Спасибо большое! Я давно хотел купить это."
                        return
                    "Книга.":
                            $ bogdan2 -= 1
                            dg "Держи. Мне кажется, ты заценишь данный подгон."
                            bog "Какая интересная книга."
                            bog "Диггер, спасибо! Я буду хранить эту вещь до конца своих дней."
                            return
            if (bogdan2 == 0) and (bogdan1 == 0):
                "У меня нет подарка для Богдана."
                dg "Ладно, я пожалуй пойду. Удачи."
                bog "Пока, Диггер!"
                scene bg koridor1 with dissolve
                jump free_time3
        "Уйти.":
            scene bg koridor1 with dissolve
            jump free_time3
label bogdan1:
    $free_time += 1
    bog "Может по мне и не скажешь, но я мёртв внутри."
    scene black with Dissolve(1)
    scene bg ronpa_bogRoom with Dissolve(1)
    show sprite_bb bogdik with dissolve
    bog "Ошихитео..."
    call bog_gift from _call_bog_gift
    if game_end == False:
        bog "На самом деле, я уже с детства был довольно богат."
        bog "Я переехал от родителей в 13 лет и самостоятельно зарабатывал деньги."
        bog "В какой-то момент, мне просто надоела опека."
        bog "Я получил стартовый капитал от родителей и всё."
        bog "Да и это не были большие деньги."
        bog "Просто я хочу сказать, что если чего-то очень сильно захотеть, то этого можно добиться."
        bog "Всю свою жизнь я стремился достичь чего-то."
        bog "У меня это вышло."
        bog "Сейчас я лидер самого популярного в мире бренда одежды «Dead Inside»."
        bog "Каждый человек в мире знает обо мне."
        bog "Однако только по достижении цели я понял, что не к этому стремился."
        dg "Что ты имеешь в виду?"
        bog "Из-за такой популярности я не могу даже выйти на улицу."
        bog "Не говоря уже о нормальной личной жизни."
        bog "Мне приходится скрываться в тайных особняках."
        bog "Никакой свободы действий."
        bog "Порой бывает, что человек просто не может вовремя остановиться."
        bog "Стремление быть лучшим не всегда приводит к хорошим последствиям."
        $bogdanr += 1
        if free_time < ft_max:
            "Мы уже довольно долго общаемся с Богданом, однако прошла только половина дня."
            menu:
                "Продолжить общаться с Богданом.":
                    if bogdanr < 2:
                        jump bogdan2
                    else:
                        "Ты уже повысил отношения с Сокийцем на максимум, найди себе другого собеседника."
                        scene bg koridor1 with dissolve
                        jump free_time3
                "Пойти поговорить с кем-то ещё.":
                        scene bg koridor1 with dissolve
                        jump free_time3
        else:
            dg "Уже достаточно поздно, пожалуй я пойду. Пока"
            bog "Бай."
            scene bg koridor1 with dissolve
            jump free_time3
    else:
        return

label bogdan2:
    $free_time += 1
    bog "Знаешь, я достаточно сильно люблю играть в доту, хоть она уже и не популярна."
    scene black with Dissolve(1)
    scene bg ronpa_bogRoom with Dissolve(1)
    show sprite_bb bogdik with dissolve
    bog "Врка худший герой."
    call bog_gift from _call_bog_gift_1
    if game_end == False:
        dg "И всё же. Почему ты решил помочь Талале?"
        dg "Это же такой риск."
        dg "Если у Пеппи ничего не выйдет, то ты можешь потерять все свои аккаунты."
        bog "Ха-х, может оно и к лучшему?"
        bog "Может тогда я заживу обычной жизнью?"
        bog "Смогу снова видеться с Талалой и Дизиком."
        bog "Любой исход для меня будет считаться победой."
        dg "Ясно..."
        bog "Мы с Талалой дружим ещё с моего детства."
        bog "Были моменты, когда нам было весело."
        bog "Были моменты, когда нам было грустно."
        bog "Однажды он помог мне, потом я ему."
        bog "Позже к нам присоединился Дизик."
        bog "Он был туповат, однако я сразу разглядел в нём человека."
        bog "Под человеком я имею виду того, кто может думать сам."
        bog "Знаешь, большинство людей в жизни ведут себя как будто они ёбаные NPC из игры."
        bog "Иной раз говоришь им что-то, а у них скрипт как будто не срабатывает и они не понимаю что ответить."
        bog "Так вот Дизик был не такой."
        bog "Он рос вмести с нами, и в итоге стал похож на человека."
        bog "Однако в какой-то момент он тоже свернул не на ту дорожку."
        bog "В теории, он мог стать не менее значимым человеком в мире, чем я."
        bog "Однако, так вышло, что он опустил руки."
        bog "Думаю, если бы я был рядом, то не допустил бы этого."
        bog "Ну а Талале уже было не помочь."
        bog "Не важно почему..."
        "В его словах прослеживается смысл."
        "Из всех осеров здесь, он выглядит самым умным."
        $bogdanr += 1
        "Вы повысили отношения с Богданом на максимум."
        "Поздравляю!"
        jump free_time3
    else:
        return
