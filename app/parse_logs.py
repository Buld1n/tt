import re
from datetime import datetime
from . import db
from .models import Message, Log


def parse_log_line(line):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\S+) (\S+) (\S+) (.*)'
    match = re.match(pattern, line)
    if match:
        timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
        int_id = match.group(2)
        flag = match.group(3)
        address = match.group(4) if flag in ('<=', '=>', '->', '**', '==') else None
        remaining_str = match.group(5)
        return timestamp, int_id, flag, address, remaining_str
    return None


def process_logs(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if parsed_line:
                timestamp, int_id, flag, address, remaining_str = parsed_line
                if flag == '<=':
                    message_id_match = re.search(r'id=(\S+)', remaining_str)
                    message_id = message_id_match.group(1) if message_id_match else None
                    if message_id:
                        message = Message(
                            created=timestamp,
                            id=message_id,
                            int_id=int_id,
                            str=line[len(line.split(' ', 3)[0]) + 1:],
                        )
                        db.session.add(message)
                else:
                    log_entry = Log(
                        created=timestamp,
                        int_id=int_id,
                        str=line[len(line.split(' ', 3)[0]) + 1:],
                        address=address
                    )
                    db.session.add(log_entry)

        db.session.commit()
