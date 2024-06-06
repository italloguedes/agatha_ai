import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Defina seu token do Telegram aqui
TOKEN_TELEGRAM = '7374171411:AAE9JMkzeBQWMdrT-a6kxF3KZNDdW2lTnWg'

# Array de versículos bíblicos em português
versiculos = [
    "E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito. (Romanos 8:28)",
    "Clama a mim, e responder-te-ei e anunciar-te-ei coisas grandes e firmes, que não sabes. (Jeremias 33:3)",
    "Porque eu bem sei os pensamentos que penso de vós, diz o Senhor; pensamentos de paz, e não de mal, para vos dar o fim que esperais. (Jeremias 29:11)",
    "O Senhor te abençoe e te guarde; o Senhor faça resplandecer o seu rosto sobre ti e tenha misericórdia de ti; o Senhor sobre ti levante o seu rosto e te dê a paz. (Números 6:24-26)",
    "O Senhor é bom, uma fortaleza no dia da angústia, e conhece os que nele confiam. (Naum 1:7)",
    "O Senhor te guardará de todo mal; ele guardará a tua alma. (Salmos 121:7)",
    "Eu, eu mesmo, sou o que apago as tuas transgressões por amor de mim, e dos teus pecados não me lembro. (Isaías 43:25)",
    "E disse-lhes: Ide por todo o mundo, pregai o evangelho a toda criatura. (Marcos 16:15)",
    "Aquele que habita no esconderijo do Altíssimo, à sombra do Onipotente descansará. (Salmos 91:1)",
    "Porque Deus não nos deu o espírito de temor, mas de fortaleza, e de amor, e de moderação. (2 Timóteo 1:7)",
    "E disse Jesus: Eu sou o pão da vida; aquele que vem a mim não terá fome; e quem crê em mim nunca terá sede. (João 6:35)",
    "Se confessarmos os nossos pecados, ele é fiel e justo para nos perdoar os pecados, e nos purificar de toda a injustiça. (1 João 1:9)",
    "Porque a palavra do Senhor é reta, e todas as suas obras são feitas com fidelidade. (Salmos 33:4)",
    "Deus é o nosso refúgio e fortaleza, socorro bem presente na angústia. (Salmos 46:1)",
    "O Senhor é a minha luz e a minha salvação; a quem temerei? O Senhor é a força da minha vida; de quem me recearei? (Salmos 27:1)",
    "E buscar-me-eis, e me achareis, quando me buscardes de todo o vosso coração. (Jeremias 29:13)",
    "Porque o Senhor conhece o caminho dos justos, mas o caminho dos ímpios perecerá. (Salmos 1:6)",
    "E sabemos que já o Filho de Deus é vindo, e nos deu entendimento para conhecermos o que é verdadeiro; e no que é verdadeiro estamos, isto é, em seu Filho Jesus Cristo. Este é o verdadeiro Deus e a vida eterna. (1 João 5:20)",
    "Disse-lhe Jesus: Eu sou a ressurreição e a vida; quem crê em mim, ainda que esteja morto, viverá; (João 11:25)",
    "E disse Deus: Haja luz; e houve luz. (Gênesis 1:3)",
    "Ainda que eu andasse pelo vale da sombra da morte, não temeria mal algum, porque tu estás comigo; a tua vara e o teu cajado me consolam. (Salmos 23:4)",
    "Eu sou o Alfa e o Ômega, o princípio e o fim, o primeiro e o derradeiro. (Apocalipse 22:13)",
    "E o que me enviou está comigo. O Pai não me tem deixado só, porque eu faço sempre o que lhe agrada. (João 8:29)",
    "Em tudo dai graças, porque esta é a vontade de Deus em Cristo Jesus para convosco. (1 Tessalonicenses 5:18)",
    "No amor não há temor, antes o perfeito amor lança fora o temor; porque o temor tem consigo a pena, e o que teme não é perfeito em amor. (1 João 4:18)",
    "E se o Espírito daquele que dos mortos ressuscitou a Jesus habita em vós, aquele que dos mortos ressuscitou a Cristo também vivificará os vossos corpos mortais, pelo seu Espírito que em vós habita. (Romanos 8:11)",
    "E Jesus, olhando para eles, disse-lhes: Aos homens é isso impossível, mas a Deus tudo é possível. (Mateus 19:26)",
    "E se o meu povo, que se chama pelo meu nome, se humilhar, e orar, e buscar a minha face, e se converter dos seus maus caminhos, então eu ouvirei dos céus, e perdoarei os seus pecados, e sararei a sua terra. (2 Crônicas 7:14)",
    "Pois, que aproveitaria ao homem ganhar todo o mundo e perder a sua alma? (Marcos 8:36)",
    "Eu sou o bom Pastor; o bom Pastor dá a sua vida pelas ovelhas. (João 10:11)",
    "E não nos cansemos de fazer o bem, porque a seu tempo ceifaremos, se não houvermos desfalecido. (Gálatas 6:9)",
    "E esta é a confiança que temos nele, que, se pedirmos alguma coisa, segundo a sua vontade, ele nos ouve. (1 João 5:14)",
    "O Senhor, teu Deus, está no meio de ti, poderoso para salvar-te; ele se deleitará em ti com alegria; renovar-te-á no seu amor, regozijar-se-á em ti com júbilo. (Sofonias 3:17)",
    "Não temas, porque eu sou contigo; não te assombres, porque eu sou teu Deus; eu te fortaleço, e te ajudo, e te sustento com a destra da minha justiça. (Isaías 41:10)",
    "E a paz de Deus, que excede todo o entendimento, guardará os vossos corações e os vossos sentimentos em Cristo Jesus. (Filipenses 4:7)",
    "O Senhor é bom para com aqueles cuja esperança está nele, para com aqueles que o buscam; (Lamentações 3:25)",
    "Alegrai-vos na esperança, sede pacientes na tribulação, perseverai na oração; (Romanos 12:12)",
    "Deleita-te também no Senhor, e ele te concederá o que deseja o teu coração. (Salmos 37:4)",
    "O Senhor está perto de todos os que o invocam, de todos os que o invocam com sinceridade. (Salmos 145:18)",
    "Confia no Senhor de todo o teu coração, e não te estribes no teu próprio entendimento. (Provérbios 3:5)",
    "Mas, buscai primeiro o reino de Deus, e a sua justiça, e todas estas coisas vos serão acrescentadas. (Mateus 6:33)",
    "Mas o Senhor é fiel; ele vos confirmará, e guardará do maligno. (2 Tessalonicenses 3:3)",
    "Porque para Deus nada é impossível. (Lucas 1:37)",
    "Pois estou convencido de que nem morte nem vida, nem anjos nem demônios, nem o presente nem o futuro, nem quaisquer poderes, nem altura nem profundidade, nem qualquer outra coisa na criação será capaz de nos separar do amor de Deus que está em Cristo Jesus, nosso Senhor. (Romanos 8:38-39)",
    "Porque sou eu que conheço os planos que tenho para vocês, diz o Senhor, planos de fazê-los prosperar e não de causar dano, planos de dar a vocês esperança e um futuro. (Jeremias 29:11)",
    "Mas ele foi ferido por causa das nossas transgressões, e moído por causa das nossas iniquidades; o castigo que nos traz a paz estava sobre ele, e pelas suas pisaduras fomos sarados. (Isaías 53:5)",
    "E não somente isto, mas também nos gloriamos nas tribulações; sabendo que a tribulação produz a paciência, e a paciência a experiência, e a experiência a esperança. (Romanos 5:3-4)",
    "Jesus Cristo é o mesmo ontem, hoje e para sempre. (Hebreus 13:8)"
]


