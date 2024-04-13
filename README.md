# GSender

GSender یک ابزار ساده برای ارسال پیام و فایل از طریق Telegram است.

## نصب

برای نصب `gsender`، مراحل زیر را دنبال کنید:

1. از ریپوزیتوری GitHub آخرین نسخه را دانلود کنید و به مسیر `/usr/local/bin/gsender` ذخیره کنید:

```bash
wget -O /usr/local/bin/gsender https://raw.githubusercontent.com/realgojo/tg-sender/main/gsender.py && chmod +x /usr/local/bin/gsender
```

## استفاده

بعد از نصب، می‌توانید از دستور `gsender` برای ارسال پیام و فایل از طریق Telegram استفاده کنید.

مثال‌ها:

- ارسال فایل:

```bash
gsender <bot_token> <chat_id> <file_path>
```

- ارسال آخرین فایل با استفاده از تنظیمات قبلی:

```bash
gsender last
```

- نمایش راهنما:

```bash
gsender help
```

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.
