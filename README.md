# ChatGPT 微信公众号机器人

把 ChatGPT 接入微信公众号。

![使用](./images/usage.jpg)

## 前置条件

1. OpenAI 账号，并[创建 API Key](https://platform.openai.com/account/api-keys)

1. 微信公众号，并[微信公众平台开发](https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html)

1. Python 3.7+

## 运行

1. `pip install -r requirements.txt`

1. `cp .env.example .env`

1. 在 `.env` 文件中，设置 OPENAI_API_KEY 和 WECHAT_TOKEN。

1. `python main.py`

1. 默认会运行在 8888 端口，可以使用 ngrok 把 localhost 服务映射到公网：

    `ngrok http 8888`

1. 根据[微信公众平台开发](https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html)的步骤，把 ngrok 的 URL 填入服务器地址（URL）。