async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    botoes = [
        [InlineKeyboardButton("Versículo do Dia", callback_data='versiculo')],
        [InlineKeyboardButton("Sobre", callback_data='sobre')],
        [InlineKeyboardButton("Teste", callback_data='teste')]
    ]
    reply_markup = InlineKeyboardMarkup(botoes)
    await context.bot.send_message(chat_id=chat_id, text="Olá! Deus tem uma mensagem importante para voçê!! Escolha uma opção:", reply_markup=reply_markup)

async def enviar_versiculo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    versiculo = random.choice(versiculos)
    await context.bot.send_message(chat_id=chat_id, text=versiculo)

async def versiculo_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    versiculo = random.choice(versiculos)
    await query.edit_message_text(text=versiculo)

async def sobre(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Eu sou um bot que envia versículos bíblicos. Desenvolvido por [@italloGuedes].")

async def teste(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Teste")

def main() -> None:
    application = Application.builder().token(TOKEN_TELEGRAM).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('versiculo', enviar_versiculo))
    application.add_handler(CallbackQueryHandler(versiculo_callback, pattern='versiculo'))
    application.add_handler(CallbackQueryHandler(sobre, pattern='sobre'))
    application.add_handler(CallbackQueryHandler(teste, pattern='sobre'))

    application.run_polling()

if __name__ == '__main__':
    main()
