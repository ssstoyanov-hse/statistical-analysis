with open('author.txt', 'tw', encoding='utf-8') as file:
    file.write("Стоянов Станислав Степанович\n19ПИ-1\nПрограммная инженерия, факультет компьютерных наук");

with open('author.txt', 'r', encoding='utf-8') as file:
    a = set(file.read());

with open('author.txt', 'a', encoding='utf-8') as file:
    file.write('\n');
    for char in a:
        file.write(char);