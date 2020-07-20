echo off
echo c:\
cd\
echo c:\linebot
cd linebot
echo 將資料加到git 
git add .
echo 確認git 資料修改 
git commit -am "ok"
echo git上傳
git push heroku master
pause
echo.