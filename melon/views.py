from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import re
import requests
from bs4 import BeautifulSoup as bs


# 멜론차트
@login_required(login_url="common:login")
def chart(request):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36"
    headers = {"User-Agent": user_agent}
    response = requests.get("https://www.melon.com/chart/index.htm", headers=headers)

    soup = bs(response.text, "html.parser")
    trs = soup.select("table > tbody > tr")

    chart_list = []
    for tr in trs:
        # 순위, 노래, 가수, 앨범
        rank = tr.select_one("span.rank").text.strip()
        rank01 = tr.select_one("div.ellipsis.rank01").text.strip()
        rank02 = tr.select_one("div.ellipsis.rank02 > a").text.strip()
        rank03 = tr.select_one("div.ellipsis.rank03").text.strip()
        # print(rank, rank01, rank02, rank03)

        # 가수 ID
        rank02_href = tr.select_one("div.ellipsis.rank02 > a").get("href").strip()
        rank02_id = re.sub("[^0-9]", "", rank02_href)
        # print(rank02_href, rank02_id)

        # 앨범 ID
        rank03_href = tr.select_one("div.ellipsis.rank03 > a").get("href").strip()
        rank03_id = re.sub("[^0-9]", "", rank03_href)
        print(rank03_href, rank03_id)

        chart_dict = {
            "rank": rank,
            "rank01": rank01,
            "rank02": rank02,
            "rank03": rank03,
            "rank02_id": rank02_id,
            "rank03_id": rank03_id,
        }
        chart_list.append(chart_dict)

    context = {"chart_list": chart_list}
    return render(request, "melon/chart.html", context)