import json
import time
from Utils.Helpers import Helpers
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Emotes import Emotes

class Player:
    try:
        config = open('config.json', 'r')
        content = config.read()
    except FileNotFoundError:
        Helpers().create_config()
        config = open('config.json', 'r')
        content = config.read()

    settings = json.loads(content)

    skins_id = Skins().get_skins_id()
    brawlers_id = Characters().get_brawlers_id()

    delivery_type = 0
    ID = 0
    token = None

    emotes_id = Emotes().get_emotes_id()
    pass_tokens = 0
    buyed_count = 0
    buyed_cnt = 0

    trophies = settings['Trophies']
    tickets = settings['Tickets']
    gems = settings['Gems']
    resources = [{'ID': 1, 'Amount': settings['BrawlBoxTokens']}, {'ID': 8, 'Amount': settings['Gold']}, {'ID': 9, 'Amount': settings['BigBoxTokens']}, {'ID': 10, 'Amount': settings['StarPoints']}]
    high_trophies = 0
    trophy_reward = 0
    exp_points = settings['ExperiencePoints']
    profile_icon = 0
    name_color = 0
    selected_brawler = 0
    region = settings['Region']
    content_creator = ""
    name_set = False
    name = 'Guest'
    map_id = 0
    use_gadget = True
    starpower = 76
    gadget = 255
    home_brawler = 0
    home_skin = 0
    leaderboard_type = 0
    leaderboard_is_global = False
    bp_activated = False
    token_doubler = 0
    welcome_msg_viewed = False
    theme_id = settings['ThemeID']
    content_creator_codes = settings['ContentCreatorCodes']
    maintenance_old = settings['Maintenance']
    maintenance_time  = settings['SecondsTillMaintenanceOver']
    patch = settings['Patch']
    patch_url = settings['PatchURL']
    patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")
    update_url = settings['UpdateURL']


    perm = 0
    doubles = [{'trophies': False}, {'boxTokens': False}]

    delivery_items = {}
    box_rewards = {}

    db = None

    battle_tick = 0

    unlocked_skins = []

    selected_skins = {}
    for id in brawlers_id:
        selected_skins.update({f"{id}": 0})

    brawlers_unlocked = [0]

    brawlers_card_id = []
    for x in brawlers_unlocked:
        brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

    brawlers_spg = Cards().get_spg_id()

    def_trophies = 0
    def_high_trophies = 0

    brawlers_trophies = {}
    for x in brawlers_id:
        brawlers_trophies.update({f'{x}': def_trophies})

    brawlers_high_trophies = {}
    for x in brawlers_id:
        brawlers_high_trophies.update({f'{x}': def_high_trophies})

    def_level = 0

    brawlers_level = {}
    for x in brawlers_id:
        brawlers_level.update({f'{x}': def_level})

    def_pp = 0

    brawlers_powerpoints = {}
    for x in brawlers_id:
        brawlers_powerpoints.update({f'{x}': def_pp})


    club_id = 0
    club_role = 0

    message_tick = 0

    clients = {}
    account_ban = False
    ban_reason = ''
    ban_support = True

    acc_maintenance = False
    maintenance_type = 0
    maintenance_text = ''

    donateid = 0
    buyed = []
    
    battle_multiplier = 1
    premium = False
    beta_enabled = False
    first_donate = 0
    
    everyday_buy = 0
    trophies_strike = 0
    bpfree_claimed = []
    bpdonate_claimed = []
    bp_progress = 0
    pass_tokens = 0
    reserve_tokens = 0
    
    
    notifications = {"0": {"NotifID": 81, "NotifIndex": 0, "NotifRead": "true", "NotifTime": 1714401876, "Notiftext": "Есть вопросы?\nПоддержка: @edgesupport_bot\nЭто единственный оффициальный бот.Не верьте фейкам"}}
    
    m_time = int(time.time()) + 604800 


    def __init__(self, device):
        self.device = device


