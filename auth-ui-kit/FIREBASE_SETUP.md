# Firebase Authentication Setup

This auth UI kit includes Google login functionality, but requires Firebase configuration to work.

## 🚀 Quick Demo Setup

The current demo config in `app.js` has placeholder credentials. To see it working:

1. **Create a Firebase Project**
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Click "Create a project"
   - Name it (e.g., "my-auth-demo")

2. **Enable Google Authentication**
   - Go to Authentication → Sign-in method
   - Enable "Google" provider
   - Add your support email

3. **Get Your Config**
   - Project Settings → General → Your apps
   - Click Web app icon `</>`
   - Register app with nickname
   - Copy the `firebaseConfig` object

4. **Update app.js**
   ```javascript
   const firebaseConfig = {
     apiKey: "your-real-api-key",
     authDomain: "your-project.firebaseapp.com",
     projectId: "your-project-id",
     storageBucket: "your-project.appspot.com",
     messagingSenderId: "123456789",
     appId: "your-app-id"
   };
   ```

## 🔧 Local Development

For local testing (http://localhost):
- Add `localhost` to Authorized domains in Firebase Console
- Authentication → Settings → Authorized domains

## 🌐 Production Deployment

For your live site:
1. Add your domain to Authorized domains
2. Update CORS settings if needed
3. Consider adding security rules

## ✨ Features Included

- ✅ Email/password authentication
- ✅ Google OAuth login
- ✅ Password reset functionality
- ✅ Account creation with email verification
- ✅ Remember me functionality
- ✅ Dark mode support
- ✅ Accessibility (WCAG 2.1 AA compliant)
- ✅ Mobile responsive design

## 📝 Testing the Demo

With proper Firebase config, the Google login button will:
1. Open Google OAuth popup
2. Handle user selection
3. Return authentication token
4. Display success message
5. Store user session

The demo shows a fully functional auth flow that you can integrate into any web application.