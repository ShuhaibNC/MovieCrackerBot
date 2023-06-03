import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
import requests
import bs4
import random
import json

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == "private":
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
                f"<b>ꜰɪʀꜱᴛɴᴀᴍᴇ: </b> {first}\n<b>ʟᴀꜱᴛɴᴀᴍᴇ: </b> {last}\n<b>ᴜꜱᴇʀɴᴀᴍᴇ: </b> {username}\n<b>ɪᴅ: </b> <code>{user_id}</code>\n<b>ᴅᴀᴛᴀᴄᴇɴᴛᴇʀ: </b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += (
                "<b>ᴄʜᴀᴛ ɪᴅ: </b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                    "<b>ᴜꜱᴇʀ ɪᴅ:</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>ʀᴇᴩʟɪᴇᴅ ᴜꜱᴇʀ ɪᴅ: </b>: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                    "<b>ᴜꜱᴇʀ ɪᴅ: </b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )
        
def msonescrap(query, key):
    resultlist = []
    if " " in query:
        query = query.replace(' ', '+')
    resp = requests.get('https://malayalamsubtitles.org/?s='+query)
    soup = bs4.BeautifulSoup(resp.content, 'html.parser')
    if key == 'link':
        title_links = soup.find_all('a', class_='entry-title-link')
        for links in title_links:
            resultlist.append(links['href'])
        if not resultlist:
            return 'Nothing'
        else: return resultlist
    elif key == 'title':
        total_titles = soup.find_all('a', class_='entry-title-link')
        for titles in total_titles:
            resultlist.append(titles.get_text())
        if not resultlist:
            return 'Nothing'
        else:
            return resultlist
            
@Client.on_message(filters.command('msone') & filters.incoming)
async def msone(client, message):
    if len(message.command) < 2:
        return await message.reply('<b>Example:</b>\n<code>/msone Triangle</code>')
    res = await message.reply('Searching...', quote=True)
    cmd = message.text.split(' ', 1)[1]
    buttons = []
    names = msonescrap(cmd, 'title')
    links = msonescrap(cmd, 'link')
    if names == 'Nothing' or links == 'Nothing':
        return await res.edit('No results found.')
    i = 0
    bu_list = []
    while i < len(names):
        if names[i] in bu_list:
            i += 1
            pass
        else:
            buttons.append([InlineKeyboardButton(names[i], url= links[i])])
            bu_list.append(names[i])
            i += 1
    buttons.append([InlineKeyboardButton('❌ CLOSE', callback_data='close')])
    markup = InlineKeyboardMarkup(buttons)
    await res.edit('Here is your result.', reply_markup=markup)
    
