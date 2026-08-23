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

// Tailwind CDN defaults to media-query-based dark mode; without this, the
// theme toggle below flips a `dark` class that no dark: utility class
// actually responds to.
window.tailwind.config = { darkMode: "class" };

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
  btn.setAttribute("aria-busy", "true");
  btn.textContent = "Loading...";
  try {
    await fn();
  } finally {
    btn.disabled = false;
    btn.removeAttribute("aria-busy");
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
    } catch {
      // Collapsed to one generic message regardless of cause (wrong
      // password vs. no such account) - showing which one it was lets an
      // attacker enumerate valid emails by trying logins against them.
      showMessage("message", "Invalid email or password");
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
        showMessage("message", "❌ Google login failed. Please try again.");
      }
    }
  });
});

// Modal focus management: move focus into the modal on open, trap Tab
// within it while open, and restore focus to whatever opened it on close -
// without this, a keyboard/screen-reader user's focus stayed on the
// trigger link while the modal appeared on screen.
const MODAL_IDS = ["signup-modal", "reset-modal"];
let modalTriggerElement = null;

function getFocusableElements(container) {
  return Array.from(
    container.querySelectorAll(
      'input, button, a[href], select, textarea, [tabindex]:not([tabindex="-1"])'
    )
  ).filter((el) => !el.disabled && el.offsetParent !== null);
}

function openModal(modal, trigger) {
  modalTriggerElement = trigger || document.activeElement;
  modal.classList.remove("hidden");
  const focusable = getFocusableElements(modal);
  if (focusable.length > 0) focusable[0].focus();
}

function closeModal(modal) {
  modal.classList.add("hidden");
  if (modalTriggerElement) {
    modalTriggerElement.focus();
    modalTriggerElement = null;
  }
}

// Show/Hide modals
document.getElementById("show-signup").addEventListener("click", (e) => {
  e.preventDefault();
  openModal(document.getElementById("signup-modal"), e.currentTarget);
});
document.getElementById("signup-close").addEventListener("click", () => {
  closeModal(document.getElementById("signup-modal"));
  showMessage("signup-message", "");
});
document.getElementById("forgot").addEventListener("click", (e) => {
  e.preventDefault();
  openModal(document.getElementById("reset-modal"), e.currentTarget);
});
document.getElementById("reset-close").addEventListener("click", () => {
  closeModal(document.getElementById("reset-modal"));
  showMessage("reset-message", "");
});

// Close modals when clicking outside, or on Escape (also traps Tab inside
// whichever modal is open).
document.addEventListener("click", (e) => {
  MODAL_IDS.forEach((modalId) => {
    const modal = document.getElementById(modalId);
    if (modal && e.target === modal) closeModal(modal);
  });
});

document.addEventListener("keydown", (e) => {
  const openModalId = MODAL_IDS.find((modalId) => {
    const modal = document.getElementById(modalId);
    return modal && !modal.classList.contains("hidden");
  });
  if (!openModalId) return;
  const modal = document.getElementById(openModalId);

  if (e.key === "Escape") {
    closeModal(modal);
    return;
  }

  if (e.key === "Tab") {
    const focusable = getFocusableElements(modal);
    if (focusable.length === 0) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
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
      let errorMessage = "Failed to create account. Please try again.";
      if (err.code === "auth/email-already-in-use") {
        errorMessage = "An account with this email already exists";
      } else if (err.code === "auth/weak-password") {
        errorMessage = "Password is too weak";
      }
      showMessage("signup-message", errorMessage);
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
    } catch {
      // Ignored deliberately: showing whether the send failed because
      // there's no account with this email (vs. any other error) would
      // let an attacker enumerate valid emails via the reset flow.
    }
    showMessage("reset-message", "If an account exists for that email, a reset link has been sent.");
  });
});
