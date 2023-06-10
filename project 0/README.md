# Проект 0. Угадай число / Project 0. Guess Number

## Оглавление / Contents
[1. Описание проекта / Project description](README.md#Описание-проекта--Project-description)  
[2. Какой кейс решаем?/ What is the case solving?](README.md#Какой-кейс-решаем--What-is-the-case-solving?)  
[3. Краткая информация о данных / Short breief about data](README.md#Краткая-информация-о-данных--Short-brief-of-data)  
[4. Этапы работы над проектом / Project worksteps](README.md#Этапы-работы-над-проектом--Project-worksteps)  
[5. Результат / Result](README.md#Результат--Result)    
[6. Выводы / Conclusions](README.md#Выводы--Conclusions) 

### Описание проекта / Project description 
Угадать загаданное компьютером число за минимальное число попыток. / 
Guess the number guessed by the computer in the minimum number of attempts.

&uarr; [к оглавлению/to the contents](README.md#Оглавление--Contents)


### Какой кейс решаем? / What is the case solving?  
Нужно написать программу, которая угадывает число за минимальное число попыток. / Need to write the code that guesses the number in the minimum number of attempts.

**Условия соревнования: / Competition rules:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число». / Computer thinks an integer number and we need to write a code that guesses this number.
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам. / Algorithm counts an information if our guessed number either more or less of the required number.

**Метрика качества / Quality metric**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений. / 
Results are evaluated by the average number of attempts after 1000 code repetitions.

**Что практикуем / What we practice**     
Учимся писать хороший код на python / Learning how to write a good code on Python


### Краткая информация о данных / Short brief of data
На вход подается множество целых чисел от 1 до 100. / The input is a set of integers from 1 to 100.

Выводом также является целое число попыток. / The output is also an integer number of attempts.
  
&uarr;[к оглавлению/to the contents](README.md#Оглавление--Contents)


### Этапы работы над проектом / Project worksteps 
Внимательное изучение курса. Далее копипаста функции подсчета количества попыток.
Затем реализация собственного кода для подсчета минимального количества попыток методом деления множества из возможных чисел на равные подмножества. То есть сокращение диапазона поиска в два раза до тех пор, пока искомое число не будет найдено. / Careful study of the course. Copy-paste the function of counting the number of attempts. Then the implementation of the code for calculating the minimum number of attempts by dividing the set of possible numbers into equal subsets. That is, halving the search range until the required number is found.

&uarr;[к оглавлению/to the contents](README.md#Оглавление--Contents)


### Результат / Result 
Реализованный код показывает средний результат в 5 попыток за 1000 повторений. / The implemented code shows an average result of 5 attempts after 1000 repetitions.

&uarr;[к оглавлению/to the contents](README.md#Оглавление--Contents)


### Выводы / Conclusions
Условие поиска случайного числа от 1 до 100 за 20 попыток выполнено. / The condition for searching for a random number from 1 to 100 in 20 attempts is accomplished.

&uarr;[к оглавлению/to the contents](README.md#Оглавление--Contents)