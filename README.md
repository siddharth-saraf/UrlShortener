# UrlShortener: A Full-Stack URL Management System

**UrlShortener** is a robust, full-stack web application designed to streamline digital communication by transforming long, complex URLs into concise, manageable, and professional-looking links. Built with **Django** and **Bootstrap 5**, this project demonstrates a commitment to clean architecture, user security, and automated deployment.

### 🚀 Project Overview

In today's digital landscape, the clarity of a link can significantly impact user engagement and trust. **UrlShortener** provides a centralized platform for users to create, manage, and track shortened links. Whether for social media bios, email marketing campaigns, or print media, this application ensures that your destination is just a short click away.

### 🛠️ Key Technical Highlights

- **Full-stack Django Architecture:** Leverages the power of Django's MVC pattern for robust backend logic and efficient database management.
- **Link Analytics & Tracking:** Real-time click counting and advanced metrics logging (IP, Referrer, User-Agent) for every redirect.
- **QR Code Engine:** Dynamic, on-the-fly QR code generation for every shortened link, enabling seamless cross-media redirection.
- **Smart Link Expiration:** Built-in "self-destruct" functionality allowing users to set precise expiration dates for temporary links.
- **Secure Authentication System:** Features a complete user lifecycle including secure signup, login, and password reset functionality via SMTP.
- **Modern UI/UX Design:** Implemented with **Bootstrap 5.3** and **Inter** typography, ensuring a responsive and professional experience across all devices.
- **Enterprise-Grade Security:** Utilizes **Environment Variables** (`.env`) for managing sensitive credentials, keeping production secrets safe and out of version control.
- **Automated CI/CD Pipeline:** Integrated with **GitHub Actions** for seamless, automated deployment to **PythonAnywhere**, ensuring the production environment is always in sync with the `master` branch.
- **Custom Slug Logic:** Empowering users to create branded links by specifying custom keys for their shortened URLs.

## Features

- **Real-Time Analytics:** Track total clicks and monitor link performance directly from your dashboard.
- **Dynamic QR Codes:** Generate and download high-quality QR codes for your shortened URLs with a single click.
- **Self-Destructing Links:** Set expiration dates for your links to ensure they are only accessible when needed.
- **Modern Dashboard:** A clean, intuitive interface to create, edit, and manage all your shortened links.
- **Custom Branded Slugs:** Personalize your links with custom slugs that reflect your brand or content.
- **Secure & Fast:** Optimized for speed and security, providing a reliable experience for both link creators and visitors.

## Getting Started

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/UrlShortener.git
   cd UrlShortener
   ```

2. **Set up the virtual environment:**
   - Linux/macOS: `source myvenv/bin/activate`
   - Windows: `myvenv\Scripts\activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Copy `.env.example` to `.env` and fill in your secrets.
   ```bash
   cp .env.example .env
   ```

5. **Run Migrations & Start Server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Built With

- [Django 2.2+](https://www.djangoproject.com/)
- [Bootstrap 5.3](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [GitHub Actions](https://github.com/features/actions)
