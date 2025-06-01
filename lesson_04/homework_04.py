adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
# task 02 ==
""" Замініть .... на пробіл
"""
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# task 01-03
import re
new_adwentures_of_tom_sawer_1 = adwentures_of_tom_sawer.replace("\n", " ")
new_adwentures_of_tom_sawer_2 = new_adwentures_of_tom_sawer_1.replace("....", " ")
new_adwentures_of_tom_sawer_3 = re.sub(r' +', ' ', new_adwentures_of_tom_sawer_2).strip()
print(new_adwentures_of_tom_sawer_3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('Літера "h" зустрічається у тексті', adwentures_of_tom_sawer.count("h"), 'раз.')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words_with_caps = re.findall(r'\b[A-Z][a-z]+\b', new_adwentures_of_tom_sawer_3)
print("Кількість слів, що починаються з великої літери:", len(words_with_caps))

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_Tom_time = new_adwentures_of_tom_sawer_3.find("Tom")
print("Слово Tom зустрічається вдруге у відформатованому тексті "
      "на позиції:", new_adwentures_of_tom_sawer_3.find("Tom", first_Tom_time + 1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = new_adwentures_of_tom_sawer_3.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
new_adwentures_of_tom_sawer_sentences = fourth_sentence.lower()
print(new_adwentures_of_tom_sawer_sentences)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
index = new_adwentures_of_tom_sawer_3.find("By the time")
if index != -1:
    print(f"'By the time' знайдено на позиції {index}.")
else:
    print("Не знайдено.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_adwentures_of_tom_sawer = adwentures_of_tom_sawer_sentences[-1].split(" ")
print("Кількість слів останнього речення =", len(last_sentence_adwentures_of_tom_sawer))