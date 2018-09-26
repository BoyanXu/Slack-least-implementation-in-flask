class channel_system:
    def __init__(self):
        self.channels = []
        self.chat_history = {}  # {channel_name : message_tuple (user//personal touch) }
        self.personal_touch = {} # {display_name : feature_list}
