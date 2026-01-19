<script setup>
import { ref } from "vue"

const API_BASE = import.meta.env.VITE_API_BASE_URL

const inputText = ref("")
const outputText = ref("")
const loading = ref(false)
const error = ref("")

async function callApi(endpoint) {
  loading.value = true
  error.value = ""

  try {
    const res = await fetch(`${API_BASE}/api/${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: inputText.value,
      }),
    })

    if (!res.ok) {
      throw new Error("Server error")
    }

    const data = await res.json()
    outputText.value = data.result
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

function encode() {
  callApi("encode")
}

function decode() {
  callApi("decode")
}
</script>

<template>
  <div class="container">
    <h1>🐧 Pingu Translator</h1>

    <textarea
      v-model="inputText"
      placeholder="Enter human language here..."
    ></textarea>

    <div class="buttons">
      <button @click="encode" :disabled="loading">Encode</button>
      <button @click="decode" :disabled="loading">Decode</button>
    </div>

    <p v-if="loading">Processing...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <textarea
      v-model="outputText"
      placeholder="Result will appear here..."
      readonly
    ></textarea>
  </div>
</template>

<style>
/* ===== Reset ===== */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: #000000;
  color: #000000;
  font-family: system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", sans-serif;
}

/* ===== Card ===== */
.container {
  max-width: 480px; /* 👈 更窄 */
  margin: 48px auto;
  padding: 24px 26px;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

/* ===== Title ===== */
h1 {
  margin: 0 0 18px;
  text-align: center;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 0.3px;
}

/* ===== Textarea ===== */
textarea {
  width: 100%;
  min-height: 120px;
  padding: 12px;
  margin-top: 10px;
  border: 2px solid #000000;
  border-radius: 10px;
  background: #ffffff;
  color: #000000;
  font-size: 0.95rem;
  line-height: 1.5;
  resize: vertical;
}

textarea::placeholder {
  color: #666666;
}

textarea:focus {
  outline: none;
  border-color: #577bfb;
}

/* ===== Buttons ===== */
.buttons {
  display: flex;
  gap: 12px;
  margin: 18px 0 8px;
}

/* Encode */
button {
  flex: 1;
  padding: 10px 0;
  border-radius: 999px;
  border: 2px solid #000000;
  background: #ea7d23;
  color: #000000;
  font-weight: 700;
  cursor: pointer;
  transition: transform 0.1s ease, background 0.1s ease;
}

button:hover:not(:disabled) {
  background: #f9e94e;
  transform: translateY(-1px);
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Decode = 蓝色 */
button:nth-child(2) {
  background: #577bfb;
  color: #ffffff;
}

button:nth-child(2):hover:not(:disabled) {
  background: #f9e94e;
  color: #000000;
}

/* ===== Status ===== */
p {
  margin: 6px 0 0;
  font-size: 0.85rem;
}

.error {
  color: #ea7d23;
  font-weight: 600;
}

/* ===== Mobile ===== */
@media (max-width: 520px) {
  .container {
    margin: 24px 16px;
    padding: 20px;
  }
}
</style>

