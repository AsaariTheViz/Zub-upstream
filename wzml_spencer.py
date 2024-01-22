#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '👨‍💄1�7 OWNER'
    ST_BN1_URL = 'https://t.me/Greg_Simmonds'
    ST_BN2_NAME = '🎲 GROUP'
    ST_BN2_URL = 'https://t.me/amz_leech'
    ST_MSG = '''This bot can Leech all your links|files|torrents to Telegram 📥.\n<b>Type /help to get a list of available commands and Supports</b>\n\n➄1�7 🦊 DevS : @WZML_X'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ....⚡️</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! 💔 \nDeploy your own WZML-X Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✄1�7'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In! ✄1�7</b>'
    INVALID_PASS = '<b>Invalid Password! ❄1�7</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully! ✄1�7</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊄1�7 <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<b><i>BOT STATISTICS 🧮</i></b> \n
<b>⏄1�7 Bot Uptime :</b> {bot_uptime}

┄1�7 <b><i>🎮 RAM ( MEMORY )</i></b>
┄1�7 {ram_bar} {ram}%
┄1�7 <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┄1�7 <b><i>🍃 SWAP MEMORY</i></b>
┄1�7 {swap_bar} {swap}%
┄1�7 <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┄1�7 <b><i>💾 DISK </i></b>
┄1�7 {disk_bar} {disk}%
┄1�7 <b>Total Disk Read :</b> {disk_read}
┄1�7 <b>Total Disk Write :</b> {disk_write}
┄1�7 <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''<b><i>🧩 OS SYSTEM </i></b>
┄1�7 <b>OS Uptime :</b> {os_uptime}
┄1�7 <b>OS Version :</b> {os_version}
┄1�7 <b>OS Arch :</b> {os_arch}

<b><i>🛰︄1�7 NETWORK STATISTICS </i></b>
┄1�7 <b>🔺 Upload Data:</b> {up_data}
┄1�7 <b>🔻 Download Data:</b> {dl_data}
┄1�7 <b>Pkts Sent:</b> {pkt_sent}k
┄1�7 <b>Pkts Received:</b> {pkt_recv}k
┄1�7 <b>Total I/O Data:</b> {tl_data}

┄1�7<i><b>🖥 CPU </b></i>
┄1�7 {cpu_bar} {cpu}%
┄1�7 <b>CPU Frequency :</b> {cpu_freq}
┄1�7 <b>System Avg Load :</b> {sys_load}
┄1�7 <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┄1�7 <b>Total Core(s) :</b> {total_core}
┄1�7 <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''📊 <b><i>REPO STATISTICS :</i></b>
┄1�7 <b>Bot Updated :</b> {last_commit}
┄1�7 <b>Current Version :</b> {bot_version}
┄1�7 <b>Latest Version :</b> {lat_version}
┄1�7 <b>Last ChangeLog :</b> {commit_details}

🧬 <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''<b><i>BOT LIMITATIONS 🚧</i></b>
┄1�7<b>🎯 Direct :</b> <code>{DL} GB</code>
┄1�7<b>🧲 Torrent :</b> <code>{TL} GB</code>
┄1�7<b>☁️ GDrive :</b> <code>{GL} GB</code>
┄1�7<b>📺 YT-DLP :</b> <code>{YL} GB</code>
┄1�7<b>🎥 Playlist :</b> <code>{PL} Videos</code>
┄1�7<b>Ⓜ️ Mega :</b> <code>{ML} GB</code>
┄1�7<b>🎗︄1�7 Clone :</b> <code>{CL} GB</code>
┄1�7<b>📂 Leech :</b> <code>{LL} GB</code>

┄1�7 <b>Token Validity :</b> {TV}
┄1�7 <b>User Time Limit :</b> {UTI} / task
┄1�7 <b>User Parallel Tasks :</b> {UT}
┄1�7 <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting....♻️</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b><i>Restarted Successfully ✄1�7</i></b>
┄1�7 <b>📅 Date:</b> {date}
┄1�7 <b>⌄1�7 Time:</b> {time}
┄1�7 <b>🌍 TimeZone:</b> {timz}
┄1�7 <b>🆔 Version:</b> {version}'''
    RESTARTED = '''<b><i>Bot Restarted! ✄1�7</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping...🌋</i>'
    PING_VALUE = '<b>🎯 Pɪɴɢ: </b><code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    INKS_START = """<b>Task Started...⛓️</b>
┄1�7<b>💠 Mode:</b> {Mode}
┄1�7<b>👤 User:</b> {Tag}\n"""
    LINKS_SOURCE = """┄1�7<b>💡 Source:</b>
┄1�7<b>⏄1�7 Time:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "🧲 <b><u>Task Started :</u></b>\n┄1�7 <b>🏷︄1�7 Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "🧲 <b><u>Leech Started :</u></b>\n┄1�7 <b> User :</b> {mention} ( #ID{uid} )\n┄1�7 <b> Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '┄1�7<b>🏷︄1�7 Name:</b> <code>{Name}</code>\n'
    SIZE =                  '┄1�7<b>💾 Size: </b>{Size}\n'
    ELAPSE =                '┄1�7<b>⌄1�7 Elapsed: </b>{Time}\n'
    MODE =                  '┄1�7<b>🎭 Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┄1�7<b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┄1�7<b>💀 Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '┄1�7<b>👤 User: </b>{Tag}\n'
    PM_BOT_MSG =            '<b><i>File(s) have been Sent above 🎗︄1�7</i></b>'
    L_BOT_MSG =             '<b><i>File(s) have been Sent to Bot PM (Private) 🔐</i></b>'
    L_LL_MSG =              '<b><i>File(s) have been Sent. Access via Links...📎</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┄1�7<b>📜 Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┄1�7<b>🗂︄1�7 SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┄1�7<b>📂 Files: </b>{Files}\n'
    RCPATH =                '┄1�7<b>🚩 Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┄1�7<b>👤 User: </b>{Tag}\n'
    M_BOT_MSG =             '<b><i>Link(s) have been Sent to Bot PM (Private) </i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚄1�7 Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '┄1�7<b>🏷︄1�7 Name:</b> <code>{Name}</code>'
    
    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┄1�7 {Bar}'
    PROCESSED =         '\n┄1�7<b>🚦 Process:</b> {Processed}'
    STATUS =            '\n┄1�7<b>🪬 Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}'
    SPEED =             '\n┄1�7<b>⚄1�7 Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n┄1�7<b>⚙️ Engine:</b> {Engine}'
    STA_MODE =          '\n┄1�7<b>🎭 Mode:</b> {Mode}'
    SEEDERS =           '\n┄1�7 <b>🌾 Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>🪢 Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┄1�7<b>💾 Size:</b> {Size}'
    SEED_SPEED =     '\n┄1�7<b>⚄1�7 Speed:</b> {Speed} | '
    UPLOADED =                                     '<b>📩 Uploaded: </b> {Upload}'
    RATIO =          '\n┄1�7<b>🌀 Ratio:</b> {Ratio} | '
    TIME =                                         '<b>⌄1�7 Time: </b> {Time}'
    SEED_ENGINE =    '\n┄1�7<b>⚙️ Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┄1�7<b>💾 Size:</b> {Size}'
    NON_ENGINE =     '\n┄1�7<b>⚙️ Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┄1�7<b>👤 User:</b> <code>{User}</code> | '
    ID =                                                        '<b>🆔:</b> <code>{Id}</code>'
    BTSEL =          '\n┄1�7<b>✂️ Select:</b> {Btsel}'
    CANCEL =         '\n┄1�7<b>🚫 Stop:</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌄1�7 <b><u>BOT STATS.....</u></b>\n'
    TASKS =  '┄1�7<b>⌄1�7 Tasks:</b> {Tasks}\n'
    BOT_TASKS = '┄1�7<b>⏄1�7 Tasks:</b> {Tasks}/{Ttask} | <b>⚰️ AVL:</b> {Free}\n'
    Cpu = '┄1�7<b>🖥︄1�7 CPU:</b> {cpu}% | '
    FREE =                      '<b>💿 F:</b> {free}'
    Ram = '\n┄1�7<b>🎮 RAM:</b> {ram}% | '
    uptime =                     '<b>🚀 UP:</b> {uptime}'
    DL = '\n┄1�7<b>🔻 DL:</b> {DL}/s | '
    UL =                        '<b>🔺 UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫄1�7'
    REFRESH = '📑 Page: {Page}'
    NEXT = '⫄1�7'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷︄1�7 Name:</b> <code>{content}</code>\n<b>⚠️ This File/Folder is already available in Drive!</b>\n\n<b>📑 List Results:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <code>{LINK}</code>\n\n<b>⏄1�7 Please Wait...</b>'
    COUNT_NAME = '┄1�7<b>🏷︄1�7 Name:</b> <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '┄1�7<b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┄1�7<b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┄1�7<b>🗂︄1�7 SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┄1�7<b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┄1�7<b>👤 User: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Searching:</b> <code>{NAME}</code>'
    LIST_FOUND = '<b>ℹ️ Found {NO} Results For</b> <code>{NAME}</code>'
    LIST_NOT_FOUND = '<b>☹️ No Results Found For</b> <code>{NAME}</code>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''No Active Downloads ! 🗑︄1�7
    
⌄1�7 <u><b>BOT STATS.......</b></u>
┄1�7<b>🖥︄1�7 CPU:</b> {cpu}% | <b>💿 F:</b> {free}
┄1�7<b>🎮 RAM:</b> {ram} | <b>🚀 UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''👽 <b><u>User Settings :</u></b>
        
┄1�7<b>👤 Name :</b> {NAME}
┄1�7<b>🔖 Username :</b> {USERNAME}
┄1�7<b>🆔 ID :</b> <code>{ID}</code>
┄1�7<b>🔮 DC :</b> <code>{DC}</code>
┄1�7<b>🗣︄1�7 Language :</b> <code>{LANG}</code>

🗳︄1�7 <u><b>Available Args:</b></u>
 1�7 <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''🌐 <b><u>Universal Settings : {NAME}</u></b>

┄1�7<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┄1�7<b> Daily Tasks :</b> <code>{DT}</code> per day
┄1�7<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┄1�7<b> User Session :</b> <code>{USESS}</code>
┄1�7<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┄1�7<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┄1�7<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''🏅 <b><u>Mirror/Clone Settings : {NAME}</u></b>

┄1�7<b> RClone Config :</b> <i>{RCLONE}</i>
┄1�7<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┄1�7<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┄1�7<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┄1�7<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┄1�7<b> User TD Mode :</b> <i>{TMODE}</i>
┄1�7<b> Total User TD(s) :</b> <i>{USERTD}</i>
┄1�7<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''🧲 <b><u>Leech Settings for {NAME}</u></b>

┄1�7<b> Daily Leech : </b><code>{DL}</code> per day
┄1�7<b> Leech Type :</b> <i>{LTYPE}</i>
┄1�7<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┄1�7<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┄1�7<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┄1�7<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┄1�7<b> Leech Caption :</b> <code>{LCAPTION}</code>
┄1�7<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┄1�7<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┄1�7<b> Leech Dumps :</b> <code>{LDUMP}</code>
┄1�7<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
