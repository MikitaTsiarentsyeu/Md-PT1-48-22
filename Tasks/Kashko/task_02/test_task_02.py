from datetime import datetime

import task_02


def test_time_to_text():
    """Test time_to_text function."""
    assert task_02.time_to_text(datetime(2020, 1, 1, 0, 0)) == \
        '00:00 - двенадцать часов ровно'
    assert task_02.time_to_text(datetime(2020, 1, 1, 12, 0)) == \
        '12:00 - двенадцать часов ровно'
    assert task_02.time_to_text(datetime(2020, 1, 1, 23, 1)) == \
        '23:01 - одна минута двенадцатого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 15, 7)) == \
        '15:07 - семь минут четвертого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 4, 12)) == \
        '04:12 - двенадцать минут пятого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 7, 20)) == \
        '07:20 - двадцать минут восьмого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 8, 25)) == \
        '08:25 - двадцать пять минут девятого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 9, 30)) == \
        '09:30 - половина десятого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 10, 35)) == \
        '10:35 - тридцать пять минут одиннадцатого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 13, 45)) == \
        '13:45 - без пятнадцати минут два'
    assert task_02.time_to_text(datetime(2020, 1, 1, 11, 40)) == \
        '11:40 - сорок минут двенадцатого'
    assert task_02.time_to_text(datetime(2020, 1, 1, 14, 50)) == \
        '14:50 - без десяти минут три'
    assert task_02.time_to_text(datetime(2020, 1, 1, 15, 55)) == \
        '15:55 - без пяти минут четыре'
