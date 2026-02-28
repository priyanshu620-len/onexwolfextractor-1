import re
import json
import asyncio
import os
import requests
import aiohttp
import base64
from concurrent.futures import ThreadPoolExecutor
from pyrogram import filters, Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ParseMode
from bs4 import BeautifulSoup

# Local Imports
import config
from Extractor import app
from config import OWNER_ID, CHANNEL_ID
from Extractor.core import script
from Extractor.core.func import subscribe, chk_user
from Extractor.core.utils import forward_to_log
from Extractor.html_converter.bot import handle_txt2html, show_txt2html_help

# Module Imports
from Extractor.modules.appex_v4 import appex_v5_txt
from Extractor.modules.classplus import classplus_txt
from Extractor.modules.pw import pw_login
from Extractor.modules.exampur import exampur_txt
from Extractor.modules.careerwill import career_will
from Extractor.modules.utk import handle_utk_logic
from Extractor.modules.ak import ak_start
from Extractor.modules.mypathshala import my_pathshala_login
from Extractor.modules.khan import khan_login
from Extractor.modules.kdlive import kdlive
from Extractor.modules.iq import handle_iq_logic
from Extractor.modules.getappxotp import send_otpp
from Extractor.modules.findapi import findapis_extract
from Extractor.modules.rg_vikramjeet import rgvikramjeet
from Extractor.modules.adda import adda_command_handler
from Extractor.modules.vision import scrape_vision_ias
from Extractor.modules.enc import *
from Extractor.modules.freecp import *
from Extractor.modules.freeappx import *
from Extractor.modules.freepw import *

# Constants
thumb_path = "Extractor/thumbs/txt-5.jpg"
THREADPOOL = ThreadPoolExecutor(max_workers=2000)

# --- Keyboard Definitions ---

buttons = InlineKeyboardMarkup([
    [InlineKeyboardButton("Lᴏɢɪɴ/Wɪᴛʜᴏᴜᴛ Lᴏɢɪɴ", callback_data="modes_")],
    [
        InlineKeyboardButton("🔍 Fɪɴᴅ Aᴘɪ", callback_data="findapi_"),
        InlineKeyboardButton("📓 Aᴘᴘx Aᴘᴘs", callback_data="appxlist")
    ],
    [InlineKeyboardButton("📝 Tᴇxᴛ ⟷ HTML", callback_data="converter_")]
])

modes_button = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔏 Wɪᴛʜᴏᴜᴛ Lᴏɢɪɴ", callback_data="custom_")],
    [InlineKeyboardButton("🔑 Lᴏɢɪɴ", callback_data="manual_")],
    [InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")]
])

custom_button = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⚡ Pᴡ ⚡", callback_data="pwwp"),
        InlineKeyboardButton("🔮 Aᴘᴘx 🔮", callback_data="appxwp"),
    ],
    [InlineKeyboardButton("🎯 CʟᴀssPʟᴜs 🎯", callback_data="cpwp")],
    [InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_")]
])

