# Title     : Homework
# Objective : Exchange
# Created by: Stanislav
# Created on: 25/11/2020

# APPLE

aapl <- read.csv(file = "/home/stanislav/PycharmProjects/statistical-analysis/HW6/data/AAPL.csv", sep = ",")

# График изменения цены
plot(aapl$Date, aapl$Open, type = "l", xlab = "date", ylab = "apple price", main = "Показатели цены акций Apple")
lines(aapl$Date, aapl$Open, col = "black", lwd = 2)

# Распределение доходности
aapl_profit <- diff(aapl$Open) / aapl$Open[-1]
hist(aapl_profit, breaks = 50, main = "Распределение доходности Apple, близко к нормальному, но немного смещена вправо,
доходность акций исторически имеет положительное математическое ожидание -
это есть та добавленную стоимость, что генерирует бизнес Apple")


# Распределение цены
hist(aapl$Open, breaks = 50, main = "Распределение цены Apple близки к распределению Хи квадрат,
но имеет пробелы в графике, значит стоимость акции сложно будет спрогнозировать")

# Волатильность
plot(aapl_profit, type = 'l', xlab = "Номер", ylab = "Показатель волатильности Apple")

# Показатели волатильности
message(sprintf("Среднее значение доходности для Apple %s", mean(aapl_profit)))
message(sprintf("Медианное значение доходности для Apple %s", median(aapl_profit)))
message(sprintf("Cтандартное отклонение доходности для Apple %s", sd(aapl_profit)))

# GOOGLE

goog <- read.csv(file = "/home/stanislav/PycharmProjects/statistical-analysis/HW6/data/GOOG.csv", sep = ",")

# График изменения цены
plot(goog$Date, goog$Open, type = "l", xlab = "date", ylab = "google price", main = "Показатели цены акций Google")
lines(goog$Date, goog$Open, col = "black", lwd = 2)

# Распределение доходности
goog_profit <- diff(goog$Open) / goog$Open[-1]
hist(goog_profit, breaks = 50, main = "Распределение доходности Google, близко к нормальному, но немного смещена вправо,
доходность акций исторически имеет положительное математическое ожидание -
это есть та добавленную стоимость, что генерирует бизнес Google")

# Распределение цены
hist(goog$Open, breaks = 50, main = "Распределение цены Google не похоже на распределение Хи квадрат,
значит стоимость акции практически невозможно спрогнозировать")

# Волатильность
plot(goog_profit, type = 'l', xlab = "Номер", ylab = "Показатель волатильности Google")

# Показатели волатильности
message(sprintf("Среднее значение доходности для Google %s", mean(goog_profit)))
message(sprintf("Медианное значение доходности для Google %s", median(goog_profit)))
message(sprintf("Cтандартное отклонение доходности для Google %s", sd(goog_profit)))

# GAZPROM

gazp <- read.csv(file = "/home/stanislav/PycharmProjects/statistical-analysis/HW6/data/GAZP.csv", sep = ",")

# График изменения цены
plot(gazp$Date, gazp$Open, type = "l", xlab = "date", ylab = "gazprom price", main = "Показатели цены акций Газпром")
lines(gazp$Date, gazp$Open, col = "black", lwd = 2)

# Распределение доходности
gazp_profit <- diff(gazp$Open) / gazp$Open[-1]
hist(gazp_profit, breaks = 50, main = "Распределение доходности Gazprom, близко к нормальному, но немного смещена вправо,
доходность акций исторически имеет положительное математическое ожидание -
это есть та добавленную стоимость, что генерирует бизнес Gazprom")

# Распределение цены
hist(gazp$Open, breaks = 50, main = "Распределение цены Gazprom очень похоже на хи-квадрат,
поэтому цену акций можно спрогнозировать")

# Волатильность
plot(gazp_profit, type = 'l', xlab = "Номер", ylab = "Показатель волатильности Gazprom")

# Показатели волатильности
message(sprintf("Среднее значение доходности для Gazprom %s", mean(gazp_profit)))
message(sprintf("Медианное значение доходности для Gazprom %s", median(gazp_profit)))
message(sprintf("Cтандартное отклонение доходности для Gazprom %s", sd(gazp_profit)))
