# 功能
0. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
1. 實現爬蟲自動定時抓取。
2. 每當抓取到新的新聞時立即通知頁面。

## 實作說明
* 使用`requests`，`selenium`抓取資料

* 使用 Django REST Framework 傳遞資料
* 前端頁面使用AJAX
* 每當抓取到新的新聞時立即用`confirm`通知頁面，使用者確認後刷新頁面
* 定期運行爬蟲程式爬取資料並儲存至資料庫運行
    * 使用`crontab`
    * custom management command：`python manage.py crawling`    
* 原可部署至Heroku上，但新增立即通知功能後部署失敗
    * 部署時是使用[Heroku Scheduler Add-on](https://devcenter.heroku.com/articles/scheduler#defining-tasks)定期運行爬蟲程式
