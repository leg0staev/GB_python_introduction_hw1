ticketNumber = int(
    input('введите номер Вышего билетика, и я скажу счастливый он или нет: '))


def LuckyTicket(ticketNumber):
    if 99999 < ticketNumber < 1000000:
        firstThreeDigitSum = ticketNumber // 1000 % 10 + \
            ticketNumber // 10000 % 10 + ticketNumber // 100000 % 10
        
        secondThreeDigitSum = ticketNumber % 10 + \
            ticketNumber % 100 // 10 + ticketNumber % 1000 // 100
        
        if firstThreeDigitSum == secondThreeDigitSum:
            return "УРА! Ваш билетик счастливый! Скорее съешьте его"
        else:
            return "к сожалению, этот билет не принесет Вам счастья, придется купить еще один"
    else:
        return "неверный номер билета"


print(LuckyTicket(ticketNumber))
