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

// Rate limiting
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
  btn.textContent = "Loading...";
  
  try {
    await fn();
  } finally {
    btn.disabled = originalDisabled;
    btn.textContent = original;
  }
}

// Enhanced security functions
function sanitizeInput(input) {
  return input.trim().replace(/[<>]/g, '');
}

function generateCSRFToken() {
  return crypto.getRandomValues(new Uint32Array(4)).join('-');
}

// Session management
let csrfToken = generateCSRFToken();
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
      document.getElementById('user-verified').textContent = user.emailVerified ? 'Verified' : 'Unverified';
    }
  } else {
    if (loginSection) loginSection.style.display = 'block';
    if (dashboardSection) dashboardSection.style.display = 'none';
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
      if (email && !isValidEmail(email)) {
        showMessage(getMessageId(e.target), 'Please enter a valid email address');
      }
    });
  });
});

function getMessageId(inputElement) {
  // Determine which message element to use based on input context
  if (inputElement.id.includes('signup')) return 'signup-message';
  if (inputElement.id.includes('reset')) return 'reset-message';
  return 'message';
}

// Enhanced login handler
document.getElementById("login")?.addEventListener("click", async () => {
  const email = sanitizeInput(document.getElementById("email").value);
  const password = document.getElementById("password").value;
  const remember = document.getElementById("remember").checked;
  
  // Rate limiting check
  if (!rateLimiter.canAttempt(email)) {
    const remainingTime = Math.ceil(rateLimiter.getRemainingTime(email) / 60000);
    showMessage("message", `Too many failed attempts. Try again in ${remainingTime} minutes.`);
    return;
  }
  
  // Validation
  if (!isValidEmail(email)) {
    showMessage("message", "Please enter a valid email address");
    return;
  }
  
  if (!password) {
    showMessage("message", "Password is required");
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
      showMessage("reset-message", "Password reset email sent! Check your inbox.", "success");
    } catch (err) {
      let errorMessage = "Failed to send reset email";
      
      if (err.code === 'auth/user-not-found') {
        errorMessage = "No account found with this email address";
      }
      
      showMessage("reset-message", errorMessage);
    }
  });
});

// Modal handlers
document.getElementById("show-signup")?.addEventListener("click", (e) => {
  e.preventDefault();
  document.getElementById("signup-modal")?.classList.remove("hidden");
});

document.getElementById("signup-close")?.addEventListener("click", () => {
  document.getElementById("signup-modal")?.classList.add("hidden");
  showMessage("signup-message", "");
});

document.getElementById("forgot")?.addEventListener("click", (e) => {
  e.preventDefault();
  document.getElementById("reset-modal")?.classList.remove("hidden");
});

document.getElementById("reset-close")?.addEventListener("click", () => {
  document.getElementById("reset-modal")?.classList.add("hidden");
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

// Close modals when clicking outside
document.addEventListener('click', (e) => {
  const modals = ['signup-modal', 'reset-modal'];
  modals.forEach(modalId => {
    const modal = document.getElementById(modalId);
    if (modal && e.target === modal) {
      modal.classList.add('hidden');
    }
  });
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const modals = ['signup-modal', 'reset-modal'];
    modals.forEach(modalId => {
      const modal = document.getElementById(modalId);
      if (modal && !modal.classList.contains('hidden')) {
        modal.classList.add('hidden');
      }
    });
  }
});

// Export functions for testing
window.authUtils = {
  isValidEmail,
  validatePassword,
  sanitizeInput
};