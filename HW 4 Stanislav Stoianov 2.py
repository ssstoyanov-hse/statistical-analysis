file = open('author.txt', 'tw', encoding='utf-8');
file.write("Стоянов Станислав Степанович\n19ПИ-1\nПрограммная инженерия, факультет компьютерных наук");
file.close();

file = open('author.txt', 'r');

text = file.read();
a = set(text);
print("Оригинальный текст:\n" + text + "\nМножество букв и цифр:");
print(a);

file.close();
