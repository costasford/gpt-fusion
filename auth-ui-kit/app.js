import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  sendEmailVerification,
  sendPasswordResetEmail,
  GoogleAuthProvider,
  signInWithPopup,
} from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";

// Demo Firebase config - replace with your own for production
const firebaseConfig = {
  apiKey: "AIzaSyDemo_Replace_With_Your_Real_API_Key_12345",
  authDomain: "gpt-fusion-demo.firebaseapp.com",
  projectId: "gpt-fusion-demo",
  storageBucket: "gpt-fusion-demo.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abcdef123456789012345"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showMessage(id, msg) {
  document.getElementById(id).textContent = msg;
}

async function withLoading(btnId, fn) {
  const btn = document.getElementById(btnId);
  const original = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Loading...";
  try {
    await fn();
  } finally {
    btn.disabled = false;
    btn.textContent = original;
  }
}

// Dark mode functionality
function initTheme() {
  const theme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  
  if (theme === 'dark') {
    document.documentElement.classList.add('dark');
    document.getElementById('theme-toggle-light-icon').classList.add('hidden');
    document.getElementById('theme-toggle-dark-icon').classList.remove('hidden');
  } else {
    document.documentElement.classList.remove('dark');
    document.getElementById('theme-toggle-light-icon').classList.remove('hidden');
    document.getElementById('theme-toggle-dark-icon').classList.add('hidden');
  }
}

function toggleTheme() {
  const isDark = document.documentElement.classList.contains('dark');
  
  if (isDark) {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
    document.getElementById('theme-toggle-light-icon').classList.remove('hidden');
    document.getElementById('theme-toggle-dark-icon').classList.add('hidden');
  } else {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
    document.getElementById('theme-toggle-light-icon').classList.add('hidden');
    document.getElementById('theme-toggle-dark-icon').classList.remove('hidden');
  }
}

// Pre-fill email if saved and initialize theme
document.addEventListener("DOMContentLoaded", () => {
  const savedEmail = localStorage.getItem("savedEmail");
  if (savedEmail) {
    document.getElementById("email").value = savedEmail;
    document.getElementById("remember").checked = true;
  }
  
  initTheme();
  
  // Add theme toggle event listener
  document.getElementById("theme-toggle").addEventListener("click", toggleTheme);
});

document.getElementById("login").addEventListener("click", async () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const remember = document.getElementById("remember").checked;
  if (remember) {
    localStorage.setItem("savedEmail", email);
  } else {
    localStorage.removeItem("savedEmail");
  }
  if (!isValidEmail(email)) {
    showMessage("message", "Invalid email format");
    return;
  }
  await withLoading("login", async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      showMessage("message", "Logged in!");
    } catch (err) {
      showMessage("message", err.message);
    }
  });
});

// Google login handler
document.getElementById("google-login").addEventListener("click", async () => {
  await withLoading("google-login", async () => {
    try {
      const provider = new GoogleAuthProvider();
      await signInWithPopup(auth, provider);
      showMessage("message", "✅ Logged in with Google!");
    } catch (err) {
      // Show helpful error messages for demo setup
      if (err.code === 'auth/invalid-api-key' || err.code === 'auth/project-not-found') {
        showMessage("message", "🔧 Demo config detected. See FIREBASE_SETUP.md to configure real credentials.");
      } else if (err.code === 'auth/unauthorized-domain') {
        showMessage("message", "🌐 Domain not authorized. Add your domain in Firebase Console → Authentication → Settings.");
      } else if (err.code === 'auth/popup-blocked') {
        showMessage("message", "🚫 Popup blocked. Please allow popups and try again.");
      } else if (err.code === 'auth/popup-closed-by-user') {
        showMessage("message", "❌ Login cancelled by user.");
      } else {
        showMessage("message", `❌ ${err.message}`);
      }
    }
  });
});

// Show/Hide modals
document.getElementById("show-signup").addEventListener("click", () => {
  document.getElementById("signup-modal").classList.remove("hidden");
});
document.getElementById("signup-close").addEventListener("click", () => {
  document.getElementById("signup-modal").classList.add("hidden");
  showMessage("signup-message", "");
});
document.getElementById("forgot").addEventListener("click", () => {
  document.getElementById("reset-modal").classList.remove("hidden");
});
document.getElementById("reset-close").addEventListener("click", () => {
  document.getElementById("reset-modal").classList.add("hidden");
  showMessage("reset-message", "");
});

// Sign up handler
document.getElementById("signup-btn").addEventListener("click", async () => {
  const email = document.getElementById("signup-email").value;
  const password = document.getElementById("signup-password").value;
  const confirm = document.getElementById("signup-confirm").value;
  if (!isValidEmail(email)) {
    showMessage("signup-message", "Invalid email format");
    return;
  }
  if (password.length < 6) {
    showMessage("signup-message", "Password must be at least 6 characters");
    return;
  }
  if (password !== confirm) {
    showMessage("signup-message", "Passwords do not match");
    return;
  }
  await withLoading("signup-btn", async () => {
    try {
      const cred = await createUserWithEmailAndPassword(auth, email, password);
      await sendEmailVerification(cred.user);
      showMessage(
        "signup-message",
        "Account created. Check your email to verify."
      );
    } catch (err) {
      showMessage("signup-message", err.message);
    }
  });
});

// Password reset handler
document.getElementById("reset-btn").addEventListener("click", async () => {
  const email = document.getElementById("reset-email").value;
  if (!isValidEmail(email)) {
    showMessage("reset-message", "Invalid email format");
    return;
  }
  await withLoading("reset-btn", async () => {
    try {
      await sendPasswordResetEmail(auth, email);
      showMessage("reset-message", "Reset email sent!");
    } catch (err) {
      showMessage("reset-message", err.message);
    }
  });
});
