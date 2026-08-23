import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  sendEmailVerification,
  sendPasswordResetEmail,
  GoogleAuthProvider,
  signInWithPopup,
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";

// Tailwind CDN defaults to media-query-based dark mode; without this, the
// theme toggle below flips a `dark` class that no dark: utility class
// actually responds to. Set here (rather than an inline <script>) because
// the page's CSP has no 'unsafe-inline' in script-src.
window.tailwind.config = { darkMode: "class" };

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Enhanced validation functions
export function isValidEmail(email) {
  const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
  return emailRegex.test(email) && email.length <= 254;
}

export function validatePassword(password) {
  const errors = [];
  
  if (password.length < 8) {
    errors.push("Password must be at least 8 characters long");
  }
  
  if (!/[A-Z]/.test(password)) {
    errors.push("Password must contain at least one uppercase letter");
  }
  
  if (!/[a-z]/.test(password)) {
    errors.push("Password must contain at least one lowercase letter");
  }
  
  if (!/\d/.test(password)) {
    errors.push("Password must contain at least one number");
  }
  
  if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
    errors.push("Password must contain at least one special character");
  }
  
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Client-side-only rate limiting - NOT real protection. State lives in an
// in-memory Map scoped to this page load: a hard refresh, a private
// window, or calling signInWithEmailAndPassword directly resets or
// bypasses it entirely. This only improves the UX for accidental repeated
// clicks; it does nothing against a deliberate brute-force attempt. Real
// throttling has to be enforced server-side (Firebase App Check, or rate
// limiting in front of the Auth API) - this demo has no backend to do that.
class RateLimiter {
  constructor(maxAttempts = 3, windowMs = 900000) { // 15 minutes
    this.maxAttempts = maxAttempts;
    this.windowMs = windowMs;
    this.attempts = new Map();
  }
  
  canAttempt(key) {
    const now = Date.now();
    const userAttempts = this.attempts.get(key) || [];
    
    // Remove old attempts outside the window
    const validAttempts = userAttempts.filter(time => now - time < this.windowMs);
    this.attempts.set(key, validAttempts);
    
    return validAttempts.length < this.maxAttempts;
  }
  
  recordAttempt(key) {
    const now = Date.now();
    const userAttempts = this.attempts.get(key) || [];
    userAttempts.push(now);
    this.attempts.set(key, userAttempts);
  }
  
  getRemainingTime(key) {
    const userAttempts = this.attempts.get(key) || [];
    if (userAttempts.length === 0) return 0;
    
    const oldestAttempt = Math.min(...userAttempts);
    const timeLeft = this.windowMs - (Date.now() - oldestAttempt);
    return Math.max(0, timeLeft);
  }
}

const rateLimiter = new RateLimiter();

// Enhanced UI functions
function showMessage(id, msg, type = 'error') {
  const element = document.getElementById(id);
  if (!element) return;
  
  element.textContent = msg;
  element.className = `mt-2 text-center ${type === 'error' ? 'text-red-500 dark:text-red-400' : 'text-green-500 dark:text-green-400'}`;
  
  // Auto-hide success messages after 3 seconds
  if (type === 'success') {
    setTimeout(() => {
      element.textContent = '';
    }, 3000);
  }
}

function showPasswordStrength(password) {
  const validation = validatePassword(password);
  const strengthElement = document.getElementById('password-strength');
  
  if (!strengthElement) return;
  
  if (password.length === 0) {
    strengthElement.innerHTML = '';
    return;
  }
  
  const strength = calculatePasswordStrength(password);
  const strengthText = ['Weak', 'Fair', 'Good', 'Strong'][strength];
  const strengthColors = ['text-red-500', 'text-orange-500', 'text-yellow-500', 'text-green-500'];
  
  strengthElement.innerHTML = `
    <div class="text-sm ${strengthColors[strength]} dark:opacity-90">
      Password strength: ${strengthText}
    </div>
    ${validation.errors.length > 0 ? `
      <ul class="text-xs text-red-500 dark:text-red-400 mt-1">
        ${validation.errors.map(error => `<li>• ${error}</li>`).join('')}
      </ul>
    ` : ''}
  `;
}

