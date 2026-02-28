import config

# Safe way to get username from config
ADMIN_BOT_USERNAME = getattr(config, "ADMIN_BOT_USERNAME", "YourAdminUsername")

class script(object):
    # Renamed START to START_TXT to match your start.py
    START_TXT = f"""
<b><u>👋 Hello {{}} , I'm Txt Extractor Bot at your service. 🤖</u>

To start extracting URLs, simply send /app. 📲

<blockquote><i>🔓 I support over 100+ apps for seamless URL extraction.
📥 After extracting the URLs, you can easily download the videos/pdfs using any of my Uploader Bot.⏬</blockquote></i>

<u>For any queries, contact <a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a></u></b>
"""

    # Renamed APP to MANUAL_TXT and MODES_TXT to satisfy the callback handlers
    MANUAL_TXT = f"""
<b><i>👋 Hey there! I'm your Txt Extractor bot!🤖</i>

<blockquote>🚨 If you encounter any issues or can't extract any text file, just contact your 
<a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a>.

💬 Got an app you'd like to add? Feel free to reach out anytime!</blockquote>

<i>👇 Choose an option below and let's get started!</i></b>
"""

    MODES_TXT = "<b>Select the extraction mode below:</b>"
    
    CUSTOM_TXT = "<b>Choose a custom extraction method:</b>"

    UPGRADE = f"""
<b><u>Hey👋, Choose Your Plan Below:-</u>

<i>🆓====FREE PLAN USER====🆓</i>
<blockquote>🔍 Only extract video URLs from APPX & Classplus apks!</blockquote>

... (rest of your upgrade text)"""

    # Adding other variables for completeness
    V = "..." 
    P = "..."
    L = "..."
    AUTH = "..." # etc.
