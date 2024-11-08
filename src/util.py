import json
import re
from typing import Optional

def getJson(response: str) -> Optional[dict]:
    # stage 1 检查是否有json代码块
    pattern_1 = r'```json([\s\S]*?)```'
    matches = re.findall(pattern_1, response, re.MULTILINE)
    for match in matches:
        try:
            res = json.loads(match)
        except json.JSONDecodeError:
            continue
        else:
            return res
    
    # stage 2 检查是否有代码块
    pattern_2 = r'```([\s\S]*?)```'
    matches = re.findall(pattern_2, response, re.MULTILINE)
    for match in matches:
        try:
            res = json.loads(match)
        except json.JSONDecodeError:
            continue
        else:
            return res

    # stage 3 检查是否有 {}
    pattern_3 = r'\{[\s\S]*?\}'
    matches = re.findall(pattern_3, response, re.MULTILINE)
    for match in matches:
        try:
            res = json.loads(match)
        except json.JSONDecodeError:
            continue
        else:
            return res

    return None