function calculatePasswordStrength(password) {
  let strength = 0;
  
  if (password.length >= 8) strength++;
  if (/[A-Z]/.test(password) && /[a-z]/.test(password)) strength++;
  if (/\d/.test(password)) strength++;
  if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) strength++;
  
  return Math.min(3, strength);
}

async function withLoading(btnId, fn) {
  const btn = document.getElementById(btnId);
  if (!btn) return;

  const original = btn.textContent;
  const originalDisabled = btn.disabled;

  btn.disabled = true;
  btn.setAttribute("aria-busy", "true");
  btn.textContent = "Loading...";

  try {
    await fn();
  } finally {
    btn.disabled = originalDisabled;
    btn.removeAttribute("aria-busy");
    btn.textContent = original;
  }
}

// Light input normalization for the email fields below - NOT a general
// XSS sanitizer (it strips `<`/`>` and nothing else). It's safe here only
// because these values are passed straight to the Firebase Auth SDK, never
// inserted into the page via innerHTML. Don't reuse this function as a
// security control before rendering untrusted input into the DOM.
function sanitizeInput(input) {
  return input.trim().replace(/[<>]/g, '');
}

let isAuthenticated = false;

// Auth state management
onAuthStateChanged(auth, (user) => {
  isAuthenticated = !!user;
  updateUI(user);
});

function updateUI(user) {
  const loginSection = document.querySelector('.login-section');
  const dashboardSection = document.querySelector('.dashboard-section');

  if (user) {
    if (loginSection) loginSection.style.display = 'none';
    if (dashboardSection) {
      dashboardSection.style.display = 'block';
      document.getElementById('user-email').textContent = user.email;
      // Informational only - the dashboard is shown to any signed-in user
      // regardless of this value. Gating real content on verification has
      // to happen server-side (e.g. Firebase Security Rules checking
      // request.auth.token.email_verified), since a client-side-only check
      // here would just be a UI label an attacker can ignore by calling
      // the API directly.
      document.getElementById('user-verified').textContent = user.emailVerified ? 'Verified' : 'Unverified';
      document.getElementById('resend-verification-btn')?.classList.toggle('hidden', user.emailVerified);
      document.getElementById('verification-message').textContent = '';
    }
  } else {
    if (loginSection) loginSection.style.display = 'block';
    if (dashboardSection) dashboardSection.style.display = 'none';
  }
}

// Eye / eye-slash icon paths for the password-visibility toggle buttons.
const EYE_ICON =
  '<path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"></path><path fill-rule="evenodd" d="M10 12a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path>';
const EYE_SLASH_ICON =
  '<path fill-rule="evenodd" d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z" clip-rule="evenodd"></path><path d="M12.454 16.697L9.75 13.992a4 4 0 01-3.742-3.741L2.335 6.578A9.98 9.98 0 00.458 10c1.274 4.057 5.065 7 9.542 7 .847 0 1.669-.105 2.454-.303z"></path>';

function togglePasswordVisibility(inputId, button) {
  const input = document.getElementById(inputId);
  if (!input) return;
  const svg = button.querySelector("svg");

  if (input.type === "password") {
    input.type = "text";
    svg.innerHTML = EYE_ICON;
    button.setAttribute("aria-label", "Hide password");
  } else {
    input.type = "password";
    svg.innerHTML = EYE_SLASH_ICON;
    button.setAttribute("aria-label", "Show password");
  }
}

// Pre-fill email if saved
document.addEventListener("DOMContentLoaded", () => {
  const savedEmail = localStorage.getItem("savedEmail");
  if (savedEmail && isValidEmail(savedEmail)) {
    document.getElementById("email").value = savedEmail;
    document.getElementById("remember").checked = true;
  }

  // Add password strength indicator
  const signupPassword = document.getElementById("signup-password");
  if (signupPassword) {
    signupPassword.addEventListener('input', (e) => {
      showPasswordStrength(e.target.value);
    });
  }

  // Add real-time email validation
  const emailInputs = document.querySelectorAll('input[type="email"]');
  emailInputs.forEach(input => {
    input.addEventListener('blur', (e) => {
      const email = e.target.value;
      const invalid = email && !isValidEmail(email);
      if (e.target.id === 'email') {
        // The login field has its own dedicated error slot.
        showFieldError('email-error', invalid ? 'Please enter a valid email address' : '');
      } else if (invalid) {
        showMessage(getMessageId(e.target), 'Please enter a valid email address');
      }
    });
  });

  // Password visibility toggles (replaces the old inline onclick= handlers,
  // which required 'unsafe-inline' in the script-src CSP directive).
  document.querySelectorAll("[data-toggle-password]").forEach((button) => {
    button.addEventListener("click", () => {
      togglePasswordVisibility(button.dataset.togglePassword, button);
    });
  });
});

