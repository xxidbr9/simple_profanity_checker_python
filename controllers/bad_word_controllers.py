from better_profanity import profanity


def post_new_bad_word(text_list=[{"text": "", "time": ""}]):
    if len(text_list) == 1 and text_list[0]["time"] == "":
        return None, "there is no text"

    data = []

    for dict in text_list:
        for key, val in dict.items():
            is_bad = False
            if key == "text":
                is_bad = profanity.contains_profanity(val)

            if is_bad:
                data.append({"text": dict["text"], "time": dict["time"]})

    return {"texts": data}, None
