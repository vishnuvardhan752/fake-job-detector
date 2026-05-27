document.getElementById("checkBtn").addEventListener(
  "click",
  async () => {

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Checking website...";

    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true
    });

    const currentURL = tab.url;

    const response = await fetch(
      "http://127.0.0.1:8000/check-url",
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({
          url: currentURL
        })
      }
    );

    const data = await response.json();

    resultDiv.innerHTML = `
      <h3>Status: ${data.status}</h3>
      <p>Risk Score: ${data.risk_score}</p>
      <p>Keywords: ${data.matched_keywords.join(", ")}</p>
    `;
  }
);