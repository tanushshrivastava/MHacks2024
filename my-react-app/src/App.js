import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [time, setTime] = useState('');
  const [featureEnabled, setFeatureEnabled] = useState(false);

  const fetchMessage = () => {
    fetch('http://127.0.0.1:8000/api/message')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(err => console.error('Error fetching data:', err));
  };

  const fetchTime = () => {
    fetch('http://127.0.0.1:8000/api/time')
      .then(response => response.json())
      .then(data => setTime(data.time))
      .catch(err => console.error('Error fetching data:', err));
  };

  const toggleFeature = () => {
    fetch('http://127.0.0.1:8000/api/toggle')
      .then(response => response.json())
      .then(data => setFeatureEnabled(data.featureEnabled))
      .catch(err => console.error('Error fetching data:', err));
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Message from the backend: {message}
        </p>
        <button onClick={fetchMessage}>Fetch Message</button>
        <p>
          Server Time: {time}
        </p>
        <button onClick={fetchTime}>Get Time</button>
        <p>
          Feature is {featureEnabled ? "Enabled" : "Disabled"}
        </p>
        <button onClick={toggleFeature}>Toggle Feature</button>
      </header>
    </div>
  );
}

export default App;
