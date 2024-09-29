import React, { useState } from 'react';
import './styles.css';
import pfp from './pfp.png';

function App() {
  const [tags, setTags] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleKeyDown = (event) => {
    if (event.key === 'Enter' && inputValue.trim()) {
      setTags([...tags, inputValue]);
      setInputValue('');
    }
  };

  const removeTag = (indexToRemove) => {
    setTags(tags.filter((_, index) => index !== indexToRemove));
  };

  return (
    <div><h1 className="app-title">FoodFindr</h1>
    <div className="App">
      <div className="sidebar">
        <button className="sidebar-button">Schedule</button>
        <button className="sidebar-button">Feed</button>
        <button className="sidebar-button">For You Page</button>
      </div>
      <div className="main-content">
        <div className="header">
          <img src={pfp} alt="Profile" className="profile-icon" />
          <div className="search-bar">
            {tags.map((tag, index) => (
              <span className="tag" key={index}>
                {tag}
                <span className="remove-tag" onClick={() => removeTag(index)}>✖</span>
              </span>
            ))}
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Search tags..."
            />
            <button className="search-button">Search</button>
          </div>
        </div>
        <div className="calendar">
          {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].map((day) => (
            <div key={day} className="day">
              {day}
              <div className="day-content"></div>
            </div>
          ))}
        </div>
      </div>
    </div>
    </div>
  );
}

export default App;
