from telegram.ext import Updater, CommandHandler
from random import *
import datetime
from googletrans import Translator
import requests
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

def search_gifs(query):
    response = api_instance.gifs_search_get(giphy_token,
        query, limit=3, rating='g')
    lst = list(response.data)
    gif = random.choices(lst)
    return gif[0].url

def randomfungif(update, context):
    animation = "https://media.giphy.com/media/H4EUdpMOEAd4XJ6uaZ/source.gif"
    message.message.reply_animation("https://nantes-services.github.io/bot/source.gif")

def bonjour(update, context):
    saluts = [", stay cool 😎!", ", be nice !", ", vous êtes sympas 😏!", ", bienvenue à NANTES SERVICES !", ", comment allez vous 😊?", ", vous avez l'air en forme ! 🤗", ", bonne journée ?", ", combien de services avez vous rendus aujourd'hui 🙂?", ", bon courage !"]
    update.message.reply_text('Hello 👋{} {}'.format(update.message.from_user.first_name, choice(saluts)))

def service(update, context):
    msg = ""
    services = ["BRICOLAGE ET PETITS TRAVAUX", "BABYSITTING", "JARDINAGE (TONTE, TAILLE DE HAIE ...)", "ASSISTANCE INFORMATIQUE", "AIDE AU DÉMENAGEMENT", "ASSISTANCE SCOLAIRE EN MATHÉMATIQUES", "MONTAGE PHOTO / VIDÉO", "GARDE CHIEN(S) ET CHAT(S) (À VOTRE DOMICILE)"]
    for s in services:
            msg += "\n" + s
    update.message.reply_text('À NANTES SERVICES, nous rendons les services suivant : \n {}'.format(msg))

def people(update, context):
    msg = ""
    people = ["BREAN", "VALENTIN", "VICTORIA", "JACKSON", "ETHAN", "JONAH", "EVA", "ADRIEN", "OCEANE"]
    for p in people:
        msg += " ; " + p
    update.message.reply_text('À NANTES SERVICES : {} vous rendent service !'.format(msg))

def help(update, context):
    msg = ""
    commande = ["/help       : Donne la liste des commandes",
                "/bonjour    : Pour saluer Alfred",
                "/service    : Affiche la liste des services que NANTES SERVICES rends",
                "/people     : Affiche la liste des jeunes prêts à rendre service",
                "/lien       : Affiche le lien du site",
                "/botdemerde : Je vous emmerde",
                "/laugth     : J'adore l'humour",
                "/alfred     + ça va ? : Demande à Alfred comment il va. \n                + traduis ou Traduis : Donne la traduction en anglais et en français du mot ou de la phrase qui suit\n                + spam + mot + nombre : Spam le mot le nombre de fois défini."]
    for c in commande:
        msg += "\n" + c
    update.message.reply_text(msg)

def lien(update, context):
    msg = "https://nantes-services.github.io"
    update.message.reply_text(msg)

def botdemerde(update, context):
    rep = ["FERMEZ LÀ JE VOUS PRIS {}, {}", "TA GUEULE {} {}", "VA TE FAIRE {} {}"]
    emoji = ["😡", "😤", "🤬"]
    msg = choice(rep).format(choice(emoji), update.message.from_user.first_name)
    update.message.reply_text(msg)

def laugth(update, context):
    msg = ""
    rire = [" EXCELLENT ", " MDR ", " PTDR ", " TRÈS DRÔLE "]
    user = " ".join(context.args)
    msg = "😂, {} {}".format(choice(rire), user)
    update.message.reply_text(msg)

def alfred(update, context):
    translator = Translator()
    quest = " ".join(context.args)
    cv = ["ça va ?", "ça va?", "Ça va ?", "Ça va?", "Comment ça va?", "Comment ça va ?", "comment ça va ?", "comment ça va?", "cv ?", "cv?"]
    now = datetime.datetime.now()
    msg = ""
    t = ""
    q = [i for i in quest]
    a = "".join(q[:7])
    b = "".join(q[:4])
    if a=="Traduis" or a=="traduis":
        def translate(p):
            translation = translator.detect(p)
            msg = ""
            if translation.lang == 'fr':
                translation = translator.translate(p, dest='en')
                msg = 'On dit : ' + translation.text
                update.message.reply_text(msg)
            elif translation.lang == 'en':
                translation = translator.translate(p, dest='fr')
                msg = 'On dit : ' + translation.text
                update.message.reply_text(msg)
            else:
                msg = "Je ne parle qu'anglais et français, désolé 🙃"
                update.message.reply_text(msg)
        t = quest.replace(a, "")
        translate(t)
    elif b=="spam" or b=="Spam":
        t = quest.replace(b, "")
        mot = ""
        for l in t:
            if l.isdigit() == False:
                mot += l
                t = t.replace(l, "")
        if t.isdigit() == True:
            for i in range (int(t)+1):
                update.message.reply_text(mot)
        else:
            msg = "Veuillez préciser le nombre de spam. 🔢"
            update.message.reply_text(msg)
    else:
        for c in cv:
            if quest == c and q[len(q)-1]=="?":
                translation = translator.translate(now.strftime("%A"), dest='fr')
                repd = "Comme un {}...".format(translation.text)
                rep = ["Très bien et vous {} ? 😁", "Parfaitement bien {}... 😎", "Comme toujours, ça va, et vous {}? 😌", "Eh bien tranquille et vous {}? 😙", repd]
                msg = choice(rep)
                update.message.reply_text(msg.format(update.message.from_user.first_name))
                break
            else:
                msg = "Commande non reconnue 🧐"
                update.message.reply_text(msg)
                break


updater = Updater('630362446:AAFEmPVceIGjYfjbTnRl6o5NHHaTIHuuiEs', use_context=True)

updater.dispatcher.add_handler(CommandHandler('bonjour', bonjour))
updater.dispatcher.add_handler(CommandHandler('service', service))
updater.dispatcher.add_handler(CommandHandler('people', people))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('lien', lien))
updater.dispatcher.add_handler(CommandHandler('laugth', laugth))
updater.dispatcher.add_handler(CommandHandler('botdemerde', botdemerde))
updater.dispatcher.add_handler(CommandHandler('alfred', alfred))
updater.dispatcher.add_handler(CommandHandler('randomfungif', randomfungif))

updater.start_polling()
updater.idle()
