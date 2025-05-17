import logging
import aiohttp
import random
from telegram.ext import MessageHandler, filters, ApplicationBuilder, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)
bot = Bot(token="7722525166:AAGFlEno9NwSsx5jWzB1qnDmoSsfg8ZrfhA")


async def start(update, context):
    context.user_data["id"] = update.message.chat.id
    await update.message.reply_text(
        "Привет. Это бот для текстового квеста. \n"
        "Вы можете прервать квест написав /stop.\n"
        "Готовы начать?",
        reply_markup=ReplyKeyboardMarkup([["Да", "Об игре"]], one_time_keyboard=True))
    return 1


async def first_response(update, context):
    if update.message.text == "Об игре":
        with open('FAQ.txt', encoding="UTF-8") as f:
            f = f.readline()
            print(f)
        await update.message.reply_text(f)
        return ConversationHandler.END
    await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8Z.jpg')
    await update.message.reply_text(
        "Вы проснулись в неизвестной вам комнате без воспоминаний о том, как попали сюда. \n"
        "Но вы чувствуете что вам стоит покинуть это место. \n"
        "В комнате есть окно, стол, кровать и дверь с замком. Что вы будете делать?",
        reply_markup=ReplyKeyboardMarkup([["Проверить окно", "Проверить стол", "Проверить дверь"]],
                                         one_time_keyboard=True))
    return 2


async def second_response(update, context):
    await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8Z.jpg')
    first_choice = update.message.text
    if first_choice == "Проверить окно":
        await update.message.reply_text(
            'Вы решили проверить в окно. \n'
            'Пару раз попытавшись открыть окно, вы поняли что оно закрыто. \n'
            'Судя по всему эта комната находится на втором этаже.\n'
            'За окном видно небольшой лес и металлический забор, который обычно бывает у больших дорогих особняков \n'
            'Что вы будете делать? Вы можете попытаться разбить окно или дальше исследовать комнату',
            reply_markup=ReplyKeyboardMarkup([["Проверить стол", "Ударить окно"]], one_time_keyboard=True))
    if first_choice == "Проверить стол":
        await update.message.reply_text(
            'Вы подходите к столу. \n'
            'На нем находится ключ и записка. \n'
            'На ней написано "Попробуй выбраться из здания до заката и получи награду! \n'
            'Подпись А.Н. Оним',
            reply_markup=ReplyKeyboardMarkup([["Взять ключ"]], one_time_keyboard=True))
    if first_choice == "Проверить дверь":
        await update.message.reply_text(
            'Пару раз дернув дверь вы поняли что она закрыта. \n'
            'У двери есть замочная скважина, так что возможно где-то в комнате есть ключ к ней. \n'
            'Что вы проверите?',
            reply_markup=ReplyKeyboardMarkup([["Проверить стол", "Проверить окно"]], one_time_keyboard=True))
    return 3


async def third_response(update, context):
    second_choice = update.message.text
    if second_choice == "Проверить стол":
        await update.message.reply_text(
            'Вы подходите к столу. \n'
            'На нем находится ключ и записка. \n'
            'На ней написано "Попробуй выбраться из здания до заката и получи награду! \n'
            'Подпись А.Н. Оним',
            reply_markup=ReplyKeyboardMarkup([["Взять ключ и открыть дверь"]], one_time_keyboard=True))
    if second_choice == "Ударить окно":
        await update.message.reply_text(
            'Не придумав ничего лучше вы решаете разбить окно. \n'
            'После удара окна кулаком оно разбивается, но у вас начинается кровотечение. \n'
            'Вы решаете как можно быстрее бежать отсюда и выпрыгиваете из окна. \n'
            'К сожалению это было последним решением в вашей жизни, ибо вы умираете. \n'
            'Конец!')
        return ConversationHandler.END
    if second_choice == "Проверить окно":
        await update.message.reply_text(
            'Вы решили проверить в окно. \n'
            'Пару раз попытавшись открыть окно, вы поняли что оно закрыто. \n'
            'Судя по всему эта комната находится на втором этаже.\n'
            'За окном видно небольшой лес и металлический забор, который обычно бывает у больших дорогих особняков \n'
            'Не придумав ничего лучше вы решаете разбить окно. \n'
            'После удара окна кулаком оно разбивается, но у вас начинается кровотечение. \n'
            'Вы решаете как можно быстрее бежать отсюда и выпрыгиваете из окна. \n'
            'К сожалению это было последним решением в вашей жизни, ибо вы умираете. \n'
            'Конец!')
        return ConversationHandler.END
    if second_choice == "Взять ключ":
        await update.message.reply_text(
            'Вы берете ключ и подходите к двери. \n'
            'Пару раз дернув её вы поняли что она закрыта. \n'
            'У двери есть замочная скважина, так что возможно ключ в ваших руках от нее. \n'
            'Остается только одно.',
            reply_markup=ReplyKeyboardMarkup([["Открыть дверь"]], one_time_keyboard=True))
    return 4


