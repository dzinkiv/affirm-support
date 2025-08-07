import { useState } from 'react';
// import TypingResponse from './TypingResponse.jsx';

function Body() {
  const [inputValue, setInputValue] = useState('');
  const [response, setResponse] = useState("");
  const [aiSelected, setAISelected] = useState(false);
  const [loading, setLoading] = useState(false);
  const BASE_URL = 'http://localhost:8000';

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = async (e) => {
    if (!aiSelected) {
      window.location.href = `https://helpcenter.affirm.ca/s/affirm-searchresults?language=en_US&q=${encodeURIComponent(inputValue)}`;
      return;
    }
    e.preventDefault();
    console.log("sending input value:", inputValue);
    setLoading(true);
    setInputValue('');
    const res = await fetch(`${BASE_URL}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: inputValue }),
    });
    const data = await res.json();
    console.log("received response:", data);
    setLoading(false);
    setResponse(data);
  
  };

  return (
    <div className="min-h-screen bg-white flex flex-col items-center justify-center p-4">
      <h2 className="text-[40px] text-black font-calibre">Hi, how can we help?</h2>
      <div className="w-full max-w-md mx-auto mt-10">
        <div
          className="flex items-center justify-between px-4"
          style={{
            height: "50px",
            borderRadius: "50px",
            border: "1px solid #d1d5db",
            color: "#6B7280",
          }}
        >
          <div className="flex items-center gap-2 flex-1">
            <ion-icon name="search-outline" style={{ fontSize: "20px" }}></ion-icon>
            <input
              type="text"
              className="text-sm w-full outline-none bg-transparent"
              placeholder={aiSelected ? "Search with AI" : "Find answers and resources"}
              value={inputValue}
              onChange={handleInputChange}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  handleSubmit(e);
                }
              }}
            />
          </div>
          <img
            src="polestar.png"
            alt="AI Search"
            className={`w-20 h-15 cursor-pointer transition duration-300 ${
              aiSelected ? "drop-shadow-[0_0_6px_rgba(128,0,255,0.9)]" : ""
            }`}
            onClick={() => setAISelected(!aiSelected)}
          />
        </div>
      </div>
      {loading ? (
        <div className="mt-8 w-full max-w-4xl">
          <div className="mt-2">
            <p className="text-sm text-gray-700">Processing...</p>
          </div>
        </div>
      ) : (
          <div className="mt-8 w-full max-w-4xl">
            <div className="mt-2">
              <p className="text-sm text-gray-700">{response}</p>
            </div>
          </div>
      )}
      <div className="mt-8 w-full max-w-4xl">
        <h3 className="text-[32px] font-semibold text-gray-800">Get help by topic</h3>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mt-4">
          <a href="https://helpcenter.affirm.ca/s/topic/0TO7V00000134SJWAY/about-affirm" className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <button>
              <img src="About_Affirm.svg" alt="About Affirm" className="mx-auto mb-2" />
              <h4 className="text-lg font-medium text-black">About Affirm</h4>
              <p className="text-sm text-gray-600">Get to know the basics</p>
            </button>
          </a>
          <a href="https://helpcenter.affirm.ca/s/topic/0TO7V00000134SKWAY/account-payments" className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <button>
              <img src="Account_and_Security.svg" alt="Account & Payments" className="mx-auto mb-2" />
              <h4 className="text-lg font-medium text-black">Account & payments</h4>
              <p className="text-sm text-gray-600">Manage your account and payments</p>
            </button>
          </a>
          <a href="https://helpcenter.affirm.ca/s/topic/0TO7V00000134SMWAY/disputes-refunds" className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <button>
              <img src="Disputes_and_Refunds.svg" alt="Disputes & Refunds" className="mx-auto mb-2" />
              <h4 className="text-lg font-medium text-black">Disputes & refunds</h4>
              <p className="text-sm text-gray-600">Fix order issues and returns</p>
            </button>
          </a>
          <a href="https://helpcenter.affirm.ca/s/topic/0TO7V00000134SOWAY/security-privacy" className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <button>
              <img src="Payments.svg" alt="Security & Privacy" className="mx-auto mb-2" />
              <h4 className="text-lg font-medium text-black">Security & privacy</h4>
              <p className="text-sm text-gray-600">Protect your account and information</p>
            </button>
          </a>
        </div>
      </div>

      <div className="mt-8 w-full max-w-4xl">
        <h3 className="text-[32px] font-semibold text-gray-800">Learn how Affirm works</h3>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mt-4">
          <button className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <h4 className="text-lg font-medium text-black">How Affirm works</h4>
          </button>
          <button className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <h4 className="text-lg font-medium text-black">About prequalifying</h4>
          </button>
          <button className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <h4 className="text-lg font-medium text-black">Create an account</h4>
          </button>
          <button className="p-4 border-[0.5px] border-gray-400 rounded-lg text-center">
            <h4 className="text-lg font-medium text-black">Apply for a loan</h4>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Body;