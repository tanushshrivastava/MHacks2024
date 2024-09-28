import React, { useState } from 'react';
import './App.css';

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
    <div className="App" style={{ backgroundColor: '#e0f7e9', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <div className="header" style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
        <div className="profile-icon" style={{ width: '50px', height: '50px', borderRadius: '50%', backgroundColor: '#9a8c98', marginRight: '20px' }}></div>
        <div className="search-bar" style={{ display: 'flex', alignItems: 'center', flexGrow: 1 }}>
          <input 
            type="text" 
            value={inputValue} 
            onChange={(e) => setInputValue(e.target.value)} 
            onKeyDown={handleKeyDown} 
            placeholder="Search tags..." 
            style={{ flexGrow: 1, padding: '10px', borderRadius: '5px', border: '1px solid #c9ada7', marginRight: '10px' }}
          />
          <button style={{ backgroundColor: '#c9ada7', border: 'none', borderRadius: '5px', padding: '10px 20px', color: '#fff' }}>
            Search
          </button>
        </div>
      </div>
      <div className="tags-container" style={{ display: 'flex', gap: '5px', flexWrap: 'wrap', marginBottom: '20px' }}>
        {tags.map((tag, index) => (
          <div key={index} style={{ display: 'flex', alignItems: 'center', backgroundColor: '#f2e9e4', padding: '5px 10px', borderRadius: '20px' }}>
            {tag}
            <span 
              onClick={() => removeTag(index)} 
              style={{ marginLeft: '5px', cursor: 'pointer', color: '#9a8c98' }}
            >
              ✖
            </span>
          </div>
        ))}
      </div>
      <div className="calendar" style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].map((day) => (
          <div key={day} style={{ padding: '10px', backgroundColor: '#f2e9e4', borderRadius: '5px', flexGrow: 1, textAlign: 'center' }}>
            {day}
          </div>
        ))}
      </div>
      <div className="sidebar" style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        <button style={{ backgroundColor: '#9a8c98', border: 'none', borderRadius: '5px', padding: '10px', color: '#fff' }}>Schedule</button>
        <button style={{ backgroundColor: '#9a8c98', border: 'none', borderRadius: '5px', padding: '10px', color: '#fff' }}>Feed</button>
        <button style={{ backgroundColor: '#9a8c98', border: 'none', borderRadius: '5px', padding: '10px', color: '#fff' }}>For You Page</button>
      </div>
    </div>
  );
}

export default App;