async def fourth_response(update, context):
    await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8W.jpg')

    third_choice = update.message.text
    if third_choice == "Открыть дверь" or third_choice == "Взять ключ и открыть дверь":
        await update.message.reply_text(
            'Выйдя из комнаты вы попадаете в прямой коридор. \n'
            'Начиная идти прямо на вашем пути встречается множество закрытых комнат. \n'
            'Также в этом месте висит очень много дорогих на вид картин. \n'
            'Вся атмосфера этого здания так и кричит о богатстве и благородстве. \n'
            'Вы продолжаете идти в никуда слепо веря что вы найдете выход. \n'
            'В конце концов вы приходите к лестнице и спускаетесь по ней. \n'
            'Судя по всему это место является центром здания, в то время как вы пришли из левого крыла. \n'
            'Надо решить куда идти дальше',
            reply_markup=ReplyKeyboardMarkup(
                [["Пойти в зал", "Пойти на кухню", "Пойти в задний двор", "Выйти из здания"]], one_time_keyboard=True))
    return 5


async def fifth_response(update, context):
    fourth_choice = update.message.text

    if fourth_choice == "Пойти в зал":
        await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8V.jpg')
        await update.message.reply_text(
            'Вы входите в комнату, которая должна быть чем-то вроде гостевой. \n'
            'В ней находится несколько мест где можно приятно посидеть \n'
            'и небльшой столик с загадочным предметом на нем. \n'
            'Подойдя ближе к загадочному предмету вы понимаете что это черный планшет с головоломкой \n'
            'Видимо вам надо решить ее')

    if fourth_choice == "Пойти на кухню":  # картинка кухни
        await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8a.jpg')
        await update.message.reply_text(
            'Вы входите в комнату, которая должна быть чем-то вроде кухни. \n'
            'После небольшого осмотра этой комнаты вы находите нож и черный планшет. \n'
            'На планшете есть головоломка, которую вам видимо надо решить. \n')

    if fourth_choice == "Пойти в задний двор":  # картинка заднего дворика
        await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8Y.jpg')
        await update.message.reply_text(
            'Вы наконец-то выходите на улицу, \n'
            'Но вы понимаете что не можете выйти дальше этого небольшого дворика. \n'
            'Среди красивых цветов стоит кресло с плашетом на нем \n'
            'Взяв планшет вы понимаете что на нем есть головоломка, которую как вы поняли вам надо решить')

    if fourth_choice == "Выйти из здания":  # картинка ворот
        await bot.sendPhoto(context.user_data['id'], 'https://i.yapx.ru/ZBE8X.jpg')
        await update.message.reply_text(
            'На удивление входная дверь была не закрыта и вы смогли выйти. \n'
            'Пробежав 100 метров вы подходите к закрытым воротам. \n'
            'Но вы видите, что рядом с дверью лежит планшет. \n'
            'Подобрав его вы видите головломку на нем и решаете решить ее.')
    async with aiohttp.ClientSession() as session:
        async with session.get("https://opentdb.com/api.php?amount=1&type=multiple") as resp:
            data = await resp.json()
            q = data["results"][0]
            question = q["question"]
            correct = q["correct_answer"]
            answers = q["incorrect_answers"] + [correct]
            random.shuffle(answers)
            context.user_data["correct_trivia"] = correct
            await update.message.reply_text(
                f"Вопрос: {question}",
                reply_markup=ReplyKeyboardMarkup([[a] for a in answers], one_time_keyboard=True))

    return 6


async def handle_trivia(update, context):
    answer = update.message.text
    if answer == context.user_data["correct_trivia"]:
        await update.message.reply_text(
            "Вдали гремит громкий взрыв! \n"
            "Вы не понимаете, что происходит и бежите к месту, где он произошёл. \n"
            "Оно оказывается рядом со входом в здание. \n"
            "Там, вы видите поднятую от взрыва пыль! \n"
            "Когда она начинает оседать, вы замечаете странного человека.....")
        await update.message.reply_text("Для перехода к эпилогу напишите /epilogue")
    else:
        await update.message.reply_text(
            "На планшете появляется надпись НЕПРАВИЛЬНЫЙ ОТВЕТ \n"
            "Вы думаете, что теперь делать, но, не успевая сделать и шагу, умираете \n"
            "Планшет взорвался и нанес вам несовместимые с жизнью травмы!")
    return ConversationHandler.END


