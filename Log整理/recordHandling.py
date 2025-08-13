import re
'''
这个脚本用来处理手动复制下来的QQ聊天记录。
将聊天记录中的时间戳和ID提取出来，并格式化为可读的形式。
'''
# 核心代码
IGNORE_COMMENTS = True # 是否忽略括号中内容
IGNORE_COMMANDS = True # 是否忽略掷骰命令
IDPattern = r'([A-Za-z\u4e00-\u9fa5]+): \d{2}-\d{2} \d{2}:\d{2}:\d{2} '

def process_chat_log(chat_log):
    content = []
    segments = re.split(IDPattern, chat_log)
    for i in range(1, len(segments), 2):
        speaker = segments[i].strip()
        message = segments[i + 1].strip()
        if message.startswith('![]'):
            continue
        if not message:
            message = "(no message)"
        if message.startswith(('(', '（')) and IGNORE_COMMENTS:
            continue
        if message.startswith('.') and IGNORE_COMMANDS:
            continue
        content.append(f"<{speaker}>: {message}")
    return content


with open('处理前记录.md', 'r', encoding='utf-8') as inputFile:
    '''
    文件放同一目录下，文件名记得改成你的聊天记录文件名
    这里假设文件名为 '处理前记录.md'，我使用的Obsidian在复制时会去除换行符，如使用txt格式是不会的。
    使用txt的话换行符可能会多一个，导致每段空2行，自己改代码就行了，但我没测过
    '''
    text = inputFile.read()

with open('处理后记录.md', 'w', encoding='utf-8') as outputFile:
    chat_log = process_chat_log(text)
    for line in chat_log:
        outputFile.write(f"{line}\n\n")



