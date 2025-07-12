import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  sendEmailVerification,
  sendPasswordResetEmail,
} from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
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

// Pre-fill email if saved
document.addEventListener("DOMContentLoaded", () => {
  const savedEmail = localStorage.getItem("savedEmail");
  if (savedEmail) {
    document.getElementById("email").value = savedEmail;
    document.getElementById("remember").checked = true;
  }
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