button1 = InlineKeyboardMarkup([              
    [
        InlineKeyboardButton("👑 Aᴘɴɪ Kᴀᴋsʜᴀ", callback_data="ak_"),
        InlineKeyboardButton("👑 Aᴅᴅᴀ 𝟸𝟺𝟽", callback_data="adda_")
    ],
    [
        InlineKeyboardButton("👑 CʟᴀssPʟᴜs", callback_data="classplus_"),
        InlineKeyboardButton("👑 Kʜᴀɴ Gs", callback_data="khan_")
    ],
    [
        InlineKeyboardButton("👑 Pʜʏsɪᴄs Wᴀʟʟᴀʜ", callback_data="pw_"),
        InlineKeyboardButton("👑 Sᴛᴜᴅʏ IQ", callback_data="iq_")
    ],
    [
        InlineKeyboardButton("👑 Kᴅ Cᴀᴍᴘᴜs", callback_data="kdlive_"),
        InlineKeyboardButton("👑 Uᴛᴋᴀʀsʜ", callback_data="utkarsh_")
    ],
    [
        InlineKeyboardButton("👑 Mʏ Pᴀᴛʜsʜᴀʟᴀ", callback_data="my_pathshala_"),
        InlineKeyboardButton("👑 ExᴀᴍPᴜʀ", callback_data="exampur_txt")
    ],
    [
        InlineKeyboardButton("👑 Vɪsɪᴏɴ Iᴀs", callback_data="vision_ias_"),
        InlineKeyboardButton("👑 Rᴀɴᴋᴇʀs Gᴜʀᴜᴋᴜʟ", callback_data="maintainer_")
    ],
    [InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_")]
])

# --- Helper Functions ---

def get_photo():
    return getattr(config, "THUMB_URL", None)

def get_alphabet_keyboard():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    keyboard = []
    row = []
    for letter in alphabet:
        row.append(InlineKeyboardButton(f"{letter}", callback_data=f"alpha_{letter}"))
        if len(row) == 7:
            keyboard.append(row)
            row = []
    if row: keyboard.append(row)
    keyboard.append([InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")])
    return InlineKeyboardMarkup(keyboard)

def get_apps_by_letter(letter):
    try:
        with open('appxapis.json', 'r', encoding='utf-8') as f:
            apps = json.load(f)
        filtered = [app for app in apps if app['name'].upper().startswith(letter)]
        filtered.sort(key=lambda x: x['name'])
        return filtered
    except: return []

def create_app_keyboard(apps, page=0, letter=None):
    keyboard = []
    row = []
    items_per_page = 40
    total_pages = (len(apps) + items_per_page - 1) // items_per_page
    start_idx = page * items_per_page
    current_apps = apps[start_idx:start_idx + items_per_page]
    
    for app_item in current_apps:
        name = app_item['name']
        styled_name = name.replace("api", "").replace("Api", "").strip().capitalize()
        row.append(InlineKeyboardButton(f"👑 {styled_name}", callback_data=f"app_{name}"))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        if len(row) == 1: row.append(InlineKeyboardButton(" ", callback_data="ignore"))
        keyboard.append(row)
    
    nav_row = []
    if page > 0: nav_row.append(InlineKeyboardButton("« Prev", callback_data=f"page_{letter}_{page-1}"))
    nav_row.append(InlineKeyboardButton("« 𝐁𝐚𝐜𝐤 »", callback_data="appxlist"))
    if page < total_pages - 1: nav_row.append(InlineKeyboardButton("Next »", callback_data=f"page_{letter}_{page+1}"))
    keyboard.append(nav_row)
    return keyboard, total_pages

def deobfuscate_url(encoded_url):
    try:
        decoded = base64.b64decode(encoded_url.encode()).decode()
        decoded = base64.b64decode(decoded.encode()).decode()
        return decoded[8:]
    except: return encoded_url

# --- Main Handlers ---

@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    join = await subscribe(_, message)
    if join == 1: return
    
    caption = script.START_TXT.format(message.from_user.mention)
    try:
        if get_photo():
            await message.reply_photo(photo=get_photo(), caption=caption, reply_markup=buttons)
        else:
            await message.reply_text(caption, reply_markup=buttons)
    except:
        await message.reply_text(caption, reply_markup=buttons)

@app.on_callback_query()
async def handle_callback_query(client, query):
    data = query.data
    mention = query.from_user.mention

    if data == "home_":
        await query.message.edit_text(script.START_TXT.format(mention), reply_markup=buttons)
    
    elif data == "modes_":
        await query.message.edit_text(script.MODES_TXT, reply_markup=modes_button)
        
    elif data == "custom_":        
        await query.message.edit_text(script.CUSTOM_TXT, reply_markup=custom_button)
        
    elif data == "manual_":        
        await query.message.edit_text(script.MANUAL_TXT, reply_markup=button1)

    elif data == "appxlist":
        await query.message.edit_text("𝐒𝐞𝐥𝐞𝐜𝐭 𝐀 𝐋𝐞𝐭𝐭𝐞𝐫 𝐓𝐨 𝐕𝐢𝐞𝐰 𝐀𝐩𝐩𝐬 ✨", reply_markup=get_alphabet_keyboard())

    elif data.startswith("alpha_"):
        letter = data.split("_")[1]
        apps = get_apps_by_letter(letter)
        if not apps:
            await query.answer(f"No apps found for {letter}", show_alert=True)
            return
        keyboard, total_pages = create_app_keyboard(apps, 0, letter)
        await query.message.edit_text(f"📱 Apps: {letter} (1/{total_pages})", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("page_"):
        _, letter, page = data.split("_")
        apps = get_apps_by_letter(letter)
        keyboard, total_pages = create_app_keyboard(apps, int(page), letter)
        await query.message.edit_text(f"📱 Apps: {letter} ({int(page)+1}/{total_pages})", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("app_"):
        app_name = data.split("_")[1]
        try:
            with open('appxapis.json', 'r', encoding='utf-8') as f:
                apps = json.load(f)
            selected = next((a for a in apps if a['name'] == app_name), None)
            if selected:
                api = selected['api'].replace("https://", "").replace("http://", "")
                await appex_v5_txt(client, query.message, api, selected['name'])
        except Exception as e:
            await query.answer(f"Error: {str(e)}", show_alert=True)

    # Coaching Callbacks
    elif data == "pwwp": await process_pwwp(client, query.message, query.from_user.id)
    elif data == "appxwp": await process_appxwp(client, query.message, query.from_user.id)
    elif data == "cpwp": await process_cpwp(client, query.message, query.from_user.id)
    elif data == "pw_": await pw_login(client, query.message)
    elif data == "classplus_": await classplus_txt(client, query.message)
    elif data == "ak_": await ak_start(client, query.message)
    elif data == "utkarsh_": await handle_utk_logic(client, query.message)
    elif data == "maintainer_": await query.answer("This feature is under development", show_alert=True)
    elif data == "converter_":
        await query.message.edit_text("🔄 **File Conversion Tools**", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 Tᴇxᴛ ᴛᴏ HTML", callback_data="txt2html_"), InlineKeyboardButton("📄 HTML ᴛᴏ Tᴇxᴛ", callback_data="html2txt_")],
            [InlineKeyboardButton("𝐁 𝐀 𝐂 Ｋ", callback_data="home_")]
        ]))
    elif data == "txt2html_": await show_txt2html_help(client, query.message)
    elif data == "ignore": await query.answer()

@app.on_message(filters.command("txt2html"))
async def txt2html_cmd(client, message):
    await show_txt2html_help(client, message)

@app.on_message(filters.private & filters.document)
async def handle_document(client, message):
    if message.document.file_name.endswith('.txt'):
        await handle_txt2html(client, message)
    elif message.document.file_name.endswith('.html'):
        # Add your html2txt logic call here if needed
        pass