def catimage():
    image = ["https://i.imgur.com/IwRre0V.png","https://i.imgur.com/4aZlMPa.png","https://i.imgur.com/EEp2jtQ.png","https://i.imgur.com/ea7Ivps.png","https://i.imgur.com/CxouTiT.png","https://i.imgur.com/5ib8lL0.png","https://i.imgur.com/YhGnwKA.png","https://i.imgur.com/K8GphFQ.png","https://i.imgur.com/zrB3kwI.png","https://i.imgur.com/d4y82hH.png","https://i.imgur.com/lHZqKzi.png","https://i.imgur.com/dhuQljI.png","https://i.imgur.com/AXgK9eq.png","https://i.imgur.com/hbPAhtC.png","https://i.imgur.com/WZbiZJv.png","https://i.imgur.com/FCxTtOf.png","https://i.imgur.com/d4m4Grt.png","https://i.imgur.com/1gsmfoh.png","https://i.imgur.com/RKct0Qx.png","https://i.imgur.com/u4c59Fi.png","https://i.imgur.com/EYGlGQ7.png","https://i.imgur.com/JXiyghi.png","https://i.imgur.com/3WrDGrT.png","https://i.imgur.com/D3oeEc7.png","https://i.imgur.com/gnbOZIm.png","https://i.imgur.com/KPWWwvg.png","https://i.imgur.com/djmZiiV.png","https://i.imgur.com/pPlciN9.png","https://i.imgur.com/DZ8s0tR.png","https://i.imgur.com/s8NrwYk.png","https://i.imgur.com/s1RThQw.png","https://i.imgur.com/SiYCWY7.png","https://i.imgur.com/IF2ekZa.png","https://i.imgur.com/GqKwRlX.png","https://i.imgur.com/U5mWKSp.png","https://i.imgur.com/WkpTKit.png","https://i.imgur.com/3zssaMs.png","https://i.imgur.com/jvGOTYd.png","https://i.imgur.com/JBLdvSZ.png","https://i.imgur.com/7EN3mgz.png","https://i.imgur.com/sPQuJs4.png","https://i.imgur.com/1ASWQxy.png","https://i.imgur.com/k4sWdfU.png","https://i.imgur.com/cSujnZV.png","https://i.imgur.com/eF8ISdD.png","https://i.imgur.com/njxqsOx.png","https://i.imgur.com/ler9KmL.png","https://i.imgur.com/T5TDRf6.png","https://i.imgur.com/qf0Bh1S.png","https://i.imgur.com/BGakdjq.png","https://i.imgur.com/8yGY3uS.png","https://i.imgur.com/aNTZCgC.png","https://i.imgur.com/EaHQ3AJ.png","https://i.imgur.com/d1NKF7O.png","https://i.imgur.com/jnqHifF.png","https://i.imgur.com/2Ijm2qT.png","https://i.imgur.com/p94EP8r.png","https://i.imgur.com/TE3W4Mf.png","https://i.imgur.com/qMmZihq.png","https://i.imgur.com/RmltsiH.png","https://i.imgur.com/90X0ddu.png","https://i.imgur.com/yCM0LP3.png","https://i.imgur.com/K7lbNGj.png","https://i.imgur.com/TQZ7j77.png","https://i.imgur.com/bSTtPCC.png","https://i.imgur.com/jdl5vKy.png","https://i.imgur.com/0mkRAP2.png","https://i.imgur.com/vzWxTvr.png","https://i.imgur.com/E9daLGv.png","https://i.imgur.com/jKZUDfL.png","https://i.imgur.com/5vWvYfa.png","https://i.imgur.com/uMdaz5r.png","https://i.imgur.com/XpbV257.png","https://i.imgur.com/oNqBGLp.png","https://i.imgur.com/ksAR3IL.png","https://i.imgur.com/ixX65pT.png","https://i.imgur.com/ajgWdon.png","https://i.imgur.com/lbsHbJ2.png","https://i.imgur.com/OVJwKxB.png","https://i.imgur.com/UAuh6f5.png","https://i.imgur.com/zZPmOVS.png","https://i.imgur.com/WrjPpll.png","https://i.imgur.com/mKkfT5E.png","https://i.imgur.com/VOxAgdp.png","https://i.imgur.com/mR2bzw3.png","https://i.imgur.com/btEL6vw.png","https://i.imgur.com/oMA8Ww0.png","https://i.imgur.com/9jdcZRE.png","https://i.imgur.com/D472YrP.png","https://i.imgur.com/r6siMkJ.png","https://i.imgur.com/vUGwffT.png","https://i.imgur.com/EwFCsSt.png","https://i.imgur.com/veRARwD.png","https://i.imgur.com/HvdKI9R.png","https://i.imgur.com/XxJMwJE.png","https://i.imgur.com/TY2oiBR.png","https://i.imgur.com/LBif5wP.png","https://i.imgur.com/P7c3W9t.png","https://i.imgur.com/rVHg3Hz.png","https://i.imgur.com/ifrz9SL.png","https://i.imgur.com/TQGlu9y.png","https://i.imgur.com/eVGeRZn.png","https://i.imgur.com/K8Ovc2z.png","https://i.imgur.com/fHFFJQy.png","https://i.imgur.com/zhyzNyv.png","https://i.imgur.com/UwL7F78.png","https://i.imgur.com/w8eBYBq.png","https://i.imgur.com/mHi6BOk.png","https://i.imgur.com/JNsII8N.png","https://i.imgur.com/A3DcUzf.png","https://i.imgur.com/JnN8ijm.png","https://i.imgur.com/R8oLzFu.png","https://i.imgur.com/LWkQl8D.png","https://i.imgur.com/8YBKGt2.png","https://i.imgur.com/Oxt5xmg.png","https://i.imgur.com/9uKkH32.png","https://i.imgur.com/szmSQVV.png","https://i.imgur.com/hUsX3Ug.png","https://i.imgur.com/Jw9vOER.png","https://i.imgur.com/vjXHkJO.png","https://i.imgur.com/qMNS8ha.png","https://i.imgur.com/pepHYFI.png","https://i.imgur.com/KAqvYIP.png","https://i.imgur.com/2cOlHuI.png","https://i.imgur.com/4rWRqY9.png","https://i.imgur.com/y5lcVfN.png","https://i.imgur.com/ZADqXhQ.png","https://i.imgur.com/9j1JAW8.png","https://i.imgur.com/7xuVIZd.png","https://i.imgur.com/xEweZ9B.png","https://i.imgur.com/38EUjgJ.png","https://i.imgur.com/gekyrOS.png","https://i.imgur.com/5lqo6sg.png","https://i.imgur.com/QHZV150.png","https://i.imgur.com/9QXYxAt.png","https://i.imgur.com/vJFtYnY.png","https://i.imgur.com/FdyYRCM.png","https://i.imgur.com/ksKqA0a.png","https://i.imgur.com/18q5PYJ.png","https://i.imgur.com/1X4TVTv.png","https://i.imgur.com/bbLvCyz.png","https://i.imgur.com/iyd0yLW.png","https://i.imgur.com/DV92HR3.png","https://i.imgur.com/XiQO6gS.png","https://i.imgur.com/qEUMl9k.png","https://i.imgur.com/PwV3oA9.png","https://i.imgur.com/CK54Lpz.png","https://i.imgur.com/3Lbkw8v.png","https://i.imgur.com/VwTxVS2.png","https://i.imgur.com/v2pqqqf.png","https://i.imgur.com/WEqJddT.png","https://i.imgur.com/r2lDxqz.png","https://i.imgur.com/OzWRLde.png","https://i.imgur.com/PzvZSOS.png","https://i.imgur.com/KeIkeVy.png","https://i.imgur.com/9eZl8eU.png","https://i.imgur.com/MOWSuzE.png","https://i.imgur.com/zFjUk40.png","https://i.imgur.com/YS5CGEb.png","https://i.imgur.com/1k4Eji9.png","https://i.imgur.com/6YOFVkN.png","https://i.imgur.com/BaJD6Uq.png","https://i.imgur.com/o7yKPLM.png","https://i.imgur.com/610E0Bp.png","https://i.imgur.com/dGS6xm3.png","https://i.imgur.com/nqLeyqk.png","https://i.imgur.com/c1TEOsZ.png","https://i.imgur.com/7lwyzdf.png","https://i.imgur.com/Dm5v9vJ.png","https://i.imgur.com/kLFLXoY.png","https://i.imgur.com/8aame6S.png","https://i.imgur.com/sFdxoeV.png","https://i.imgur.com/uEOCCv5.png","https://i.imgur.com/vHUhZdD.png","https://i.imgur.com/KLSuEGi.png","https://i.imgur.com/rOuLKHi.png","https://i.imgur.com/Gm8ziKT.png","https://i.imgur.com/IMAppGQ.png","https://i.imgur.com/6neYZeB.png"]
    choice = random.choice(image)
    return choice