function getMessageId(inputElement) {
  // Determine which message element to use based on input context
  if (inputElement.id.includes('signup')) return 'signup-message';
  if (inputElement.id.includes('reset')) return 'reset-message';
  return 'message';
}

// Writes into the small per-field error text below the login form's email/
// password inputs (referenced by their aria-describedby), rather than the
// shared banner - only those two fields have a dedicated slot for this.
function showFieldError(elementId, msg) {
  const el = document.getElementById(elementId);
  if (el) el.textContent = msg;
}

// Enhanced login handler
document.getElementById("login")?.addEventListener("click", async () => {
  const email = sanitizeInput(document.getElementById("email").value);
  const password = document.getElementById("password").value;
  const remember = document.getElementById("remember").checked;

  showFieldError('email-error', '');
  showFieldError('password-error', '');

  // Rate limiting check
  if (!rateLimiter.canAttempt(email)) {
    const remainingTime = Math.ceil(rateLimiter.getRemainingTime(email) / 60000);
    showMessage("message", `Too many failed attempts. Try again in ${remainingTime} minutes.`);
    return;
  }

  // Validation
  if (!isValidEmail(email)) {
    showFieldError('email-error', 'Please enter a valid email address');
    return;
  }

  if (!password) {
    showFieldError('password-error', 'Password is required');
    return;
  }

  await withLoading("login", async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);

      // Save email if remember is checked
      if (remember) {
        localStorage.setItem("savedEmail", email);
      } else {
        localStorage.removeItem("savedEmail");
      }
      
      showMessage("message", "Login successful!", "success");
    } catch (err) {
      rateLimiter.recordAttempt(email);
      
      let errorMessage = "Login failed. Please check your credentials.";
      
      switch (err.code) {
        case 'auth/user-not-found':
        case 'auth/wrong-password':
          errorMessage = "Invalid email or password";
          break;
        case 'auth/too-many-requests':
          errorMessage = "Too many failed attempts. Please try again later.";
          break;
        case 'auth/user-disabled':
          errorMessage = "This account has been disabled";
          break;
      }
      
      showMessage("message", errorMessage);
    }
  });
});

// Google login handler with enhanced error handling
document.getElementById("google-login")?.addEventListener("click", async () => {
  await withLoading("google-login", async () => {
    try {
      const provider = new GoogleAuthProvider();
      provider.addScope('profile');
      provider.addScope('email');
      
      await signInWithPopup(auth, provider);
      showMessage("message", "Successfully logged in with Google!", "success");
    } catch (err) {
      let errorMessage = "Google login failed";
      
      switch (err.code) {
        case 'auth/popup-closed-by-user':
          errorMessage = "Login cancelled";
          break;
        case 'auth/popup-blocked':
          errorMessage = "Popup blocked. Please allow popups for this site.";
          break;
        case 'auth/account-exists-with-different-credential':
          errorMessage = "Account already exists with different login method";
          break;
      }
      
      showMessage("message", errorMessage);
    }
  });
});

// Enhanced signup handler
document.getElementById("signup-btn")?.addEventListener("click", async () => {
  const email = sanitizeInput(document.getElementById("signup-email").value);
  const password = document.getElementById("signup-password").value;
  const confirm = document.getElementById("signup-confirm").value;
  
  // Validation
  if (!isValidEmail(email)) {
    showMessage("signup-message", "Please enter a valid email address");
    return;
  }
  
  const passwordValidation = validatePassword(password);
  if (!passwordValidation.isValid) {
    showMessage("signup-message", passwordValidation.errors[0]);
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
      showMessage("signup-message", "Account created! Please check your email to verify your account.", "success");
    } catch (err) {
      let errorMessage = "Account creation failed";
      
      switch (err.code) {
        case 'auth/email-already-in-use':
          errorMessage = "An account with this email already exists";
          break;
        case 'auth/weak-password':
          errorMessage = "Password is too weak";
          break;
      }
      
      showMessage("signup-message", errorMessage);
    }
  });
});

