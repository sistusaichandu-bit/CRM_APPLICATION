# Healthcare CRM - Web Application

A professional Healthcare Customer Relationship Management (CRM) web application built with vanilla HTML5, CSS3, and JavaScript.

## 🎯 Features

### Navigation System
- **Fixed Top Navbar**: Hospital branding, user menu, notifications
- **Fixed Left Sidebar**: Organized menu with 6 main sections
- **Responsive Design**: Sidebar toggles on mobile/tablet devices
- **Active Menu Highlighting**: Current page is automatically highlighted

### User Management
- **Login Page**: Professional login form with validation
- **Remember Me**: Saves email using localStorage
- **User Profile Menu**: Quick access to profile, settings, logout
- **Logout Confirmation**: Confirms before signing out

### Responsive Breakpoints
- **Desktop (1024px+)**: Full sidebar visible with labels
- **Tablet (768px - 1024px)**: Hamburger menu for sidebar toggle
- **Mobile (480px - 768px)**: Sidebar hidden by default, toggled with menu button
- **Small Mobile (<480px)**: Optimized layout and typography

## 📂 Project Structure

```
healthcare-crm/
├── templates/
│   ├── base.html              # Master template (sidebar + navbar)
│   ├── login.html             # Login page
│   └── dashboard.html         # Dashboard page
├── static/
│   ├── css/
│   │   └── style.css          # All styling (CSS variables, responsive design)
│   └── js/
│       └── main.js            # All JavaScript (navigation, form handling)
└── IMPLEMENTATION_SUMMARY.md  # Detailed feature documentation
```

## 🚀 Quick Start

### Opening the Application
1. Open `templates/login.html` in a web browser
2. Use test credentials:
   - **Email**: test@example.com (or any valid email)
   - **Password**: password123 (minimum 6 characters)
3. Check "Remember me" to save your email for next login
4. Click "Sign In" to access the dashboard

### Navigation
- **Desktop**: Use sidebar links to navigate between pages
- **Mobile/Tablet**: Click the hamburger menu (☰) to toggle sidebar
- **Keyboard**: Press Escape key to close sidebar/menus

## 🎨 Design Highlights

### Color Scheme
- **Primary**: Medical Blue (#3498db)
- **Background**: Light Gray (#f5f7fa)
- **Accent**: Red for logout (#e74c3c)
- **Success**: Green (#27ae60)

### Key Components
1. **Navbar** (60px height)
   - Logo with hospital icon
   - Notification bell with badge
   - User profile dropdown

2. **Sidebar** (250px width, collapsible)
   - Dashboard section
   - Healthcare Staff (Doctors)
   - Patients section
   - Appointments (Visits, Follow-ups)
   - Clinical (Referrals)
   - Logout button

3. **Main Content**
   - Page header with title and subtitle
   - Scrollable content area
   - Responsive grid layout

## 📋 Menu Items

| Icon | Section | Items |
|------|---------|-------|
| 📊 | Dashboard | Main dashboard view |
| 👨‍⚕️ | Healthcare Staff | Doctors management |
| 👥 | Patients | Patient records |
| 📅 | Appointments | Visits & Follow-ups |
| 📤 | Clinical | Referrals |
| 🚪 | User | Logout |

## 🔐 Form Validation

### Login Form
- **Email**: Must be valid email format (example@domain.com)
- **Password**: Minimum 6 characters required
- **Remember Me**: Saves email to browser storage
- **Error Messages**: Real-time validation feedback

### Password Features
- Toggle visibility with eye icon (👁️)
- Auto-focus on error fields
- Clear errors when user starts typing

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Escape | Close sidebar and dropdown menus |

## 🎬 JavaScript Functions

### Navigation
- `toggleSidebar()` - Open/close sidebar
- `toggleUserDropdown()` - Open/close user menu
- `handleMenuLinkClick()` - Navigate to page

### Form Handling
- `handleLoginSubmit()` - Process login
- `validateLoginForm()` - Validate inputs
- `togglePasswordVisibility()` - Show/hide password

### Utilities
- `closeSidebar()` - Force close sidebar
- `closeDropdownOnOutsideClick()` - Auto-close menus
- `appLog()` - Debug logging

## 🛠️ Customization

### Changing Colors
Edit CSS variables in `style.css`:
```css
:root {
    --color-primary: #3498db;        /* Primary color */
    --color-danger: #e74c3c;         /* Logout button color */
    --color-light-bg: #f5f7fa;       /* Background color */
}
```

### Changing Layout Dimensions
```css
:root {
    --navbar-height: 60px;           /* Navbar height */
    --sidebar-width: 250px;          /* Sidebar width */
}
```

### Adding New Menu Items
Edit `templates/base.html` sidebar section:
```html
<div class="menu-section">
    <h3 class="menu-section-title">Your Section</h3>
    <a href="#page" class="menu-item menu-link" data-page="page">
        <span class="menu-icon">🎯</span>
        <span class="menu-label">Page Name</span>
    </a>
</div>
```

## 🔗 File Connections

- `base.html` links to:
  - `static/css/style.css` - All styling
  - `static/js/main.js` - All functionality

- `login.html` links to:
  - `static/css/style.css` - Login page styling
  - `static/js/main.js` - Login form handling

- `dashboard.html` uses `base.html` as master template

## 💾 Browser Storage

The application uses localStorage for:
- **rememberedEmail**: Stores email if "Remember me" is checked
- **userToken**: Mock authentication token (replace with real API)

## 📱 Responsive Testing

Test on these breakpoints:
- Desktop: 1920px, 1440px, 1024px
- Tablet: 768px, 600px
- Mobile: 480px, 375px, 360px
- Small Mobile: 320px

## ✨ Best Practices Implemented

✅ Semantic HTML structure
✅ CSS custom properties for maintainability
✅ Mobile-first responsive design
✅ Form validation on client-side
✅ Accessibility considerations
✅ Keyboard navigation support
✅ Consistent spacing and typography
✅ Smooth transitions and animations
✅ Clean, commented code
✅ No external dependencies

## 🚀 Next Steps for Development

1. **Backend Integration**: Connect to authentication API
2. **Data Pages**: Create content for Doctors, Patients, Visits pages
3. **API Integration**: Replace mock data with real API calls
4. **User Management**: Implement real user authentication
5. **Database**: Connect to healthcare database
6. **Advanced Features**: Add search, filters, reporting, etc.

## 📞 Support

For questions or issues, refer to the code comments and IMPLEMENTATION_SUMMARY.md for detailed documentation.

---

**Built with**: HTML5, CSS3, Vanilla JavaScript
**Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
**License**: Open source
