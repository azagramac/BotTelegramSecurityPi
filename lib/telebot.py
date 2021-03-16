import collections
import telepot

class Telebot(telepot.Bot):
 
    def __init__(self, token_id, chat_id):
        super().__init__(token_id)
        self._handle = collections.defaultdict(list)
        self.message_loop(self._postreceive)
        self.chat_id = chat_id
        self.command = None
        self._is_listen = False

    @property
    def is_listen(self):
        return bool(self._is_listen)

    @is_listen.setter
    def is_listen(self, status):
        self._is_listen = status

    def handler(self, cmd):
        def decorator(func):
            self._handle[cmd].append(func)
            return func

        return decorator

    def _get_args(self):
        args = self.command.split()
        self.command = args[0]
        return tuple(args[1:])

    def _authorized_chat_id(self, incoming_chat_id):
        return bool(int(self.chat_id) == int(incoming_chat_id))

    def _postreceive(self, msg):
        incoming_chat_id = msg['chat']['id']
        self.command = msg['text']
        if self._authorized_chat_id(incoming_chat_id):
            args = self._get_args()
            for handle in self._handle.get(self.command, []):
                return handle(*args)
        return None

    def send_photo(self, file, msg):
        with open(file, 'rb') as photo_file:
            self.sendPhoto(self.chat_id, photo=photo_file, caption=msg)

    def send_message(self, msg):
        self.sendMessage(self.chat_id, str(msg))

    def send_video(self, video, msg):
        if video["return_code"] is None:
            with open(video["name"], 'rb') as video_file:
                super().sendVideo(self.chat_id, video=video_file, caption=msg)
        else:
            super().sendMessage(self.chat_id, video["return_code"])