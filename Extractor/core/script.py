import config

# Safe way to get username from config
ADMIN_BOT_USERNAME = getattr(config, "ADMIN_BOT_USERNAME", "YourAdminUsername")

class script(object):
    # We use a regular string here so .format() in start.py works correctly
    START_TXT = f"""
<b><u>👋 Hello {{}} , I'm Txt Extractor Bot at your service. 🤖</u>

To start extracting URLs, simply send /app. 📲

<blockquote><i>🔓 I support over 100+ apps for seamless URL extraction.
📥 After extracting the URLs, you can easily download the videos/pdfs using any of my Uploader Bot.⏬</blockquote></i>

<u>For any queries, contact <a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a></u></b>
"""

    # These are needed for your button callbacks
    MODES_TXT = "<b>Please select the extraction mode you want to use below:</b>"
    
    CUSTOM_TXT = "<b>Select a direct extraction method (No login required):</b>"

    MANUAL_TXT = f"""
<b><i>👋 Hey there! I'm your Txt Extractor bot!🤖</i>

<blockquote>🚨 If you encounter any issues or can't extract any text file, just contact your 
<a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a>.

💬 Got an app you'd like to add? Feel free to reach out anytime!</blockquote>

<i>👇 Choose an option below and let's get started!</i></b>
"""

    UPGRADE = """
<b><u>Hey👋, Choose Your Plan Below:-</u></b>
<i>Contact Admin for premium features.</i>
"""
