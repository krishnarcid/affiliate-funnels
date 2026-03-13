@echo off
REM Daily Sales Engine Runner
REM Run this script to execute the sales engine

cd /d "C:\Users\krish\.openclaw\workspace\affiliate-funnels"
python sales-engine.py > logs\run-%date:~-4,4%%date:~-10,2%%date:~-7,2%.log 2>>1

echo Sales engine completed at %date% %time%
pause
