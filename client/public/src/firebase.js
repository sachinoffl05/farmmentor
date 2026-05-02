import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyBau1teVxd8T1Dp7-jOCueNpQdDMKj2KOY",
  authDomain: "agrisense-ai-2026.firebaseapp.com",
  projectId: "agrisense-ai-2026",
  appId: "1:721789282233:web:f9d87eef8f1f85581df868"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();