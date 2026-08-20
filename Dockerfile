# Use the official Python 3.12 slim image
FROM python:3.12-slim


# ۱. نصب ابزارهای ضروری لینوکس (برای حل خطای Dev Containers و ساخت پکیج‌ها)

# ۲. تعیین پوشه کاری اولیه
WORKDIR /app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy only the requirements file first for layer caching
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project source code into /app
COPY . .

# ۳. تغییر پوشه کاری به core (محل manage.py)
WORKDIR /app/todo
    
# Expose Django development server port
EXPOSE 8000

# Default command (کاراکتر اضافی ' از انتهای خط حذف شد)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]