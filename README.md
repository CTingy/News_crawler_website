# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 實現爬蟲自動定時抓取。
2. 每當抓取到新的新聞時立即通知頁面。
3. 将本 demo 部署至服务器并可正确运行。

## 答題說明
* 使用`requests`，`selenium`抓取資料

* 使用 Django REST Framework 傳遞資料
* 前端頁面使用AJAX
* 每當抓取到新的新聞時立即用`confirm`通知頁面，使用者確認後刷新頁面
* 定期運行爬蟲程式爬取資料並儲存至資料庫運行
    * 使用`crontab`
    * 指令為：`python manage.py crawling`    
* 原可部署至Heroku上: https://crawlnba.herokuapp.com/，但新增立即通知功能後部署失敗
    * 部署時是使用[Heroku Scheduler Add-on](https://devcenter.heroku.com/articles/scheduler#defining-tasks)定期運行爬蟲程式