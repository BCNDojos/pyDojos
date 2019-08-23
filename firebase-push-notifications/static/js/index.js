// Initialize Firebase
const config = {
  apiKey: "your-token-goes-here",
  authDomain: "python-april-2019.firebaseapp.com",
  databaseURL: "https://python-april-2019.firebaseio.com",
  projectId: "python-april-2019",
  storageBucket: "python-april-2019.appspot.com",
  messagingSenderId: "your-token-goes-here"
};
firebase.initializeApp(config);

// Retrieve Firebase Messaging object.
const messaging = firebase.messaging();

// Register Firebase Service Worker
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/static/js/firebase-messaging-sw.js", {
        scope: "/static/js/firebase-cloud-messaging-push-scope"
      })
      .then(registration => {
        messaging.useServiceWorker(registration);
      });
  });
} else {
  console.error("Your browser doesn't support ServiceWorkers");
}

// Get current token
const getToken = async () => {
  let token;

  try {
    // Get Instance ID token. Initially this makes a network call, once retrieved
    // subsequent calls to getToken will return from cache.
    token = await messaging.getToken();
    if (!token) {
      // Show permission request.
      await messaging.requestPermission();
      token = await messaging.getToken();
    }
    console.log({ token });
  } catch (error) {
    console.error("An error occurred while retrieving token. ", error);
  }

  return token;
};

const button = document.getElementById("token-button");
const input = document.getElementById("token-input");

if (button && input) {
  button.addEventListener("click", () => {
    getToken().then(token => {
      input.value = token;

      if (token) {
        const body = JSON.stringify({ token });
        const headers = { 'Content-Type': 'application/json' };
        const request = new Request("/save-token", { method: "POST", body, headers });

        fetch(request)
          .then(response => response.json())
          .then(response => console.log({ response }));
      }
    });
  });
}