async def epilogue(update, context):  # тут картинка особняка прикола, если не лень можно еще прифотошопить дэна
    context.user_data["id"] = update.message.chat.id
    await bot.sendPhoto(context.user_data['id'],
                        'AgACAgIAAxkBAAIGfmgoplw1tSV_EE91tZsiQ5w5zKhqAAKI8TEbPWZISfjbE7kWqXJKAQADAgADeAADNgQ')
    await update.message.reply_text(
        "Вы видите человека лет тридцати, который стоит возле особняка. \n"
        "Кто это? Что делать? Как сбежать из этого места? \n"
        "Именно эти вопросы проносятся у вас в голове."
        "Вы можете попробовать убежать отсюда как можно быстрее,"
        "или, может, быть лучше, пойти и поговорить с этим человеком...",
        reply_markup=ReplyKeyboardMarkup(
            [["Подойти к человеку с готовностью атаковать"], ["Убежать", 'Подойти к человеку']],
            one_time_keyboard=True))
    return 1


async def sixth_response(update, context):  # тут тоже особняк
    await bot.sendPhoto(context.user_data['id'],
                        'AgACAgIAAxkBAAIGfmgoplw1tSV_EE91tZsiQ5w5zKhqAAKI8TEbPWZISfjbE7kWqXJKAQADAgADeAADNgQ')
    sixth_choice = update.message.text
    if sixth_choice == "Убежать":
        await update.message.reply_text(
            'Вы решили, что лучшим решением будет убежать от него как можно быстрее. \n'
            'Конечно же это была ошибка, поворачиваться спиной к незнакомцу было фатальным решением \n'
            'Как только вы попробовали убежать, вы упали, почувствовали удар по спине и услышали громкий хлопок. \n'
            'Это был выстрел. \n'
            'Некто убил вас...')
        return ConversationHandler.END
    if sixth_choice == "Подойти к человеку с готовностью атаковать":
        await update.message.reply_text(
            'Вы решили, что лучшая защита это нападение, смелости вам не занимать! \n'
            'Подойдя к незнакомцу вы наносите удар правой рукой \n'
            'Но не успеваете вы ударить, как оказываетесь на земле с пулей в груди \n'
            'Нападать на незнакомых людей очень плохое решение...')
        return ConversationHandler.END
    if sixth_choice == "Подойти к человеку":
        await update.message.reply_text(
            'Вы решили что лучшим решением будет попробовать поговорить с незакомцем. \n'
            'Как только вы попали в его поле зрение, человек начал говорить первым \n'
            '- Меня зовут Дэн. Тихий Дэн. \n'
            'Это были единственные слова незнакомца, хотя это больше был не незнакомец \n'
            'Это был Дэн. Тихий Дэн \n'
            'Но что делать теперь? Поможет ли Дэн выбраться вам отсюда? \n'
            'Или вы захотите решить загадку этого поместья?',
            reply_markup=ReplyKeyboardMarkup([["Попросить помощи", "Предложить помощь"]], one_time_keyboard=True))
    return 2


async def seventh_response(update, context):
    seventh_choice = update.message.text
    if seventh_choice == "Попросить помощи":
        await update.message.reply_text(
            'Вы начинаете диалог с просьб о помощи \n'
            'Говоря про то, что с вами случилось, и как вы хотите убежать отсюда, лицо Дэна стало мрачнее \n'
            '-Я понял твою ситуацию, держи эту ключ карту и уходи из этого места! \n'
            'Дрожащими руками вы взяли карту и убежали из особняка! \n'
            'Конец!')
        return ConversationHandler.END
    if seventh_choice == 'Предложить помощь':
        await update.message.reply_text(
            'Вы начинаете диалог с того, что рассказываете Дэну о том что произошло с вами. \n'
            'В ваших словах нет трусости, в конце вашего рассказа вы говорите, что хотите узнать кто это сделал и зачем \n'
            'Тихий Дэн с улыбкой посмотрел вам в глаза и заговорил \n'
            '- Я рад что человек, очутившийся в этом месте, оказался таким храбрым! \n'
            'Дэн протянул вам банковский чек на котором было написано очень большое число. \n'
            '- Можно сказать ты прошел испытание, я не могу многого говорить, но ты заслужил эти деньги. Теперь уходи. \n'
            'Вы не понимаете что происходит, но большая сумма затуманивает ваш разум и вы решаете уйти с деньгами. \n'
            'Лучший конец!')
        return ConversationHandler.END


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


async def help_command(update, context):
    await update.message.reply_text("Просто нажимай на кнопки и отвеачй на вопросы Тихого Дэна")


def main():
    app = ApplicationBuilder().token("7722525166:AAGFlEno9NwSsx5jWzB1qnDmoSsfg8ZrfhA").build()

    first_chapter = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, third_response)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_response)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, fifth_response)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_trivia)]
        },
        fallbacks=[CommandHandler('stop', stop)])

    second_chapter = ConversationHandler(
        entry_points=[CommandHandler('epilogue', epilogue)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, sixth_response)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, seventh_response)]
        },
        fallbacks=[CommandHandler('stop', stop)])

    app.add_handler(first_chapter)
    app.add_handler(second_chapter)
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()


if __name__ == '__main__':
    main()
