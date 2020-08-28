from rivescript import RiveScript

bot = RiveScript(utf8=True)
bot.load_directory(".")
bot.sort_replies()
def chat(user_id, message):
    if message == '':
        return -1, "No Message to response"
    else:
        response = bot.reply(str(user_id), str(message))
    if response == "":
        return -1, "No Message to response"
    return 0, response