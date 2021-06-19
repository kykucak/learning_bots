from aiogram.types import ChatPermissions


def get_read_only_permission():
    permission = ChatPermissions(
        can_send_messages=False,
        can_send_polls=False,
        can_pin_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False
    )
    return permission
