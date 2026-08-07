# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ۱. ریشه پروژه را /app قرار می‌دهیم تا کپی فایل‌ها درست انجام شود
WORKDIR /app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy only the requirements file first
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project source code into /app
COPY . .

# ۲. اکنون پوشه کاری را به core تغییر می‌دهیم (محل manage.py)
WORKDIR /app/todo

# Expose Django development server port
EXPOSE 8000

# Default command (کوتیشن اضافی آخر حذف شد)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]