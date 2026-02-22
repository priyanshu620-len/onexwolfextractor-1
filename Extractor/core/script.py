import config

# Safe way to get username from config
ADMIN_BOT_USERNAME = getattr(config, "ADMIN_BOT_USERNAME", "YourAdminUsername")

# ------------------------------------------------------------ #

START = f"""
<b><u>👋 Hello {{}} , I'm Txt Extractor Bot at your service. 🤖</u>

To start extracting URLs, simply send /app. 📲

<blockquote><i>🔓 I support over 100+ apps for seamless URL extraction.
📥 After extracting the URLs, you can easily download the videos/pdfs using any of my Uploader Bot.⏬</blockquote></i>

<u>For any queries, contact <a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a></u></b>
"""

APP = f"""
<b><i>👋 Hey there! I'm your Txt Extractor bot!🤖</i>

<blockquote>🚨 If you encounter any issues or can't extract any text file, just contact your 
<a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a>.

💬 Got an app you'd like to add? Feel free to reach out anytime!</blockquote>

<i>👇 Choose an option below and let's get started!</i></b>
"""

UPGRADE = f"""
<b><u>Hey👋, Choose Your Plan Below:-</u>

<i>🆓====FREE PLAN USER====🆓</i>
<blockquote>🔍 Only extract video URLs from APPX & Classplus apks!</blockquote>

<i>🤑====VIP PLAN USER====🤑</i>
<blockquote>🕵🏻‍♀️ Unlimited URL extraction for 1 month only For Few Apks!
❌ Txt-to-Video (Non-DRM) bot is not available in this plan.</blockquote>
<blockquote>💵 Price: ₹800 for 28 days</blockquote>

<i>🦁====PRO PLAN USER====🦁</i>
<blockquote>🔓 Extract URLs of Special Apps!
🔑 Extract only 5 batch URLs/per day without needing any ID or password!
✅ Enjoy Txt-to-Video (Non-DRM) bot with this plan.</blockquote>
<blockquote>💵 Price: ₹1000 for 10 days (or) ₹2000 for 28 days</blockquote>

<i>👑====LEGEND PLAN USER====👑</i>
<blockquote>🗿 Everything Unlimited</blockquote>
<blockquote>🚀 You get separate Non-Drm Bot</blockquote>
<blockquote>💵 Price: ₹2500 for 28 days</blockquote>

<i>Upgrade now and take your experience to the next level! 🚀</i></b>
"""

V = """<b><i>🤑====VIP PLAN USER====🤑</i>
🕵🏻‍♀️ Unlimited URL extraction for 1 month only For Few Apk!
❌ Txt-to-Video (Non-DRM) bot is not available in this plan.</b>
"""

P = """<b><i>🦁====PRO PLAN USER====🦁</i>
🔓 Extract URLs of Special Apps!
🔑 Extract only 5 batches URLs Per Day without needing any ID or password!
✅ Enjoy Txt-to-Video (Non-DRM) bot with this plan.</b>
"""

L = """<b><i>👑====LEGEND PLAN USER====👑</i>
🗿 You Can extract Unlimited Txts
🚀 You get separate Non-Drm Bot</b>
"""

auth = f"""
<b>🎉 Congrats [{{}}](tg://openmessage?user_id={{}}) for gaining access to Txt Extractor Bot! 🎉

<i>You have access to the bot as a:</i>

{{}}

<u><i>🚀 Enjoy your access for {{}} days!</i></u>

If you need any assistance, feel free to contact 
<a href="https://t.me/{ADMIN_BOT_USERNAME}">Admin</a></b>
"""
