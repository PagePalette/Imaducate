import openai
import conf


def translate(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        api_key=conf.API_KEY,
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You will be provided with a sentence in Korean, and your task is to translate it into English."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=256
    ).choices[0].message.content
    print(response)
    return response


def gen_img(prompt: str, w: int = 512, h: int = 512) -> str:
    if conf.MODE == conf.TEST_MODE:
        return "https://dummyimage.com/512x512/000/fff"

    response = openai.Image.create(
        api_key=conf.API_KEY,
        prompt="a photo that describes `"+translate(prompt)+"` cutey enough for kids",
        n=1,
        size=f"{w}x{h}"
    )
    return response['data'][0]['url']