def eemoji(text):
    url = 'https://levanter.onrender.com/emoji?q='
    respo = requests.get(url + text)
    image = json.loads(respo.content)
    
    return image['url']
    
def emix(text):
    url = 'https://levanter.onrender.com/emix?q='
    response = requests.get(url+text)
    data = json.loads(response.content)
    return data['result']
    
def get_thanosquote():
    thanos_quotes = [
    "Reality is often disappointing.",
    "I am inevitable.",
    "You're not the only one cursed with knowledge.",
    "Dread it. Run from it. Destiny still arrives.",
    "The hardest choices require the strongest wills.",
    "I ignored my destiny once, I can not do that again.",
    "The universe required correction. After that, the stones served no purpose beyond temptation.",
    "I thought by eliminating half of life, the other half would thrive, but you have shown me... that's impossible.",
    "The work is done. I won. What I'm about to do, I'm gonna enjoy it. Very, very much.",
    "Fun isn't something one considers when balancing the universe. But this... does put a smile on my face.",
]
    return random.choice(thanos_quotes)
    
    
@Client.on_message(filters.command('thanos') & filters.incoming)
async def thanos(client, message):
    await message.reply('<b>'+get_thanosquote()+'</b>')
    
    
@Client.on_message(filters.command('emoji') & filters.incoming)
async def cmdemoji(client, message):
    if len(message.command) < 2:
        return await message.reply('Example:\n<code>/emoji 🌚</code>')
    text = message.command[1]
    #text : Message = await client.listen(message.chat.id)
    await message.reply_photo(photo=eemoji(text))
    
@Client.on_message(filters.command('emix') & filters.incoming)
async def myemix(client, message):
    if len(message.command) < 2:
        return await message.reply('Example:\n<code>/emix 😁😄</code>')
    text = message.command[1]
    await message.reply_photo(photo=emix(text))
    
    
@Client.on_message(filters.command('cat') & filters.incoming)
async def cat(client, message):
    await message.reply_photo(photo=catimage())
    

@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info... 🌚`"
    )
    await status_message.edit(
        "`Processing user info... ✨️`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>➲First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>➲Last Name:</b> {last_name}\n"
    message_out_str += f"<b>➲Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesnt Have A Valid DP]"
    message_out_str += f"<b>➲Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>➲User Name:</b> @{username}\n"
    message_out_str += f"<b>➲User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in (("supergroup", "channel")):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode="html",
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode="html",
            disable_notification=True
        )
    await status_message.delete()

@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('Searching in IMDB')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("No results Found")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('Here is what i found on IMDb', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('Give me a movie / series Name')

@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, query: CallbackQuery):
    i, movie = query.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')}",
                    url=imdb['url'],
                )
            ]
        ]
    if imdb:
        caption = IMDB_TEMPLATE.format(
            query = imdb['title'],
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url']
        )
    else:
        caption = "No Results"
    if imdb.get('poster'):
        try:
            await query.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await query.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        except Exception as e:
            logger.exception(e)
            await query.message.reply(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
        await query.message.delete()
    else:
        await query.message.edit(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
    await query.answer()
        

        
