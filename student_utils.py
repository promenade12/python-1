
def parse_student(line):
    line = line.strip()
    if not line:
        raise ValueError("空行")
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误，得到{len(parts)}个字段")
    name, score_str = parts
    name = name.strip()
    if not name:
        raise ValueError("姓名为空")
    score = int(score_str.strip())
    if not (0 <= score <= 100):
        raise ValueError(f"分数{score}超出0‑100范围")
    return {"name": name, "score": score}