// Enhanced password reset handler
document.getElementById("reset-btn")?.addEventListener("click", async () => {
  const email = sanitizeInput(document.getElementById("reset-email").value);
  
  if (!isValidEmail(email)) {
    showMessage("reset-message", "Please enter a valid email address");
    return;
  }
  
  await withLoading("reset-btn", async () => {
    try {
      await sendPasswordResetEmail(auth, email);
    } catch (err) {
      // Deliberately not distinguishing "no such account" from any other
      // failure here (same reasoning as the login handler above): doing so
      // lets an attacker enumerate which emails have accounts by watching
      // which ones get a different reset-flow response.
    }
    // Always show success, regardless of whether the account exists.
    showMessage("reset-message", "If an account exists for that email, a password reset link has been sent.", "success");
  });
});

// Modal focus management: move focus into the modal on open (so keyboard/
// screen-reader users land somewhere sensible instead of a dialog that
// visually appeared but left focus behind on the trigger link), trap Tab
// within it while open, and restore focus to whatever opened it on close.
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

// Modal handlers
document.getElementById("show-signup")?.addEventListener("click", (e) => {
  e.preventDefault();
  const modal = document.getElementById("signup-modal");
  if (modal) openModal(modal, e.currentTarget);
});

document.getElementById("signup-close")?.addEventListener("click", () => {
  const modal = document.getElementById("signup-modal");
  if (modal) closeModal(modal);
  showMessage("signup-message", "");
});

document.getElementById("forgot")?.addEventListener("click", (e) => {
  e.preventDefault();
  const modal = document.getElementById("reset-modal");
  if (modal) openModal(modal, e.currentTarget);
});

document.getElementById("reset-close")?.addEventListener("click", () => {
  const modal = document.getElementById("reset-modal");
  if (modal) closeModal(modal);
  showMessage("reset-message", "");
});

// Logout handler
document.getElementById("logout-btn")?.addEventListener("click", async () => {
  try {
    await signOut(auth);
    localStorage.removeItem("savedEmail");
    showMessage("message", "Logged out successfully", "success");
  } catch (err) {
    showMessage("message", "Logout failed");
  }
});

// Resend verification email - the one actionable thing an unverified user
// can actually do, unlike the "Unverified" label above it (which is purely
// informational and doesn't gate anything on its own).
document.getElementById("resend-verification-btn")?.addEventListener("click", async () => {
  if (!auth.currentUser) return;
  await withLoading("resend-verification-btn", async () => {
    try {
      await sendEmailVerification(auth.currentUser);
      document.getElementById("verification-message").textContent =
        "Verification email sent. Check your inbox.";
    } catch (err) {
      document.getElementById("verification-message").textContent =
        err.code === "auth/too-many-requests"
          ? "Too many requests. Please wait before trying again."
          : "Failed to send verification email. Please try again.";
    }
  });
});

// Close modals when clicking outside
document.addEventListener('click', (e) => {
  MODAL_IDS.forEach(modalId => {
    const modal = document.getElementById(modalId);
    if (modal && e.target === modal) {
      closeModal(modal);
    }
  });
});

// Keyboard navigation: Escape closes the open modal (restoring focus to
// its trigger), Tab is trapped inside it so keyboard focus can't silently
// leave a dialog that's still visually open.
document.addEventListener('keydown', (e) => {
  const openModalId = MODAL_IDS.find((modalId) => {
    const modal = document.getElementById(modalId);
    return modal && !modal.classList.contains('hidden');
  });
  if (!openModalId) return;
  const modal = document.getElementById(openModalId);

  if (e.key === 'Escape') {
    closeModal(modal);
    return;
  }

  if (e.key === 'Tab') {
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

// Export functions for testing
window.authUtils = {
  isValidEmail,
  validatePassword,
  sanitizeInput
};