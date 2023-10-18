from os import getenv
from dotenv import load_dotenv

load_dotenv()

""" General config """
ENV = getenv("ENV")  # set this only in prod environment
TZ_OFFSET = 8.0  # (UTC+08:00)
JOB_LIMIT_PER_PERSON = 10

""" Telegram config """

# configuration
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
BOTHOST = getenv("BOTHOST")  # only required in prod environment

# custom messages
start_message = "*Terima kasih telah menggunakan Bot Pesan Berulang\!*\n\nUntuk memulai, beri tahu saya zona waktu Anda dalam satuan UTC\. Misalnya, jika zona waktu Anda adalah UTC\+08:30, masukkan \+08:30\.\n\n\(geser ke kiri untuk membalas pesan ini\)"
help_message = "Saya dapat membantu Anda menjadwalkan pesan berulang menggunakan <a href='https://crontab.guru/'>cron schedule expressions</a> (min. interval 1 menit).\n\n<b>Perintah yang tersedia</b>\n/add - menambahkan pekerjaan baru\n/list - daftar pekerjaan yang sedang berjalan\n/delete - menghapus pekerjaan\n/options - melihat opsi pekerjaan lanjutan\n/checkcron - memeriksa validitas/makna ekspresi cron\n\n<b>Menemukan bug?</b>\nSilakan hubungi pemilik bot di https://t.me/bukankenjan."  # html
delete_message = "Hai, beri tahu saya nama pekerjaan yang ingin Anda hapus. Kirim /list untuk melihat pekerjaan yang tersedia.\n\n(geser ke kiri untuk membalas pesan ini)"
request_jobname_message = (
    "Berikan NAMA untuk pekerjaan Anda\n\n(geser ke kiri untuk membalas pesan ini)"
)
request_crontab_message = "Berikan saya ekspresi jadwal cron Anda (mis. 4 5 * * *), tekan disini <a href='https://crontab.guru/'>here</a> jika butuh bantuan. Use /checkcron to check your cron expression.\n\n(swipe left to reply to this message)"  # html
request_text_message = (
    "Now give me what you want to send\n\n(swipe left to reply to this message)"
)
simple_prompt_message = "\/add to create a new job"
prompt_new_job_message = "The job already got this field\. Please \/add and create a new job\. If you want to override, \/delete job and create again\."
invalid_new_job_message = "A job with this name already exists\. Please \/add and create a new job\. If you want to override, \/delete job and create again\."
confirm_message_prepend = "Ok. Done. Added."
confirm_message_append = "To set advanced options, please use /options."
invalid_crontab_message = "This expression is invalid. Please provide a valid expression. Click <a href='https://crontab.guru/'>here</a> if you need help. Use /checkcron to check your cron expression."  # html
list_jobs_message = "Hey, choose the job you are interested to know more about. The jobs are listed on the reply keyboard.\n\n(swipe left to reply to this message)"
delete_success_message = "Yeet! This job is now gone."
error_message = "You know that's not right..."
checkcron_message = "Hey, send me your cron expression, I'll decrypt it for you.\n\n(swipe left to reply to this message)"
checkcron_invalid_message = "Alright, that's not a valid cron. Click <a href='https://crontab.guru/'>here</a> if you need help."
checkcron_meaning_message = "Ok, that means: "
list_options_message = "Currently I only have one advanced option available LOL.\n\n/deleteprevious - Delete the previous message when the next message is sent. Ensures that only one message per job is in the chat at a time. Disabled by default. Note that this option is subject to the limitations mentioned in the <a href='https://core.telegram.org/bots/api#deletemessage'>Telegram API documentation</a>.\n\nTo request for a new feature, please contact the bot owner at hs.develops.1@gmail.com.\n\n<b>Enjoying the bot?</b>\nYou can <a href='https://www.buymeacoffee.com/rmteam'>buy the RM team a coffee</a>!"  # html
option_delete_previous_message = "Tell me the name of the job you want to toggle the /deleteprevious option for. The jobs are listed on the reply keyboard.\n\n(swipe left to reply to this message)"
exceed_limit_error_message = (
    "Recurring Messages currently only supports %d jobs per person, in an effort to reduce spam.\n\nIf you need to create more than %d jobs, please contact the bot owner at hs.develops.1@gmail.com specifying:\n1. the number of jobs you need, and\n2. your Telegram handle.\n\n<b>Enjoying the bot?</b>\nYou can <a href='https://www.buymeacoffee.com/rmteam'>buy the RM team a coffee</a>!"
    % (JOB_LIMIT_PER_PERSON, JOB_LIMIT_PER_PERSON)
)  # html

""" GSheets config """
# Create the Google Sheet manually. Set all values as plain text format.
# Remember to share the Google Sheet with SERVICE_ACCOUNT_INFO_CLIENT_EMAIL

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
GSHEET_ID = getenv("GSHEET_ID")  # can be found in the gsheet's url
JOB_DATA_SHEETNAME = (
    "job data"  # depends on what you name your sheet, defaults to Sheet1.
)
CHAT_DATA_SHEETNAME = (
    "chat data"  # depends on what you name your sheet, defaults to Sheet2.
)
USER_DATA_SHEETNAME = (
    "user data"  # depends on what you name your sheet, defaults to Sheet3.
)
USER_WHITELIST_SHEETNAME = (
    "whitelist"  # depends on what you name your sheet, defaults to Sheet4.
)


# To use Google Sheets API,
# create a google cloud project: https://developers.google.com/workspace/guides/create-project
# create service account credentials: https://developers.google.com/workspace/guides/create-credentials#service-account
if ENV:
    SERVICE_ACCOUNT_INFO_TYPE = getenv("SERVICE_ACCOUNT_INFO_TYPE")
    SERVICE_ACCOUNT_INFO_PROJECT_ID = getenv("SERVICE_ACCOUNT_INFO_PROJECT_ID")
    SERVICE_ACCOUNT_INFO_PRIVATE_KEY_ID = getenv("SERVICE_ACCOUNT_INFO_PRIVATE_KEY_ID")
    SERVICE_ACCOUNT_INFO_PRIVATE_KEY = getenv(
        "SERVICE_ACCOUNT_INFO_PRIVATE_KEY"
    ).replace("\\n", "\n")
    SERVICE_ACCOUNT_INFO_CLIENT_EMAIL = getenv("SERVICE_ACCOUNT_INFO_CLIENT_EMAIL")
    SERVICE_ACCOUNT_INFO_CLIENT_ID = getenv("SERVICE_ACCOUNT_INFO_CLIENT_ID")
    SERVICE_ACCOUNT_INFO_AUTH_URI = getenv("SERVICE_ACCOUNT_INFO_AUTH_URI")
    SERVICE_ACCOUNT_INFO_TOKEN_URI = getenv("SERVICE_ACCOUNT_INFO_TOKEN_URI")
    SERVICE_ACCOUNT_INFO_AUTH_PROVIDER_X509_CERT_URL = getenv(
        "SERVICE_ACCOUNT_INFO_AUTH_PROVIDER_X509_CERT_URL"
    )
    SERVICE_ACCOUNT_INFO_CLIENT_X509_CERT_URL = getenv(
        "SERVICE_ACCOUNT_INFO_CLIENT_X509_CERT_URL"
    )
