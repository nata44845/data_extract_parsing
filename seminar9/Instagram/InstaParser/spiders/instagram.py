import json
from copy import deepcopy
from gc import callbacks

import scrapy
from scrapy.http import HtmlResponse
from urllib.parse import urlencode

from seminar7.main import options
from seminar9.Instagram.InstaParser.items import InstaparserItem


class InstagramSpider(scrapy.Spider):
    name = "instagram"
    allowed_domains = ["instagram.com"]
    start_urls = ["https://instagram.com"]
    inst_login_link = "https:/instagram.com/api/v1/web/accounts/login/ajax/"
    inst_login = "gamer_udm18"
    inst_password = "#PWD..."
    user_for_parse = {"name":"machinelearning", "id":"27790688603"}

    def parse(self, response: HtmlResponse):
        yield scrapy.FormRequest(
        self.inst_login_link,
              method="POST",
              callback=self.authorize,
              formdata={"username":self.inst_login,
                        "enc_password":self.inst_password},
              headers = {"X-Csrftoken": "T..."}

        )

    def authorise(self, response: HtmlResponse):
        j_data = response.json()
        if j_data.get("authenticated"):
            yield response.follow(f"/{self.user_for_parse.get("name")}",
                                  callback=self.user_data_parse,
                                  cb_kwargs = {"username" : self.user_for_parse.get("name")}
                                )

    def user_data_parse(self, response: HtmlResponse, username):
        print()
        user_id = self.user_for_parse.get("id")
        params = {"count": 12}
        url_posts = f"https:/instagram.com/api/v1/feed/user/{user_id}/?{urlencode(params)}"

        yield response.follow(url_posts,
                              callback=self.user_posts_parse,
                              cb_kwargs={'username': username,
                                         'user_id': user_id,
                                         'params': deepcopy(params)},
                              headers={"User-Agent": "Instagram 37.0.0.21.97"})

    def user_posts_parse(self, response: HtmlResponse,username,user_id,params):
        # self.save_to_json(response.json())
        j_data = response.json()
        next_page = j_data.get("more_available")
        if next_page:
            next_max_id = j_data.get("next_max_id")
            params["max_id"] = next_max_id
            url_posts = url_posts = f"https:/instagram.com/api/v1/feed/user/{user_id}/?{urlencode(params)}"
            yield response.follow(url_posts,
                                  callback=self.user_posts_parse,
                                  cb_kwargs={'username': username,
                                             'user_id': user_id,
                                             'params': deepcopy(params)},
                                  headers={"User-Agent": "Instagram 37.0.0.21.97"})
        posts = j_data.get("items")
        for post in posts:
            item = InstaparserItem(
                text = post.get("caption").get("text"),
                photo = post.get("image_versions2").get("candidates")[0].get("url"),
                post_data = post,
                user_id = user_id,
                username = username
            )
            yield item


    def save_to_json(self, text):
        with open("page.json", "w") as f:
            json.dump(text, f)