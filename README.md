# SkillCore - Mobile Repair Price Comparison Platform

**SkillCore** is a comprehensive price comparison platform for mobile device repair services in Sweden. We connect users with verified local repair shops, making it easy to compare prices, read reviews, and find the best service for their devices.

## 🎯 Project Overview

SkillCore is **not a repair shop** and does not sell parts or fix phones. Our sole purpose is to help users find the right professional for the job at the right price by providing:

- **Price Comparison**: Compare repair costs across multiple shops for specific device models
- **Verified Shops**: Browse listings from vetted, professional repair businesses
- **User Reviews**: Read authentic feedback from other customers
- **Vendor Dashboard**: Shop owners can manage their listings and update prices

## 🏗️ Project Structure

```
skillcore/
├── apps/                   # Modular Django apps
│   ├── users/             # User authentication and management
│   ├── shops/             # Repair shop data and vendor dashboard
│   ├── phones/            # Phone brands and models database
│   ├── pricing/           # Price comparison logic and search
│   └── pages/             # Static pages (About, Contact, Terms, Privacy)
├── config/                # Project settings and configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   └── sitemaps.py        # SEO sitemap configuration
├── media/                 # User-uploaded files
├── static/                # Static assets (CSS, JS, Images)
├── templates/             # Global HTML templates
│   ├── base.html          # Base template with navigation and footer
│   ├── pricing/           # Price comparison templates
│   ├── shops/             # Shop detail and dashboard templates
│   ├── users/             # Authentication templates
│   └── pages/             # Static page templates
├── .env                   # Environment variables (not in git)
├── .env.example           # Example environment configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🚀 Features

### For Users
- **Search & Compare**: Find repair prices by device model and service type
- **Shop Profiles**: View detailed information about repair shops
- **Reviews & Ratings**: Read and write reviews for repair shops
- **User Accounts**: Create an account to leave reviews

### For Shop Owners
- **Vendor Dashboard**: Manage shop information and pricing
- **Price Management**: Add, edit, and delete repair service prices
- **Shop Registration**: Easy onboarding process for new shops
- **Verification System**: Get verified to build trust with customers

## 🛠️ Technology Stack

- **Backend**: Django 6.0.2
- **Database**: SQLite (development) / PostgreSQL (production-ready)
- **Frontend**: HTML, Tailwind CSS, Fluent UI Web Components (Fluent 2), Vanilla JavaScript
- **Authentication**: Django's built-in auth system
- **Environment Management**: django-environ

## 📦 Local Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository** (if applicable)
   ```bash
   git clone <repository-url>
   cd skillcore
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` as needed
   ```bash
   cp .env.example .env
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data** (optional)
   ```bash
   python manage.py loaddata sample_data.json
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🗄️ Database Models

### Core Models

- **PhoneBrand**: Mobile device manufacturers (Apple, Samsung, etc.)
- **PhoneModel**: Specific device models (iPhone 13, Galaxy S21, etc.)
- **ServiceType**: Types of repairs (Screen Repair, Battery Replacement, etc.)
- **Shop**: Repair shop information and owner relationship
- **Price**: Repair service pricing (links Shop, PhoneModel, and ServiceType)
- **Review**: User reviews and ratings for shops

## 🔐 Environment Variables

Key environment variables (defined in `.env`):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## 📱 API Endpoints

### Public Endpoints
- `GET /` - Homepage with search
- `GET /pricing/results/` - Search results
- `GET /shops/<id>/` - Shop detail page
- `GET /about/` - About page
- `GET /contact/` - Contact page

### Authenticated Endpoints
- `POST /shops/<id>/review/` - Submit a review
- `GET /shops/dashboard/` - Vendor dashboard
- `POST /shops/dashboard/add-price/` - Add new price

### AJAX Endpoints
- `GET /phones/api/models/?brand=<id>` - Get models for a brand

## 🎨 Design System

The project uses a combination of **Fluent UI Web Components (Fluent 2)** for interactive elements and a custom **Tailwind CSS** configuration for layout and typography with the following color scheme:

- **Primary**: `#7D53FF` (Purple) - Main brand color
- **Secondary**: `#64748B` (Slate) - Text and accents
- **Background**: `#F8FAFC` - Page background
- **Success**: `#B6FF00` - Success states

## 📄 License

This project is proprietary software. All rights reserved.

## 👥 Contact

For questions or support:
- Email: support@skillcore.se
- Website: https://skillcore.se

---

**Note**: This is a price comparison platform. We do not perform repairs or sell products. All repair services are provided by independent third-party shops.
